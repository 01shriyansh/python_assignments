#to find the numbers which are divisible of 7 and not a multiple of 5  between [2000,32000].

li=[]

for i in range(2000,3201):
	if(i%7==0):
		if(i%5!=0):
			li.append(i)

for i in li:
	print(i,end=",")


