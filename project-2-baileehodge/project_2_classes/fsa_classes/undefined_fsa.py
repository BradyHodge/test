from .fsa import FSA
from typing import Callable


#implement this for real
class UndefinedFSA(FSA):
    
    def __init__(self):
        super().__init__()
        self.token_type = "UNDEFINED"
    
    def S0(self, input) -> None:
        self.num_read = 1 
        return
        #if all of the other fsa read 0, this wins
