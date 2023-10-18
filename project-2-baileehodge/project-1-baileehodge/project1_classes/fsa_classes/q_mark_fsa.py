from .fsa import FSA


class QMarkFSA(FSA):
    def __init__(self):
        super().__init__()
        self.token_type = "Q_MARK"
    
    def S0(self, input) -> None:
        if (input[0] == '?'):
            self.num_read += 1
            return
    
        else:
            self.num_read = 0
            return

