from nltk.corpus import wordnet
from nltk.corpus.reader.wordnet import Synset


def simplified_lesk(word: str, sentence: str) -> Synset:
    """
    Implements the well-known word disambiguation algorithm.

    :param word: the word to be disambiguated
    :param sentence: input sentence which contains param 'word'
    :return: best_sense, which is a Wordnet Synset, for param 'word'
    """

    '''synsets = wordnet.synsets(word)
    context = set(sentence.split())

    max_overlap = 0
    best_sense = synsets[0]

    for sense in synsets:
        signature = set(sense.definition().split(" "))
        overlap = len(signature.intersection(context))

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense'''
    synsets = wordnet.synsets(word)
    best_sense = wordnet.synsets(word)[0]
    max_overlap = 0
    context = set(sentence.split(" "))

    for sense in synsets:
        signature = set(sense.definition().split(" "))  # examples
        overlap = len(signature - (signature - context))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense

