S=str(input("Dati elemente in sirul dat:"))
x=S.count('A')
print("a) Numarul de aparitii ale caracerului 'A' in sir:",x)
for i in S:
    sir2=S.replace('A','*')
print("b) Sirul obtinut prin substituirea caracterului 'A' prin caracterul '*' :",sir2)
for i in S:
    sir3=S.replace('B',' ')
print("c) Sirul obtinut prin radierea din sirul S a tuturor aparitiilor caracterului 'B':",sir3)
if 'MA' in S:
    y=S.count('MA')
    print("d) Numarul de aparitii a silabei 'MA' in sir:",y)
else:
    print("Nu exista silaba 'MA' in sir" )
if 'MA' in S:
    sir4=S.replace('MA','TA')
    print("e) Sirul obinut prin substituirea tuturor aparitiilor in sirul S a silabei 'MA' prin silaba 'TA':",sir4)
else:
    print("Nu exista silaba 'MA' in sir")
if 'TA' in S:
    sir5=S.replace('TO',' ')
    print("f) Sirul obtinut prin radierea din sirul S a tuturor aparitiilor silabei 'TO:",sir5)
else:
    print("Nu exista silaba 'TO' in sir")
print("g) Scrierea inversa a sirului:",S[::-1])