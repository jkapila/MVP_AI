"""
Prediction Processor:

This adaptor act as the interface between the prediction process's output and the activity you want to perform on that.

As this is an independent adaptor, we can replicate the same for many multiple output methods.
"""

from __future__ import print_function, division, with_statement
from AnalyticalEngine import AnalyticalEngine

class PredictionProcessor(object):

    def __init__(self, analytical_method):
        print('Prediction Processor Invoked!')
        self.analytical_method = analytical_method
        self.prediction = None
        self.output = None
        self.model_object = AnalyticalEngine(analytical_method)
        print('This prediction can be directly sent and can be stored temporarily!')

    def outputs(self):
        return self.output

    def make_prediciton(self, inputs):
        self.prediction = self.model_object.get_prediction(inputs)
        print('We get prediction as: ', self.prediction)
        self.output = self.prediction
        return self.prediction
