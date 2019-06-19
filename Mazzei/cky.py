from sys import exit
from numpy import ndarray
from nltk import CFG, Tree
from Mazzei.utils import find_lhs_lexical_rule, find_lhs_grammar_rule, get_syntactic_tree


def cky(words: list, grammar: CFG) -> Tree:
    """
    The Cocke Kasami Younger Algorithm (CKY) is an efficient parsing algorithm for Context-Free grammars.

    The structure of the rules must be in Chomsky Normal Form. CNF rules' right hand side can contain:
        1 - at most 2 symbols;
        2 - a terminal;
        3 - a null string identified by ε

    Given a sentence, the algorithm builds up, via dynamic programming, a syntactic tree consistent with the CFG input
    grammar.

    :param words: sentence split into words
    :param grammar: CFG grammar
    :return: syntactic tree, instance of nltk Tree.
    """
    table_dimension = len(words) + 1
    table = ndarray(shape=(table_dimension, table_dimension), dtype=list)

    for j in range(1, table_dimension):
        table[j - 1, j] = list()

        lexical_lhs = find_lhs_lexical_rule(words[j - 1], grammar)
        if lexical_lhs is not None:
            table[j - 1, j].append(Tree(lexical_lhs, [words[j - 1]]))

        for i in reversed(range(0, j - 1)):
            table[i, j] = list()
            for k in range(i + 1, j):
                if table[i, k] is not None and len(table[i, k]) != 0 \
                        and table[k, j] is not None and len(table[k, j]) != 0:

                    for non_terminal_1 in table[i, k]:
                        for non_terminal_2 in table[k, j]:

                            current_lhs = find_lhs_grammar_rule(non_terminal_1, non_terminal_2, grammar)
                            if current_lhs is not None:
                                table[i, j].append(Tree(current_lhs, [non_terminal_1, non_terminal_2]))

    if len(table[0, table_dimension - 1]) != 0:
        return get_syntactic_tree(table[0, table_dimension - 1])
    else:
        exit('Sentence not supported by chosen grammar!')


