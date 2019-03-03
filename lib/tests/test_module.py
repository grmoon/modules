from unittest import TestCase

from biz_log import Module


class IntType():
    @staticmethod
    def cast(value):
        return int(value)


class AdditionModule(Module):
    @staticmethod
    def _run(inputs):
        return inputs['addend'] + inputs['augend']

    @staticmethod
    def get_input_types():
        return {
            'addend': IntType,
            'augend': IntType
        }


class ModuleTestCase(TestCase):
    def test_run(self):
        output = AdditionModule.run({
            'addend': '11',
            'augend': 2
        });

        import pdb
        pdb.set_trace()

