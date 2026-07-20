#string formatting
line="Hey my name is {1} and i live in {0}"
country="India"
name="Sahil"
print(line.format(country,name))

#fstrings
name1="Kim"
country1="America"
print(f"Hey my name is {name1} and i live in {country1}")

price=100.232343423
print(f" {price:.3f}")# .f is used to print desired nummber of the decimal places