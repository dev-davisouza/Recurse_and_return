import math
def hipotenusa(a,o):
    a = a**2
    o = o**2
    soma = a+o
    hipotenusa = math.sqrt(soma)
    return hipotenusa

def area(raio): #cálculo básico de raio usando a biblioteca math e usando valor de retorno, para que a função;
    a = math.pi * raio **2 #não retorne valor nulo.
    return a

#print(f'{area(360):.2f}')

#Aqui eu formato a exibição da função para limitar a qtde. de casas decimais;

def contagem_regressiva(n):
    if n <= 0: #Caso n (O nosso parâmetro) seja menor ou igual a 0...
        print('E morreu')#:D
    else:
        print(n)
        contagem_regressiva(n-1) #O ato de uma função chamar a si mesma é chamada de recursividade;
        #Então veja, neste caso em específico eu quero que uma contagem regressiva e instantânea seja exibida
        #Na tela.

        # Então sempre que a primeira condição for falsa, a função se chamará novamente com base nos argumentos que eu
        #passo para o parâmetro, menos 1;

#contagem_regressiva(10)

def print_n(a,n): #Para entender o contexto,'a' significa algo, neste caso, algo a ser exibido,
    if n <= 0:    #e 'n' o número de vezes que 'a' deve ser exebido na tela;
        return    #Caso 'n' seja negativo ou zero, ele retorna uma valor nulo ('None', em python)
    print(a)      #o que significa que nada será exibido.
    print_n(a,n-1)

def valor_absoluto(x):
    if x < 0:
        return -x
    if x > 0:
        return x

def is_divisible(x,y):
    if x % y == 0:
        return True
    else:
        return False

#para ser mais conciso...
def is_divisible2(x,y):
    return x % y == 0

def fatorial(n):
    if not isinstance(n,int):
        print('Fatorial só pode ser definido por inteiros')
        return None
    elif n < 0:
        print('Fatorial só poder ser definido por inteiros positivos')
        return None
    elif n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))