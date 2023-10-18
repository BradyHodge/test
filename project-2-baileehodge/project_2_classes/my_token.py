from enum import Enum

#Dummy of the token class you made in project 1
# class Token():
#     def __init__(self, token_type: str, value: str, line_num: int):
#         self.token_type = token_type
#         self.value = value
#         self.line = line_num

#     def to_string(self) -> str:
#         return self.__str__()

#     def __str__(self) -> str:
#         return "(" + self.token_type + "," + self.value + "," + str(self.line) + ")"


class Token():
    def __init__(self, token_type: str, value: str, line_num: int):
        self.token_type = token_type
        self.value = value
        self.line = line_num

    def to_string(self) -> str:
        token_type_str = str(self.token_type)
        return "(" + token_type_str + ",\"" + self.value + "\"," + str(self.line) + ")"