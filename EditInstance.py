__author__ = 'dmitrijdackov'

def Min(a, b):
    if a < b:
        return a
    return b

def Min3(a, b, c):
    return Min(Min(a, b), c)

def Distance(X, Y, substcost = 2):

    """
    Calculates Distance: X, Y are strings and substcost is a substitute cost
    """

    dimx = len(X) + 1
    dimy = len(Y) + 1

    dist = [[0 for x in range(dimy)] for y in range(dimx)]

    for i in range(dimx):
        dist[i][0] = i

    for j in range(dimy):
        dist[0][j] = j

    for i in range(1, dimx):
        for j in range (1, dimy):

            temp = 0
            if X[i - 1] != Y[j - 1]:
                temp = substcost

            d1 = dist[i - 1][j] + 1 #deletion
            d2 = dist[i][j - 1] + 1 #insertion
            d3 = dist[i - 1][j - 1] + temp #substittion

            dist[i][j] = Min3(d1, d2, d3)

    return dist[-1][-1]

print (Min3(1, 2, 3))
print (Min3(3, 2, 3))
print (Min3(3, 3, 3))

print ('aaa ', 'aaa', ' ', Distance('aaa', 'aaa', 1))
print ('aaa ', 'aab', ' ', Distance('aaa', 'aab', 1))
print ('aaa ', 'abb', ' ', Distance('aaa', 'abb', 1))
print ('aaa ', 'bbb', ' ', Distance('aaa', 'bbb', 1))

print ('aaa ', 'bb', ' ', Distance('aaa', 'bb', 1))
print ('aaa ', 'aa', ' ', Distance('aaa', 'aa', 1))
print ('aaa ', 'a', ' ', Distance('aaa', 'a', 1))
print ('aaa ', '', ' ', Distance('aaa', '', 1))

print ('aaa ', 'aab', ' ', Distance('aaa', 'aab'))

print ('inte*ntion ', '*execution', ' ', Distance('inte*ntion', '*execution', 1))
print ('inte*ntion ', '*execution', ' ', Distance('inte*ntion', '*execution'))


