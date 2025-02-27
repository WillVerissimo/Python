# Extraia as cores da lista a seguir e coloca-as em uma nova lista. Finalmente, imprime a nova lista na tela.

def extrair_cor(nova_lista):
    return nova_lista[1]

pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]

# Usando map para aplicar a função extrair_cor a cada sublista
cores = list(map(extrair_cor, pinturas))
print(cores)