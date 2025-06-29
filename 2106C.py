t=int(input())

for _ in range(t):
	inputs= list(map(int,input().split()))
	n,k = inputs[0], inputs[1]
	a= list(map(int,input().split()))
	b = list(map(int,input().split()))

	res=-1
	d={}
	for i in range(n):
		if b[i] != -1 :
			if "check" not in d:
				d["check"]=a[i]+b[i]

			elif d["check"] != a[i]+b[i]:
				res = 0

	if res==-1:
		if "check" in d:
			x=d["check"]
			i = 0
			while i < n and (x>=a[i]>=x-k) :
				i+=1
			if i==n:
				res = 1
			else:
				res = 0
		else:
			res = max(0, min(a)+k - max(a)+1)



	print(res)
