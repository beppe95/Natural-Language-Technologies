import numpy
from nltk import CFG, Tree
import Mazzei.utils as utils


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
    table = numpy.ndarray(shape=(table_dimension, table_dimension), dtype=list)

    for j in range(1, table_dimension):
        table[j - 1, j] = list()
        table[j - 1, j].append(Tree(utils.find_lhs_lexical_rule(words[j - 1], grammar), [words[j - 1]]))
        for i in reversed(range(0, j - 1)):
            table[i, j] = list()
            for k in range(i + 1, j):
                if table[i, k] is not None and table[k, j] is not None:
                    table[i, j].append(Tree(utils.find_lhs_grammar_rule(list(table[i, k])[0],
                                                                        list(table[k, j])[0], grammar),
                                            [list(table[i, k])[0], list(table[k, j])[0]]))

    return table[0, table_dimension - 1][0] if table[0, table_dimension - 1][0] \
        else Exception("Sentence not supported by written grammar!")
