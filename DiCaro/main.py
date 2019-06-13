from DiCaro.utils import make_novel_dict, named_entity_tagging, relation_extraction


def main():
    novel_dict = make_novel_dict("alice_in_wonderland")

    ne = named_entity_tagging(novel_dict[1][0][0])
    print(ne, "\n")

    relation = relation_extraction(ne, r'.*\bin\b(?!\b.+ing)')


main()


