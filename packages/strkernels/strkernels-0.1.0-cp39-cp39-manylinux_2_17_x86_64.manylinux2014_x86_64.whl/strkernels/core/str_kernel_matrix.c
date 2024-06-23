/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#include <stdbool.h>
#include <stdint.h>
#include <omp.h>
#include "str_kernel_matrix.h"
#include "str_kernel.h"
#include "normalizer.h"

void compute_km(char **X_rows, char **X_cols, 
                int32_t X_rows_len, int32_t X_cols_len,
                bool symmetric,
                char *kernel_name,
                double param_1, double param_2, 
                double param_3, double param_4,
                char *normalizer,
                double **km)
{
    int32_t i, j;

    #pragma omp parallel for private(i, j) schedule(dynamic, 32)
    for(i=0; i < X_rows_len; ++i) 
	{
        for(j=0; j < X_cols_len; ++j) 
		{
            if(symmetric && i > j)
            {
                km[i][j] = km[j][i]; 
            }
            else
            {
                km[i][j] = compute_kernel(X_rows[i], X_cols[j],
                                          kernel_name,
                                          param_1, param_2, 
                                          param_3, param_4);
            }
            // printf("%.0f ", km[i][j]);
        }
        // printf("\n");
    }

    normalize(X_rows, X_cols, 
              X_rows_len, X_cols_len,
              symmetric,
              kernel_name,
              param_1, param_2, 
              param_3, param_4,
              normalizer,
              km);
}
