/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#ifndef SQRT_DIAG_NORMALIZER_H
#define SQRT_DIAG_NORMALIZER_H

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>
#include "sqrt_diag_normalizer.h"
#include "str_kernel.h"

void normalize_sqrt_diag(char **X_rows, char **X_cols, 
                         int32_t n_rows, int32_t n_cols,
                         bool symmetric,
                         char *kernel_name,
                         double param_1, double param_2, 
                         double param_3, double param_4,
                         double **km)
{
    double* X_rows_self_kernel = NULL;
    double* X_cols_self_kernel = NULL;

    if (!symmetric) 
    {
        X_rows_self_kernel = (double*)malloc(n_rows * sizeof(double));
        X_cols_self_kernel = (double*)malloc(n_cols * sizeof(double));
        
        for (int32_t i=0; i < n_rows; i++) 
        {
            X_rows_self_kernel[i] = compute_kernel(X_rows[i], X_rows[i],
                                                   kernel_name,
                                                   param_1, param_2, 
                                                   param_3, param_4);
        }
        for (int32_t j=0; j < n_cols; j++) 
        {
            X_cols_self_kernel[j] = compute_kernel(X_cols[j], X_cols[j],
                                                   kernel_name,
                                                   param_1, param_2, 
                                                   param_3, param_4);
        }
    }

    double **normalized_km = (double**)malloc(n_rows * sizeof(double*));
    
    for (int32_t i=0; i < n_rows; i++) 
    {
        normalized_km[i] = (double*)malloc(n_cols * sizeof(double));
    }

    for (int32_t i=0; i < n_rows; i++) 
    {
        for (int32_t j=0; j < n_cols; j++) 
        {
            double denominator;

            if (symmetric) 
            {
                denominator = sqrt(km[i][i] * km[j][j]);
            } 
            else 
            {
                denominator = sqrt(X_rows_self_kernel[i] * X_cols_self_kernel[j]);
            }
            if (denominator == 0.0) 
            {
                denominator = DBL_EPSILON;
            }
            
            normalized_km[i][j] = km[i][j] / denominator;
        }
    }

    for (int32_t i=0; i < n_rows; i++) 
    {
        for (int32_t j=0; j < n_cols; j++) 
        {
            km[i][j] = normalized_km[i][j];
        }
    }

    for (int32_t i=0; i < n_rows; i++) 
    {
        free(normalized_km[i]);
    }
    free(normalized_km);

    if (!symmetric) 
    {
        free(X_rows_self_kernel);
        free(X_cols_self_kernel);
    }
}

#endif
