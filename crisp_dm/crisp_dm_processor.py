from utils.exception import MyException
from crisp_dm.helpers.data_preparation_helper import DataPrepairationHelper
from crisp_dm.helpers.data_understanding_helper import DataUnderstandingHelper
from crisp_dm.helpers.modeling_helper import ModelingHelper
from crisp_dm.helpers.evaluating_helper import EvaluatingHelper

class CRISPDMProcessor:
    def __init__(self, steps=1, evaluation_func=None, parse_X=lambda x: x, parse_y=lambda y: y):
        self.steps = steps
        self.evaluation_func = evaluation_func

        # Step 1
        self.data_preparation_helper = DataPrepairationHelper()

        # Step 2
        self.data_understanding_helper = DataUnderstandingHelper()
        self.parse_X = parse_X
        self.parse_y = parse_y

        # Step 3
        self.modeling_helper = ModelingHelper()

        # Step 4
        self.evaluating_helper = EvaluatingHelper()

        # ==================================

        self.draw_data = None
        self.prepaired_data = None
        self.model = None
        self.X = None
        self.y = None

        self.trained_model = None
        self.y_hat = None

        self.result = None
        pass

    def set_data_preparation_helper(self, helper):
        self.data_preparation_helper = helper

    def set_data_understanding_helper(self, helper):
        self.data_understanding_helper = helper

    def set_modeling_helper(self, helper):
        self.modeling_helper = helper

    def set_evaluating_helper(self, helper):
        self.evaluating_helper = helper

    def validate(self):
        if (self.draw_data is None) and \
            (self.prepaired_data is None) and \
                (self.X is None or self.y is None):
            raise MyException("Missing draw data!")

    def process(self):
        try:
            self.validate()

            if self.steps is not None:
                for step in range(self.steps):
                    print 'Step', step, ":"

                    print ' - Data prepairation:'

                    if self.draw_data is not None:
                        self.prepaired_data = self.data_preparation_helper.process(self.draw_data)

                    print ' - Data understanding:'

                    if self.prepaired_data is not None:
                        self.X, self.y = self.data_understanding_helper.process(self.prepaired_data, self.parse_X, self.parse_y)

                    print ' - Modeling:'

                    if self.X is not None and self.y is not None:
                        self.trained_model, self.y_hat = self.modeling_helper.process(self.model, self.X, self.y)

                    print ' - Evaluation:'

                    if self.y is not None and self.y_hat is not None:
                        self.result = self.evaluating_helper.process(self.y, self.y_hat)

                    if self.result is not None:
                        print 'Result =', step, ':', self.result

                    if self.evaluation_func is not None and self.evaluation_func(self.result):
                        break

                    print '========================================='
            else:
                raise MyException("Missing steps!")
        except MyException, (exception):
            print exception.msg
