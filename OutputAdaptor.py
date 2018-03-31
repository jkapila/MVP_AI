"""
Output Apadtor:

This adaptor act as the interface between the prediction process's output and the activity you want to perform on that.

As this is an independent adaptor, we can replicate the same for many multiple output methods.
"""

from __future__ import print_function, division, with_statement


class OutputAdaptor(object):
    def __init__(self, output_method):
        print('Output Adaptor Invoked!')
        self.output_method = output_method
        self.prediction = None
        self.output = None

    def outputs(self):
        print('The Output is:', self.output)
        return self.output

    def adapat_y(self, predictions):
        self.prediction = predictions
        self.output = self.prediction
