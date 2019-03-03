from biz_log.type import Type


class BooleanType(Type):
    @staticmethod
    def cast(value):
        return bool(value)
