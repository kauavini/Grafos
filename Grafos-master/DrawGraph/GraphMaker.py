import pygraphviz as pvg
def salvaImagemGrafo(meuGrafo, arquivo, r):
  resp = ''
  if r == 1:
    G = pvg.AGraph(directed=True)
  if r == 2:
    G = pvg.AGraph()
  while True:
    print('''[1]Quer adicionar ao grafo os vétices?
[2] Quer adicionar as adjacências?
[3] Quer organizar o grafo em um arquivo .dot?
[4] Quer criar um arquivo .png com a representação do grafo?
''')
    resp = input().strip()
    if resp == '1':
      for u in meuGrafo:
       G.add_node(u)
    if resp == '2':
       for u in meuGrafo:
         for v in meuGrafo[u]['adjacencias']:
      	   G.add_edge(u, v)
    if resp == '3':
       G.layout(prog='dot')
    if resp == '4':
       G.draw(arquivo)

G = {}
print('-='* 20)
print('GRAPH MAKER')
print('-='* 20)
print('[1] Grafo dirigido')
print('[2] Grafo grafo')
r = int(input())
if r == 1:
  print('Digite os vétices: (Digite {stop} para parar!)')
  n1 = ''
  linha = str(input()).split()
  while(n1 !='STOP'):
    if len(linha) == 1:
      v1 = linha[0]
      G[v1] = {'cor':'BRANCO', 'd':0, 'f':0, 'pai':'NULO','adjacencias':[]}
    else:
      v1 = linha[0]
      v2 = linha[1]
      if(v1 not in G):
        G[v1]={'cor':'BRANCO','d':0,'f':0,'pai':'NULO','adjacencias':list([v2])}
      else:
	G[v1]['adjacencias'].append(v2)

      if(v2 not in G):
	G[v2]={'cor':'BRANCO','d':0,'f':0,'pai':'NULO','adjacencias':list([])}
    linha = input()
    n1 = linha.upper()
    linha = linha.split()
if r == 2:
  n1 = ''
  print('Digite os vétices: (Digite {stop} para parar!)')
  linha = input().split()
  while(n1 != 'STOP'):
    if len(linha) == 1:
      v1 = linha[0]
      G[v1] = {'cor':'BRANCO', 'd':0, 'f':0, 'pai':'NULO','adjacencias':[]
    else:
      if (v1 not in G):
	G[v1]={'cor':'BRANCO','d':0,'f':0,'pai':'NULO','adjacencias':list([v2])}
      else:
	G[v1]['adjacencias'].append(v2)
      if(v2 not in G):
	 G[v2]={'cor':'BRANCO','d':0,'f':0,'pai':'NULO','adjacencias':list([v1])}
      else:
	 G[v2]['adjacencias'].append(v1) 
   linha = input()
   n1 = linha
   linha = linha.split()
  
    
    

print(G)     

print('Você quer salvar o grafo?[s/n]')
resp = input()
if resp == 's':
  salvaImagemGrafo(G,"meugrafo.png", r)
else:
  print('Fim do Programa')

