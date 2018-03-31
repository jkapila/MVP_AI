"""
Input Apadtor:

This adaptor act as the interface between the input as it exist and the the readable foramt for the Prediction process.

As this is an independent adaptor, we can replicate the same for many multiple input methods.
"""

from __future__ import print_function, division, with_statement


class InputAdaptor(object):
    def __init__(self, input_method = "Default"):
        print('Input Adaptor Invoked!')
        self.input_method = input_method
        self.processedX = None
        self.inputs = None
        self._data_len = len(input_method)-1
        self.input_objects = 0

    # def inputs(self, inputs):
    #     self.inputs = inputs

    def adapat_x(self, input_val):
        self.inputs = input_val
        self.processedX = self.inputs

    def get_input(self):
        return self.processedX

    def has_input(self):
        if self.__iter__():
            return True
        else:
            return False

    def __iter__(self):
        return self

    def next(self):
        if self.input_objects > self._data_len:
            raise StopIteration
        else:
            self.input_objects += 1
            return self.input_objects - 1

    def __len__(self):
        return self._data_len
