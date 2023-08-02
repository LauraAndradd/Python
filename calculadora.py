def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero não é permitida."

def calculator():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

    while True:
        try:
            choice = int(input("Digite o número da operação desejada: "))

            if choice == 0:
                break

            if choice not in range(1, 5):
                print("Opção inválida. Tente novamente.")
                continue

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if choice == 1:
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == 2:
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == 3:
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == 4:
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")

if __name__ == "__main__":
    calculator()
