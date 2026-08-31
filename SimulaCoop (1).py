valor = float(input("Valor do financiamento: R$ "))
taxa = 0.19
meses = int(input("Número de parcelas em meses: "))

tipo = input("Tipo de financiamento (SAC ou PRICE)Digite 1 para SAC ou 2 para PRICE: ")


def sac(valor, taxa, meses):

    taxa_mensal = (1 + taxa) ** (1 / 12) - 1

    amortizacao = valor / meses
    saldo = valor

    juros_total = 0

    for i in range(meses):

        juros = saldo * taxa_mensal
        parcela = amortizacao + juros

        juros_total = juros_total + juros
        saldo = saldo - amortizacao

        if i == 0:
            primeira = parcela

        ultima = parcela

    total = valor + juros_total

    cet = ((total / valor) ** (12 / meses) - 1) * 100

    print()
    print("===== SAC =====")
    print("Primeira parcela: R$", round(primeira, 2))
    print("Última parcela: R$", round(ultima, 2))
    print("Total de juros: R$", round(juros_total, 2))
    print("Total pago: R$", round(total, 2))
    print("CET:", round(cet, 2), "% ao ano")


def price(valor, taxa, meses):

    taxa_mensal = (1 + taxa) ** (1 / 12) - 1

    parcela = (valor * taxa_mensal) / (
        1 - (1 + taxa_mensal) ** (-meses)
    )

    total = parcela * meses

    juros = total - valor

    cet = ((total / valor) ** (12 / meses) - 1) * 100

    print()
    print("===== PRICE =====")
    print("Valor da parcela: R$", round(parcela, 2))
    print("Total de juros: R$", round(juros, 2))
    print("Total pago: R$", round(total, 2))
    print("CET:", round(cet, 2), "% ao ano")


if tipo == "1":
    sac(valor, taxa, meses)

elif tipo == "2":
    price(valor, taxa, meses)

else:
    print("Opção inválida!")