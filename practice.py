# panagram or not
'''
sentence = input('Enter a sentence: ').lower()
alphabets = 'abcdefghijklmnopqrstuvwxyz'

def panagram_detector(sentence):
    missing_letters=[]
    for i in alphabets:
        if i not in sentence:
            missing_letters.append(i)

    if missing_letters:
        print(sentence, "-is Not a pangram",'missing letters:', missing_letters)
    else:
        print('The Sentence is a panagram')

panagram_detector(sentence)
'''
from itertools import count
from pickletools import long1

# remove duplicates
'''
user_input=input("Enter a String:").split()
print(user_input)
words=[]
for word in user_input:
    if word not in words:
        words.append(word)

print(" ".join(words))
'''
#calculate weight
'''
word=input('enter a word: ').lower()
def calculate_weight(word):
    total_weight = 0
    for i in word:
        if i.isalpha():
            weight=ord(i)-96
            total_weight= total_weight+weight
    return total_weight

weight=calculate_weight(word)
print('the weight of the word is ',weight)
'''
# S is first character with unique letters in a word
strings=input('enter words: ').split()
print(strings)
def s_word(strings):
    l1 = []
    for i in strings:
        if i[0]=='s' or i[0]=='S':
            if len(i)==len(list(set(i))):
                l1.append(i)
    return l1
obj=s_word(strings)
print(set(obj))




#reverse the given sentence but preserve the order of word
'''
input_sentence = input("Enter a sentence:")

input_rev=input_sentence[::-1].replace(' ','')

print(input_rev)
count=0
word=[]
for i in input_sentence:
    if i==' ':
        word.append(i)
        print(word)
    else:
        word.append(input_rev[count])
        count+=1


output="".join(word)
print(output)
'''

#fibonacci series
'''
n=int(input('enter a num: '))
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        temp=a
        a=b
        b=temp+b

fibonacci(n)
'''
