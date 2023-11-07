nota = int(input('Digite a nota do aluno:'))
if nota >= 90:
    print('A - Excelente')
elif nota >= 80:
    print('B - Muito Bom')
elif nota >= 70:
    print('C - Bom')
elif nota >= 60:
    print('D - Regular')
else:
    print('F - Reprovado')