import time

from biz_log.module import Module
from biz_log.types import FloatType


class SleepModule(Module):
    @staticmethod
    def _run(inputs):
        time.sleep(inputs['seconds'])

        return { }

    @staticmethod
    def get_input_types():
        return { 'seconds': FloatType }

    @staticmethod
    def get_output_types():
        return { }

