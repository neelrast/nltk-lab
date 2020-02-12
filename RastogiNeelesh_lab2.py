# Lab2
# author: Neelesh Rastogi
# email = neelesh.rastogi15@stjohns.edu
# Lab Due date: March 4th
# Date/time your Lab submitted: 03/04/2018 @ 11:55pm

'''
References:
https://stackoverflow.com/questions/22762893/nltk-function-to-count-occurrences-of-certain-words
https://docs.python.org/3/tutorial/datastructures.html
https://rstudio-pubs-static.s3.amazonaws.com/115676_ab6bb49748c742b88127e8b5ce3e1298.html
https://github.com/walshbr/nltk/blob/
https://github.com/sahiga/nlp-exercises/blob/
'''

import nltk
from nltk.corpus import brown, state_union, wordnet as wn
import sys

# Question 1: Ex4 Ch2
# Read in the texts of the State of the Union addresses, using the state_union corpus reader.
# Count occurrences of men, women, and people in each document. What has happened to the usage of these words over time?
def question1():
    a = nltk.ConditionalFreqDist(
    (x, id[:4])

    for id in state_union.fileids()
        for w in state_union.words(id)
            for x in ['men', 'women', 'people']

    if w.lower().startswith(x)
    )
    a.plot()

# Question 2: Ex16 Ch2
# Write a program to generate a table of lexical diversity scores (i.e. token/type ratios), as we saw in 1.1.
# Include the full set of Brown Corpus genres (nltk.corpus.brown.categories()).
# Which genre has the lowest diversity (greatest number of tokens per type)? Is this what you would have expected?
def question2():

    a = nltk.ConditionalFreqDist(
    (genre, (len(brown.words(categories=genre)) / len(set(brown.words(categories=genre)))))
    for genre in brown.categories()
    )
    return a.tabulate()

# Question 3: Ex27 Ch2
# The polysemy of a word is the number of senses it has.
# Using WordNet, we can determine that the noun dog has 7 senses with: len(wn.synsets('dog', 'n')).
# Compute the average polysemy of nouns, verbs, adjectives and adverbs according to WordNet.
def question3():
    n = list(wn.all_synsets('n'))
    a = list(wn.all_synsets('a'))
    v = list(wn.all_synsets('v'))
    r = list(wn.all_synsets('r'))

    def avgpolysemy(synset):
        w = []
        for syn in synset:
            w += syn.lemma_names()
            average = sum(1 for x in synset) / len(set(w))
            return average

    print('Average Polysemy for nouns:')
    print(avgpolysemy(n))
    print('Average Polysemy for adjectives:')
    print(avgpolysemy(a))
    print('Average Polysemy for verbs:')
    print(avgpolysemy(v))
    print('Average Polysemy for adverbs:')
    print(avgpolysemy(r))

# Question 4: Ex28 Ch2
# Use one of the predefined similarity measures to score the similarity of each of the following pairs of words.
# Rank the pairs in order of decreasing similarity.
# How close is your ranking to the order given here, an order that was established experimentally by (Miller & Charles, 1998):
# car-automobile, gem-jewel, journey-voyage, boy-lad, coast-shore, asylum-madhouse, magician-wizard, midday-noon, furnace-stove, food-fruit, bird-cock, bird-crane, tool-implement, brother-monk, lad-brother, crane-implement, journey-car, monk-oracle, cemetery-woodland, food-rooster, coast-hill, forest-graveyard, shore-woodland, monk-slave, coast-forest, lad-wizard, chord-smile, glass-magician, rooster-voyage, noon-string.
def question4():
    words = ['car-automobile', 'gem-jewel', 'journey-voyage', 'boy-lad', 'coast-shore', 'asylum-madhouse',
    'magician-wizard', 'midday-noon', 'furnace-stove', 'food-fruit', 'bird-cock', 'bird-crane', 'tool-implement',
    'brother-monk', 'lad-brother', 'crane-implement', 'journey-car', 'monk-oracle', 'cemetery-woodland', 'food-rooster',
    'coast-hill', 'forest-graveyard', 'shore-woodland', 'monk-slave', 'coast-forest', 'lad-wizard', 'chord-smile', 'glass-magician',
    'rooster-voyage', 'noon-string']
    s = {}
    for l in words:
        w1, w2 = l.split('-')
        set1 = wn.synset(w1 + '.n.01')
        set2 = wn.synset(w2 + '.n.01')
        s[w1 + '-' + w2] = set1.path_similarity(set2)

    for keys, values in s.items():
        print(keys + " \t: "+str(values))

# Question 5: Ex24 Ch 5
# How serious is the sparse data problem? Investigate the performance of n-gram taggers as n increases from 1 to 6.
# Tabulate the accuracy score.
# Estimate the training data required for these taggers, assuming a vocabulary size of 10^5 and a tagset size of 10^2.
def question5():
    a = brown.tagged_sents(categories='news')
    train = a[:(int(len(a) * 0.9))]
    test = a[(int(len(a) * 0.9)):]
    n = 6
    for i in range(n):
        x = nltk.NgramTagger(i, train)
        print(str(i+1) + ': ' + str(x.evaluate(test)))

# Question 6: Ex29 Ch 5
# Recall the example of a bigram tagger which encountered a word it hadn't seen during training, and tagged the rest of the sentence as None.
# It is possible for a bigram tagger to fail part way through a sentence even if it contains no unseen words (even if the sentence was used during training).
# In what circumstance can this happen?
# Can you write a program to find some examples of this?
def question6():
    trainingsentence = brown.sents()[0]
    shuffledsentence = sorted(trainingsentence)

    x = list(nltk.bigrams(shuffledsentence))
    y = list(nltk.bigrams(trainingsentence))

    # tests to see if two inputted sentences are identical.
    def test_unknown_contexts(corpus_one, corpus_two):
        if list(set(corpus_one) - set(corpus_two)):
            print("--> This corpus contains unknown contexts.")
        else:
            print("--> No unknown Contexts found.")

    test_unknown_contexts(x,y)

    print("\nIn a bigram tagger, if a word is not recognized then it fails to recognize the whole bigram and hence claims it to be unknown.")
    print("Because the tagger does not know how to account for the pairs of tags with unknows, each subsequent pair after will also have an unknown in them.")
    print("So the answer is yes that it is possible as, even if the bigram tagger has read the whole text, it has a tendency to think differently of same")

# Question 7: Ex 38 Ch 5 Extra Credit
# Consider the code in 5 which determines the upper bound for accuracy of a trigram tagger.
# Review Abney's discussion concerning the impossibility of exact tagging (Church, Young, & Bloothooft, 1996).
# Explain why correct tagging of these examples requires access to other kinds of information than just words and tags.
# How might you estimate the scale of this problem?
def question7():
    print("Extra Credit: Ex 38 Ch 5\n")
    print("For a perfect tagger system the program/algorithm needs to know everything about the english language, therefore more information will be required to have a perfect tagging system.")
    print("The scale of this problem, I believe is that, for one to attain maximum accuracy, one has to have a training size approaching to infinity.")

#main function to call fucntions in cmd.
def main():
    if(sys.argv[1] == 'question1'):
        question1();
    elif(sys.argv[1] == 'question2'):
        question2();
    elif(sys.argv[1] == 'question3'):
        question3();
    elif(sys.argv[1] == 'question4'):
        question4();
    elif(sys.argv[1] == 'question5'):
        question5();
    elif(sys.argv[1] == 'question6'):
        question6();
    elif(sys.argv[1] == 'question7'):
        question7();
    else:
        print("fucntion error: function doesn't exist");
        SystemExit

if __name__ == "__main__":
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()
    # main()
