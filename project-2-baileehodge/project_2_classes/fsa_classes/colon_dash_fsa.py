from .fsa import FSA
from typing import Callable

class ColonDashFSA(FSA):
    def __init__(self):
        super().__init__()
        self.token_type = "COLON_DASH"
    
    def S0(self, input) -> None:
        # print(type(input[0]))
        if(input):
            if (input[0] == ':'): 
                self.num_read += 1
                self.S1(input[1:])
            else:
                self.num_read = 0
                return
    
    def S1(self, input) -> None: 
        if(input):
            # print(type(input[0]))       
            if (input[0] == '-'):
                self.num_read += 1
                return
            
            else:
                self.num_read = 0
                return

