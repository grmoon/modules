from biz_log.type import Type


class StringType(Type):
    @staticmethod
    def cast(value):
        return str(value)
