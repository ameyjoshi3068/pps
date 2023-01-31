#Importing random module
from random import shuffle

#Defining decoder function
def mydecode(sentence):
    sentence=list(sentence.split())
    dec_sentence=[]
    for word in sentence:
        if len(word)<3:
            dec_sentence.append(word[::-1])
        else:
            word=word[3:-3]
            last=word[-1]
            dec_sentence.append((last+word[:-1]))
    return " ".join(dec_sentence)

#Defining a encoder
def myencode(sentence):
    wordlist=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    sentence=list(sentence.split())
    enc_sentence=[]
    for word in sentence:
        if len(word)<3:
            enc_sentence.append(word[::-1])
        else:
            shuffle(wordlist)
            letters1="".join(wordlist[:3])
            shuffle(wordlist)
            letters2="".join(wordlist[:3])
            firstW=word[0]
            word=word[1:]+firstW
            list1=letters1+word+letters2
            enc_sentence.append(list1)
    return " ".join(enc_sentence)

enstr=myencode("My name is amey")
print(enstr)
print(mydecode(enstr))