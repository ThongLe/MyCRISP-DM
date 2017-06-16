from crisp_dm.helpers.data_processing_helper import DataProcessingHelper
from utils.exception import MyException
from sklearn.model_selection import train_test_split

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
        X_train, X_test, y_train, y_test = self.train_test_split(X, y)
        trained_model = model.fit(X_train, y_train)
        return trained_model, X_test, y_test

    def train_test_split(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4, random_state=42)
        return X_train, X_test, y_train, y_test