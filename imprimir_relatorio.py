
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
