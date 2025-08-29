n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {} \no produto é {} \ne a divisão é {}'.format(s,m,d))
print('A divisão inteira é {} \ne o exponencial {}'. format(di,e))

numero = int(input('Digite um valor: '))
ant = numero - 1
suc = numero + 1
print('o número {} tem como sucessor {} e antecessor {} são: '.format(numero,suc,ant))

valor = int(input('Escolha um valor: '))
dobro = valor * 2
triplo = valor * 3
raiz = valor ** (1/2)
print('O número {} tem como dobro {} \ntriplo {} \ne sua raiz quadrada é {}'.format(valor,dobro,triplo,raiz))

nota1 = int(input('Digite o valor da nota: '))
nota2 = int(input('Digite o valor de outra nota: '))
media = (nota1 + nota2)/2
total = 50
ap = (media > total)
rp = (media < total)
print('A nota do aluno é igual {}'.format(media))
print('Escreva aprovado se {} for maior que {} e reprovado se {} menor que {}'.format(ap,total,rp,total))

n3 = int(input('Digite um valor: '))

t1 = n3 * 1 
t2 = n3 * 2
t3 = n3 * 3
t4 = n3 * 4
t5 = n3 * 5
t6 = n3 * 6
t7 = n3 * 7 
t8 = n3 * 8
t9 = n3 * 9
t10 = n3 * 10 

print(f'{n3} x 1 =',t1)
print(f'{n3} x 2 =',t2)
print(f'{n3} x 3 =',t3)
print(f'{n3} x 4 =',t4)
print(f'{n3} x 5 =',t5)
print(f'{n3} x 6 =',t6)
print(f'{n3} x 7 =',t7)
print(f'{n3} x 8 =',t8)
print(f'{n3} x 9 =',t9)
print(f'{n3} x 10 =',t10)

m = int(input('digite um valor: '))
cen = m * 100
mili = m * 1000
print('{} metros convertidos para centimetros da {}'.format(m,cen))
print('{} metros convertidos por milimetros da {}'.format(m,mili))
