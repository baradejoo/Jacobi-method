import numpy as np

max_iteration = 100


class Error(Exception):
    """Base class for other exceptions"""
    pass


class IncompatibleSizes(Error):
    def __init__(self, matrix_A, vector_b, message="Incompatible sizes between matrix A and vector b"):
        self.matrix_A_ = matrix_A
        self.vector_b_ = vector_b
        self.message_ = message
        super().__init__(self.message_)

    def __str__(self):
        return f'{self.message_} -> size of A = {len(self.matrix_A_)}, size of b = {self.vector_b_.size}'


class NotNonSingular(Error):
    def __init__(self, message="Matrix A is singular, no more calculations..."):
        self.message_ = message
        super().__init__(self.message_)

    def __str__(self):
        return f'{self.message_}'


def JM(A_, b_):
    """
        Jacobi method

        inputs: A_ - Matrix: np.array
                b_ - Absolute term in an expression: np.array

        outputs: Tuple: (x - Solution of Ax=b, err - Convergence)

        Comments: 1. Algorithm works great for determining the solutions of a strictly diagonally dominant system of
            linear equations. In the other cases, that method doesn't always converge.

        Script with necessary knowledge: https://en.wikipedia.org/wiki/Jacobi_method
        """

    if b_.size != len(A_):
        raise IncompatibleSizes(A_, b_)

    if np.linalg.det(A_) == 0:  # checking if matrix is non-singular
        raise NotNonSingular

    # checking if matrix A is diagonally dominant, if not: algorithm still will be working
    for i in range(len(A_)):
        sum_row = 0
        for k, j in enumerate(A_[i]):
            if k != i:
                sum_row += abs(j)
        if A_[i, i] <= sum_row:
            print("Matrix A is for sure not diagonally dominant")

    x = np.zeros(len(A_))
    for it in range(max_iteration):
        x_new = np.zeros(len(A_))

        for i in range(A_.shape[0]):
            x_new[i] = (b_[i] - A_[i, :i] @ x[:i] - A_[i, i + 1:] @ x[i + 1:]) / A_[i, i]
            if x_new[i] == x_new[i - 1]:
                break

        if np.allclose(x, x_new, atol=1e-5, rtol=0.):
            print("The end of the algorithm. Convergence is enough small.")
            break

        x = x_new

    err = A_ @ x - b_
    sol_err = (x, err)
    return sol_err


if __name__ == "__main__":
    pass
