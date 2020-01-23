"""
Реализуйте программу, которая будет эмулировать работу с пространствами имен.
Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

create <namespace> <parent> –  создать новое пространство имен
с именем <namespace> внутри пространства <parent>

add <namespace> <var> – добавить в пространство <namespace> переменную <var>

get <namespace> <var> – получить имя пространства,
из которого будет взята переменная <var> при запросе из пространства <namespace>,
или None, если такого пространства не существует
"""
#
# a = 0
# def foo():
#   b = 1
#   get(a)
#   get(c)
#   def bar():
#     a = 2
#     get(a)
#     get(b)


namespaces = {'global': None} # ключ - namespace. значение - parent
variables = {'global': set()} # ключ - namespace. значение - множество переменных


def create(namespace, parent):
    pass


def get(namespace, var):
    pass


def add(namespace, var):
    namespace.var
