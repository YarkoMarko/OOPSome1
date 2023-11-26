# class Bank:
#     def __init__(self, count):
#         self.__count = count
#
#     def get_count(self):
#         if self.__count > 0:
#             return self.__count
#
#         else:
#             return "There no money on your count"
#
#     def set_count(self, money):
#         if money < 0:
#             raise ValueError("You cannot fill account with value sub 0")
#         self.__count = money
#
#     count = property(fget=get_count, fset=set_count)
#
#
# b = Bank(100)
#
# print(b.count)
#
# b.count = 120
#
# print(b.count)

class Bank:
    def __init__(self, count):
        self.__count = count

    @property
    def count(self):
        if self.__count > 0:
            return self.__count

        else:
            return "There no money on your count"

    @count.setter
    def count(self, money):
        if money < 0:
            raise ValueError("You cannot fill account with value sub 0")
        self.__count = money


b = Bank(100)

print(b.count)

b.count = 120

print(b.count)