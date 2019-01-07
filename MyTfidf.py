import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import math

def clean_text(s):
    """
    This function removes special characters from within a string.
	The function accepts a string input and returns a string output.
    """

    #Replace special characters with ' '
    stripped = re.sub('[^\w\s]', '', s)
    stripped = re.sub('_', '', stripped)

    #Change any whitespace to one space
    stripped = re.sub('\s+', ' ', stripped)

    #Remove start and end white spaces
    stripped = stripped.strip()

    return stripped



text_input = """
A coin goes up the air.
The coin can land on either its head or tail side.
What if a coin is heavier on one side?
Then it is more likely to land on that one side.
"""	


	
cltext = clean_text(text_input)

#raw_text is a tokenized list of unclean sentences
raw_text = sent_tokenize(text_input)

#cleaned_text is a list of clean sentences
cleaned_text = [clean_text(sen) for sen in raw_text]

#mainw is tokenize (breakdown of a sentence into words) of cleaned_text,
#the list order is maintained
mainw = [word_tokenize(sen) for sen in cleaned_text]

#some printings to see the difference if necessary
#print(cleaned_text)
#print(mainw)

#total number of all sentences
totalallsen = len(mainw)

#initialize the main output list, number of elements depends on the number of
#documents
output_list = list(range(0, totalallsen))

#initialize the loop variable, which is used for output_list assignment
counter = 0

#initialize of store has to be done outside the loop
#store is a list to be appended in the following manner:
#[word, aon, tf, idf, tfidf], see the full descriptions below
#store becomes longer with each increasing words in the sentence
store = []

#e.g. output_list = [store1, store2, store3] for a three-sentence example

###full descriptions for store###
#word is the word in the sentence
#aon is short for appear or not, is a list, e.g. [True, False, True]
#means the word appears in sentences 1 and 3, but do not appear in sentence 2
#tf, idf, and tfidf are term frequency, inverse term frequency, and their
#products respectively

for sen in mainw:
    #for each (tokenized) in mainw
    totalsen = len(sen) #compute the total length of each sentence
    for word in sen:
        #for every word in the sentence
        aon = [word in sen2 for sen2 in mainw] #aon, see store description
        #aon is needed to check if a word appears across different sentences
        

        #this part is needed to calculate the frequency
        freq = 0
        for word2 in sen:
            #for every word in the sentence
            if word.lower() == word2.lower():
                freq+=1
        #calculation of freq ends

                
        tf = freq/totalsen #compute tf
        idf = math.log(totalallsen/sum(aon)) #compute idf
        tfidf = tf*idf #compute the product
        store.append([word, tf, idf, tfidf])#the store list increases
        #with each word loop

    #before proceeding to the next sentence, increase the counter
    counter+=1
    #and then assign, note the adjustment of minus one
    output_list[counter-1]=store
    #clean store for the next assignment
    store = []

#the output_list prints the word, its tf, idf, and tfidf scores (in that order)
#for each word in the text_input.    
print(output_list)



