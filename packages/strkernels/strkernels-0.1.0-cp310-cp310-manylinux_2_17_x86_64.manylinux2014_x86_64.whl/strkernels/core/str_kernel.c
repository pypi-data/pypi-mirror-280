/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#include <string.h>
#include <stdint.h>
#include "str_kernel.h"
#include "fixed_degree_sk.h"
#include "locality_improved_sk.h"
#include "subsequence_sk.h"

double compute_kernel(char *str_a, char *str_b,
                      char *kernel_name,
                      double param_1, double param_2, 
                      double param_3, double param_4)
{
    if (strcmp(kernel_name, "FixedDegreeStringKernel") == 0) 
    {
        int32_t degree = (int32_t) param_1;
        return (double)compute_fixed_degree_sk(str_a, str_b, degree);
    } 
    else if (strcmp(kernel_name, "LocalityImprovedStringKernel") == 0) 
    {
        int32_t length = (int32_t) param_1;
        int32_t inner_degree = (int32_t) param_2;
        int32_t outer_degree = (int32_t) param_3;
        return compute_locality_improved_sk(str_a, str_b, length, inner_degree, outer_degree);
    }    
    else if (strcmp(kernel_name, "SubsequenceStringKernel") == 0) 
    {
        int32_t maxlen = (int32_t) param_1;
        double lambda = param_2;
        return compute_subsequence_sk(str_a, str_b, maxlen, lambda);
    }

    return 0.;
}
