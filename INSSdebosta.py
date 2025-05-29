sala= float(input("Qual seu salário?: "))

if sala<=1518:
    aliquota=0.075

if sala>1518.01 and sala<=2793.88:
    aliquota=0.09

if sala>2793.88 and sala <=4190.83:
    aliquota=0.12

if sala>4190.84 and sala <= 8157.41:
    aliquota=0.14

desconto=aliquota*sala
print ('seu salario desconto é de',desconto)
