num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada(+, -, *, /):")

# Verifique qual operação foi escolhida e realiza o cálculo

if operacao == "+":
    resultado = num1 + num2
    
elif operacao == "-":
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1 * num2

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else: resultado = "Erro! Divisão por zero não permitida."

else: print("Operação inválida!")

# Exibe o resultado

print(f"{resultado}")