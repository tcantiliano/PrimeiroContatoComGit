#tela de boas vindas
print('Dunga lanches')
#criar uma bibliotecas com itens e valores diferentes. Por exemplo um cardapio somente para porções, lanches etc.

cardapio = {
   "item":"Porção-X","preco":10.00,
   "item":"Porção-Y","preco":22.00,
   "item":"Beirute-Y","preco":32.00,
   "item":"Beirute-Y","preco":42.00,
   "item":"Pizzas-Y","preco":52.00,
   "item":"Pizzas-Y","preco":62.00
}

for chave,valor in cardapio.items():
    print(f'{chave},{valor}')

#após selecionar um cardapio adiciona e exibir as informações dele selecionar um item e ter a opção de adicionar no pedido, além de uma opção para excluir.

