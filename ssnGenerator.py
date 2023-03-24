import random

def generateRandomSSN():
    possible_chars = "0123456789"

    prefixValues = [random.choice(possible_chars) for _ in range(3)]
    prefix = ''.join(prefixValues)

    midfixValues = [random.choice(possible_chars) for _ in range(2)]
    midfix = ''.join(midfixValues)

    postfixValues = [random.choice(possible_chars) for _ in range(4)]
    postfix = ''.join(postfixValues)
 
    ssn = prefix + '-' + midfix + '-' + postfix

    return ssn