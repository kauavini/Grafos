import pygraphviz as pvg
def salvaImagemGrafo(meuGrafo, arquivo):
  resp = ''
  G = pvg.AGraph(directed=True)
  while True:
    print('''[1]Quer adicionar ao grafo os vétices?
[2] Quer adicionar as adjacências?
[3]Quer adicionar as arestas?
[4] Quer organizar o grafo em um arquivo .dot?
[5] Quer criar um arquivo .png com a representação do grafo?
''')
  resp = input().strip()
  if resp == '1':
    for u in meuGrafo:
      G.add_node(u)
  if resp == '2':
    for u in meuGrafo:
      for v in meuGrafo[u]['adjacencias']:
      G.add_edge(u, v)
  if resp == '5'
  G.layout(prog='dot')
  G.draw(arquivo)

G = {}
print('-='* 20)
print('GRAPH MAKER')
print('-='* 20)
print('Digite os vétices: (Digite {stop} para parar!)')

linha = input()
while(linha !='STOP'):
  if len(linha) == 1:
    linha.lower()
    v1 = linha.split()
    v1 = v1[0]
    G[v1] = {'cor':'BRANCO', 'd':0, 'f':0, 'pai':'NULO','adjacencias':[]}
  else:
    linha.lower()
    v1, v2 = linha.split()
    if(v1 not in G):

      G[v1]={'cor':'BRANCO','d':0,'f':0,'pai':'NULO','adjacencias':list([v2])}
    else:
      G[v1]['adjacencias'].append(v2)

    if(v2 not in G):
      G[v2]={'cor':'BRANCO','d':0,'f':0,'pai':'NULO','adjacencias':list([])}
  linha = input().upper()

print('Você quer salvar o grafo?[s/n]')
resp = int(input())
if resp == 's':
  salvaImagemGrafo(G,"meugrafo.png")
else:
  print('Fim do Programa')

