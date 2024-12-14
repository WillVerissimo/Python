# Desafios Regex

# DESAFIO 1

# Encontre a palavra simples'

'Olá! sou uma frase simples'
#simples

# DESAFIO 2

# Encontre todas as ocorrências de 23 (os números juntos) e exatamente com esses valores

'dev123com'
'developer 123'
'dev = 123'
'dev = 1234'
'dev = 1337'
'dev = 9000'
#23

# DESAFIO 3

# Encontre todos os valores onde o valor inicial é 2, porém o segundo valor você não conhece: ex: 23, 24,21, 26 etc..

'dev123com'
'developer 123'
'dev = 123'
'dev = 1234'
'dev = 1337'
'dev = 9000'
#\d\.

# DESAFIO 4

# Usando os cvalores a seguir, encontre os seguintes números por completo, usando regex

'13.35.86'
'22.36.77'
'53.12.34'
# \d\d\.\d\d\.\d\d

# DESAFIO 5

# Crie um regex para encontrar o seguinte padrão: Encontre apenas as combinações segundo o descrito abaixo

'bah pular'
'tah encontrar'
'jah encontrar'
'nah encontrar'
'uai pular'
#[tjn]ah

# DESAFIO 6

# Encontre a combinação de acordo com o descrito abaixo:

'(123)1234-1235 encontrar'
'(123)1234-1235 encontrar'
'(129)1234-1235 pular'
'(129)1234-1235 pular'
#[(]123[)]\d\d\d\d[-]\d\d\d\d

# DESAFIO 7

# Usando regex, encontre apenas a sequência 1234 abaixo

'1234 encontrar'
'6462 pular'
#[1-4]

# DESAFIO 8

# Usando regex, encontre apenas as letras iniciandos de p a v

'pqrstuv encontrar'
'wxyz pular'
'abcdefg pular'
#[p-v]

# DESAFIO 9

# Crie um regex para encontrar tanto pizzas enviadas como pizza enviada

'2 pizzas enviadas' 

'1 pizza enviada'

'3 pizzas enviadas'
#pizzas? enviadas?
