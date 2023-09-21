from logica.calculoMCD import MCDCalculator

def ingresar_numero():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            return num
        except ValueError:
            print("Error: Ingrese un número entero válido.")


def main():
    print("Cálculo del Máximo Común Divisor (MCD)")

    num1 = ingresar_numero()
    num2 = ingresar_numero()

    mcd = MCDCalculator.calcular_mcd(num1, num2)

    print(f"El MCD de {num1} y {num2} es {mcd}")


if __name__ == "__main__":
    main()