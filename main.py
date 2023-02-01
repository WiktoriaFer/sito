N = 30
sito = [True for x in range(N+1)]
sito[0]=False
sito[1]=False
for i in range(2, N+1):
    if sito[i]:
        j = i*i
        while j<=N+1:
            sito[j]=False
            j += i
print(sito)

