
i = 0

while i<5 :
	print(i)
	i = i + 1
    

# Modify the loop to print numbers up to and including 20
while i<=20:
	print(i)
	i = i + 1
# Add further logic so that a message is printed if the number is a multiple of 4
# Hint: we discused operators such as % and // in recent weeks
while i<=20:
	if i % 4 == 0:
		print(f"{i} is a multiple of 4")
	else:
		print(f"{i} is not a multiple of 4")
	i = i + 1