NombreCom = input("ingrese su nombre completo:")
print(f"su nombre completo es: {NombreCom}")
circulo = float(input("ingrese el area del circulo:"))
cuadrado = float(input("ingrese el area del cuadrado:"))
rectangulo = float(input("ingrese el area del rectangulo:"))
triangulo = float(input("ingrese el area del triangulo:"))

#Opcion para calcular el are del circulo
if input("¿Quieres calcular el área del círculo? (s/n): ").lower() == "s":
    radioC = float(circulo)
    areaC = 3.14159 * radioC**2
    print(f"El área del círculo es: {areaC}")
else:
    print("No se calculará el área del círculo.")

#Opcion para calcular el area del cuadrado
if input("¿Quieres calcular el área del cuadrado? (s/n): ").lower() == "s":
    radioCu = float(cuadrado)
    areaCu = radioCu**2
    print(f"El área del cuadrado es: {areaCu}")
else:
    print("No se calculará el área del cuadrado")

#Opcion para calcular el area del rectángulo
if input("¿Quieres calcular el área del rectángulo? (s/n): ").lower() == "s":
    radioRe = int(rectangulo)
    areaRe = radioRe * 2
    print(f"El área del rectángulo es: {areaRe}")
else:
    print("No se calculará el área del rectángulo.")

#Opcion para calcular el area del triangulo
if input("¿Quieres calcular el área del triángulo? (s/n): ").lower() == "s":
    areaTr = int(triangulo)
    areaTr = (areaTr * 2) / 2
    print(f"El área del triángulo es: {areaTr}")
else:
    print("No se calculará el área del triángulo.")