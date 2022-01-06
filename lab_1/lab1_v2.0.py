#Перероблене

import numpy as np
import pandas as pd

X = pd.DataFrame(np.array([['Вдома', 'Вище', 'Висока', 'Так'],
                           ['Вдома', 'Нижче', 'Норма', 'Ні'],
                           ['В гостях', 'Нижче', 'Норма', 'Так'],
                           ['В гостях', 'Нижче', 'Висока', 'Так'],
                           ['Вдома', 'Вище', 'Висока', 'Ні'],
                           ['Вдома', 'Нижче', 'Висока', 'Так'],
                           ['В гостях', 'Нижче', 'Висока', 'Ні'],
                           ['В гостях', 'Вище', 'Норма', 'Ні']]), columns=['Де грає', 'Суперник', 'Температура', 'Дощ'])
y = pd.Series(['Ні', 'Так', 'Так', 'Ні', 'Так', 'Ні', 'Ні', 'Так'])
victory = pd.DataFrame({'Перемога': y})

T = pd.concat([X, victory], axis = 1)
print(T)

m = len(X.keys())
c = np.array(X[X.keys()[0]].unique())
for i in X.keys()[1:]:
    c = np.vstack([c, X[i].unique()])
S = y.unique()
keys = X.keys()
G = np.zeros((m, c.shape[1]))
for h in range(m):
    for i in range(c.shape[1]):
        count = np.zeros(S.shape[0])
        common = np.zeros(S.shape[0])
        for j in range(S.shape[0]):
            count[j] = np.count_nonzero((X[keys[h]]==c[h][i])&(y==S[j]))
            common[j] = np.count_nonzero((X[keys[h]]==c[h][i]))    
        G[h][i] = (common[j]/len(T))*(-(count[j]/common[j])*np.log2(count[j]/common[j])-(count[j]/common[j])*np.log2(count[j]/common[j]))
G = np.sum(G, axis = 1)
result = np.where(G==G.min())
xh = keys[result[0]]
print('\nXh* = ', xh)
print('Gain = ', G.min())