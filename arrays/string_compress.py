import pprint

# Given a string in the form "AAAAABBBCCCC" compress it to become 'A5B3C3'. The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'

def compress(s):
    # This solution compresses without checking. Known as the Run Length Compression algorithm

    r = ''
    l = len(s)

    if l == 0:
        return ''

    if l == 1:
        return s+'1'

    cnt = 1
    i = 1

    while i < l:

        # if the current element is equal to the element before it
        if s[i] == s[i-1]:
            cnt += 1
       
        else: 
            # Otherwise we store the previous datta
            r = r + s[i-1] + str(cnt)
            # reinit cnt
            cnt = 1

        i += 1

    # we add up all the rs together
    r = r + s[i-1] + str(cnt)

    return r

pprint.pprint(compress('AAAAAaaaBBBCCCCccccW'))