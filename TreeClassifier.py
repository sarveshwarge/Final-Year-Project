import cv2
from sklearn import tree
from sklearn.metrics import accuracy_score

class TreeClassifier:
	'''
	This class is used to train and test our decision tree classifier.
	'''

	def __init__(self):
		self.tree_classifier = tree.DecisionTreeClassifier()
		self.train_images = []
		self.test_images = []
		self.predicted_results = []

	def trainClassifier(self,train_data_x,train_target_y):
		'''
		This module is used to train our classifier.

		#Parameters: 'train_data_x' is the training image samples,
					 'train_target_y' is the training labels for the training data. 
		#Return: None
		'''
		self.train_images = train_data_x
		self.tree_classifier.fit(train_data_x,train_target_y)

	def testClassifier(self,test_data_x,test_target_y):
		'''
		This module is used to test our classifier.

		#Parameters: 'test_data_x' is the testing image samples,
					 'test_target_y' is the testing labels for the testing data.
		#Return: Accuracy of the classifier.
		'''
		self.test_images = test_data_x
		self.predicted_results = self.tree_classifier.predict(test_images)
		return accuracy_score(test_target_y,predicted_results)


