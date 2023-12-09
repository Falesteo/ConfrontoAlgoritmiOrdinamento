import matplotlib.pyplot as plt
import numpy as np
import time
import random


def insertion_sort(arr):
    # Scorre attraverso tutti gli elementi a partire dal secondo
    for i in range(1, len(arr)):
        key = arr[i]

        # Muove gli elementi di arr[0...i-1] che sono maggiori di key
        # alla loro posizione successiva rispetto alla posizione corrente
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Inserisce l'elemento nella posizione corretta
        arr[j + 1] = key


def counting_sort(arr):
    # Trova il valore massimo nella lista
    max_val = max(arr)

    # Crea un array di conteggio con dimensione pari al valore massimo + 1
    count = [0] * (max_val + 1)

    # Conta le occorrenze di ciascun elemento nella lista
    for num in arr:
        count[num] += 1

    # Ricostruisce la lista ordinata utilizzando l'array di conteggio
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr


def plotSortGraph(algType, insertType, arrayDim, plot=True):
    x, y = [], []
    for i in range(1, arrayDim, 5):
        x.append(i)
        A = np.arange(i) if insertType == 0 else random.sample(range(i), i)
        if algType == 0:
            start = time.perf_counter()
            insertion_sort(A)
            end = time.perf_counter()
        else:
            start = time.perf_counter()
            counting_sort(A)
            end = time.perf_counter()
        z = y[-1] if (len(y) != 0) else 0
        y.append((end - start) / i + z)
    if plot:
        plt.plot(x, y)
        title = 'Insertion Sort' if algType == 0 else 'Counting Sort'
        title += ' on Ordered List ' if insertType == 0 else ' on Randomized List '
        title += str(arrayDim)
        plt.title(title)
        plt.show()
    else:
        return x, y


if __name__ == '__main__':
    size = [100, 500, 1000]
    [[[plotSortGraph(i, j, s) for i in range(2)] for j in range(2)] for s in size]