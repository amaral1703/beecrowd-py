#media 1
A= float(input())
B= float(input())
Media = float((A*3.5+B*7.5)/11)
print(f"MEDIA = {Media:.5f}")

#salario 1008
nf = int(input())
ht = int(input())
v_h = float(input())

print(f"NUMBER = {nf}\nSALARY = U$ {(ht*v_h):.2f}")

#salario com bonus 1009 
name = input()
sf = float(input())
v_h = float(input())

print(f"TOTAL = R$ {(sf+(v_h*0.15)):.2f}")

#media2 1006
A= float(input())
B= float(input())
C= float(input())
Media = float((A*2+B*3+C*5)/10)
print(f"MEDIA = {Media:.1f}")

#diferença 1007
A= int(input())
B= int(input())
C= int(input())
D= int(input())
print(f"DIFERENCA = {A*B-C*D}")

#Cálculo Simples 1010
A,B,C = input().split() 
A =int(A); B = int(B); C = float(C)
A2,B2,C2 = input().split() 
A2 =int(A2); B2 = int(B2); C2 = float(C2)
print(f"VALOR A PAGAR: R$ {B*C + B2*C2:.2f}")

#esfera 1011
R= float(input())
print(f"VOLUME = {(4.0/3.0)*3.14159*(R**3):.3f}")

#AREA 1012
A,B,C = input().split(); A= float(A); B= float(B);C= float(C); 
print(f"TRIANGULO: {(A*C)/2:.3f}\nCIRCULO: {3.14159*(C**2):.3f}\nTRAPEZIO: {((A+B)*C)/2:.3f}\nQUADRADO: {(B*B):.3f}\nRETANGULO: {(A*B):.3f}")

#o maior 1013
A,B,C = input().split(); A= int(A); B= int(B);C= int(C);
maiorAB= (A+B+(abs(A-B)))/2
maiorABC= (maiorAB+C+(abs(maiorAB-C)))/2
print(f"{int(maiorABC)} eh o maior")

#consumo1014
X = int(input())
Y = float(input())
print(f"{X/Y:.3f} km/l")

#Distância Entre Dois Pontos 1015
X1, Y1= input().split() 
X1 =float(X1); Y1 = float(Y1); 
X2,Y2 = input().split() 
X2 =float(X2); Y2 = float(Y2); 
print(round(((X2-X1)**2+(Y2-Y1)**2)**(1/2), 4))

#distancia 1016
X= int(input())
print(f"{X*2} minutos")

#Gasto de Combustível 1017
X= int(input())
Z= int(input())
print(f"{(X*Z)/12:.3f}")

#cedulas 1018
N= int(input())

print(f"{N}\n{N//100} nota(s) de R$ 100,00"); N = N%100
print(f"{N//50} nota(s) de R$ 50,00"); N = N%50
print(f"{N//20} nota(s) de R$ 20,00"); N = N%20
print(f"{N//10} nota(s) de R$ 10,00"); N = N%10
print(f"{N//5} nota(s) de R$ 5,00"); N = N%5
print(f"{N//2} nota(s) de R$ 2,00"); N = N%2
print(f"{N} nota(s) de R$ 1,00"); 


#Conversão de Tempo 1019 
N = int(input())

print(f"{N//3600}:{(N%3600)//60}:{N%60}")

##Idade em Dias 1020
N = int(input())
print(f"{N//365} ano (s)"); N= N%365
print(f"{N//30} mes (es)"); N= N%30
print(f"{N} dia (s)")

#notas e moedas1021
N= float(input())
N = N *100
#colocar os numeros depois da virgula como se fosem inteiros
print(f"NOTAS:\n{N//10000:.0f} nota(s) de R$ 100.00"); N = N%10000
print(f"{N//5000:.0f} nota(s) de R$ 50.00"); N = N%5000
print(f"{N//2000:.0f} nota(s) de R$ 20.00"); N = N%2000
print(f"{N//1000:.0f} nota(s) de R$ 10.00"); N = N%1000
print(f"{N//500:.0f} nota(s) de R$ 5.00"); N = N%500
print(f"{N//200:.0f} nota(s) de R$ 2.00"); N = N%200
print(f"MOEDAS:\n{N//100:.0f} moeda(s) de R$ 1.00"); N = N%100
print(f"{N//50:.0f} moeda(s) de R$ 0.50"); N = N%50
print(f"{N//25:.0f} moeda(s) de R$ 0.25"); N = N%25
print(f"{N//10:.0f} moeda(s) de R$ 0.10"); N = N%10
print(f"{N//5:.0f} moeda(s) de R$ 0.05"); N = N%5
print(f"{N:.0f} moeda(s) de R$ 0.01")

#teste de selecao 1 1035
A,B,C,D= input().split(); A= int(A); B= int(B);C= int(C); D= int(D)

if((B>C) and (D>A) and ((C+D)>(A+B)) and (C>=0 and D>=0) and (A%2 ==0)):
    
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

#formula de bhaskara 1036
A,B,C= input().split(); A =float(A); B = float(B); C = float(C)

DELTA = (B**2)-(4*A*C)

if ((DELTA<0) or (A==0.0)):
    print("Impossivel calcular")
else:
    print(f"R1 = {((-B+(DELTA**(1/2)))/(2*A)):.5f}")
    print(f"R2 = {((-B-(DELTA**(1/2)))/(2*A)):.5f}")

#intervalo 1037
X= float(input())

if (X>100 or X<0):
    print("Fora de intervalo")
elif (X>75):
    print("Intervalo (75,100]")
elif (X>50):
    print("Intervalo (50,75]")
elif (X>25):
    print("Intervalo (25,50]")
else:
    print("Intervalo [0,25]")

#mês 1052
meses =["January","February","March","April","May","June","July", "August","September","October", "November", "December"]
A = int(input())
print(meses[A-1])

