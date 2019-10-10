import numpy as np

def sigma(x):
    return (1/(1+np.exp(-x)))

training_inputs = np.array([[0,0,1],
                           [1,1,1],
                           [1,0,1],
                           [0,1,1]])
training_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weight = 2 * np.random.random((3,1)) - 1

print('Случайные веса:')
print(synaptic_weight)

for i in range(20000):
    input_layer = training_inputs
    outputs = sigma(np.dot(input_layer, synaptic_weight))
    err = training_outputs - outputs
    adjustmet = np.dot(input_layer.T, err * (outputs*(1-outputs)))
    synaptic_weight +=adjustmet



print("Веса нейронов после цикла")
print(synaptic_weight)
print('Результат после обучения:')
print(outputs)
