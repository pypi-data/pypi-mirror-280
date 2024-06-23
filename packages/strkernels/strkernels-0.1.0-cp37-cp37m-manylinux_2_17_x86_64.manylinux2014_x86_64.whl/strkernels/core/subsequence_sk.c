/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include "subsequence_sk.h"

double*** allocate_3d_array(int32_t x, int32_t y, int32_t z) {
    double*** array = (double***)malloc(x * sizeof(double**));
    for (int32_t i = 0; i < x; ++i) {
        array[i] = (double**)malloc(y * sizeof(double*));
        for (int32_t j = 0; j < y; ++j) {
            array[i][j] = (double*)calloc(z, sizeof(double));
        }
    }
    return array;
}

void free_3d_array(double*** array, int32_t x, int32_t y) {
    for (int32_t i = 0; i < x; ++i) {
        for (int32_t j = 0; j < y; ++j) {
            free(array[i][j]);
        }
        free(array[i]);
    }
    free(array);
}

double compute_subsequence_sk(char *str_a, char *str_b, int32_t maxlen, double lambda) 
{
    int32_t str_a_len = strlen(str_a);
    int32_t str_b_len = strlen(str_b);

    // allocating memory for computing K' (Kp)
    double*** Kp = allocate_3d_array(maxlen + 1, str_a_len, str_b_len);

    // initialize for 0 subsequence length for both the strings
    for (int32_t j = 0; j < str_a_len; j++) {
        for (int32_t k = 0; k < str_b_len; ++k) {
            Kp[0][j][k] = 1.0;
        }
    }

    // computing the K' (Kp) function
    for (int32_t i = 0; i < maxlen; i++) {
        for (int32_t j = 0; j < str_a_len - 1; j++) {
            double Kpp = 0.0;
            for (int32_t k = 0; k < str_b_len - 1; k++) {
                Kpp = lambda * (Kpp + lambda * (str_a[j] == str_b[k]) * Kp[i][j][k]);
                Kp[i + 1][j + 1][k + 1] = lambda * Kp[i + 1][j][k + 1] + Kpp;
            }
        }
    }

    // compute the kernel function
    double kernel_value = 0.0;
    for (int32_t i = 0; i < maxlen; i++) {
        for (int32_t j = 0; j < str_a_len; j++) {
            for (int32_t k = 0; k < str_b_len; k++) {
                kernel_value += lambda * lambda * (str_a[j] == str_b[k]) * Kp[i][j][k];
            }
        }
    }

	// free memory
    free_3d_array(Kp, maxlen + 1, str_a_len);

    return kernel_value;
}
