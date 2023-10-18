from .fsa import FSA
from typing import Callable


# separate this class into different classes. 
# separate classes for Schemes, Rules, Queries, 
# Facts, and ID

class IDFSA(FSA):
    def __init__(self):
        super().__init__()
        self.token_type = "ID"

    def S0(self, input) -> None:
            self.num_read = 0
            if (input and input[0].isalpha()): 
                #self.num_read += 1 
                self.S1(input)
            else:
                self.num_read = 0
                return
    #checks to make sure it starts with a letter
    # bc otherwise it's not an ID

    def S1(self, input) -> None:
        # if (input)
        self.num_read = 0
        if (input and input[0] != '\n'):
            keywords = ["Schemes", "Rules", "Facts", "Queries"]
            for keyword in keywords:
            #if it matches a keyword, we're done here
                if input.startswith(keyword) and input[len(keyword)].isspace():
                    self.num_read = len(keyword)
                    self.token_type = keyword.upper()
                    return
                if input.startswith(keyword) and input[len(keyword)] == ':':
                    self.num_read = len(keyword)
                    self.token_type = keyword.upper()
                    return
            # If it doesn't match a keyword, move to the next state
                else:
                    self.num_read = 0
                    self.S2(input)
    def S2(self, input) -> None:
        if (input):
            if (input[0].isalnum()):
                self.num_read += 1
                self.token_type = "ID"
                self.S2(input[1:])
            else:
                return
        else:
            return



# class SchemesFSA(FSA):
#     def __init__(self):
#         super().__init__()
#         self.token_type = "SCHEMES"

#     def S0(self, input) -> None:
#         if input.startswith("Schemes"):
#             self.num_read += len("Schemes")
#         else:
#             self.num_read = 0


# class RulesFSA(FSA):
#     def __init__(self):
#         super().__init__()
#         self.token_type = "RULES"

#     def S0(self, input) -> None:
#         if input.startswith("Rules"):
#             self.num_read += len("Rules")
#         else:
#             self.num_read = 0

# class QueriesFSA(FSA):
#     def __init__(self):
#         super().__init__()
#         self.token_type = "QUERIES"

#     def S0(self, input) -> None:
#         if input.startswith("Queries"):
#             self.num_read += len("Queries")
#         else:
#             self.num_read = 0

# class FactsFSA(FSA):
#     def __init__(self):
#         super().__init__()
#         self.token_type = "FACTS"

#     def S0(self, input) -> None:
#         if input.startswith("Facts"):
#             self.num_read += len("Facts")
#         else:
#             self.num_read = 0

# class IDFSA(FSA):
#     def __init__(self):
#         super().__init__()
#         self.token_type = "ID"

#     def S0(self, input) -> None:
#         if input and input[0].isalpha():
#             self.S1(input)
#         else:
#             self.num_read = 0

#     def S1(self, input) -> None:
#         if input and input[0].isalnum():
#             self.num_read += 1
#             self.S1(input[1:])
#         else:
#             return
