import sklearn
import pandas
import csv
import numpy
from settings import EMOJIS
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.svm import LinearSVC

filename = 'data_emojis_4.csv'

def analyze_classes():

    labels = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            labels.append(row[3])
    print(Counter(labels))   

def classify():
    X = []
    y = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            X.append(row[2])
            y.append(row[3])
    X = numpy.array(X)
    y = numpy.array(y)

    tfidfvec = TfidfVectorizer(analyzer='word', strip_accents='ascii', ngram_range=(1,1))
    classifier = LinearSVC()

    X = tfidfvec.fit_transform(X)
    X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=.25)

    # train the model
    classifier.fit(X_train, y_train)

    # test model on new data
    predicted = classifier.predict(X_test)

    print("Score pour le classifieur " + str(classifier) + " : \n" + str(numpy.mean(predicted == y_test)) + "\n")
    print(sklearn.metrics.classification_report(y_test, predicted))
    print(sklearn.metrics.confusion_matrix(y_test, predicted))

if __name__ == '__main__':

    classify()
    analyze_classes()