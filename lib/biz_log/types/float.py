from biz_log.type import Type


class FloatType(Type):
    @staticmethod
    def cast(value):
        return float(value)
