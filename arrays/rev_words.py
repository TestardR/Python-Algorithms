import pprint

# Given a string of words, reverse all the words

# def rev_words1(s):
#     return " ".join(reversed(s.split()))

# def rev_words2(s):
#     return " ".join(s.split()[::-1])

# rev_words1('I am the best')


def rev_words(s):   
    words = []
    length = len(s)
    spaces = [' ']

    i = 0

    while i < length: 
        
        if s[i] not in spaces:

            word_start = i

            while i < length and s[i] not in spaces:

                i += 1

            words.append(s[word_start:i])

        i += 1

    return ' '.join(reversed(words))

pprint.pprint(rev_words('I am the best'))
