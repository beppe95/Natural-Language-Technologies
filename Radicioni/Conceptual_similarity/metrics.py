import math
from nltk.corpus import wordnet
from nltk.corpus.reader.wordnet import Synset


def wu_palmer_similarity(s1: Synset, s2: Synset) -> float:
    """
    
    :param s1: 
    :param s2: 
    :return: 2 * depth(LCS) ? / depth(s1) ? + depth(s2) ?
    """
    return None


def shortest_path_similarity(s1: Synset, s2: Synset) -> float:
    """

    :param s1:
    :param s2:
    :return:
    """
    return None


def leakcock_chodorow_similarity(s1: Synset, s2: Synset) -> float:
    """

    The relationship is given as -log(p/2d) where p is the shortest path length and d the taxonomy depth.

    :param s1:
    :param s2:
    :return:
    """
    return None
