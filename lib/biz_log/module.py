class Module(object):
    def __init__(self):
        raise NotImplementedError()

    @classmethod
    def run(cls, raw_inputs):
        input_types = cls.get_input_types()
        cleaned_inputs = {}

        for input_key, input_type in input_types.items():
            if not input_key in raw_inputs:
                raise Exception()

            cleaned_inputs[input_key] = input_type.cast(raw_inputs[input_key])

        return cls._run(cleaned_inputs)

    @classmethod
    def _run(cls, inputs):
        raise NotImplementedError()

    @staticmethod
    def get_input_types():
        raise NotImplementedError()

    @classmethod
    def get_output_types(cls):
        raise NotImplementedError()

