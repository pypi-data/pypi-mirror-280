
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import numpy as np

from .string_kernel import StringKernel


class LocalityImprovedStringKernel(StringKernel):
    """
    Locality Improved string kernel.
    """

    def __init__(self, normalizer='sqrt_diagonal', **kernel_params):
        """
        Kernel constructor.

        Parameters:
            **kernel_params: keyword arguments with specific kernel parameters.
        """
        super().__init__()  # base class constructor

        # kernel name
        self._kernel_name = 'LocalityImprovedStringKernel'

        # specific kernel parameters
        if 'length' not in kernel_params:
            kernel_params['length'] = 3  # default length value
        if 'inner_degree' not in kernel_params:
            kernel_params['inner_degree'] = 2  # default inner degree value
        if 'outer_degree' not in kernel_params:
            kernel_params['outer_degree'] = 1  # default outer degree value

        # set kernel parameters
        self.set_params(**kernel_params)
        
        # set normalizer
        self._normalizer = normalizer


    def set_params(self, **kernel_params):

        super().set_params(**kernel_params)

        # ctypes parameters conversion
        self._param_1 = np.float64(self._kernel_params['length'])
        self._param_2 = np.float64(self._kernel_params['inner_degree']) 
        self._param_3 = np.float64(self._kernel_params['outer_degree'])
        self._param_4 = 0.0
