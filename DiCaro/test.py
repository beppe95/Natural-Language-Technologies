import re, nltk


def main():
    '''a ='hello,how are you?I am fine,thank you. And you?'

    li = re.split('[?.]', a)'''

    a = "Alice was beginning to get very tired of sitting by her sister on the bank, " \
        "and of having nothing to do: once or twice she had peeped into the" \
        "book her sister was reading, but it had no pictures or conversations in" \
        "it, and what is the use of a book, thought Alice without pictures or" \
        "conversations?" \
        "So she was considering in her own mind (as well as she could, for the" \
        "hot day made her feel very sleepy and stupid), whether the pleasure" \
        "of making a daisy-chain would be worth the trouble of getting up andpicking the daisies, when suddenly a White Rabbit with pink eyes ran" \
        "close by her."



    sent_text = nltk.sent_tokenize(a)
    print(len(sent_text))

    '''for sentence in sent_text:
        tokenized_text = nltk.word_tokenize(sentence)
        print(tokenized_text)'''

main()