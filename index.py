print("Bem vindo a loja Sol Nascente")

# Entrada de dados
valor_produto = float(input("Entre com o valor do produto:"))
qtd_produto = int(input("Entre com a quantidade desejada:"))

valor_total = 0

# Analise dos descontos baseada na quantidade de produtos
if qtd_produto < 9:
    desconto_produto = 0  # sem desconto
elif qtd_produto >= 10 and qtd_produto <= 100:
    desconto_produto = 0.05  # 5% de desconto
elif qtd_produto >= 100 and qtd_produto <= 999:
    desconto_produto = 0.10  # 10% de desconto
else:
    desconto_produto = 0.15  # 15% de desconto

# calcula os preços
total_sem_desconto = qtd_produto * valor_total
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto

# imprime na tela o valor do produto com desconto e sem desconto
total_sem_desconto = valor_produto * qtd_produto
print("o valor sem desconto foi : R$ {:.2f}".format(total_sem_desconto))

total4_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print("o valor com desconto foi : R$ {:.2f}".format(total4_com_desconto))

# exibe mensagem final
print("Tenha um ótimo dia!")                                                                                                         