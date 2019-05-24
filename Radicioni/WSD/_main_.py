from Radicioni.WSD.simplified_lesk import simplified_lesk
from nltk.wsd import lesk


def main(word: str, sentence: str):
    my_best_sense = simplified_lesk(word, sentence)
    nltk_best_sense = lesk(sentence.split(), word)
    assert my_best_sense == nltk_best_sense
    print(my_best_sense, my_best_sense.definition(), "\n")
    print(nltk_best_sense, nltk_best_sense.definition())


main("bass", "An electric guitar and bass player stand off to one side, not really part of the scene")
