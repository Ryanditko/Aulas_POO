import random

def gerar_cpf():
    return "".join([str(random.randint(0, 9)) for _ in range(9)])

def gerar_subconjunto(conjunto):
    return set(random.sample(list(conjunto), int(random.random() * 100)))

# Criando um conjunto vazio para receber 'pessoas'
pessoas = set()

# Conjunto de pessoas
for _ in range(0, 100):
    cpf = gerar_cpf()
    pessoas.add(cpf)

# Conjunto de esportes
esportes = {
    "judo": gerar_subconjunto(pessoas),
    "volei_de_praia": gerar_subconjunto(pessoas),
    "ginastica": gerar_subconjunto(pessoas),
    "surfe": gerar_subconjunto(pessoas)
}

# a) Probabilidade de assistir Judô ou Surfe
judô_ou_surfe = esportes["judo"].union(esportes["surfe"])
prob_judo_ou_surfe = len(judô_ou_surfe) / len(pessoas) * 100

# b) Probabilidade de assistir pelo menos dois esportes
participantes_multiplos = sum(1 for pessoa in pessoas if sum(pessoa in esporte for esporte in esportes.values()) >= 2)
prob_pelo_menos_dois = participantes_multiplos / len(pessoas) * 100

# c) Probabilidade de assistir todos os esportes
todos_esportes = set.intersection(*esportes.values())
prob_todos_esportes = len(todos_esportes) / len(pessoas) * 100

# d) Probabilidade de não assistir nenhum esporte
nao_participantes = pessoas - set().union(*esportes.values())
prob_nenhum_esporte = len(nao_participantes) / len(pessoas) * 100

# Exibir resultados
print(f"Probabilidade de assistir Judô ou Surfe: {prob_judo_ou_surfe:.2f}%")
print(f"Probabilidade de assistir pelo menos dois esportes: {prob_pelo_menos_dois:.2f}%")
print(f"Probabilidade de assistir todos os esportes: {prob_todos_esportes:.2f}%")
print(f"Probabilidade de não assistir nenhum esporte: {prob_nenhum_esporte:.2f}%")
