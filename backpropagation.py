import numpy as np

# Training data
inputs = np.array([[0, 0, 1],
                   [1, 1, 1],
                   [1, 0, 1]])

output = np.array([[0, 1, 0]]).T

# Random weights
np.random.seed(1)
weights = 2 * np.random.random((3, 1)) - 1

# Train the network
for i in range(10000):

    # Calculate output using sigmoid
    prediction = 1 / (1 + np.exp(-np.dot(inputs, weights)))

    # Calculate error
    error = output - prediction

    # Update weights
    weights += np.dot(inputs.T, error * prediction * (1 - prediction))

# Test the network
test = np.array([0, 1, 1])

prediction = 1 / (1 + np.exp(-np.dot(test, weights)))

print("Predicted Output:", prediction)

#Explanation
#Backpropagation is a supervised learning algorithm used to train a neural network. It calculates the error between the predicted and expected output and sends this error backward to adjust the weights. This process is repeated until the network learns the required pattern.