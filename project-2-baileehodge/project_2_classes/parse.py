from .my_token import Token
from .predicate import Predicate

class Parser():
    def __init__(self):
        self.index = 0
        self.tokens = []
        pass


    def throw_error(self):
        raise ValueError (self.get_curr_token().to_string())
    
    def advance(self):
        self.index += 1

    def get_curr_token(self) -> Token:
        if self.index >= len(self.tokens):
            self.index = len(self.tokens) - 1
            self.throw_error()
        while self.tokens[self.index].token_type == "COMMENT":
            self.advance()
        return self.tokens[self.index]
        
    def get_prev_token_value(self) -> str:
        return self.tokens[self.index - 1]. value

    def match(self, expected_type: str):
        if self.get_curr_token().token_type == expected_type:
            self.advance()
        else:
            self.throw_error()

    def run(self, tokens: list[Token]) -> str:
        self.index: int = 0
        self.tokens: list[Token] = tokens

        try:
            self.parse_datalogProgram()
            return "Success!"
            # scheme: Predicate = self.parse_scheme()
            # return "Success!\n" + scheme.to_string()      
        except ValueError as ve:
            return f"Failure!\n  {ve}"
        
    #datalogProgram	->	SCHEMES COLON scheme schemeList FACTS COLON factList RULES COLON ruleList QUERIES COLON query queryList EOF
    def parse_datalogProgram(self):
        self.match("SCHEMES")
        self.match("COLON")
        self.parse_scheme()
        self.parse_schemeList()
        self.match("FACTS")
        self.match("COLON")
        self.parse_factList()
        self.match("RULES")
        self.match("COLON")
        self.parse_ruleList()
        self.match("QUERIES")
        self.match("COLON")
        self.parse_query()
        self.parse_queryList()
        self.match("EOF")
        
        
    # schemeList -> scheme, schemeList | lambda
    def parse_schemeList(self):
        if self.get_curr_token().token_type == "ID":
            self.parse_scheme()
            self.parse_schemeList()
            return
        else:
            return

    # factList -> fact, factList | lambda
    def parse_factList(self):
        if self.get_curr_token().token_type == "ID":
            self.parse_fact()
            self.parse_factList()
            return
        else:
            return
        
    # ruleList -> fact, ruleList | lambda
    def parse_ruleList(self):
        if self.get_curr_token().token_type == "ID":
            self.parse_rule()
            self.parse_ruleList()
            return
        else:
            return
        
    # queryList -> query, queryList | lambda
    def parse_queryList(self):
        if self.get_curr_token().token_type == "ID":
            self.parse_query()
            self.parse_queryList()
            return
        else:
            return



    # scheme 	-> 	ID LEFT_PAREN ID idList RIGHT_PAREN
    def parse_scheme(self) -> Predicate:
        name: str = ""
        parameters: list[str] = []
        
        self.match("ID")
        name = self.get_prev_token_value()
        self.match("LEFT_PAREN")
        self.match("ID")
        parameters.append(self.get_prev_token_value())
        parameters += self.parse_idList()
        self.match("RIGHT_PAREN")
        return Predicate(name, parameters)
    
    # fact -> ID LEFT_PAREN STRING stringList RIGHT_PAREN PERIOD
    def parse_fact(self) -> Predicate: 
        name: str = ""
        parameters: list[str] = []
        
        self.match("ID")
        name = self.get_prev_token_value()
        
        self.match("LEFT_PAREN")
        self.match("STRING")
        parameters.append(self.get_prev_token_value())
        
        parameters += self.parse_idList()
        
        self.match("RIGHT_PAREN")
        self.match("PERIOD")
        
        return Predicate(name, parameters)
        
    # rule -> headPredicate COLON_DASH predicate predicateList PERIOD
    def parse_rule(self):
        self.parse_headPredicate()
        self.match("COLON_DASH")
        self.parse_predicate()
        self.parse_predicateList()
        self.match("PERIOD")
        
    #query -> predicate Q_MARK
    def parse_query(self) -> Predicate:
        name: str = ""
        parameters: list[str] = []
        
        name = self.get_curr_token().value
        self.parse_predicate()
        
        parameters.append(name)
        parameters =+ self.parse_predicate()
        self.match("Q_MARK")
        return Predicate(name, parameters)
    
##

    # headPredicate -> ID LEFT_PAREN ID idList RIGHT_PAREN
    def parse_headPredicate(self):
        name = self.get_curr_token().value
        self.match("ID")
        self.match("LEFT_PAREN")
        self.match("ID")
        self.parse_idList()
        self.match("RIGHT_PAREN")
        
    # predicate -> ID LEFT_PAREN parameter parameterList RIGHT_PAREN
    def parse_predicate(self):
        self.match("ID")
        self.match("LEFT_PAREN")
        self.parse_parameter()
        self.parse_parameterList()
        self.match("RIGHT_PAREN")

##
    
    # predicateList -> COMMA predicate predicateList | lambda
    def parse_predicateList(self) -> list[str]:
        if self.get_curr_token().token_type == "COMMA":
            self.match("COMMA")
            first_pred: list[str] = self.parse_predicate()
            pred_list: list[str] = self.parse_predicateList()
            return first_pred + pred_list
        else:
            return []
        
    # parameterList -> COMMA parameter predicateList | lambda
    def parse_parameterList(self):
        if self.get_curr_token().token_type == "COMMA":
            self.match("COMMA")
            self.parse_parameter()
            self.parse_parameterList()
            return
        else:
            return
        
    # stringList - > COMMA STRING stringList | lambda
    def parse_stringList(self):
        if self.get_curr_token().token_type == "COMMA":
            self.match("COMMA")
            self.match("STRING")
            self.parse_stringList()
        else:
            return
    
    # parameter -> STRING | ID
    def parse_parameter(self):
        if self.get_curr_token().token_type == "STRING":
            self.match("STRING")
            return self.get_prev_token_value()
        elif self.get_curr_token().token_type == "ID":
            self.match("ID")
            return self.get_prev_token_value()
        else:
            self.throw_error()
            
    
    # idList  	-> 	COMMA ID idList | lambda
    def parse_idList(self) -> list[str]:
        # the first set is {COMMA} << TODO: add a similar statement in all functions
        if self.get_curr_token().token_type == "COMMA":
            self.match("COMMA")
            self.match("ID")
            curr_id: list[str] = [self.get_prev_token_value()]
            # [Name]
            rest_ids: list[str] = self.parse_idList()
            # [Address, PhoneNumber]
            return curr_id + rest_ids
            # -> [Name, Address, PhoneNumber]
        
        #lambda
        else:
            return []
        
        
        
        #remeber to add () or to_string and other functions
        
        # detailed plan