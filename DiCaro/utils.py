from pathlib import Path
from collections import defaultdict
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk, Tree
from nltk.sem import extract_rels, rtuple
from re import compile


def make_novel_dict(novel: str) -> defaultdict:
    """

    :param novel:
    :return:
    """

    dataset_path = Path.cwd() / "datasets" / novel

    with open(dataset_path / "info") as dataset_file:
        dataset_info = dataset_file.readlines()
        numbers_of_chapters = dataset_info[2].split(':')[1]

    novel_dict = defaultdict(tuple)
    for chapter_number in range(1, int(numbers_of_chapters) + 1):
        with open(dataset_path / ("ch" + str(chapter_number))) as chapter_file:
            chapter_content = " ".join(line.rstrip("\n") for line in chapter_file)
            dict_data = ie_pre_process(chapter_content)
            novel_dict[chapter_number] = (dict_data, len(dict_data))

    return novel_dict


def ie_pre_process(sentence: str) -> list:
    """

    :param sentence:
    :return:
    """
    sentence = sent_tokenize(sentence)
    sentence = [word_tokenize(sent) for sent in sentence]
    sentence = [pos_tag(sent) for sent in sentence]
    return sentence


def named_entity_tagging(tagged_sentence: list) -> Tree:
    """

    :param tagged_sentence:
    :return:
    """
    return ne_chunk(tagged_sentence, binary=True)


def relation_extraction(chunk_tree, pattern) -> str:
    """

    :param chunk_tree:
    :param pattern:
    :return:
    """
    reg_expr = compile(pattern)
    for rel in extract_rels('NE', 'NE', chunk_tree, corpus='ieer', pattern=reg_expr):
        print(type(rtuple(rel)))


