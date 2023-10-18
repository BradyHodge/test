import os
from project_2_classes.my_token import Token
from project_2_classes.parse import Parser
from project_2_classes.lexer_fsm import LexerFSM
# import your lexer

def project2(input: str) -> str:
    lexer = LexerFSM()
    lexer.run(input)
    tokens = lexer.get_tokens()

    # this is our example list of tokens, for the actual project you will use the lexer to generate this
    # tokens = [
    #     Token("ID", "snap", 1),
    #     Token("LEFT_PAREN", "(", 1),
    #     Token("ID", "StudentId", 1),
    #     Token("COMMA", ",", 1),
    #     Token("ID", "Name", 1),
    #     Token("COMMA", ",", 1),
    #     Token("ID", "Address", 1),
    #     Token("COMMA", ",", 1),
    #     Token("ID", "PhoneNumber", 1),
    #     Token("RIGHT_PAREN", ")", 1)
    # ]    
    # scheme   	-> 	ID LEFT_PAREN ID idList RIGHT_PAREN
    # idList  	-> 	COMMA ID idList | lambda


    parser = Parser()

    return parser.run(tokens)


def read_file_contents(filepath):
    with open(filepath, "r") as f:
        return f.read()


# Use this to run and debug code within VS
if __name__ == "__main__":
    # input_contents = read_file_contents("Path to input file goes here")
    os.chdir('.')
    input_contents = read_file_contents("./project2-passoff/80/input4.txt")
    print(project2(input_contents))
    
    
    
    
    # how to run
    # pres run on project2.py






# ORDER OF OPS
# [1] Implement more functions in parser.oy for each rule in the grammar - DONE
# [2] test
# finish that ^
# [3] make your datalog program classes
# [4] populate the datalog program classes
# resources for 3 and 4 include the diagrams, the help session video, etc
# [5] implement the datalog program classes in the parser