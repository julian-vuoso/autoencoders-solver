import numpy as np


class SimplePerceptron(object):

    def __init__(self, activation_function, activation_function_derived,
                 dimension: int, hidden: bool = False, index: int = 0):
        self.index = index
        self.hidden: bool = hidden
        self.act_func = activation_function
        self.act_func_der = activation_function_derived
        self.w: np.ndarray = np.zeros(dimension)
        self.input: np.ndarray = np.zeros(dimension)

        # for epoch training
        self.accu_w = np.zeros(dimension)

    # out, a 1D array, is used only in the most superior layer
    # sup_w is a 2D matrix with all the W vectors of the superior layer
    # sup_delta is a 1D array, resulting in all the delta values of the superior layer
    # the two above are only used in hidden layers
    def retro(self, out: np.ndarray, sup_w: np.ndarray, sup_delta: np.ndarray, eta: float) \
            -> (np.ndarray, float):
        # activation for this neuron
        activation_derived = self.act_func_der(np.dot(self.input, self.w))

        # delta sub i using the activation values
        if not self.hidden:
            delta = (out[self.index] - self.activation(self.input)) * activation_derived
        else:
            delta = np.dot(sup_delta, sup_w[:, self.index]) * activation_derived

        # calculate the delta w
        delta_w = (eta * delta * self.input)

        # epoch training accumulation
        self.accu_w += delta_w

        return self.w, delta

    # returns the activation value/s for the given input in this neuron
    # returns int or float depending on the input data and activation function
    def activation(self, input_arr: np.ndarray, training: bool = False):
        if training:
            self.input = input_arr

        # activation for this neuron, could be int or float, or an array in case is the full dataset
        return self.act_func(np.dot(input_arr, self.w))

    # resets the w to a randomize range
    def randomize_w(self, ref: float) -> None:
        self.w = np.random.uniform(-ref, ref, len(self.w))

    # for epoch training delta is the accum value
    def update_w(self):
        self.w += self.accu_w

    def __str__(self) -> str:
        return f"SP=(i={self.index}, w={self.w})"

    def __repr__(self) -> str:
        return f"SP=(i={self.index}, w={self.w})"
