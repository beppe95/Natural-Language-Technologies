from nltk.corpus import wordnet
from nltk.corpus.reader.wordnet import Synset


def simplified_lesk(word: str, sentence: str) -> Synset:
    """
    Implements a simplified version of Lesk algorithm.

    :param word: the word to be disambiguated
    :param sentence: input sentence which contains param 'word'
    :return: best_sense, which is a Wordnet Synset, for param 'word'
    """

    synsets = wordnet.synsets(word)
    context = set(sentence.split())

    max_overlap = 0
    best_sense = synsets[0]

    for sense in synsets:
        # get the synset meaning
        signature = set(sense.definition().split(" "))

        # compute the overlap between synset signature and synset context
        overlap = len(signature.intersection(context))

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense


