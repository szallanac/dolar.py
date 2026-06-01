print("=== CONVERSOR DE DÓLAR ===")

try:
    # Entrada de dados
    cotacao = float(input("Digite a cotação do dólar: "))
    reais = float(input("Digite o valor em reais (R$): "))

    # Verifica se a cotação é válida
    if cotacao > 0:
        dolares = reais / cotacao

        # Exibe o resultado
        print(f"R$ {reais:.2f} equivalem a US$ {dolares:.2f}")
    else:
        print("Erro: a cotação do dólar deve ser maior que zero.")

except ValueError:
    print("Erro: digite apenas números.")