/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <math.h>
#include "locality_improved_sk.h"

double compute_locality_improved_sk(char *str_a, char *str_b, 
                                    int32_t length,
                                    int32_t inner_degree,
                                    int32_t outer_degree) 
{

    int32_t str_a_len = strlen(str_a);

    double* match = (double*)malloc((str_a_len) * sizeof(double));

    // initialize match table
    for (int32_t i = 0; i < str_a_len; i++)
        match[i] = (str_a[i] == str_b[i]) ? 1.0 : 0.0;

    double outer_sum = 0.0;

    for (int32_t t = 0; t < str_a_len - length; t++) {
        double sum = 0.0;
        for (int32_t i = 0; i < length && t + i + length + 1 < str_a_len; i++)
            sum += (i + 1) * match[t + i] + (length - i) * match[t + i + length + 1];

        // add middle element + normalize with sum_i=0^2l+1 i = (2l+1)(l+1)
        double inner_sum = (sum + (length + 1) * match[t + length]) / ((2 * length + 1) * (length + 1));
        inner_sum = pow(inner_sum, inner_degree + 1);
        outer_sum += inner_sum;
    }
    
    free(match);

    return pow(outer_sum, outer_degree + 1);
}
