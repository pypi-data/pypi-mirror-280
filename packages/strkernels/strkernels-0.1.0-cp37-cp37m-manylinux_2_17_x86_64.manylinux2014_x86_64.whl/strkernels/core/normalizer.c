/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#include <string.h>
#include <stdbool.h>
#include <stdint.h>
#include "normalizer.h"
#include "sqrt_diag_normalizer.h"

void normalize(char **X_rows, char **X_cols, 
               int32_t X_rows_len, int32_t X_cols_len,
               bool symmetric,
               char *kernel_name,
               double param_1, double param_2, 
               double param_3, double param_4,
               char *normalizer,
               double **km)
{
    if (strcmp(normalizer, "sqrt_diagonal") == 0) 
    {
        normalize_sqrt_diag(X_rows, X_cols, 
                            X_rows_len, X_cols_len,
                            symmetric,
                            kernel_name,
                            param_1, param_2, 
                            param_3, param_4,
                            km);
    } 
}  
