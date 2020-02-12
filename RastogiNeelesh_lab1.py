# Lab1
# author: Neelesh Rastogi
# email = neelesh.rastogi15@stjohns.edu
# Lab Due date: Feb 6th
# Date/time your Lab submitted: 02/12/2018 @ 1:32pm

from nltk.book import text1, text6
# import getopt
import sys

# Question 1:
# Define the string silly = “newly formed bland ideas are unexpressible in an infuriating
# way” and create a new string where bland has been replaced with genial

def question1():
    print("--------------------------------------------------------------------------------------")
    silly = "newly formed bland ideas are unexpressible in an infuriating way"
    new_string = silly.replace("bland", "genial")
    print("Silly: " + silly)
    print("New String: " + new_string)



# Question 2:
# Write code to abbreviate text by removing all the vowels.
# Define sentence to hold any string you like (but formed of more than 3 words).
# Write a for loop to process the string sentence, one character at a time, to remove the vowels.

def question2():
    print("--------------------------------------------------------------------------------------")
    sentence = "Hello! My Name is Neel and I'm Awesome."
    vowels = "aeiouAEIOU"
    print("Original Sentence: " + sentence)
    for i in vowels:
        sentence = sentence.replace(i, "")
    print("Removed Vowels: " + sentence)


#   Question 3:
#   What is the difference between the following two lines? Which one
#   will give a larger value? Will this be the case for other texts?
#   >>> sorted(set([w.lower() for w in text1]))
#   >>> sorted([w.lower() for w in set(text1)])

def question3():
    print("--------------------------------------------------------------------------------------")
    print("Statement1 size: ")
    print(len(sorted(set([w.lower() for w in text1]))))
    print("Statement2 size: ")
    print(len(sorted([w.lower() for w in set(text1)])))
    print("Reason: As in the first statment set is called outside the loop it remove maximum number of duplicate values compared to the second statement.")


#   Question 4:
#   Write expressions for finding all words in text6 that meet the conditions
#   listed below. The result should be in the form of a list of words: ['word1', 'word2', ...].
#   a. Ending in ize
#   b. Containing the letter z
#   c. Containing the sequence of letters pt
#   d. Having all lowercase letters except for an initial capital (i.e., titlecase)

def question4():
    print("--------------------------------------------------------------------------------------")
    print("a.")
    print([e for e in text6 if len(e) > 4 and e[-3:] == ('ize')])
    print("b.")
    print(set([e for e in text6 if e.lower().find('z') != -1]))
    print("c.")
    print(set([e for e in text6 if e.lower().find('pt') != -1]))
    print("d.")
    print(set([e for e in text6 if e[0].isupper() and e[1:].islower()]))


#   Question 5:
#   Define sent to be the list of words ['she', 'sells', 'sea', 'shells', 'by', 'the',
#   'sea', 'shore']. Now write code to perform the following tasks:
#   a. Print all words beginning with sh
#   b. Print all words longer than four characters

def question5():
    print("--------------------------------------------------------------------------------------")
    words = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
    print("a")
    print([e for e in words if e[0:2] == 'sh'])
    print("b")
    print([e for e in words if len(e)>4])

#   Question 6:
#   What does the following Python code do?
#   >>> sum([len(w) for w in text1])
def question6():
    print("--------------------------------------------------------------------------------------")
    print(sum([len(w) for w in text1]))
    print("Reason: It evaluates the length of each word and returns the total sum of all lengths.")

#  Question 7:
#  Write code to find all the position in the text of a given word. Define a function indexes(word, text) that returns a list of all the word positions in the text.  Try calling that function for whale in text1.
def indexes(word, text):
    list = [i for i, item in enumerate(text) if item == word]
    return list

def question7():
    print("--------------------------------------------------------------------------------------")
    print(indexes('whale', text1))

# main function to call fucntions in cmd.
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