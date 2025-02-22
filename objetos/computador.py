class Computador:
    marca = "Dell"
    processador = "Intel Core i5"
    ram = 8

pc1 = Computador()
pc2 = Computador()

pc2.marca = "Positivo"
pc2.processador = "Xeon E5 2670 V3"
pc2.ram = 16

print(f"\nMarca do pc: {pc1.marca}\nProcessador: {pc1.processador}\nMemória RAM: {pc1.ram}")
print(f"\nMarca do pc: {pc2.marca}\nProcessador: {pc2.processador}\nMemória RAM: {pc2.ram}\n")