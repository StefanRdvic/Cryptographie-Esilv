from matplotlib.pylab import *


def anniv_non_commun(k, N):
    probability = 1  # 100% au départ
    for i in range(1, k):
        probability *= 1 - (i / N)

    return probability


print(anniv_non_commun(23, 365))

t = range(1, 100)
scatter(t, [(1 - anniv_non_commun(x, 365)) * 100 for x in t])
xlabel('k personne')
ylabel('proba d\'anniversaire commun')
title('Théorème de l\'anniversaire')
show()

