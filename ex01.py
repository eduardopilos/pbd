#Exercício 01
print("Digite o valor de A: ") 
A = int(input()) 
print("Digite o valor de B: ") 
B = int(input()) 
X = A+B 
print("X = ", X)

#Exercício 02
print("Digite os valores do primeiro plano: ")
p1 = input()
x1, y1 = float(p1.split()[0]), float(p1.split()[1]) 
print("Digite os valores do segundo plano: ")
p2 = input()
x2, y2 = float(p2.split()[0]), float(p2.split()[1]) 
print("A distância é: ",((x2-x1)**2 + (y2-y1)**2)**0.5)

#Exercício 03
print("Insira o valor a ser multiplicado pela tabuada: ")
X = int(input())
for i in range(1,11):
    print(i, "x", X, "=", i*X)

#Exercício 04
print("Quantos casos serão testados?")
p = int(input())
q = ""
for i in range (p):
    print("Insira os diamantes:"), 
    q += input().strip(".,") + " "
q = q.split()
cont = 0
for i in range(p):
    