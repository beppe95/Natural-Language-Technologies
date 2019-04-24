from nltk import CFG, Nonterminal


def find_head_lr(word: str, grammar: CFG):
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


def find_head_gr(first: Nonterminal, second: Nonterminal, grammar: CFG):
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