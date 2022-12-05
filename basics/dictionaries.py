# The dictionary Junior shows a schedule for a junior year semester. 
# The key is the course name and the value is the number of credits.
# Find the total number of credits taken this semester and assign it to
# the variable credits. Do not hardcode this – use dictionary accumulation!

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for i in Junior:
    credits = credits + Junior[i]




# Create a dictionary, freq, that displays each character in string str1
# as the key and its frequency as the value.

str1 = "peter piper picked a peck of pickled peppers"
freq = {}

for c in str1:
    if c not in freq:
        # we have not seen this character before, so initialize a counter for it
        freq[c] = 0

    #whether we've seen it before or not, increment its counter
    freq[c] = freq[c] + 1




# Create a dictionary, freq_words, that contains each word in string str1 as
# the key and its frequency as the value.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
st = str1.split()

for word in st:
    if word not in freq_words:
        # we have not seen this character before, so initialize a counter for it
        freq_words[word] = 0

    #whether we've seen it before or not, increment its counter
    freq_words[word] = freq_words[word] + 1




# Create a dictionary called wrd_d from the string sent, so that the key is a
# word and the value is how many times you have seen that word.

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
sent = sent.split()
wrd_d = {}

for word in sent:
    if word not in wrd_d:
        # we have not seen this character before, so initialize a counter for it
        wrd_d[word] = 0

    #whether we've seen it before or not, increment its counter
    wrd_d[word] = wrd_d[word] + 1

print(wrd_d)




# Create the dictionary characters that shows each character from the string
# sally and its frequency. Then, find the most frequent letter based on the
# dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"
characters = {}

for word in sally:
    if word not in characters:
        # we have not seen this character before, so initialize a counter for it
        characters[word] = 0

    #whether we've seen it before or not, increment its counter
    characters[word] = characters[word] + 1

thekeys = characters.keys()
best_char = list(thekeys)[0]  # Have to turn ks into a real list before using [] to select an item
for m in thekeys:
    if characters[m] > characters[best_char]:
        best_char = m

print("key " + best_char + " has the highest value, " + str(characters[best_char]))


# Find the least frequent letter. Create the dictionary characters that shows
# each character from string sally and its frequency. Then, find the least
# frequent letter in the string and assign the letter to the variable
# worst_char.

sally = "sally sells sea shells by the sea shore and by the road"
characters = {}

for word in sally:
    if word not in characters:
        # we have not seen this character before, so initialize a counter for it
        characters[word] = 0

    #whether we've seen it before or not, increment its counter
    characters[word] = characters[word] + 1

thekeys = characters.keys()
worst_char = list(thekeys)[0]  # Have to turn ks into a real list before using [] to select an item
for n in thekeys:
    if characters[n] < characters[worst_char]:
        worst_char = n

print("key " + worst_char + " has the lowest value, " + str(characters[worst_char]))




# Create a dictionary named letter_counts that contains each letter and the
# number of times it occurs in string1. Challenge: Letters should not be
# counted separately as upper-case and lower-case. Intead, all of them should
# be counted as lower-case.

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts = {}

for char in string1.lower() :
    if char not in letter_counts :
        letter_counts[char] =0
    letter_counts[char]=letter_counts[char]+1



# Create a dictionary called low_d that keeps track of all the characters in
# the string p and notes how many times each character was seen. Make sure
# that there are no repeats of characters as keys, such that “T” and “t”
# are both seen as a “t” for example.

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}

for char in p.lower() :
    if char not in low_d :
        low_d[char] =0
    low_d[char]=low_d[char]+1
