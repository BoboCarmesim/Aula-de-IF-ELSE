a = float(input("Digite a primeira medida: "))
b = float(input("Digite a segunda medida: "))
c = float(input("Digite a terceira medida: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("É um triângulo")
else:
    print("Não é triângulo")