def fatorial (x):

	f = 1

	while x > 1:

		f = f * x

		x = x - 1

	return f


# m!/((m-n)!n!)


print()

m = int(input("Entre com o valor de m: "))

n = int(input("Entre com o valor de n: "))


coeficiente = fatorial(m)/(fatorial(m - n)*fatorial(n))


print()


if m < n or m < 0 or n < 0:

	print("Não existe fatorial de número negativo.")

else:

	print("O coeficiente binomial é", coeficiente, ".")
