from crisp_dm.helpers.data_processing_helper import DataProcessingHelper
from utils.exception import MyException
import numpy as np

class EvaluatingHelper(DataProcessingHelper):
    def __init__(self):
        pass

    def validate_data(self, *args):
        y     = args[0] if len(args) >= 1 else None
        y_hat = args[1] if len(args) >= 2 else None

        if y is None:
            raise MyException("Missing y!")

        if y_hat is None:
            raise MyException("Missing y_hat!")

    def run(self, *args):
        y, y_hat = args[0], args[1]
        return self.errors(y, y_hat)

    def errors(self, y, y_hat):
        return float(np.linalg.norm(np.array(y) - np.array(y_hat), 1)) / len(y)