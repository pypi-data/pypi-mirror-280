/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#ifndef LOCALITY_IMPROVED_SK_H
#define LOCALITY_IMPROVED_SK_H

#include <stdint.h>

double compute_locality_improved_sk(char *str_a, char *str_b, 
                                    int32_t length,
                                    int32_t inner_degree,
                                    int32_t outer_degree);

#endif
