
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


from abc import ABC, abstractmethod
import os
import numpy as np
import ctypes as ct


class StringKernel(ABC):
    """
    Base class to represent a string kernel.
    """

    def __init__(self):
        """
        Constructor with attributes definition.
        """
        self._kernel_name = None
        self._kernel_params = {}
        self._normalizer = None

        # for ctypes parameters conversion        
        self._param_1 = None 
        self._param_2 = None 
        self._param_3 = None
        self._param_4 = None


    @abstractmethod
    def set_params(self, **kernel_params):
        """
        Set or update kernel parameters.

        Parameters:
            **kernel_params: keyword arguments with specific kernel parameters.
        """
        for key, value in kernel_params.items():
            self._kernel_params[key] = value


    def __call__(self, X_rows, X_cols):
        """
        Compute the kernel matrix between strings in X_rows and X_cols.

        Parameters:
            X_rows: ndarray or list of strings.
            X_cols: ndarray or list of strings.

        Returns:
            A float matrix of shape (len(X_rows), len(X_cols)).
        """
        if X_cols is X_rows:  # in training
            symmetric = True
        else:  # in prediction
            symmetric = False

        # creating empty kernel matrix
        kernel_matrix = np.zeros((len(X_rows), len(X_cols)), dtype=np.float64)

        # including C library
        c_lib_path = os.path.dirname(os.path.abspath(__file__))

        for filename in os.listdir(c_lib_path):
            if filename.startswith('libcore'):
                c_lib_file_path = os.path.join(c_lib_path, filename)
                break
        else:
            raise ImportError(f"Cannot find the core module in {c_lib_path}")

        c_lib = ct.CDLL(c_lib_file_path)

        # ctypes compute kernel matrix function signature
        c_lib.compute_km.argtypes = [ct.POINTER(ct.c_char_p), ct.POINTER(ct.c_char_p), 
                                     ct.c_int32, ct.c_int32,
                                     ct.c_bool,
                                     ct.c_char_p,
                                     ct.c_double, ct.c_double,
                                     ct.c_double, ct.c_double,
                                     ct.c_char_p,
                                     # **var in C is an array of type np.uintp:   
                                     np.ctypeslib.ndpointer(dtype=np.uintp, ndim=1, flags='C')]
        
        c_lib.compute_km.restype = None

        # converting attributes to ctypes
        X_rows_ct = (ct.c_char_p * len(X_rows))()
        X_rows_ct[:] = [s.encode('utf-8') for s in X_rows]
        X_cols_ct = (ct.c_char_p * len(X_cols))()
        X_cols_ct[:] = [s.encode('utf-8') for s in X_cols]

        X_rows_len_ct = ct.c_int32(len(X_rows))
        X_cols_len_ct = ct.c_int32(len(X_cols))

        symmetric_ct = ct.c_bool(symmetric)

        kernel_name_ct = ct.c_char_p(self._kernel_name.encode('utf-8'))

        param_1_ct = ct.c_double(self._param_1)
        param_2_ct = ct.c_double(self._param_2)
        param_3_ct = ct.c_double(self._param_3)
        param_4_ct = ct.c_double(self._param_4)

        if self._normalizer is None:
            normalizer = ''
        else:
            normalizer = self._normalizer
        normalizer_ct = ct.c_char_p(normalizer.encode('utf-8'))

        kernel_matrix_ct = (kernel_matrix.__array_interface__['data'][0] 
                            + np.arange(kernel_matrix.shape[0])
                            * kernel_matrix.strides[0]).astype(np.uintp)

        # computing kernel matrix
        c_lib.compute_km(X_rows_ct, X_cols_ct, 
                         X_rows_len_ct, X_cols_len_ct,
                         symmetric_ct,
                         kernel_name_ct,
                         param_1_ct, param_2_ct,
                         param_3_ct, param_4_ct,
                         normalizer_ct,
                         kernel_matrix_ct)

        return kernel_matrix


    def __str__(self):
        str_ret = str(self._kernel_name)
        if self._kernel_params:
            str_ret += ' ' + str(self._kernel_params)
        return str_ret


    def __repr__(self):
        return self.__str__()
