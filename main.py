import random


def gerar_caso_de_teste(num_segmentos, num_ligacoes):
  ligacoes = set()

  while len(ligacoes) < num_ligacoes:
    x = random.randint(1, num_segmentos)
    y = random.randint(1, num_segmentos)
    if x != y:  # Garante que os segmentos são diferentes
      ligacao = (min(x, y), max(x, y))
      ligacoes.add(ligacao)

  print(num_segmentos, num_ligacoes)
  for ligacao in ligacoes:
    print(ligacao[0], ligacao[1])


def DFS(N, grafo, v):
  cor[v] = 'C'
  for w in range(N):
    if (grafo[v][w] == 1) and (cor[w] == 'B'):
      DFS(N, grafo, w)


N, L = map(int, input().split())

grafo = []
cor = []

#criando a matriz de adjacencia
for _ in range(N):
  grafo.append([0] * N)
  cor.append('B')  #para o algoritmo de DFS

for _ in range(L):
  x, y = map(int, input().split())
  grafo[x - 1][y - 1] = 1
  grafo[y - 1][x - 1] = 1  #nao direcionado

#matriz (visual)
#for row in grafo:
#  print(row)

#DFS
DFS(N, grafo, 0)

#print(cor)

if ('B') in cor:
  print('INCOMPLETO\n')
else:
  print('COMPLETO\n')

#gerar_caso_de_teste(99, 99)

exit(0)
