from Radicioni.WSD.lesk_algorithm import simplified_lesk, remove_stopwords_lesk, extended_context_lesk

'''
- Arms bend at the elbow.
- Germany sells arms to Saudi Arabia.
- The key broke in the lock.
- The key problem was not one of quality but of quantity. 
- Work out the solution in your head.
- Heat the solution to 75° Celsius. 
- The house was burnt to ashes while the owner returned.
- This table is made of ash wood.
- The lunch with her boss took longer than she expected. 
- She packed her lunch in her purse.
- The classification of the genetic data took two years.
- The journal Science published the classification this month.
- His cottage is near a small wood.
- The statue was made out of a block of wood.
'''


def main():
    sent = 'The statue was made out of a block of wood.'
    word = 'wood'

    print(simplified_lesk(word, sent).definition())
    print(remove_stopwords_lesk(word, sent).definition())
    print(extended_context_lesk(word, sent).definition())


main()
