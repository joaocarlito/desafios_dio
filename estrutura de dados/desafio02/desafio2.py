T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    numero_garrafas = (N % K) + (N / K)
    print(int(numero_garrafas))
    numero_garrafas = 0