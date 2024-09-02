num = int(input("numero? "))
a, b = 0, 1
while a < num:
    a, b = b, a + b

if a == num:
    print('Está no fibonacci')
else:
    print('Não está no fibonacci')