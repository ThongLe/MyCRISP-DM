from utils.exception import MyException
from crisp_dm.helpers.data_understanding_helper import DataUnderstandingHelper
from crisp_dm.helpers.data_preparation_helper import DataPreparationHelper
from crisp_dm.helpers.modeling_helper import ModelingHelper
from crisp_dm.helpers.evaluating_helper import EvaluatingHelper

class CRISPDMProcessor:
    def __init__(self, steps=1, evaluation_func=lambda x: True, parse_X=lambda x: x, parse_y=lambda y: y):
        self.steps = steps
        self.evaluation_func = evaluation_func

        # Step 1
        self.data_understanding_helper = DataUnderstandingHelper()

        # Step 2
        self.data_preparation_helper = DataPreparationHelper()
        self.parse_X = parse_X
        self.parse_y = parse_y

        # Step 3
        self.modeling_helper = ModelingHelper()

        # Step 4
        self.evaluating_helper = EvaluatingHelper()

        # ==================================

        self.draw_data = None
        self.understood_data = None
        self.model = None
        self.X = None
        self.y = None

        self.trained_model = None
        self.X_test = None
        self.y_test = None

        self.error = None
        pass

    def set_data_understanding_helper(self, helper):
        self.data_understanding_helper = helper

    def set_data_preparation_helper(self, helper):
        self.data_preparation_helper = helper

    def set_modeling_helper(self, helper):
        self.modeling_helper = helper

    def set_evaluating_helper(self, helper):
        self.evaluating_helper = helper

    def validate(self):
        if (self.draw_data is None) and \
            (self.understood_data is None) and \
                (self.X is None or self.y is None):
            raise MyException("Missing draw data!")

    def process(self):
        try:
            self.validate()

            if self.steps is not None:
                for step in range(self.steps):
                    print 'Step', step, ":"

                    print ' - Data understanding:'

                    if self.draw_data is not None:
                        self.understood_data = self.data_understanding_helper.process(self.draw_data)

                    print ' - Data preparation:'

                    if self.understood_data is not None:
                        self.X, self.y = self.data_preparation_helper.process(self.understood_data, self.parse_X, self.parse_y)

                    print ' - Modeling:'

                    if self.X is not None and self.y is not None:
                        self.trained_model, self.X_test, self.y_test = self.modeling_helper.process(self.model, self.X, self.y)

                    print ' - Evaluation:'

                    if self.X_test is not None and self.y_test is not None:
                        y_hat = self.trained_model.predict(self.X_test)
                        self.error = self.evaluating_helper.process(self.y_test, y_hat)

                    if self.error is not None:
                        print 'error =', self.error * 100, '%'

                    if self.evaluation_func is not None and self.evaluation_func(self.error):
                        break

                    print '========================================='
            else:
                raise MyException("Missing steps!")
        except MyException, (exception):
            print exception.msg
