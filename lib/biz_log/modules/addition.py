from biz_log.module import Module
from biz_log.types import FloatType


class AdditionModule(Module):
    @staticmethod
    def _run(inputs):
        return {
            'sum': inputs['addend'] + inputs['augend']
        }

    @staticmethod
    def get_input_types():
        return {
            'addend': FloatType,
            'augend': FloatType,
        }

    @staticmethod
    def get_output_types():
        return {
            'sum': FloatType
        }

