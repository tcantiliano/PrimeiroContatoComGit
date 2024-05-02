from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MenuInicial(BoxLayout):
    def __init__(self, **kwargs):
        super(MenuInicial, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label_titulo = Label(text="Bem-vindo ao Restaurante XYZ")
        self.add_widget(self.label_titulo)

        self.botao_cardapio = Button(text="Ver Cardápio", on_press=self.mostrar_cardapio)
        self.add_widget(self.botao_cardapio)

    def mostrar_cardapio(self, instance):
        self.clear_widgets()
        self.add_widget(Cardapio())


class Cardapio(BoxLayout):
    def __init__(self, **kwargs):
        super(Cardapio, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.cardapio = {
            1: {"nome": "Porção-X", "preco": 10.0},
            2: {"nome": "Porção-Y", "preco": 15.0},
            3: {"nome": "Beirute-X", "preco": 8.0},
            4: {"nome": "Beirute-Y", "preco": 3.0}
        }
        self.pedido = []

        self.label_cardapio = Label(text="Selecione um item:")
        self.add_widget(self.label_cardapio)

        for item, info in self.cardapio.items():
            btn = Button(text=f"{info['nome']} - R${info['preco']}", on_press=self.adicionar_item_pedido)
            btn.item_numero = item  # Armazena o número do item no botão
            self.add_widget(btn)

        self.label_pedido = Label(text="Pedido:")
        self.add_widget(self.label_pedido)

        self.add_widget(Button(text="Finalizar Pedido", on_press=self.mostrar_pedido))

    def adicionar_item_pedido(self, instance):
        numero_item = instance.item_numero
        self.pedido.append(self.cardapio[numero_item])
        self.label_pedido.text = f"Pedido: {', '.join(item['nome'] for item in self.pedido)}"

    def mostrar_pedido(self, instance):
        total = sum(item['preco'] for item in self.pedido)
        self.label_pedido.text = f"Total do pedido: R${total}"


class RestauranteApp(App):
    def build(self):
        return MenuInicial()


if __name__ == '__main__':
    RestauranteApp().run()
