import nltk
import random

from nltk.corpus import names

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

train_names = labeled_names[1500:]
devtest_names = labeled_names[500:1500]
test_names = labeled_names[:500]

train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
test_set = [(gender_features(n), gender) for (n, gender) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, devtest_set))
errors = []
for (name, tag) in devtest_names:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append( (tag, guess, name) )

for (tag, guess, name) in sorted(errors):
    print('correct={:<8} guess={:<8s} name={:<30}'.format(tag, guess, name))

def gender_features(word):
    return {'suffix1': word[-1:],'suffix2': word[-2:]}

train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, devtest_set))