import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.metrics import confusion_matrix

class KMeansOnDigits:
    def __init__(self, n_clusters, random_state):
          self.n_clusters = n_clusters
          self.random_state = random_state

    def load_dataset(self):
        from sklearn.datasets import load_digits
        self.digits = load_digits()

    def predict(self):
        model = KMeans(n_clusters = self.n_clusters,random_state = self.random_state)
        self.clusters = model.fit_predict(self.digits.data)

    def get_labels(self): 
        result = np.zeros(self.clusters.shape)
        for item in np.unique(self.clusters):
            mask = (self.clusters == item)
            tmp = self.digits.target[mask]
            modus = np.bincount(tmp).argmax()
            result[mask] = modus
        self.labels = result

    def calc_accuracy(self):
        self.accuracy = np.round(accuracy_score(self.labels,self.digits.target),2)

    def confusion_matrix(self):
        self.mat = confusion_matrix(self.digits.target, self.labels)
         
