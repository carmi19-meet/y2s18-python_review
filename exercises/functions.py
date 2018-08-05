# Write your solution for 1.4 here!

def is_prime(x):
	prime = True
	i = x-1
	while i>1:
		if x%i==0:
			prime=False
		i-=1
	return (prime)
##print(is_prime(5191))

def b_prime():
	i=5
	b=0
	if is_prime(i):
		b=i
	while b<1000000:
		i+=1
	return (b)
b_prime()