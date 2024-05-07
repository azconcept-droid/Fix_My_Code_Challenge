#!/usr/bin/python3
"""
User class module
"""


class User():
    """ User class model """

    def __init__(self, value=None):
        """ Initialize user class """
        self.__email = value

    @property
    def email(self):
        """ Return user email """
        return self.__email

    @email.setter
    def email(self, value):
        """ Get user email if it is str """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
