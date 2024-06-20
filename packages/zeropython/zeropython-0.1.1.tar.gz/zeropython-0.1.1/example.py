"""
Write a function that returns the name of the oldest of the list "people"

Example:
    people = [
        ["karine", 30],
        ["dorian", 28],
        ["hamza", 32],
    ]

print(oldest(people)) => hamza
print(max(people, key=lambda x: x[1])[0]) => hamza


Check the example:

import pathlib
import ast

import zeropython.ast_cleaner
import zeropython.report

file = pathlib.Path("example.py")

report = zeropython.report.Report()
ast_, report = zeropython.ast_cleaner.ast_clean(file.read_text(), report)

print(report)
print(ast.unparse(ast_))
"""


def list_len(_list):
    index = 0
    while _list[index] != "\0":
        index = index + 1
    return index


def list_append(_list, store):
    length_list = list_len(_list)
    new_list = [None] * (length_list + 2)

    index = 0
    while _list[index] != '\0':
        new_list[index] = _list[index]
        index = index + 1
    new_list[-1] = "\0"
    new_list[-2] = store
    return new_list


def null_terminate(_list):
    if str(_list) == "[]":
        return ['\0']

    store = _list[-1]
    _list[-1] = "\0"
    return list_append(_list, store)


def oldest(p):
    p = null_terminate(list(p))

    if list_len(p) == 0:
        return ""

    oldest_name = p[0][0]
    if list_len(p) == 1:
        return oldest_name

    oldest_age = p[0][1]

    index = 1
    while index < list_len(p):
        if p[index][1] > oldest_age:
            oldest_name = p[index][0]
            oldest_age = p[index][1]
        index = index + 1

    return oldest_name
