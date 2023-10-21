# calculadora-descontos
Um programa Python que simula um sistema de vendas em uma loja. Calcula o preço e oferece descontos de acordo com algumas regras da loja.

# Como funciona:⚙️

1 -  print("Bem vindo a loja Sol Nascente"): Isso imprime uma mensagem de boas-vindas na tela quando o programa é executado.

 # Entrada de Dados:

2- valor_produto = float(input("Entre com o valor do produto:")): Solicita ao usuário que insira o valor do produto. O valor é lido como um número de ponto flutuante (float).

3- qtd_produto = int(input("Entre com a quantidade desejada:")): Solicita ao usuário que insira a quantidade desejada do produto. A quantidade é lida como um número inteiro (int).

4-  valor_total = 0: Inicializa a variável valor_total com o valor zero, mas essa variável não é usada no cálculo do preço total.

# Análise dos Descontos:

5- A seção seguinte usa uma estrutura condicional (if, elif, else) para determinar o desconto com base na quantidade de produtos comprados.

Se a quantidade de produtos for menor que 9, nenhum desconto é aplicado (desconto_produto recebe 0).
Se a quantidade estiver entre 10 e 100, um desconto de 5% é aplicado.
Se a quantidade estiver entre 100 e 999, um desconto de 10% é aplicado.
Se a quantidade for maior ou igual a 1000, um desconto de 15% é aplicado.

# Cálculo de Preços:

6- total_sem_desconto é calculado multiplicando o valor_produto pelo qtd_produto. Isso representa o valor total sem desconto.

7-  total_com_desconto é calculado subtraindo o valor do desconto do valor total sem desconto.

# Impressão na Tela:

8- A seção a seguir imprime na tela o valor do produto com e sem desconto.

total_sem_desconto é impresso formatado com duas casas decimais para representar o valor total sem desconto.

total_com_desconto é impresso de maneira semelhante, representando o valor com desconto.

print("Tenha um ótimo dia!"): Uma mensagem de despedida que é impressa no final do programa.
