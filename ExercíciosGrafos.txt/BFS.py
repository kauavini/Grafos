def BFS(G, s):
	for u in G:
		G[u]['cor'] = 'BRANCO'
		G[u]['d'] = INF
		G[u]['pai'] = 'NULO'
	G[s]['cor'] = 'CINZA'
	G[s]['d'] = 0
	G[s]['pai'] = 'NULO'

	Q = list([])
	Q.append(s)
	while len(Q) > 0:
		u = Q.pop(0)
		for v in G[u]['arestas']:
			if G[v]['cor'] == 'BRANCO':
				G[v]['cor'] = 'CINZA'
				G[v]['d'] = G[u]['d'] + 1
				G[v]['pai'] = u
				Q.append(v)
			G[u]['cor'] = 'PRETO'



# Cria o Grafo
G = {}
print('Implementação da BFS')
INF = 9999999999999999999999999999999
linha = input()
while linha != '':
	v1, v2 = linha.split()
	if v1 not in G:
		G[v1] = {'cor':'BRANCO', 'd':INF, 'pai':'NULO', 'arestas':list(v2)}
	else:
		G[v1]['arestas'].append(v2)
	if v2 not in G:
		G[v2] = {'cor':'BRANCO','d':INF,'pai':'NULO', 'arestas':list(v1)}
	else:
		G[v2]['arestas'].append(v1)
	
	linha = input()

print('Qual vétice começar?', end='')
s = input()
BFS(G, s)
conexo = True
for i in G:
	if G[i]['cor'] == 'BRANCO':
		conexo = False

if conexo:
	print('É conexo')
else:
	print('Desconexo')

