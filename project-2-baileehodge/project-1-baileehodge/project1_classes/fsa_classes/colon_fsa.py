from .fsa import FSA
from typing import Callable

class ColonFSA(FSA):
    def __init__(self):
        super().__init__()
        self.token_type = "COLON"
    
    def S0(self, input) -> None:
        if (input[0] == ':'):
            self.num_read += 1
            return
        else:
            self.num_read = 0
            return

