import numpy as np

def step_function(x):
    return 1 if x >= 0 else 0

def perceptron(input_values, weights, bias):
    weighted_sum = np.dot(input_values, weights) + bias
    return step_function(weighted_sum)

# AND gate
def and_gate(x1, x2):
    input_values = np.array([x1, x2])
    weights = np.array([1, 1])
    bias = -2
    return perceptron(input_values, weights, bias)

# OR gate
def or_gate(x1, x2):
    input_values = np.array([x1, x2])
    weights = np.array([1, 1])
    bias = -1
    return perceptron(input_values, weights, bias)

# NOT gate
def not_gate(x):
    input_values = np.array([x])
    weights = np.array([-1])
    bias = 0.5
    return perceptron(input_values, weights, bias)

# XOR gate (combination of AND, OR, and NOT gates)
def xor_gate(x1, x2):
    not_x1 = not_gate(x1)
    not_x2 = not_gate(x2)
    and_result = and_gate(x1, x2)
    or_result = or_gate(not_x1, not_x2)
    return and_gate(and_result, or_result)

# Testing the gates
print("AND Gate:")
print(and_gate(0, 0))  # Output: 0
print(and_gate(0, 1))  # Output: 0
print(and_gate(1, 0))  # Output: 0
print(and_gate(1, 1))  # Output: 1

print("\nOR Gate:")
print(or_gate(0, 0))   # Output: 0
print(or_gate(0, 1))   # Output: 1
print(or_gate(1, 0))   # Output: 1
print(or_gate(1, 1))   # Output: 1

print("\nNOT Gate:")
print(not_gate(0))     # Output: 1
print(not_gate(1))     # Output: 0

print("\nXOR Gate:")
print(xor_gate(0, 0))  # Output: 0
print(xor_gate(0, 1))  # Output: 1
print(xor_gate(1, 0))  # Output: 1
print(xor_gate(1, 1))  # Output: 0
