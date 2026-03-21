n = int(input())
print(n)
notas = [100,50,20,10,5,2,1]

for ni in notas:
    val = int(n / ni)
    n -= val * ni
    print(f"{val} nota(s) de R$ {ni},00")