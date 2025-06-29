t=int(input())

for _ in range(t):
	n=int(input())
	tab = list(map(int,input().split()))

	if n==1:
		print(1)
	else:
		left = 0
		right = 1
		compteur = 1

		while right < n:
			if tab[right] - tab[left] >= 2:
				compteur+=1
				left=right
				right+=1
			else:
				right+=1
		print(compteur)

