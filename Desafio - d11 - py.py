codP1, nP1, vlrP1 = input().split()
codP1 = int(codP1)
nP1 = int(nP1)
vlrP1 = float(vlrP1)

codP2, nP2, vlrP2 = input().split()
codP2 = int(codP2)
nP2 = int(nP2)
vlrP2 = float(vlrP2)

total = nP1 * vlrP1 + nP2 * vlrP2

print(f'VALOR A PAGAR: R$ {total:.2f}')