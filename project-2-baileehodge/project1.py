from .project_2_classes.lexer_fsm import LexerFSM
from typing import List


# Return your program output here for grading (can treat this function as your "main") -
def project1(input: str) ->str:
    lexer: LexerFSM = LexerFSM()
    lexer.run(input)
    tokens = ""
    for token in lexer.tokens:
        tokens += token.to_string()
        tokens += "\n" 

    #TODO: make this print the undefined thing when it's undefined
    if (token.token_type != "UNDEFINED"):    
        len_tokens = str(len(lexer.tokens))
        tokens += 'Total Tokens = ' + len_tokens
    else:
        #TODO this vvv line does not work, obviously
        line_num = str(token.line)
        tokens += '\nTotal Tokens = Error on line ' + line_num

    return tokens

def read_file_contents(filepath):
    with open(filepath, "r") as f:
        return f.read() 

def read_file_contents(filepath):
    with open(filepath, "r") as f:
        return f.read() 

# Use this to run and debug code within VS Code
if __name__ == "__main__":
    input_contents = read_file_contents("./project1-passoff/20/input23.txt") # Put path to input file here
    print(project1(input_contents))
