"""
Just a starter script for the program

"""
from __future__ import print_function
from InputAdaptor import InputAdaptor
from PredictionProcessor import PredictionProcessor
from OutputAdaptor import OutputAdaptor

meth = 'The Video and Sound Adaptor'
InputsToAI = InputAdaptor(meth)
ProcessPredOfAI = PredictionProcessor("AI")
OutputsOfAI = OutputAdaptor("Impulses")

# InputsToAI.inputs("This is an input to the model!")


print('    Making prediction on the inputs given to Model!   ')
for inp in InputsToAI:
    print('This is iterative:', inp)
    InputsToAI.adapat_x('Value {}'.format(meth[inp]))
    pred = ProcessPredOfAI.make_prediciton(InputsToAI.get_input())
    OutputsOfAI.adapat_y(pred)
    OutputsOfAI.outputs()
