from biz_log.type import Type


class IntegerType(Type):
    @staticmethod
    def cast(value):
        return int(value)
