# Função para verificar se o número é par ou ímpar
def verificar_par_impar(numero):
    if numero % 2 == 0:
        return f"O número {numero} é PAR."
    else:
        return f"O número {numero} é ÍMPAR."

# Entrada do usuário
numero = int(input("Digite um número: "))

# Chama a função e imprime o resultado
print(verificar_par_impar(numero))