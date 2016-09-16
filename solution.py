m=0
v=0
c=0
for i in range(10):
	a=input("enter your cellphone number(10digits)")
	if a[:3]=="083":
		print("this is an mtn user")
		m=m+1
	elif a[:3]=="082":
		print("this is a vodacom user")
		v=v+1
	elif a[:3]=="076":
		print("this is a vodacom user")
		v=v+1
	elif a[:3]=="062":
		print("this is a cell c")
	elif a[:3]=="084":
		print("this is a cell c user")
		c=c+1
	else:
		print("error")
print(" there was",m,"amount of mtn users,",v,"amount of vodacom users and",c,"amount of cell c users")

