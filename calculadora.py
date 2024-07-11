def suma():
    res = num1 + num2
    print("el resultado de la operacion es: ", res) 

def resta():
    res =num1 - num2
    print("el resultado de la operacion es: ", res) 

def multiplicacion():
    res =num1 * num2
    print("el resultado de la operacion es: ", res) 

def division():
    res =num1 / num2
    print("el resultado de la operacion es: ", res) 
while True: 
    num1 =  int(input("Digite un numero: "))
    ope = str(input("digite el signo de la operacion que desea realizar: "))
    num2 = int(input("Digite el segundo numero: "))
    if ope == "+":
        suma()
    elif  ope == "-":
        resta()
    elif ope == "*":
        multiplicacion()
    elif ope == "/":
        division()
    se = str(input("Desea terminar?"))
    if se == "S":
        print("Gracias por usar")
        break       
    
    
