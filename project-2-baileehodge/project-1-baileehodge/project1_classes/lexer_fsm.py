from .fsa_classes.fsa import FSA
from .fsa_classes.colon_dash_fsa import ColonDashFSA
from .fsa_classes.colon_fsa import ColonFSA
from .fsa_classes.period_fsa import PeriodFSA
from .fsa_classes.q_mark_fsa import QMarkFSA
from .fsa_classes.left_paren_fsa import LeftParenFSA
from .fsa_classes.right_paren_fsa import RightParenFSA
from .fsa_classes.comma_fsa import CommaFSA
from .fsa_classes.comment_fsa import CommentFSA
from .fsa_classes.id_fsa import IDFSA
from .fsa_classes.string_fsa import StringFSA
from .fsa_classes.undefined_fsa import UndefinedFSA
from .token import Token

class LexerFSM:
    tokens: list[Token]
    automata: list[FSA]

    def __init__(self):
        self.tokens: list[Token] = []
        self.automata: list[FSA] = []
        
        # Instantiate FSAs
        self.colon_dash_fsa = ColonDashFSA()
        self.colon_fsa = ColonFSA()
        self.period_fsa = PeriodFSA()
        self.q_mark_fsa = QMarkFSA()
        self.left_paren_fsa = LeftParenFSA()
        self.right_paren_fsa = RightParenFSA()
        self.comma_fsa = CommaFSA()
        self.comment_fsa = CommentFSA()
        self.string_fsa = StringFSA()
        self.undefined_fsa = UndefinedFSA()
        self.id_fsa = IDFSA()  # This will handle Schemes, Rules, Queries, and Facts
        
        # Add FSAs to the automata list
        self.automata.extend([
            self.colon_dash_fsa, self.colon_fsa, self.period_fsa,
            self.q_mark_fsa, self.left_paren_fsa, self.right_paren_fsa,
            self.comma_fsa, self.comment_fsa, self.string_fsa,
            self.id_fsa, self.undefined_fsa
        ])

    
    def run(self, input: str) -> None:
        line_num: int = 1
        token_type = "null"
        while (input): 
            if(input[0].isspace()):
                if(input[0] == '\n'): 
                    line_num += 1
                input = input[1:]
                continue

            max_read: int = 0
            max_automaton: FSA = None
            for automaton in self.automata:
                num_read = 0
                automaton.run(input)
                num_read = automaton.get_num_read()
                if(num_read > max_read):
                    max_read = num_read
                    max_automaton = automaton
                    # print(automaton.token_type)


            if max_automaton is None:
                max_automaton = "UNDEFINED"

            # create the token associated with the max automaton
            # prev token_type = max_automaton.get_name()
            if max_automaton != "UNDEFINED":
                token_type = max_automaton.token_type
            else:
                token_type = "UNDEFINED"
            # token_value = input[:max_read]
            token_value = input[:max_read].rstrip('\n')
            token = Token(token_type, token_value, line_num)
            self.tokens.append(token)
            if (token_type == "UNDEFINED"):
                break


            input = input[max_read:]
            line_num += max_automaton.get_new_lines_read()

        #create an EOF token
        if (token_type != 'UNDEFINED'):
            eof_token = Token("EOF", "", line_num)
            self.tokens.append(eof_token)
            
        #printing functionality formerly in project1.py

        len_tokens = str(len(self.tokens))

        for token in self.tokens:
            if token.token_type == 'UNDEFINED':
                #print(token.to_string())  # Print the current token
                len_tokens = f"Error on line {token.line}"
                break
            else:
                print(token.to_string())

        #print(f'Total Tokens = {len_tokens}')



        #end project1.py repeat