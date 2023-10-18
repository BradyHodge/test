from predicate import Predicate
from rule import Rule

class Datalog():
    def __init__(self, schemes: list[Predicate], facts: list[Predicate], rules: list[Rule], queries: list[Predicate]):
        self.schemes = schemes
        self.facts = facts
        self.rules = rules
        self.queries = queries
    def to_string(self):
        print(f'Schemes({len(self.schemes)})')
        for scheme in self.schemes:
            print(scheme.to_string())
            
        print(f'Facts({len(self.facts)}):')
        for fact in self.facts:
            print(fact.to_string())
            
        print(f'Rules({len(self.rules)}):')
        for rule in self.rules:
            print(rule.to_string())
            
        print(f'Queries({len(self.queries)}):')
        for query in self.queries:
            print(query.to_string())