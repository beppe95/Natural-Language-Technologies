def remove_asterisks(sentence: str) -> str:
    list_sentence = list(sentence)
    list_sentence.remove("*")
    return ''.join(list_sentence)