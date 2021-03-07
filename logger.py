from enum import unique, Enum


@unique
class LogLevel(Enum):
    NONE = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    SEVERE = 4
    KEY = 5


class Logger:
    __level : LogLevel = LogLevel.INFO
    __key = None

    @classmethod
    def getlevel(cls): return cls.__level

    @classmethod
    def setlevel(cls, level): cls.__level = level

    level = property(getlevel, setlevel)

    @classmethod
    def getkey(cls): return cls.__key

    @classmethod
    def setkey(cls, key): cls.__key = key

    key = property(getkey, setkey)

    @classmethod
    def log(cls, msg, level=LogLevel.INFO, key=None):
        if level.value < cls.level.value:
            return
        if level == LogLevel.KEY and key != cls.key:
            return
        print('log (' + level.name + '): ' + msg)
