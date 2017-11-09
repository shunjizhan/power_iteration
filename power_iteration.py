import scipy.sparse
import scipy.sparse.linalg
import numpy as np
import time
import matplotlib.pyplot as plt


def power_iteration(A, U, max_iteration):
    x = np.random.rand(n, 1)

    for i in range(max_iteration):
        yi = A.dot(x) + U.dot(UT.dot(x))
        x_ = AT.dot(yi) + U.dot(UT.dot(yi))
        x = x_ / np.linalg.norm(x_)

    return x


if __name__ == "__main__":
    n, k = 10000, 20

    A = scipy.sparse.rand(n, n, density=0.01)
    AT = A.transpose()

    U = np.random.rand(n, k)
    UT = U.transpose()
    UUT = np.dot(U, UT)

    C = A + UUT

    # U1, s, V = scipy.sparse.linalg.svds(C, k=1)

    iterations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    times_total = np.zeros(10)
    for i in range(10):
        times = []
        for t in range(len(iterations)):
            ite = iterations[t]
            start = time.time()
            power_iteration(A, U, ite)
            end = time.time()
            times.append(end - start)
        times_total += np.array(times)

    times_total /= 10

    plt.plot(iterations, times_total, 'ro')
    plt.ylabel('time')
    plt.xlabel('iterations')
    plt.show()







