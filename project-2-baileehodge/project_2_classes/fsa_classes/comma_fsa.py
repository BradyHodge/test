from .fsa import FSA


class CommaFSA(FSA):
    def __init__(self):
        super().__init__()
        self.token_type = "COMMA"
    
    def S0(self, input) -> None:
        if (input[0] == ','):
            self.num_read += 1
            return
    
        else:
            self.num_read = 0
            return

