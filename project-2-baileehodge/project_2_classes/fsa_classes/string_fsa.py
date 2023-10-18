from .fsa import FSA
from typing import Callable

#implement this for real

class StringFSA(FSA):
    
    def __init__(self):
        super().__init__()
        self.token_type = "STRING"
    
    def S0(self, input) -> None:
        if (input[0] == '\''): #if it starts with a ', keep going
            self.num_read += 1
            self.S1(input[1:])
    
        else:
            self.num_read = 0
            return
        
    def S1(self, input) -> None: #stop when you hit another '
        if (input):
            if (input[0] == '\''):
                self.num_read += 1
                self.S2(input[1:]) #go to S2 to check for another '
            else:
                self.num_read += 1
                self.S1(input[1:])
        else:
            self.num_read = 0
            return

    def S2(self, input) -> None:
        if (input):
            if (input[0] == '\''):
                self.num_read += 1
                self.S1(input[1:])

        else:
            # self.num_read = 0
            return

# an additional state for after ', it there's another ', go back to state 1
# if not, that's the end of the string
