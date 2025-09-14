import random
import math
#meu código porco
produtos = {(60,10), (100,20), (120,30), (90,15), (30,5), (70,12), (40,7),
            (160,25), (20,3), (50,9), (110,18), (85,14), (95,16), (200,28), (55,6)}
produtos = list(produtos)

#começando a função do hill climbing(hc)
def hill_climbing(produtos, capacidade_mochila):
    peso = 0
    valor = 0
    mochila = []
    random.shuffle(produtos)
    for produto in produtos:
        if peso + produto[0] <= capacidade_mochila:
            mochila.append(produto)
            peso += produto[0]
            valor += produto[1]
    melhor_valor = valor
    melhor_mochila = mochila.copy()
    melhor_peso = peso
    melhor_produtos = produtos.copy()
    for _ in range(300):
        random.shuffle(melhor_produtos)
        peso = 0
        valor = 0
        mochila = []
        for produto in melhor_produtos:
            if peso + produto[0] <= capacidade_mochila:
                mochila.append(produto)
                peso += produto[0]
                valor += produto[1]
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_mochila = mochila.copy()
                    melhor_peso = peso
    return melhor_mochila, melhor_peso, melhor_valor

#definindo capacidade da mochila
capacidade_mochila = 50
melhor_mochila, melhor_peso, melhor_valor = hill_climbing(produtos, capacidade_mochila)
print("Melhor combinação de produtos:")
for produto in melhor_mochila:
    print(f"Peso: {produto[0]}, Valor: {produto[1]}")
print(f"Peso total: {melhor_peso}")
print(f"Valor total: {melhor_valor}")
# DE ACORDO COM O CHATGPT, MINHA RESPOSTA ESTÁ CERTA, MAS O HC NÃO ESTÁ O VERDADEIRO, POIS NÃO TEM VIZINHANÇA.


#CÓDIGO COM AUXILIO DO CHATGPT:
produtos = [(60,10), (100,20), (120,30), (90,15), (30,5), (70,12), (40,7),
            (160,25), (20,3), (50,9), (110,18), (85,14), (95,16), (200,28), (55,6)]

capacidade_mochila = 50

def fitness(mochila):
    """Retorna (peso, valor) reais — sem mascarar."""
    peso = sum(p[0] for p in mochila)
    valor = sum(p[1] for p in mochila)
    return peso, valor

def gerar_vizinhos(mochila, produtos, capacidade):
    viz = []
    # flip: adicionar ou remover um item
    for p in produtos:
        if p in mochila:
            nova = mochila.copy()
            nova.remove(p)
            peso, _ = fitness(nova)
            if peso <= capacidade:
                viz.append(nova)
        else:
            nova = mochila + [p]
            peso, _ = fitness(nova)
            if peso <= capacidade:
                viz.append(nova)
    # swaps: remove 1 (de dentro) e adiciona 1 (de fora)
    for out_item in list(mochila):
        for in_item in produtos:
            if in_item not in mochila:
                nova = mochila.copy()
                nova.remove(out_item)
                nova.append(in_item)
                peso, _ = fitness(nova)
                if peso <= capacidade:
                    viz.append(nova)
    return viz

def hill_climbing(produtos, capacidade, restarts=50):
    melhor_global = ([], 0, 0)  # (mochila, peso, valor)
    for _ in range(restarts):
        # SOLUÇÃO INICIAL (guloso + aleatoriedade)
        itens = produtos.copy()
        random.shuffle(itens)
        mochila = []
        for p in itens:
            peso_novo, _ = fitness(mochila + [p])
            if peso_novo <= capacidade:
                mochila.append(p)

        peso_atual, valor_atual = fitness(mochila)

        # subida de encosta: procura vizinho melhor e move
        melhorou = True
        while melhorou:
            melhorou = False
            viz = gerar_vizinhos(mochila, produtos, capacidade)
            # escolhe o vizinho com maior valor (se houver melhor)
            melhor_viz = None
            melhor_val = valor_atual
            for v in viz:
                _, val_v = fitness(v)
                if val_v > melhor_val:
                    melhor_val = val_v
                    melhor_viz = v
            if melhor_viz is not None:
                mochila = melhor_viz
                peso_atual, valor_atual = fitness(mochila)
                melhorou = True

        # atualiza global
        if valor_atual > melhor_global[2]:
            melhor_global = (mochila, peso_atual, valor_atual)

    return melhor_global

# Executa
melhor_mochila, melhor_peso, melhor_valor = hill_climbing(produtos, capacidade_mochila, restarts=100)

print("Melhor combinação de produtos:")
for produto in melhor_mochila:
    print(f"Peso: {produto[0]}, Valor: {produto[1]}")
print(f"Peso total: {melhor_peso}")
print(f"Valor total: {melhor_valor}")


#Função SA feita com auxilio do chatgpt
# lista de produtos (peso, valor)
produtos = [(60,10), (100,20), (120,30), (90,15), (30,5), (70,12), (40,7),
            (160,25), (20,3), (50,9), (110,18), (85,14), (95,16), (200,28), (55,6)]

CAPACIDADE = 50

def fitness(mochila):
    peso = sum(p[0] for p in mochila)
    valor = sum(p[1] for p in mochila)
    if peso > CAPACIDADE:
        return 0  # inválido
    return valor

def vizinho(mochila):
    # troca 1 item aleatório
    nova = mochila[:]
    idx = random.randrange(len(produtos))
    if produtos[idx] in nova:
        nova.remove(produtos[idx])
    else:
        nova.append(produtos[idx])
    return nova

