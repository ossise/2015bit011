def table(n):
	for i in range(1,11):
		print(""+str(n)+"*"+str(i)+"="+str(n*i))
def fact(n):
	x = 1
	for i in range(1,n+1):
		x*i;
	print("Factorial is:"+str(x))
if __name__ == '__main__':
	print("Enter Number:")
	n = int(input())
	print("Table of "+str(n)+":")
	table(n)
	fact(n)
