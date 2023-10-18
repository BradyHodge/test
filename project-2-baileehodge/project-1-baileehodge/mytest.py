class FSA:
    num_read: int = 0
    new_lines_read: int = 0

    def __init__(self, name: str):
        ...
        self.fsa_name: str = name
        self.start_state: function = self.S0
        self.accept_states: set[function] = set()
        self.input_string: str = ""
        self.num_chars_read: int = 0
    
    def S0(self) -> None:
        raise NotImplementedError()
    
    def run(self, input_string: str) -> bool:
        #self.reset()
        #self.s0(input_string) 
        self.input_string = input_string
        current_state: function = self.start_state
        while self.num_chars_read < len(self.input_string):
            current_state = current_state()
        if current_state in self.accept_states:
            return True
        else:
            return False


    def reset(self) -> None:
        #self.num_lines_read = 0
        #self.new_lines_read = 0
        self.num_chars_read = 0
        self.input_string = ""
        ...

    def get_fsa_name(self) -> str: 
        return self.fsa_name

    def set_name(self, FSA_name) -> None:
        self.fsa_name = FSA_name

    def __get_current_input(self) -> str:  # The double underscore makes the method private
        ...

class ColonDashFSA(FSA):
    def __init__(self) -> None:
        FSA.__init__(self, "ColonDashFSA")
        self.accept_states.add(self.S2)
    
    def S0(self, input) -> None:
        if (input[0] == ':'):
            self.num_read += 1
            self.S1(input[1:])
    
    def S1(self, input) -> None:
        if (not input):
            self.num_read = 0
            return
        
        if (input[0] == '-'):
            self.num_read += 1
            self.S2(input[1:])
            return
        ...



import unittest


class TestFSA(unittest.TestCase):
    def setUp(self):
        with open('./project1-passoff/20/input22.txt', 'r') as file:
            input22 = file.read()
        self.fsa = FSA("test_fsa")

    def test_run(self):
        # Call the run method with some input
        with open('./project1-passoff/20/answer22.txt', 'r') as file:
            answer22 = file.read()

        result = self.fsa.run(answer22)

        # Assert that the run method returned the expected result
        self.assertEqual(result, answer22.txt)

if __name__ == '__main__':
    unittest.main()