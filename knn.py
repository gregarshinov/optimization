from math import sqrt
import numpy as np
import collections
from sklearn.datasets import load_iris
from sklearn.utils import shuffle


def euclidian_distance(x, y):

    distance_between_x_and_y = 0
    for i in range(len(x)):
        distance_between_x_and_y += (x[i] - y[i])**2

    return sqrt(distance_between_x_and_y)


def l_k_distance(x, y):
    distance_between_x_and_y = 0
    for i in range(len(x)):
        distance_between_x_and_y += (x[i] - y[i])**k

    return distance_between_x_and_y**(1/k)


def cos_distance(x, y):

    scalar = 0
    norm_x = 0
    norm_y = 0

    for i in range(len(x)):
        scalar += x[i]*y[i]
        norm_x += x[i]*x[i]
        norm_y += y[i]*y[i]

    return sqrt(1 - scalar/(sqrt(norm_x)*sqrt(norm_y)))

def knn(train, test, k, distance_function):
    number_of_test_obj = test.shape[0]
    labels = np.zeros(number_of_test_obj)
    for x in range(number_of_test_obj):
        distance = np.zeros(number_of_test_obj)

        for y in range(train.shape[0]):
            distance[x] = distance_function(test[x], train[y, :-1])

        index_of_k_nearest = np.argsort(distance)[:k]

        most_common = collections.Counter([train[x, -1] for x in index_of_k_nearest]).most_common(1)[0]

        labels[x] = most_common[0]

        return labels


iris = load_iris()
data_iris = np.column_stack([iris['data'], iris['target']])
iris = shuffle(data_iris)
train = iris[:100, :]
test = iris[100:150, :-1]
true_labels = iris[100:150, -1]

k = 0.3

labels = knn(train, test, 5, euclidian_distance)

error = 0

for i in range(len(labels)):
    if true_labels[i] != labels[i]:
        error += 1

print(error)

