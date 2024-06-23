
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import numpy as np

from .string_kernel import StringKernel


class SubsequenceStringKernel(StringKernel):
    """
    Subsequence string kernel.
    """

    def __init__(self, normalizer='sqrt_diagonal', **kernel_params):
        """
        Kernel constructor.

        Parameters:
            **kernel_params: keyword arguments with specific kernel parameters.
        """
        super().__init__()  # base class constructor

        # kernel name
        self._kernel_name = 'SubsequenceStringKernel'

        # specific kernel parameters
        if 'maxlen' not in kernel_params:
            kernel_params['maxlen'] = 3  # default maxlen value
        if 'ssk_lambda' not in kernel_params:
            kernel_params['ssk_lambda'] = 0.5  # default lambda value

        # set kernel parameters
        self.set_params(**kernel_params)
        
        # set normalizer
        self._normalizer = normalizer


    def set_params(self, **kernel_params):

        super().set_params(**kernel_params)

        # ctypes parameters conversion
        self._param_1 = np.float64(self._kernel_params['maxlen'])
        self._param_2 = np.float64(self._kernel_params['ssk_lambda']) 
        self._param_3 = 0.0
        self._param_4 = 0.0
