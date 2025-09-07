from collections import deque

def executar_bfs(mapa, inicio, objetivo, mostrar_processo=True):
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
    fila = deque([(inicio[0], inicio[1], [inicio])])
    visitados = set()
    visitados.add(inicio)
    nos_expandidos = 0
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while fila:
        linha, coluna, caminho = fila.popleft()
        nos_expandidos += 1
        if mostrar_processo:
            print(f"Expandindo nó: ({linha}, {coluna})")
        if (linha, coluna) == objetivo:
            return caminho, f"Sucesso! Nós expandidos: {nos_expandidos}", nos_expandidos
        for dl, dc in movimentos:
            nova_linha, nova_coluna = linha + dl, coluna + dc
            if (0 <= nova_linha < linhas and 0 <= nova_coluna < colunas and
                mapa[nova_linha][nova_coluna] != '#' and 
                (nova_linha, nova_coluna) not in visitados):
                visitados.add((nova_linha, nova_coluna))
                novo_caminho = caminho + [(nova_linha, nova_coluna)]
                fila.append((nova_linha, nova_coluna, novo_caminho))
    return None, f"Nenhum caminho encontrado. Nós expandidos: {nos_expandidos}", nos_expandidos

def visualizar_caminho(mapa, caminho=None):
    if not caminho:
        for linha in mapa:
            print(''.join(linha))
        return
    mapa_visual = [linha[:] for linha in mapa]
    for i, (linha, coluna) in enumerate(caminho):
        if i == 0:
            mapa_visual[linha][coluna] = 'I'
        elif i == len(caminho) - 1:
            mapa_visual[linha][coluna] = 'O'
        else:
            mapa_visual[linha][coluna] = '°'
    for linha in mapa_visual:
        print(''.join(linha))

def imprimir_relatorio(caminho, nos_expandidos, nome_mapa):
    print(f"\n{'='*60}")
    print("RELATÓRIO DA BUSCA BFS")
    print('='*60)
    if caminho:
        print("Existe caminho entre início e objetivo? SIM")
        print(f"Número de passos do caminho mais curto: {len(caminho)-1} passos")
    else:
        print("Existe caminho entre início e objetivo? NÃO")
        print("Número de passos do caminho mais curto: N/A")
    print(f"Nós explorados no processo: {nos_expandidos} nós")
    print(f"\nInformações adicionais:")
    print(f"   Mapa: {nome_mapa}")
    if caminho:
        print(f"   Coordenadas do caminho: {caminho}")
        print(f"   Eficiência: {len(caminho)}/{nos_expandidos} = {len(caminho)/nos_expandidos:.2%}")
    print('='*60)
