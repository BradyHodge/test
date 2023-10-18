#not currently in use

from .fsa import FSA
from typing import Callable

class SingleFSA(FSA):
    def __init__(self):
        super().__init__()
    
    def S0(self, input) -> None:
        if (input[0] == '.'):
            self.num_read = 1
            token_type = "PERIOD"
            return
        else:
            self.num_read = 0
            self.S1(input[0])

    def S1(self, input) -> None:        
        if (input[0] == '-'):
            self.num_read = 1
            token_type = "DASH"
            return
        else:
            self.num_read = 0
            self.S2(input[0])
    
    def S2(self, input) -> None:        
        if (input[0] == ':'):
            self.num_read = 1
            token_type = "COLON"
            return
        else:
            self.num_read = 0
            return
