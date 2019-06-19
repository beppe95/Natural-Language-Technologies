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


def get_parent(index: tuple) -> tuple:
    """
    Finds node's parent index.

    :param index: tuple which contains the node's index
    :return: index of the parent node
    """
    return index[:-1]


def get_right_child(index: tuple) -> tuple:
    """
    Finds node's right child index.

    :param index: tuple which contains the node's index
    :return: index of the right child node
    """
    return index + (1, )


def get_syntactic_tree(tree_list: list) -> Tree:
    """
    Looks for the first tree, contained into tree_list param, whose label is equal to the non-terminal symbol 'S'
    which is the start symbol of the CFG grammar.

    If no tree is founded, exit we'll be called up with 'No tree founded inside CKY table!'.

    :param tree_list: list containing the syntactic trees built-up with CKY algorithm.
    :return: first tree whose label is equal to the non-terminal symbol 'S'
    """
    for current_tree in tree_list:
        if current_tree.label() == Nonterminal('S'):
            current_tree.draw()
            return current_tree

    exit('No tree founded inside CKY table!')
