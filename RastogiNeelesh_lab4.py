# Lab4
# author: ‘Neelesh Rastogi'
# email = ‘neelesh.rastogi15@stjohns.edu'
# Lab Due date: April 3rd, 2018
# Date/time your Lab submitted: 5/9/2018 @ 7:50 am

# Using any of the three classifiers described in this chapter,
# and any features you can think of, build the best name gender classifier you can.
# Begin by splitting the Names Corpus into three subsets: 500 words for the test set,
# 500 words for the dev-test set, and the remaining 6900 words for the training set.
# Then, starting with the example name gender classifier, make incremental improvements.
# Use the dev-test set to check your progress. Once you are satisfied with your classifier,
# check its final performance on the test set. How does the performance on the test set compare
# to the performance on the dev-test set? Is this what you'd expect?
import nltk
from nltk.corpus import brown
from nltk.corpus import names
from nltk.classify import apply_features
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
import random

# generate the name_gender set
name_gen =[(name,'male') for name in names.words('male.txt')]+[(name,'female')for name in names.words('female.txt')]

# randomly shuffle the dataset
random.shuffle(name_gen)

# define feature 1
def get_feature(name):
    return {'last letter':name[-1]}

# generate feature set
featureset= [(get_feature(name),gender)for name,gender in name_gen]

#split the data into 3 subsets
test =apply_features(get_feature,name_gen[:500])
dev_test =apply_features(get_feature,name_gen[500:1000])
train =apply_features(get_feature,name_gen[1000:])

# train a classifier
clf1 = nltk.NaiveBayesClassifier.train(train)

# check the accuracy on validation set
print("NaiveBayes classifier accuracy on validation set is "+ str(nltk.classify.accuracy(clf1,dev_test)))

# check the accuracy on the test set
print('NaiveBayes classifier accuracy on test set is '+ str(nltk.classify.accuracy(clf1,test)))

# generate feature2
def get_feature2(word):
    feature= {}
    feature['first letter'] = word[0].lower()
    feature['last letter']=word[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        feature['count(%s)' % letter]= word.lower().count(letter)
        feature['has (%s)' % letter] = letter in word.lower()
    return feature

# generate feature set
featureset2= [(get_feature2(name),gender) for name, gender in name_gen]
test_set= apply_features(get_feature2,name_gen[:500])
cv_set = apply_features(get_feature2,name_gen[500:1000])
train_set = apply_features(get_feature2,name_gen[1000:])

# train 3 classifier : Naive Bayes Classifier, decision tree , maximum entropy
classifier1 = nltk.NaiveBayesClassifier.train(train_set)
classifier2 = nltk.DecisionTreeClassifier.train(train_set)
classifier3 = nltk.MaxentClassifier(train_set,weights = 0.8)

#accuracy for naivebayes classifier
print("NaiveBayes classifier accuracy on validation set is "+ str(nltk.classify.accuracy(classifier1,cv_set)))
print('NaiveBayes classifier accuracy on test set is '+ str(nltk.classify.accuracy(classifier1,test_set)))
# accuracy on  decision tree
print('Decision Tree classifier accuracy is '+ str(nltk.classify.accuracy(classifier2, cv_set)))
print('Decision Tree classifier accuracy is '+ str(nltk.classify.accuracy(classifier2, test_set)))
# accuracy for maximum entropy
print('Maximum entropy Classfier accuracy is ' + str(nltk.classify.accuracy(classifier3,cv_set)))
print('Maximum entropy Classfier accuracy is ' + str(nltk.classify.accuracy(classifier3,test_set)))


# Using the movie review document classifier discussed in this chapter, generate a list of the 30 features that the classifier finds to be most informative. Can you explain why these particular features are informative? Do you find any of them surprising?


# create a list of document divied by category
documents = [(list(movie_reviews.words(fileid)),category)for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

# create the feature :count the frequency of all the words
all_words = nltk.FreqDist(word.lower()for word in movie_reviews.words())

# limit the word feature to 2000
word_features = list(all_words.keys())[:2000]

# document_features
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contain(%s)' % word] = (word in document_words)
    return features

# split the data into training and test set
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]

# train a classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier,test_set))
classifier.show_most_informative_features(30)


# Select one of the classification tasks described in this chapter, such as name gender detection, document classification, part-of-speech tagging, or dialog act classification. Using the same training and test data, and the same feature extractor, build three classifiers for the task: a decision tree, a naive Bayes classifier, and a Maximum Entropy classifier.
# Compare the performance of the three classifiers on your selected task. How do you think that your results might be different if you used a different feature extractor?
suffix_fidst = nltk.FreqDist()
for word in brown.words():
    word = word.lower()
    suffix_fidst[word[-1:]] +=1 # count the occurency of the last letter of word
    suffix_fidst[word[-2:]] +=1
    suffix_fidst[word[-3:]] +=1
common_suffixes =  list(suffix_fidst.keys())[:100]

# def features function to retrive suffix from
def pos_features(word):
    features= {}
    for suffix in common_suffixes:
        features['endswith(%s)'% suffix] = word.lower().endswith(suffix)
    return features

# create feature sets
tagged_words = brown.tagged_words(categories= 'news')
featuresets= [(pos_features(n),g) for (n,g) in tagged_words]

# spilt the featureset into train and test
size = int(len(featuresets) * 0.2)
test_set,train_set = featuresets[:size],featuresets[size:]

#train 3 model
#naive bayes model
clf1 = nltk.NaiveBayesClassifier.train(train_set)
nltk.classify.accuracy(clf1,test_set)

# decision tree model
clf2 = nltk.DecisionTreeClassifier.train(train_set)
nltk.classify.accuracy(clf2,test_set)

# Word features can be very useful for performing document classification, since the words that appear in a document give a strong indication about what its semantic content is
# However, many words occur very infrequently, and some of the most informative words in a document may never have occurred in our training data.
# One solution is to make use of a lexicon, which describes how different words relate to one another.
# Using WordNet lexicon, augment the movie review document classifier presented in this chapter to use features that generalize the words that appear in a document,
# making it more likely that they will match words found in the training data.
documents = [(list(movie_reviews.words(fileid)), category)for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

# word_feature sets
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]

def document_features(document):
    from nltk.corpus import wordnet as wn
    document_words = set(document)
    features = {}
    for word in word_features:
        for synset in wn.synsets(word):
            for lemma in synset.lemmas():
                features['contain(%s)' % lemma.name()] = (lemma.name() in document_words)
        #features['contains(%s)' % word] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print (nltk.classify.accuracy(classifier, test_set))

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words.keys())[:2000]
add_word_feature= set()

for word in word_features:
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            add_word_feature.add(lemma.name())

# define feature
def document_features(document):
    document_words = set(document)
    features = {}
    for word in add_word_feature:
        features['contains(%s)' % word] = (word in document_words)
    return features

# build a classifier
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set)*100)