#and gate
import numpy as np

# AND gate input and output
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
output = np.array([0, 0, 0, 1])

# Initial weights
weights = np.array([0.0, 0.0])

# Hebb learning
for i in range(4):
    weights = weights + inputs[i] * output[i]

print("Final Weights:", weights)

# Test AND gate
print("AND Gate Output:")

for x in inputs:
    result = np.dot(x, weights)
    result = int(result >= 1)
    print(x, "=", result)

#OR Gate
import numpy as np

# OR gate input and output
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
output = np.array([0, 1, 1, 1])

# Initial weights
weights = np.array([0.0, 0.0])

# Hebb learning
for i in range(4):
    weights = weights + inputs[i] * output[i]

print("Final Weights:", weights)

# Test OR gate
print("OR Gate Output:")

for x in inputs:
    result = np.dot(x, weights)
    result = int(result >= 1)
    print(x, "=", result)




# Algorithm:
# Initialize the weights.
# Take the input values and their corresponding output.
# Calculate the change in weights using the input and output.
# Update the weights using Hebb's learning rule.
# Repeat the process for all training examples.
# Use the final weights to calculate the output for new inputs.

#New Weight = Old Weight + Input × Output

#Hebb's Rule is a learning rule based on the idea that when an input and output neuron are activated together, the connection between them becomes stronger. The weights are increased according to the product of the input and output values.