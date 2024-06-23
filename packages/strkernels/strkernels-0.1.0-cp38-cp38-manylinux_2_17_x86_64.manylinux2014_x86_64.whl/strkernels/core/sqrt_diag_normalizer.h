/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#ifndef SQRT_DIAG_NORMALIZER_H
#define SQRT_DIAG_NORMALIZER_H

#include <stdbool.h>
#include <stdint.h>

void normalize_sqrt_diag(char **X_rows, char **X_cols, 
                         int32_t n_rows, int32_t n_cols,
                         bool symmetric,
                         char *kernel_name,
                         double param_1, double param_2, 
                         double param_3, double param_4,
                         double **km);

#endif
