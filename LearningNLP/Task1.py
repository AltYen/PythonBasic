import nltk
import random

from nltk.corpus import names
from nltk.corpus import movie_reviews

def gender_features(word): #Function
    return {'last_letter': word[-1]} #returns the last letter of the given word

print("---------Chapter 1---------")
print("----1.1.1----\n")
print("find last letter in sent variable")
word="Shrek"
print(word,gender_features(word))#Calling the function


print("\n----1.1.2----\n")
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +[(name, 'female') for name in names.words('female.txt')]) # taking male and female name from nltk.corpus name and assignment of the labeled names
random.shuffle(labeled_names) # shuffling the array in which names occur
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names] #prepare the set
train_set, test_set = featuresets[500:], featuresets[:500] #Creating the train and test set
classifier = nltk.NaiveBayesClassifier.train(train_set) #training set with naive bayes

#we are testing the set we trained.
print("Neo ",classifier.classify(gender_features('Neo')))
print("Trinity",classifier.classify(gender_features('Trinity')))
print("Altan ",classifier.classify(gender_features('Altan')))
#Accuracy rate
print("Accuracy",nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(5)) #determine which features it found most effective for distinguishing the names' genders:

print("\n----1.2.1----\n")

def gender_features2(name):
    features = {} #creating dictionary
    features["first_letter"] = name[0].lower() #taking first letter of sended name and add to dictionary with "first_letter" key
    features["last_letter"] = name[-1].lower() #taking last letter of sended name and add to dictionary with "last_letter" key
    for letter in 'abcdefghijklmnopqrstuvwxyz': #for loop that calculates how many letters are in the sent name and adds it to the dictionary structure
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

print(gender_features2('John'))                                                #like this [{'first_letter': 'A', 'last_letter': 'n', 'count(a)': 1, 'has(a)': True,.......,Altan},and continue like this...]
featuresets = [(gender_features2(n), gender) for (n, gender) in labeled_names] #In this variable, we take the names in the labeled_names and calculate how many letters are in each name and assign them to the variable.
train_set, test_set = featuresets[500:], featuresets[:500] #define the sets
classifier = nltk.NaiveBayesClassifier.train(train_set) #training the sets
print(nltk.classify.accuracy(classifier, test_set)) #checking the accuracy rate of the trained set.
print("\n----------\n")
train_names = labeled_names[1500:] #We get all the elements after 1500 elements.
devtest_names = labeled_names[500:1500] #We get values of 500-1500.
test_names = labeled_names[:500] #We get the first 500 values.

train_set = [(gender_features(n), gender) for (n, gender) in train_names] #for example train_set=[['last_letter': 'n',Altan],...continues in this structure according to the name. ]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names] #same of above.
test_set = [(gender_features(n), gender) for (n, gender) in test_names] #same of above
classifier = nltk.NaiveBayesClassifier.train(train_set) #training with sets
print(nltk.classify.accuracy(classifier, devtest_set)) #checking the accuracy rate of the trained set.
errors = []
for (name, tag) in devtest_names: #We catch the errors in the set and throw the correct, guess and name into the error array.
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append( (tag, guess, name) )

for (tag, guess, name) in sorted(errors): #We print the errors we catch.
    print('correct={:<8} guess={:<8s} name={:<30}'.format(tag, guess, name))

def gender_features(word): #updating our function. Instead of guessing according to the last letter of the name, we will try to guess according to the last 2 letters of the name.
    return {'suffix1': word[-1:],'suffix2': word[-2:]}

train_set = [(gender_features(n), gender) for (n, gender) in train_names] #for example train_set=[['suffix1': 'n' 'suffix2': 'a',Altan],... and continues in this structure according to the name.]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names] #same of above.
classifier = nltk.NaiveBayesClassifier.train(train_set) #training with sets
print(nltk.classify.accuracy(classifier, devtest_set)) #checking the accuracy rate of the trained set.

#With this update, we increase our accuracy rate by guessing with the last 2 letters instead of guessing with the last 1 letter.

print("\n----1.3----\n")

documents = [(list(movie_reviews.words(fileid)), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

print(document_features(movie_reviews.words('pos/cv957_8737.txt')))

featuresets = [(document_features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)