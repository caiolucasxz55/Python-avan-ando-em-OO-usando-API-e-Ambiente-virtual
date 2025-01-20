from modelos.Restaurante import*
from modelos.cardapio.bebida import*
from modelos.cardapio.prato import*
from modelos.cardapio.sobremesa import*

restaurante_hiro = Restaurante('hiro', 'japonesa')
bebida_suco = Bebida('laranjinha',3.0,'medio')
sobremesa_lemon = Sobremesa('lemon',20.0,'limao feito com mousse de limao e chocolate bramco')
prato_principal = Prato('kare raisu',45.0,'arroz,curry, com porco frito e salada de acompanhamento')

sobremesa_lemon.aplicar_desconto()
bebida_suco.aplicar_desconto()

restaurante_hiro.adicionar_item_cardapio(bebida_suco)
restaurante_hiro.adicionar_item_cardapio(prato_principal)
restaurante_hiro.adicionar_item_cardapio(sobremesa_lemon)

def main():
    restaurante_hiro.exibir_cardapio

if __name__ == '__main__':
    main()