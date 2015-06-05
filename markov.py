
# coding: utf-8

# In[7]:

from collections import defaultdict
from random import choice as rc
from random import sample as rs
import re


# In[8]:

# Go to gutenberg.org and find a book you'd like to use
# as your corpus. Save the plain text file as 'book.txt'.

fileObj = open('book.txt', 'r')
fileText = fileObj.read().lower() # note .lower()
fileObj.close()


# In[9]:

# 1) tokenize the book

tokens = re.findall(r"\b[a-zA-Z0-9']+\b", fileText)

# Test our data...
# print len(tokens)
# print rs(tokens, 10)


# In[16]:

# 2) Build n-gram model as a dictionary

# NOTE: There are lots of ways to do this!
# We could use sets instead of lists,
# we could count the number of times each
# word appears, and add weights based on
# that, etc, etc, etc.

nGramDict = defaultdict(list)

for i in range(1, len(tokens)-1):
    nGramDict[(tokens[i-1], tokens[i])].append(tokens[i+1])
    
# Test our data...
# print nGramDict[('he', 'was')]


# In[28]:

# 3) Make generator function
# NOTE: Again, here are lots of ways to do this!

def generate(numWords, seed=rc(nGramDict.keys())):
    if len(seed) != 2:
        raise Exception("Exactly 2 seed tokens required!")
    w1, w2 = seed
    result = list(seed)
    for _ in range(numWords):
        try:
            w3 = rc( nGramDict[(w1, w2)] )
        except IndexError:
            raise Exception("Seed tokens not present in corpus!")
        result.append(w3)
        w1, w2 = w2, w3 # Why do we need to do it this way?
    return result
        

# print ' '.join(generate(1000, seed=('the', 'whale')))


# In[ ]:

# How do we decide what text to use?
# How would we find where sentences begin and end?
# Let's export this to a Python file so we can reuse this code...

