from enum import Enum
from abc import ABC, abstractmethod
from typing import Optional

class DBType(Enum):
    SQL_SERVER_W:'{ODBC Driver 18 for SQL Server}'
    MongoDB: 'mongo'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    @classmethod
    def has_name(cls, name):
        return name in cls._member_names_


def abstractfunc(func):
    func.__isabstract__ = True
    return func


class Interface(type):

    def __init__(self, name, bases, namespace):
        for base in bases:
            must_implement = getattr(base, 'abstract_methods', [])
            class_methods = getattr(self, 'all_methods', [])
            for method in must_implement:
                if method not in class_methods:
                    err_str = """Can't create from abstract class {name}!
                    {name} must implement abstract method {method} of class {base_class}!""".format(name=name,
                        method=method,
                        base_class=base.__name__)
                    raise TypeError(err_str)

    def __new__(metaclass, name, bases, namespace):
        namespace['abstract_methods'] = Interface._get_abstract_methods(namespace)
        namespace['all_methods'] = Interface._get_all_methods(namespace)
        cls = super().__new__(metaclass, name, bases, namespace)
        return cls

    def _get_abstract_methods(namespace):
        return [name for name, val in namespace.items() if callable(val) and getattr(val, '__isabstract__', False)]

    def _get_all_methods(namespace):
        return [name for name, val in namespace.items() if callable(val)]


class FactoryDriverInterface(metaclass=Interface):

    DRIVER: DBType
    DATABASE: str
    UID: Optional[str]
    PWD: Optional[str]
    DSN: Optional[str]
    TRUSTED_CONNECTION: Optional[str]

    @abstractfunc
    def create_connection(self):
        pass

    @abstractfunc
    def kill_connection(self):
        pass

    @abstractfunc
    def getData(self):
        pass


