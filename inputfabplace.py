import sys
sys.set_int_max_str_digits(0)
a=1
b=1
c=0
abcd=int(input("last no. :   "))
f=open("fabonacci1logs.txt","w+")
print("0\n1\n1")
for x in range(3,abcd+1):
	c=a+b
	a=b
	b=c
	f.writelines(f"{x}===={c} \n ")
	#debug
	print(str(x))
f.close()
fa=open("fab"+str(abcd)+".txt", "w+")
fa.writelines(f"{str(abcd)}==== {c}")
fa.close()