def simulated_annealing(produtos, T0=50.0, Tmin=0.1, alpha=0.95, passos_por_T=30):
    # solução inicial
    atual = []
    melhor = atual[:]
    melhor_val = fitness(atual)

    T = T0
    while T > Tmin:
        for _ in range(passos_por_T):
            candidato = vizinho(atual)
            delta = fitness(candidato) - fitness(atual)
            if delta > 0 or random.random() < math.exp(delta / T):
                atual = candidato[:]
                if fitness(atual) > melhor_val:
                    melhor = atual[:]
                    melhor_val = fitness(atual)
        T *= alpha
    return melhor, sum(p[0] for p in melhor), melhor_val

# execução
mochila, peso, valor = simulated_annealing(produtos)
print("=== Simulated Annealing ===")
for p in mochila:
    print(f"Peso: {p[0]}, Valor: {p[1]}")
print(f"Peso total: {peso}, Valor total: {valor}")


#função GA feita com auxilio do chatgpt
produtos = [(60,10), (100,20), (120,30), (90,15), (30,5), (70,12), (40,7),
            (160,25), (20,3), (50,9), (110,18), (85,14), (95,16), (200,28), (55,6)]

CAPACIDADE = 50

def fitness(individuo):
    peso = sum(produtos[i][0] for i in range(len(produtos)) if individuo[i] == 1)
    valor = sum(produtos[i][1] for i in range(len(produtos)) if individuo[i] == 1)
    if peso > CAPACIDADE:
        return 0
    return valor

def reparar(individuo):
    """Remove itens até o peso ficar dentro da capacidade"""
    while True:
        peso = sum(produtos[i][0] for i in range(len(produtos)) if individuo[i] == 1)
        if peso <= CAPACIDADE:
            break
        # remove aleatoriamente um item que está na mochila
        idxs = [i for i in range(len(produtos)) if individuo[i] == 1]
        if not idxs:
            break
        remover = random.choice(idxs)
        individuo[remover] = 0
    return individuo

def gerar_individuo():
    ind = [random.randint(0,1) for _ in range(len(produtos))]
    return reparar(ind)

def torneio(pop, k=3):
    return max(random.sample(pop, k), key=lambda ind: fitness(ind))

def crossover(pai1, pai2):
    if random.random() < 0.9:  # p_cross
        ponto = random.randint(1, len(produtos)-1)
        filho1 = pai1[:ponto] + pai2[ponto:]
        filho2 = pai2[:ponto] + pai1[ponto:]
        return reparar(filho1), reparar(filho2)
    return reparar(pai1[:]), reparar(pai2[:])

def mutacao(ind):
    for i in range(len(ind)):
        if random.random() < 0.02:  # p_mut
            ind[i] = 1 - ind[i]
    return reparar(ind)

def genetic_algorithm(geracoes=120, pop_size=50):
    pop = [gerar_individuo() for _ in range(pop_size)]
    for g in range(geracoes):
        nova_pop = []
        # elitismo
        elite = sorted(pop, key=lambda ind: fitness(ind), reverse=True)[:2]
        nova_pop.extend(elite)

        while len(nova_pop) < pop_size:
            pai1 = torneio(pop)
            pai2 = torneio(pop)
            filho1, filho2 = crossover(pai1, pai2)
            nova_pop.append(mutacao(filho1))
            if len(nova_pop) < pop_size:
                nova_pop.append(mutacao(filho2))
        pop = nova_pop

    melhor = max(pop, key=lambda ind: fitness(ind))
    peso = sum(produtos[i][0] for i in range(len(produtos)) if melhor[i] == 1)
    valor = fitness(melhor)
    mochila = [produtos[i] for i in range(len(produtos)) if melhor[i] == 1]
    return mochila, peso, valor

# execução
mochila, peso, valor = genetic_algorithm()
print("=== Algoritmo Genético (corrigido) ===")
for p in mochila:
    print(f"Peso: {p[0]}, Valor: {p[1]}")
print(f"Peso total: {peso}, Valor total: {valor}")

"""
===========================
Comparação dos Algoritmos
===========================

Problema: Mochila 0/1 com capacidade de 50 kg
Produtos: [(peso, valor), ...]

Ótimo global conhecido: (50, 9)

------------------------------------------
1) Hill Climbing (HC)
------------------------------------------
- Estratégia: inicia solução aleatória, gera vizinhos (flip de 1 item),
  aceita apenas melhorias.
- Limitação: trava facilmente em ótimos locais.
- Resultado típico: encontra (50, 9), mas depende da ordem de vizinhos.

------------------------------------------
2) Simulated Annealing (SA)
------------------------------------------
- Estratégia: similar ao HC, mas permite aceitar piores soluções 
  temporariamente com probabilidade controlada pela "temperatura".
- Vantagem: consegue escapar de ótimos locais.
- Resultado observado: 
    - Encontrou (20+30=50, valor=8) em uma execução.
    - Pode encontrar (50,9) em outras rodadas.
- Conclusão: mais flexível que HC, mas estocástico (varia).

------------------------------------------
3) Algoritmo Genético (AG)
------------------------------------------
- Estratégia: população inicial de soluções, seleção por torneio (k=3),
  crossover de 1 ponto (p=0.9), mutação por bit flip (p=0.02),
  elitismo (2 melhores).
- Adaptação: função de reparo garante peso <= 50.
- Resultado observado: convergiu para (50,9) consistentemente.
- Conclusão: diversidade da população + reparo = ótima solução.

------------------------------------------
Reflexão sobre estocasticidade
------------------------------------------
- Os três métodos são estocásticos → usam sorteio/aleatoriedade
  (embaralhamento, vizinho aleatório, seleção genética).
- Isso significa que cada execução pode gerar resultados diferentes.
- Diferem de métodos determinísticos (como Programação Dinâmica), 
  que sempre retornam o mesmo resultado para a mesma entrada.
"""
