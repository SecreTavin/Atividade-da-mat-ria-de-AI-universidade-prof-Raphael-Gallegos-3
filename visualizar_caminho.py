
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
