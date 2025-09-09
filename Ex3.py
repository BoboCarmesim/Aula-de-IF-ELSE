km_saida = float(input("Digite a quilometragem de saída (km): "))
km_chegada = float(input("Digite a quilometragem de chegada (km): "))
hora_saida =int( input("Digite a hora de saída (formato HH): "))
hora_chegada =int( input("Digite a hora de chegada (formato HH): "))

media=km_chegada + km_saida
tempo=hora_chegada + hora_saida
velo_media=media/tempo

if velo_media > 80:
    km_acima=velo_media - 80
    multa=km_acima * 5
    print(f"Você excedeu o limite! multa de R${multa:.2f}")
else:
    print(f"Velocidade dentro do limite",{velo_media})