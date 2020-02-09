import pprint

# Given a string, determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return true. Otherwise, it should return false.


def uni_char1(s):
    return len(set(s)) == len(s)


pprint.pprint(uni_char1('abcd'))

def uni_char(s):

    chars = set()

    for let in s:

        if let in chars:
            return False
        
        else:
            chars.add(let)

    return True

