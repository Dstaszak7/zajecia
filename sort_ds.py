def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    
    return lista


liczby = [5, 2, 9, 1, 5, 6]

posortowane = bubble_sort(liczby)
print(posortowane)