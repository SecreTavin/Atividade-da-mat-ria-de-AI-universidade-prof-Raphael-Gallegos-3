import heapq

def calcular_manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def executar_a_estrela(mapa, inicio, objetivo, mostrar_processo=True):
    linhas = len(mapa)
    colunas = len(mapa[0])

    if not (0 <= inicio[0] < linhas and 0 <= inicio[1] < colunas):
        return None, "Posição inicial inválida", 0
    if not (0 <= objetivo[0] < linhas and 0 <= objetivo[1] < colunas):
        return None, "Posição objetivo inválida", 0
    if mapa[inicio[0]][inicio[1]] == '#':
        return None, "Posição inicial é obstáculo", 0
    if mapa[objetivo[0]][objetivo[1]] == '#':
        return None, "Posição objetivo é obstáculo", 0

    heap = []
    g_inicial = 0
    h_inicial = calcular_manhattan(inicio, objetivo)
    f_inicial = g_inicial + h_inicial
    heapq.heappush(heap, (f_inicial, g_inicial, inicio, [inicio]))
    
    visitados = set()
    #isitados.add(inicio)
    nos_expandidos = 0
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        f, g, (linha, coluna), caminho = heapq.heappop(heap)
        
        if (linha, coluna) in visitados:
            continue
        
        visitados.add((linha, coluna))
        nos_expandidos += 1

        if mostrar_processo:
            h = f - g
            print(f"Expandindo nó: ({linha}, {coluna}) - g={g}, h={h}, f={f}")

        if (linha, coluna) == objetivo:
            return caminho, f"Sucesso! Nós expandidos: {nos_expandidos}", nos_expandidos

        for dl, dc in movimentos:
            nova_linha, nova_coluna = linha + dl, coluna + dc

            if (0 <= nova_linha < linhas and 0 <= nova_coluna < colunas and
                mapa[nova_linha][nova_coluna] != '#' and
                (nova_linha, nova_coluna) not in visitados):

                g_novo = g + 1
                h_novo = calcular_manhattan((nova_linha, nova_coluna), objetivo)
                f_novo = g_novo + h_novo
                novo_caminho = caminho + [(nova_linha, nova_coluna)]

                heapq.heappush(heap, (f_novo, g_novo, (nova_linha, nova_coluna), novo_caminho))

    return None, f"Nenhum caminho encontrado. Nós expandidos: {nos_expandidos}", nos_expandidos


def imprimir_relatorio(caminho, nos_expandidos, nome_mapa):
    print(f"\n{'='*60}")
    print("RELATÓRIO DA BUSCA A*")
    print('='*60)
    if caminho:
        print("Existe caminho entre início e objetivo? SIM")
        print(f"Número de passos do caminho mais curto: {len(caminho)} passos")
    else:
        print("Existe caminho entre início e objetivo? NÃO")
        print("Número de passos do caminho mais curto: N/A")
    print(f"Nós explorados no processo: {nos_expandidos} nós")
    print(f"\nInformações adicionais:")
    print(f"   Mapa: {nome_mapa}")
    print(f"   Algoritmo: A* com heurística de Manhattan")
    if caminho:
        print(f"   Coordenadas do caminho: {caminho}")
        print(f"   Eficiência: {len(caminho)}/{nos_expandidos} = {len(caminho)/nos_expandidos:.2%}")
    print('='*60)
