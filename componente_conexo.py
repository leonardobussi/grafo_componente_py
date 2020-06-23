grafo = { 0 : set([1, 2, 3]),
          1 : set([0, 2, 3]),
          2 : set([0, 1, 3]),
          3 : set([0, 1, 2]),

          4 : set([5, 6]),
          5 : set([4, 6]),
          6 : set([4, 5]),
        }


def componente(grafo, comeco, fim):
    visitado, rota = set(), [comeco]
    visitadoFim, rotaFim = set(), [fim]

    while rota:
        vertice = rota.pop(0)
        if vertice not in visitado:
            visitado.add(vertice)
            rota.extend(grafo[vertice] - visitado)

    while rotaFim:
        verticeFim = rotaFim.pop(0)
        if verticeFim not in visitadoFim:
            visitadoFim.add(verticeFim)
            rotaFim.extend(grafo[verticeFim] - visitadoFim)

    a = set(), visitado 
    return print('são ', len(a), ' componentes conexo e as vercices são ', visitado, ' e ', visitadoFim)

print("\ngrafo ", grafo, "\n")
componente(grafo, 0, 6)
print()