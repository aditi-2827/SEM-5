#AND Gate
import numpy as np

# AND gate data
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
target = np.array([0, 0, 0, 1])

# Initial weights
weights = np.array([0.0, 0.0])

# Training
for epoch in range(10):

    for i in range(4):

        # Calculate output
        output = np.dot(inputs[i], weights)
        output = int(output >= 1)

        # Calculate error
        error = target[i] - output

        # Update weights
        weights = weights + inputs[i] * error

print("Final Weights:", weights)

# Test AND gate
print("AND Gate Output:")

for x in inputs:
    output = int(np.dot(x, weights) >= 1)
    print(x, "=", output)


#Perceptron — OR Gate

import numpy as np

# OR gate data
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
target = np.array([0, 1, 1, 1])

# Initial weights
weights = np.array([0.0, 0.0])

# Training
for epoch in range(10):

    for i in range(4):

        # Calculate output
        output = np.dot(inputs[i], weights)
        output = int(output >= 1)

        # Calculate error
        error = target[i] - output

        # Update weights
        weights = weights + inputs[i] * error

print("Final Weights:", weights)

# Test OR gate
print("OR Gate Output:")

for x in inputs:
    output = int(np.dot(x, weights) >= 1)
    print(x, "=", output)


# 1. Perceptron Rule
# Algorithm:
# Initialize the weights and learning parameters.
# Take the input values and calculate the weighted sum.
# Apply the step activation function to get the predicted output.
# Calculate the error between the target output and predicted output.
# If there is an error, update the weights using the perceptron learning rule.
# Repeat the process for all training examples for several epochs.
# Stop when the network correctly classifies the training data or the required number of epochs is completed.


# Weighted Sum = X · W

# Error = Target - Output

# New Weight = Old Weight + Input × Error

# The Perceptron Rule is a supervised learning method used to train a simple artificial neuron. It compares the predicted output with the target output and updates the weights whenever there is an error. The process is repeated until the perceptron learns to correctly classify the given inputs.