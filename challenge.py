"""Coding Challenge Skeleton #1
This counter function purpose is to count how many english letters does your name contain.
After writing your tests, develop the counter function as needed to pass all your tests.

"""


def counter(name):

    if name == None:
        raise AttributeError("You cannot input None values")
    name = name.replace(' ','')
    if len(name) == 0:
        raise Exception("Please input your name")
    if name.isalpha():
        return len(name)
    else:
        raise Exception("Teh string must contain eng letters")



