import hashlib
import string
from matplotlib.pyplot import scatter, show, xlabel, ylabel, title
from numpy import *
import random
import time


def random_string(n):
    return ''.join(random.choice(string.ascii_letters) for i in range(n))  # string random de n char


def proof_of_work(A, D):
    #  renvoi le temps passé à trouver une preuve de travail
    d_zero = ''.join('0' for n in range(D))
    x = 0
    start_time = time.time()

    while True:
        # concatenation A | D | x
        if hashlib.sha256((A + d_zero + str(x)).encode()).hexdigest().startswith(d_zero):
            break
        x += 1

    return time.time() - start_time


def test_pow(n, D):
    #  renvoi le temps moyen de n hash
    return mean([proof_of_work(random_string(20), D) for i in range(n)])


t = range(1, 5)
scatter(t, [test_pow(50, d) for d in t])
title('moy d\'exécution de preuve de travail')
xlabel('valeur de D')
ylabel('t(s) moy')
show()
