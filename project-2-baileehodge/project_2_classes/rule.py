from predicate import Predicate

class Rule():
    def __init__(self, head: Predicate, body: list[Predicate]):
        self.head_predicate = head
        self.body_predicates = body

    def to_string(self) -> str:
        return(f'{self.to_string()}')