# Função para verificar se uma palavra ou frase é um palíndromo
def verificar_palindromo(texto):
    # Remover espaços e converter para minúsculas
    texto_limpo = texto.replace(" ", "").lower()
    
    # Verificar se o texto limpo é igual ao seu reverso
    return texto_limpo == texto_limpo[::-1]

# Entrada do usuário
texto = input("Digite uma palavra ou frase: ")

# Verifica se é um palíndromo e imprime o resultado
if verificar_palindromo(texto):
    print(f"'{texto}' é um palíndromo!")
else:
    print(f"'{texto}' não é um palíndromo!")
