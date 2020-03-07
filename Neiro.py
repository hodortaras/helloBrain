import numpy as np

class Perceptron():

    def __init__(self,X, y, threshold = 0.5, learning_rate = 0.1, max_epoch = 10):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.y = y
        self.X = X
        self.max_epoch = max_epoch

    def initialize(self, init_type = 'zeros'):
        if init_type == 'random':
            self.weights = np.random.rand(len(self.X[0]))*0.5
        if init_type == 'zeros':
            self.weights = np.zeros(len(self.X[0]))

    def train(self):
        epoch = 0
        while True:
            error_count = 0
            epoch +=1
            for (X,y) in zip(self.X, self.y):
                error_count +=self.train_observation(X, y, error_count)
            if error_count ==0:
                print('training successfull')
                break
            if epoch >= self.max_epoch:
                print('reached maximum epoch')
                break

    def train_observation(self, X, y, error_count):
        result = np.dot(X, self.weights) > self.threshold
        error = y - result
        if error !=0:
            error_count +=1
            for index, value in enumerate(X):
                self.weights[index] += self.learning_rate * error * value
        return error_count

    def predict(self, X):
        return int(np.dot(X, self.weights) > self.threshold)

X = [(1,0,0),(1,1,0),(1,1,1),(1,1,1),(1,0,1),(1,0,1)]
y = [1,1,0,0,1,1]

p=Perceptron(X,y)
p.initialize()
p.train()
print(p.predict((0,1,0)))
print(p.predict((0,0,0)))
