def tabelaMac():
    print('''
---------CARDAPIO---------
1 - Brabo Bacon Salad.
2 - Big Mac.
3 - Duplo Quarterão.
4 - Quarterão com Bacon.
5 - Quarterão com Queijo.
6 - McChicken.
7 - Casquinha.
8 - Refrigerante 500 ml.
9 - McCrispy Chicken Deluxe.
10 - Promoções do dia.
''')

    categoria = int(input("Informe a categoria do produto (1 a 10): "))

    while categoria < 1 or categoria > 10:
        categoria = int(input("Informe a categoria novamente: "))

    if categoria == 1:
        print("Brabo Bacon Salad")
        print("R$19,90")
    elif categoria == 2:
        print("Big Mac")
        print("R$21,90")
    elif categoria == 3:
        print("Duplo Quarterão")
        print("R$22,90")
    elif categoria == 4:
        print("Quarterão com Bacon")
        print("R$22,90")
    elif categoria == 5:
        print("Quarterão com Queijo")
        print("R$23,90")
    elif categoria == 6:
        print("McChicken")
        print("R$19,90")
    elif categoria == 7:
        print("Casquinha")
        print("R$3,50")
    elif categoria == 8:
        print("Refrigerante 500 ml")
        print("R$18,90")
    elif categoria == 9:
        print("McCrispy Chicken Deluxe")
        print("R$32,90")
    elif categoria == 10:
        print("Promoções do dia")
        print("      ------Promoções do dia-----")
        print("1 - Combo BIGMAC com mcFRITAS grandes ")
        print("2 - BIG Tasty + Bebidas 500ML ")
        print("3 - 2 Chicken Jr. + Bebidas 500ML ")

        promocao = int(input("Informe a sua promoção do produto (1 a 3): "))
        while promocao < 1 or promocao > 3:
            promocao = int(input("Informe a promoção novamente: "))

        if promocao == 1:
            print("Combo BIGMAC com mcFRITAS Grandes = R$30,90")
            print("Total = R$30,90")
        elif promocao == 2:
            print("BIG Tasty + Bebidas 500ML = R$31,90")
            print("Total = R$31,90")
        elif promocao == 3:
            print("2 Chicken Jr. + Bebidas 500ML = R$19,90")
            print("Total = R$19,90")

    pagamento = input("Deseja realizar o pagamento agora? (S/N): ").upper()
    if pagamento == 'S':
        print("1 - Pix.")
        print("2 - Cartão de Crédito.")
        print("3 - Cartão de Débito.")
        print("4 - Vale Alimentação.")
    else:
        print("Você é obrigado a pagar ")
        print("1 - Pix.")
        print("2 - Cartão de Crédito.")
        print("3 - Cartão de Débito.")
        print("4 - Vale Alimentação.")

    pagamento = int(input("Informe a forma de pagamento do produto (1 a 4): "))

    while pagamento < 1 or pagamento > 4:
        pagamento = int(input("Informe a forma de pagamento novamente: "))

    if pagamento == 1:
        print("Disponibilização do QR CODE")
    elif pagamento in (2, 3, 4):
        print("Disponibilização da maquininha de pagamento")

    novamente = input('''
Quer comprar novamente?
Digite S para SIM ou N para NÃO:''')

    if novamente.upper() == 'S':
        tabelaMac()
    elif novamente.upper() == 'N':
        print('Próximo!')
    else:
        print('Opção inválida!')
        novamente = input('''
Quer comprar novamente?
Digite S para SIM ou N para NÃO:''')

tabelaMac()