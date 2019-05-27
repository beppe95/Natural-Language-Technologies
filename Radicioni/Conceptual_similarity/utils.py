from nltk.corpus import wordnet

#Loro utilizzano max_depth che prende in input un POS
def wordnet_max_depth() -> int:
    """
    Iterate through each synset in wordnet and find the distance to their top most hypernym.

    :return: max taxonomy depth for a specified wordnet version
    """
    return max(max(len(hyp_path) for hyp_path in ss.hypernym_paths()) for ss in wordnet.all_synsets())
