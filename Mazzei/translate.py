from nltk import Tree


def yoda_translation(root: Tree, translation_rules: list):
    """
    Provides translation from italian language to Yoda-speak language.

    It filters out from nltk tree's indices of the subtree whose label is contained in 'translation_rules'.
    Then, it sets the previously obtained subtree as the new left child of a new syntactic tree.

    :param root: the syntactic tree to be translated
    :param translation_rules: list of Nonterminal object used to provide translation from italian to Yoda-speak language
    """

    to_be_moved = list((index for index in root.treepositions()
                        if isinstance(root[index], Tree) and root[index].label() in translation_rules))[0]

    if to_be_moved:
        prefix = root.__getitem__(to_be_moved)
        root.__setitem__(to_be_moved, Tree("ε", []))
        root = Tree('Yoda Translation', [prefix, root])

    root.draw()
