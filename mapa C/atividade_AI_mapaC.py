from collections import deque
import heapq
#Meu código porco para a atividade:

#função para reconst caminho
def reconstruir_caminho(pais, objetivo):
    caminho = []
    pos = objetivo
    while pos is not None:
        caminho.append(pos)
        pos = pais.get(pos)
    caminho.reverse()
    return caminho

#BFS(busca em largura)
def bfs(grid, inicio, objetivo):
    lados = [(-1,0), (1,0), (0,-1), (0,1)]
    fila = deque([inicio])
    pais = {inicio: None}
    explorado = 0

    while fila:
        x, y = fila.popleft()
        explorado += 1
        
        if (x, y) == objetivo:
            return reconstruir_caminho(pais, objetivo), explorado
        
        for dx, dy in lados:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == '.' and (nx, ny) not in pais:
                    fila.append((nx, ny))
                    pais[(nx, ny)] = (x, y)
    return None, explorado

#A* (busca em largura -- Manhattan)
def a_man(grid, inicio, objetivo):
    lados = [(-1,0), (1,0), (0,-1), (0,1)]
    def heuristica(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    fila = [(0 + heuristica(inicio, objetivo), 0, inicio)]
    pais = {inicio: None}
    g_score = {inicio: 0}
    explorado = 0

    while fila:
        _, custo, atual = heapq.heappop(fila)
        explorado += 1

        if atual == objetivo:
            return reconstruir_caminho(pais, objetivo), explorado
        
        for dx, dy in lados:
            nx, ny = atual[0] + dx, atual[1] + dy
            vizinho = (nx, ny)
            if 0 <= nx <len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == '#':
                    continue
                novo_custo = g_score[atual] + 1
                if vizinho not in g_score or novo_custo < g_score[vizinho]:
                    g_score[vizinho] = novo_custo
                    prioridade = novo_custo + heuristica(vizinho, objetivo)
                    heapq.heappush(fila, (prioridade, novo_custo, vizinho))
                    pais[vizinho] = atual
    
    return None, explorado

#Func para imprimir mapa e caminho:
def print_mapa(grid, caminho):
    grid_copy = [linha[:] for linha in grid]
    if caminho:
        for (x, y) in caminho[1:-1]:
            grid_copy[x][y] = 'o'
    for linha in grid_copy:
        print(''.join(linha))
    print()

#Func para salvar mapa em txt:
def salvar_mapa_txt(grid, caminho, nome_arquivo):
    grid_copy = [linha[:] for linha in grid]
    if caminho:
        for (x, y) in caminho[1:-1]:
            grid_copy[x][y] = 'o'
    with open(nome_arquivo, 'w') as f:
        for linha in grid_copy:
            f.write("".join(linha) + "\n")

#main:
def mapa_percorrido():

    mapa_matriz_C = [
    "..##.....###...",
    ".#...#...##....",
    "###.#...##...##",
    "..#.##.#.......",
    "#....#....##...",
    "...#..######..#",
    "#.##..#......#.",
    ".##..##......#.",
    "#......#....##.",
    "...#..#####.#.#",
    "##...#....#.##.",
    "##....#..#..##.",
    "...##..#......#",
    "#.##.###..#..#.",
    "#.............."
]

    grid_C = [list(linha) for linha in mapa_matriz_C]


    inicio, objetivo = (0,0), (14,14)

#BFS
    caminho_bfs, explorados_bfs = bfs(grid_C, inicio, objetivo)
    print('=== BFS ===')
    if caminho_bfs:
        print(f'caminho encontrado! passos: {len(caminho_bfs)-1}')
        print(f'Nós explorados: {explorados_bfs}')
        print_mapa(grid_C, caminho_bfs)
        salvar_mapa_txt(grid_C, caminho_bfs, 'mapa_BFS.txt')
        print("Mapa BFS salvo em 'mapa_BFS.txt'")
    else:
        print('Nenhum caminho encontrado!')

#A*
    caminho_a, explorados_a = a_man(grid_C, inicio, objetivo)
    print('=== A* ===')
    if caminho_a:
        print(f'caminho encontrado! passos: {len(caminho_a)-1}')
        print(f'Nós explorados: {explorados_a}')
        print_mapa(grid_C, caminho_a)
        salvar_mapa_txt(grid_C, caminho_a, 'mapa_Astar.txt')
        print("Mapa A* salvo em 'mapa_Astar.txt'")
    else:
        print('Nenhum caminho encontrado!')

#comparação:
    print('=== comparação ===')
    print(f'BFS -> passos: {len(caminho_bfs)-1 if caminho_bfs else '∞'}, explorados: {explorados_bfs}')
    print(f'A* -> passos: {len(caminho_a)-1 if caminho_a else '∞'}, explorados: {explorados_a}')

if __name__ == '__main__':
    mapa_percorrido()