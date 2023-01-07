def fatorial (x):

	if x == 0:
	
		return(1)

	else:

		f = 1

		while x > 0:

			f = f * x

			x = x - 1

		return(f)


# m!/((m-n)!n!)


print()

m = int(input("Entre com o valor de m: "))

n = int(input("Entre com o valor de n: "))


coeficiente = fatorial(m)/(fatorial(m - n)*fatorial(n))

print()

print("O coeficiente binomial é", coeficiente, ".")