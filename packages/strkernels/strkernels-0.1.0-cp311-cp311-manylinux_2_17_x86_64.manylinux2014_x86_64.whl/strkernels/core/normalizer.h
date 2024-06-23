/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#ifndef NORMALIZER_H
#define NORMALIZER_H

#include <stdint.h>

void normalize(char **X_rows, char **X_cols, 
               int32_t X_rows_len, int32_t X_cols_len,
               bool symmetric,
               char *kernel_name,
               double param_1, double param_2, 
               double param_3, double param_4,
               char *normalizer,
               double **km);
#endif
