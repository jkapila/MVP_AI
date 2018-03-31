"""
Analytical Engine:

This adaptor act as the interface between the input as it exist and the the readable foramt for the Prediction process.

As this is an independent adaptor, we can replicate the same for many multiple input methods.
"""
from __future__ import print_function, with_statement, division
from Utils import getdir, get_model_from_directory


class AnalyticalEngine:

    def __init__(self, analytical_method):
        """

        :param analytical_method:
        """
        print('Analytical Engine Invoked')
        self.model = None
        self.analytical_method = analytical_method
        self.load_or_make_model(self.analytical_method)

    def load_or_make_model(self, method):
        """

        :param method:
        :return:
        """
        has_model, model = get_model_from_directory(getdir(), method)
        if has_model:
            self.model = model
        else:
            self.model = '{} {}'.format(self.analytical_method, 'Model Created')

    def get_model(self):
        """

        :return:
        """
        return self.model

    def get_prediction(self, input_val):
        return 'As {}! It will make prediction on {}'.format(self.model, input_val)
