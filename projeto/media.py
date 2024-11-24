# Função para calcular a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Entrada do usuário: número de notas
quantidade_de_notas = int(input("Digite o número de notas: "))

# Lista para armazenar as notas
notas = []

# Loop para coletar as notas
for i in range(quantidade_de_notas):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

# Calcula a média
media = calcular_media(notas)

# Exibe a média
print(f"A média das notas é: {media:.2f}")
