from biz_log.modules import AdditionModule, SleepModule

AVAILABLE_MODULES = [
    AdditionModule,
    SleepModule,
]

MODULES_BY_TYPE = {}

for available_module in AVAILABLE_MODULES:
    MODULES_BY_TYPE[available_module.__name__] = available_module

