/*
Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com
*/

#include <string.h>
#include <stdbool.h>
#include <stdint.h>
#include "fixed_degree_sk.h"

int64_t compute_fixed_degree_sk(char *str_a, char *str_b, int32_t degree) 
{
    int32_t str_a_len = strlen(str_a);
    int32_t str_b_len = strlen(str_b);
    int32_t shortest_str_len = (str_a_len < str_b_len) ? str_a_len : str_b_len;

    int64_t kernel_value = 0;
	for (int32_t i=0; i < shortest_str_len-degree+1; i++)
	{
		bool match = true;

		for (int32_t j=i; j < i+degree && match; j++)
			match = str_a[j]==str_b[j];

		if (match)
			kernel_value++;
	}
    return kernel_value;
}
