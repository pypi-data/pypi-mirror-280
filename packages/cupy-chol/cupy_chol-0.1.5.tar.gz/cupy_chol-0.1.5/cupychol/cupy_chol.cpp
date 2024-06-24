#include <pybind11/pybind11.h>
#include <cusolverSp.h>
#include <cusparse_v2.h>
#include <iostream>
#include "cusolverSp_LOWLEVEL_PREVIEW.h"

namespace py = pybind11;

void solve_cholesky(int n, int nnz, int* d_csrRowPtrA, int* d_csrColIndA, double* d_csrValA, double* d_b, double* d_x) {
    cusolverSpHandle_t cusolverH = nullptr;
    cusparseHandle_t cusparseH = nullptr;
    cusparseMatDescr_t descrA = nullptr;
    csrcholInfo_t info = nullptr;
    void* buffer = nullptr;
    size_t bufferSize = 0;
    size_t size_internal = 0;
    int singularity = 0;
    const double tol = 1e-14;

    // Create solver and sparse handles
    cusolverSpCreate(&cusolverH);
    cusparseCreate(&cusparseH);
    cusparseCreateMatDescr(&descrA);
    cusparseSetMatType(descrA, CUSPARSE_MATRIX_TYPE_GENERAL);
    cusparseSetMatIndexBase(descrA, CUSPARSE_INDEX_BASE_ZERO);

    // Create Cholesky info structure
    cusolverSpCreateCsrcholInfo(&info);

    // Analyze the sparsity pattern of A
    cusolverSpXcsrcholAnalysis(cusolverH, n, nnz, descrA, d_csrRowPtrA, d_csrColIndA, info);

    // Get the buffer size for Cholesky factorization
    cusolverSpDcsrcholBufferInfo(cusolverH, n, nnz, descrA, d_csrValA, d_csrRowPtrA, d_csrColIndA, info, &size_internal, &bufferSize);
    cudaMalloc(&buffer, bufferSize);

    // Perform Cholesky factorization
    cusolverSpDcsrcholFactor(cusolverH, n, nnz, descrA, d_csrValA, d_csrRowPtrA, d_csrColIndA, info, buffer);

    // Check if the matrix is singular
    cusolverSpDcsrcholZeroPivot(cusolverH, info, tol, &singularity);
    if (singularity >= 0) {
        std::cerr << "WARNING: A is singular at row " << singularity << std::endl;
    }

    // Solve the linear system A*x = b
    cusolverSpDcsrcholSolve(cusolverH, n, d_b, d_x, info, buffer);

    // Clean up
    cusolverSpDestroyCsrcholInfo(info);
    cudaFree(buffer);
    cusparseDestroyMatDescr(descrA);
    cusolverSpDestroy(cusolverH);
    cusparseDestroy(cusparseH);
}

void solve_cupy_csr(py::object csrRowPtrA, py::object csrColIndA, py::object csrValA, py::object b, py::object x) {
    int* d_csrRowPtrA = reinterpret_cast<int*>(csrRowPtrA.attr("data").attr("ptr").cast<ssize_t>());
    int* d_csrColIndA = reinterpret_cast<int*>(csrColIndA.attr("data").attr("ptr").cast<ssize_t>());
    double* d_csrValA = reinterpret_cast<double*>(csrValA.attr("data").attr("ptr").cast<ssize_t>());
    double* d_b = reinterpret_cast<double*>(b.attr("data").attr("ptr").cast<ssize_t>());
    double* d_x = reinterpret_cast<double*>(x.attr("data").attr("ptr").cast<ssize_t>());

    int n = csrRowPtrA.attr("size").cast<int>() - 1;
    int nnz = csrColIndA.attr("size").cast<int>();

    solve_cholesky(n, nnz, d_csrRowPtrA, d_csrColIndA, d_csrValA, d_b, d_x);
}

PYBIND11_MODULE(cupy_chol, m) {
    m.def("solve_cupy_csr", &solve_cupy_csr, "Solve a linear system using Cholesky decomposition with CuPy arrays");
}
