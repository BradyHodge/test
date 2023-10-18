

class FSA:
    num_read: int = 0
    new_lines_read: int = 0

    def __init__(self):
        self.token_type = None
        
    
    def S0(self) -> None:
        raise NotImplementedError()
    
    def run(self, input_string: str) -> bool:
        self.reset()
        self.S0(input_string)
        

    def reset(self) -> None: 
        self.num_lines_read = 0
        self.new_lines_read = 0
        self.num_read = 0

    def get_name(self) -> str: 
        return self

    def set_name(self, FSA_name) -> None:
        ...

    def __get_current_input(self) -> str:  # The double underscore makes the method private
        ...

    def get_num_read(self): 
        return self.num_read
    
    def get_new_lines_read(self):
        return self.new_lines_read