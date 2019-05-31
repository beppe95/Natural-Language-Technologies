from DiCaro.utils import make_novel_dict


def main():
    novel_dict = make_novel_dict("alice_in_wonderland")

    for elem in novel_dict[1][0]:
        print(elem, "\n")


main()


