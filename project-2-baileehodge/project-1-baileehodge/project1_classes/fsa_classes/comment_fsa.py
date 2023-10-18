from .fsa import FSA
from typing import Callable

class CommentFSA(FSA):
    def __init__(self):
        super().__init__()
        self.token_type = "COMMENT"
    
    def S0(self, input) -> None:
        if(input):
            if (input[0] == '#'):   #if it starts with a #, keep going
                self.num_read += 1
                self.S1(input[1:])
                return
        
            else:
                self.num_read = 0
                return

    def S1(self, input) -> None:
        if(input):
            if (input[0] == '\n'):  #stop when you hit a newline
                return
            else:
                self.num_read += 1
                self.S1(input[1:])
