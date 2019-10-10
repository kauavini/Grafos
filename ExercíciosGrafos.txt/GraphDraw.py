import pygraphviz as pvg


def salvaImagemGrafo(meuGrafo, arquivo):
  G = pvg.AGraph()
  for u in meuGrafo:
    G.add_node(u)
  for u in meuGrafo:
    for v in meuGrafo[u]['adjacencias']:
      G.add_edge(u, v)
  G.layout(prog='dot')
  G.draw(arquivo)

G = {}

linha = input()

while(linha !=""):
  linha = linha.split()
  if len(linha) == 1:
    v1 = linha[0]
    G[v1] = {'cor':'BRANCO', 'd':0, 'f':0, 'pai':'NULO', 'adjacencias':list([])}
  else:
    v1 = linha[0]
    v2 = linha[1]
    if(v1 not in G):
      G[v1]={'cor':'BRANCO','d':0,'f':0,'pai':'NULO','adjacencias':list([v2])}
    else:
      G[v1]['adjacencias'].append(v2)
    if(v2 not in G):
      G[v2]={'cor':'BRANCO','d':0,'f':0,'pai':'NULO','adjacencias':list([v1])}
    else:
      G[v2]['adjacencias'].append(v1) 

  linha = input()
  print(linha)

print(G)
salvaImagemGrafo(G,"meugrafo.png")