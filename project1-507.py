import math
# Problem 2. Palindromes
#
# Given a string, determine if the string is a palindrome.
#
# Examples:
#     palidrome('anna')  returns 'True'
#     palidrome('abcdef')  returns 'False'
#     palidrome('')  returns 'True'

def palindrome(word):
 ### Your code goes here

    reverseWord = []
    ogWord = list(word)

    for letter in reversed(ogWord) :
        reverseWord.append(letter)

    if ogWord == reverseWord:
        return True
    else :
        return False

  # return '' ### Replace with your code


def test(got, expected):
    score = 0;
    if got == expected:
        score = 3.33;
        print(" OK ",end=" ")
    else:
        print (" XX ", end=" ")
        print("Got: ",got, "Expected: ",expected)
    return score

def main():
    total = 0;
    print()
    print ('Task C: palindromes' """Each OK is worth five points.""")

 #  """ If this is what you get, you are good to go. Each OK is worth five points.
 # OK  Got:  True Expected:  True
 # OK  Got:  False Expected:  False
 # OK  Got:  True Expected:  True
 #  """

    total += test(palindrome('anna'), True)
    total += test(palindrome('bookkeeper'), False)
    total += test(palindrome('a'), True)

    print("You final score is: ", math.ceil(total))

if __name__ == '__main__':
    main()
