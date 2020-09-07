"""Assignment for session 7 based on first class functions part 2"""
import operator
import random
import math
from functools import reduce
from functools import partial
import re

# TODO: 1. Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
fib_list = fib(21) # Generate pre-calculated list of Fibobacci number (fib(22) is greater than 10K)
test_list = [1,2,3,4,6,55,67,99,144]

list(filter(lambda x: True if x in fib_list else False,test_list)) #<- Solution 1
# output: [1, 2, 3, 55, 144]

# TODO: # 2. Using list comprehension (and zip/lambda/etc if required) write an expression that
# TODO:  2.1 add 2 iterables a and b such that a is even and b is odd
l1 = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = list(range(21,45,3)) # [21, 24, 27, 30, 33, 36, 39, 42]

l3 = [a+b for a,b in zip(l1,l2) if a%2==0 and b%2!=0] #<- Solution 2.1
# output: [21, 29, 37, 45]

# TODO: 2.2 strips every vowel from a string provided (tsai>>t s)
str1 = 'tsai The school of AI'
''.join([x for x in str1 if x not in {'a', 'A', 'e','E','i', 'I','o', 'O','u', 'U'}])  # Vovels = A, E, I, O, U <- Solution 2.2
# output: 'ts Th schl f '

# TODO: 2.3 acts like a ReLU function for a 1D array
weights = [round(random.uniform(-5,5),1) for _ in range(10)] # Generate a weight vector of size 10 ->[-4.5, 3.7, -0.1, -1.1, -5.0, 3.7, 4.9, 2.3, -2.7, -2.5]
relu_wghts = [x if x >= 0 else 0 for x in weights] #<- Solution 2.3
# output: [0, 3.7, 0, 0, 0, 3.7, 4.9, 2.3, 0, 0] for the weights vector mentioned in comment above

# TODO: 2.4 acts like a sigmoid function for a 1D array
sigm_wghts = [round(1 / (1 + math.exp(-x)),2) for x in weights] #<- Solution 2.4
# output: [0.01, 0.98, 0.48, 0.25, 0.01, 0.98, 0.99, 0.91, 0.06, 0.08] for the weights vector mentioned in comment above

# TODO: 2.5 Takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
str2 = 'abcdefghijklmnopqrstuvwxyz'
''.join([chr(ord(ch)+5) if ord(ch) < 118 else chr((ord(ch)+5)%122+96) for ch in str2 ]) #<- Solution 2.5
# output: 'fghijklmnopqrstuvwxyzabcde'

# TODO: 3 A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words
with open('google_prof_words.txt') as f:
        lines = [line.rstrip().lower() for line in f]

text = """As a teenager, I was banned from an Atheist Republic group of which Armin was admin.
Why? I broached a controversial topic. But I had broken no rule. The geniuses simply couldn't handle it,
they branded it crazy and expelled me. I learned that day they don't really care for FOE. Received a lot
of hate from "champions of free speech" for this thread. Armin himself abused me and RTed extremely abusive tweets.
Not one counter.All of them said "how could you justify abuse" when I never justified any abuse while abusing me at the same time.
Oh the irony!I personally detest both the ideas. Insulting someone's mother and insulting mother goddess. And I am not justifying any abuse.
I just wish some people realise all humans hold some ideas dear and don't like those to be insulted.The pain of insult is the same
Completely missing the point.  I think India is just very new when it comes to freedom of expression.
They might just not exactly understand how it all works.  It’s funny to watch them interpret and explain things.
It’s like somebody who came to class a few years late"""

# Convert to lowercase then, Split text into tokens (words), leaving out punctuation, then use regex to split on non-alphanumeric characters
output = 'Good Comment' if not len(([wrd for wrd in re.split("[\\s.,!?:;'\"-]+",text.lower()) if wrd in lines])) else 'Bad Comment' # <- Solution 3
# output: 'Good Comment'

# TODO 4 Using reduce function-
# TODO: 4.1 add only even numbers in a list
lst1 = list(random.randint(1,100) for _ in range(5)) # [48, 89, 56, 88, 31]
lst_sum_even = reduce(lambda a,b: a+b if not b%2 else a,lst1,0) #< - Solution 4.1
# output: 192 for the input mentioned in the comment above

# TODO: 4.2 find the biggest character in a string (printable ascii characters)
str3 = 'sachzin'+chr(800)+'test' # sachzin'̥'test
reduce(lambda a,b: a if ord(a)>ord(b) else b,str3) #< - Solution 4.2
# output: '̥'

# TODO: 4.3 adds every 3rd number in a list
lst1 = [1,2,3,4,5,6]
reduce(lambda a,b: a+b, [val for indx, val in enumerate(lst1) if not (indx+1)%3]) #<- Solution 4.3
# output: 9

# TODO: 5. Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates,
# where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999
# there is no need to use random.choice, chr(random.randint(65,90)) is sufficient
['KA'+str(random.randint(10,99))+chr(random.randint(65,90))+random.choice([chr(x) for x in range(65,91)])+str(random.randint(1000,9999)) for _ in range(15)]  #<-Solution 5
# output: ['KA34QN8304', 'KA80DC2172', 'KA13PK4076', 'KA47UW8000', 'KA62RX5849', 'KA10LE2210', 'KA94JJ9110', 'KA53IU6857',
# 'KA33LL5787', 'KA97MG9930', 'KA16BG5312', 'KA30UF9646', 'KA49UD8503', 'KA22WX1692', 'KA44IS7992']

#TODO: 6. Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided.
# Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided
def num_plate(state, last_four_start, last_four_end, num):
    """Generates number plates
    Inputs:
        state: Two char string in caps for the state
        last_four_start: Start of range for last four numbers letters of number plate between 1000 to 9999
        last_four_end: End of range for last four numbers letters of number plate between 1000 to 9999
        num: number of plates to be returned as output
    Returns:
        num_plate: List of number plate with number in KADDAADDDD format, D stands for a digit, and A stands for Capital alphabets"""

    if not isinstance(state, str):
        raise TypeError(f"State can be only two char String")
    if not isinstance(last_four_start,int):
        raise TypeError(f"Last four digits should be between 1000 and 9999")
    if not isinstance(last_four_end,int):
        raise TypeError(f"Last four digits should be between 1000 and 9999")
    if not state:
        raise ValueError(f"State can't be null")

    cap_char = [chr(x) for x in range(65,91)]

    num_plate = [state+str(random.randint(10,99))+random.choice(cap_char)+random.choice(cap_char)+str(random.randint(last_four_start,last_four_end)) for _ in range(num)]

    return(num_plate)

func_num_plt = partial(num_plate,last_four_start=1000,last_four_end=9999, num=15) # Define partial function <- Solution 6
func_num_plt('DL')
# output: ['DL21BA5281', 'DL31VT1361', 'DL72LB8375', 'DL49MP5041', 'DL69RZ7479', 'DL71AM8685', 'DL75MU5541', 'DL60WK1447',
# 'DL71EO8572', 'DL38SD5235', 'DL73KB8382', 'DL76KN3589', 'DL27QS5296', 'DL83VJ3474', 'DL93WN1175']
