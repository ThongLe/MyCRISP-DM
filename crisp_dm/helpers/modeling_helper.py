from crisp_dm.helpers.data_processing_helper import DataProcessingHelper
from utils.exception import MyException

class ModelingHelper(DataProcessingHelper):
    def __init__(self):
        pass

    def validate_data(self, *args):
        model = args[0] if len(args) >= 1 else None
        X = args[1] if len(args) >= 2 else None
        y = args[2] if len(args) >= 3 else None

        if model is None:
            raise MyException("Missing model!")

        if X is None:
            raise MyException("Missing X!")

        if y is None:
            raise MyException("Missing y!")

        pass

    def run(self, *args):
        model, X, y = args
        trained_model = model.fit(X, y)
        return trained_model, trained_model.predict(X)