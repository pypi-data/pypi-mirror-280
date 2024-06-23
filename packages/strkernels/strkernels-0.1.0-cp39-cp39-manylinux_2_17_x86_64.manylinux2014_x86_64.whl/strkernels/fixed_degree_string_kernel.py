
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import numpy as np

from .string_kernel import StringKernel


class FixedDegreeStringKernel(StringKernel):
    """
    Fixed Degree string kernel.
    """

    def __init__(self, normalizer='sqrt_diagonal', **kernel_params):
        """
        Kernel constructor.

        Parameters:
            **kernel_params: keyword arguments with specific kernel parameters.
        """
        super().__init__()  # base class constructor

        # kernel name
        self._kernel_name = 'FixedDegreeStringKernel'

        # specific kernel parameter
        if 'degree' not in kernel_params:
            kernel_params['degree'] = 3  # default degree value

        # set kernel parameters
        self.set_params(**kernel_params)
        
        # set normalizer
        self._normalizer = normalizer


    def set_params(self, **kernel_params):

        super().set_params(**kernel_params)

        # ctypes parameters conversion
        self._param_1 = np.float64(self._kernel_params['degree'])
        self._param_2 = 0.0 
        self._param_3 = 0.0
        self._param_4 = 0.0
