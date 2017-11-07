from sys import version_info
import numpy as np
import pandas as pd
from titanic_visualizations import survival_stats
from IPython.display import display

if version_info.major !=2 and version_info.minor != 7:
	raise Exception('2.7 error')

in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

display(full_data.head())

outcomes=full_data['Survived']
data = full_data.drop('Survived',axis=1)

display(data.head())

def accuracy_score(truth,pred):
	return "accuracy: {:.2f}".format((truth == pred).mean()*100)

obj = np.zeros(full_data.shape[0],dtype=int)
predictions = pd.Series(obj)

print accuracy_score(outcomes,predictions)

# survival_stats(data,outcomes,'Sex')

def predictions_1(data):
	predictions = []
	for _,passenger in data.iterrows():
		if passenger["Sex"] == "male":
			predictions.append(0)
		else:
			predictions.append(1)
	return pd.Series(predictions)

predictions = predictions_1(data)

print accuracy_score(outcomes,predictions)

# survival_stats(data,outcomes,'Age',["Sex == 'male'"])

def predictions_2(data):
	predictions = []
	for _,passenger in data.iterrows():
		if passenger["Sex"]=="female":
			predictions.append(1)
		else:
			if passenger["Age"] < 10:
				predictions.append(1)
			else:
				predictions.append(0)
	return pd.Series(predictions)

predictions = predictions_2(data)

print accuracy_score(outcomes,predictions)

def predictions_3(data):
	predictions = []
	for _,passenger in data.iterrows():
		if passenger["Sex"]=="female":
			if passenger["SibSp"] <= 1:
				if passenger["Parch"] <= 3:
					predictions.append(1)
				else:
					predictions.append(0)
			else:
				predictions.append(0)
		else:
			if passenger["Age"] < 10:
				if passenger["Pclass"] < 3:
					predictions.append(1)
				else:
					predictions.append(0)
			else:
				predictions.append(0)
	return pd.Series(predictions)

predictions = predictions_3(data)
print accuracy_score(outcomes,predictions)

survival_stats(data,outcomes,'Parch',["Sex == 'female'"])