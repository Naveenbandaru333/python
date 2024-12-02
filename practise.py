#1)check anagram or not
'''inbuilt-method'''
from itertools import count

'''n1=input('enter a word:')
n2=input('enter a word:')
def anagram(n1,n2):
    if sorted(n1)==sorted(n2):
        print('anagram')
    else:
        print('not anagram')

anagram(n1,n2)
'''
'''user-defined'''
n1=input('enter a word:').lower()
n2=input('enter a word:').lower()
def anagram(n1,n2):
    if len(n1)!=len(n2):
        print('not anagram')
        return
    c=0
    for i in n1:
        for j in n2:
            if j in i:
              c=c+1

    if c==count(len(n1)):
        print('anagram')
    else:
        print('not anagram') 



anagram(n1,n2)


