"""


"""

from __future__  import print_function
import os


def getdir():
    """

    :return:
    """
    print(os.getcwd())
    return os.getcwd()


def get_model_from_directory(folder, method):
    """

    :param folder:
    :param method:
    :return:
    """
    has_model = False
    model = None
    print('Will Match with each methods/files and get the right model! If model dosent exist the we will create one')
    print("Directory is : ", folder,' and looking for : ', method)
    for methods in os.listdir(folder):
        print("As Looping from directory we got: ",methods)
        if methods == method:
            has_model = True
            model = "Default Model Loaded"
            break
    return has_model, model
