class operaciones:
    def suma(a, b):
        print(f"el resultado de tu suma es {a + b}")
    def resta(a, b):
        print(f"el resultado de tu resta es {a - b}")
    def multiplicacion(a,b):
        print(f"el resultado de tu multiplicacion es {a * b}")

    def division(a,b):
        print(f"el resultado de tu division es {a / b}")

try:
    a = int(input("ingresar el primer numero "))

    b = int(input("ingresar el segundo numero "))
    print(f" 1.- suma \n 2.-resta \n 3.-multiplicacion \n 4.- division")
    optionns = int(input("ingresa que funcion quieres escoger "))

    match optionns:
        case 1:
            operaciones.suma(a, b)
        case 2:
            operaciones.resta(a, b)
        case 3:
            operaciones.multiplicacion(a, b)
        case 4:
            operaciones.division(a, b)
        case _:
            print("ingresa una opcion valida")            
except Exception:
    print("ha un error: {error}")
