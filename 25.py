from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load the Iris dataset from scikit-learn
iris = load_iris()

# Create a Decision Tree classifier object
clf = DecisionTreeClassifier()

# Train the classifier on the Iris dataset
clf.fit(iris.data, iris.target)

# Get input features from user
new_flower = []
new_flower.append(float(input('Enter sepal length: ')))
new_flower.append(float(input('Enter sepal width: ')))
new_flower.append(float(input('Enter petal length: ')))
new_flower.append(float(input('Enter petal width: ')))

# Predict the species of the new flower based on input features
prediction = clf.predict([new_flower])

# Print out the prediction
if prediction[0] == 0:
    print('The new flower is predicted to be of the Setosa species.')
elif prediction[0] == 1:
    print('The new flower is predicted to be of the Versicolor species.')
else:
    print('The new flower is predicted to be of the Virginica species.')
