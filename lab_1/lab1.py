import numpy as np
import pandas as pd

X = pd.DataFrame({'Де грає': ['Вдома', 'Вдома', 'В гостях', 'В гостях', 'Вдома', 'Вдома', 'В гостях', 'В гостях'], 
                  'Суперник': ['Вище', 'Нижче', 'Нижче', 'Нижче', 'Вище', 'Нижче', 'Нижче', 'Вище'],
                  'Температура': ['Висока', 'Норма', 'Норма', 'Висока', 'Висока', 'Висока', 'Висока', 'Норма'], 
                  'Дощ': ['Так', 'Ні', 'Так', 'Так', 'Ні','Так', 'Ні', 'Ні']})

y = pd.DataFrame({'Перемога': ['Ні', 'Так', 'Так', 'Ні','Так', 'Ні', 'Ні', 'Так']})

T = pd.concat([X, y], axis = 1)
print(T)
print()

dictX = dict()
listX = list()

for t in range(len(T)):
    if y.values[t] == 'Так':
        for xi in X[t:t+1].values:
            listX.append(xi)

array = np.asarray(listX)
array = array.swapaxes(1, 0)
listX.clear()

for a in array:
    for ai in a:
        if ai == 'Вище' or ai == 'Висока':
            for i in range(len(a)):
                swap = i + np.argmin(a[i:])
                (a[i], a[swap]) = (a[swap], a[i])
        elif ai == 'Вдома' or ai == 'Так':
            for i in range(len(a)):
                swap = i + np.argmax(a[i:])
                (a[i], a[swap]) = (a[swap], a[i])
    for ai in a:
        listX.append(ai)

for word in listX:
    dictX[word] = dictX.get(word, 0) + 1

Ch = list(dictX.values())
Ch = [Ch[i:i+2] for i in range(0, len(Ch), 2)]
Ch = np.asarray(Ch)

dictX.clear()

for col in X:
    for word in X[col].values:
        dictX[word] = dictX.get(word, 0) + 1

C = list(dictX.values())
C = [C[i:i+2] for i in range(0, len(C), 2)]
C = np.asarray(C)
print(Ch)

G = (C / len(T)) * (-Ch / len(Ch) * np.log2(Ch / len(Ch)) -Ch / len(Ch) * np.log2(Ch / len(Ch)))

print(G)

G = np.sum(G, axis = 1)

keys = X.keys()
result = np.where(G==G.min())
xh = keys[result[0]]

print('Xh* = ', xh)
print('Gain = ', G.min())
