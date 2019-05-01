from nltk import CFG, Tree, Nonterminal


def find_lhs_lexical_rule(word: str, grammar: CFG) -> Nonterminal:
    """
    Finds the LHS of a lexical rule contained in the input CFG grammar.

    :param word: the RHS of a lexical rule
    :param grammar: input CFG grammar
    :return: the LHS of a lexical rule, if it exists
    """
    lexical_rules = list((prod for prod in grammar.productions()
                         if len(prod.rhs()) == 1 and prod.rhs()[0] == word))
    if lexical_rules:
        return lexical_rules[0].lhs()


def find_lhs_grammar_rule(first: Tree, second: Tree, grammar: CFG) -> Nonterminal:
    """
    Finds the LHS of a grammar rule contained in the input CFG grammar.

    :param first: first half of the grammar rule's RHS
    :param second: latter half of the grammar rule's RHS
    :param grammar: input CFG grammar
    :return: the LHS of a grammar rule, if it exists
    """
    grammar_rules = list((prod for prod in grammar.productions()
                          if len(prod.rhs()) == 2
                          and first.label() == prod.rhs()[0] and second.label() == prod.rhs()[1]))

    if grammar_rules:
        return grammar_rules[0].lhs()


def get_node_to_be_moved(vp_index: tuple) -> tuple:
    return vp_index[:len(vp_index) - 1] + (1,)
