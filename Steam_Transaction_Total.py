file = open("C:\steamtransactions.txt")
total = 0;
for line in file:
	if line.find('$') != -1:
		line = line[line.find('$')+1:]
		line = line[:line.find('P')]
		print line
		line = line.replace('.', '')
		total = total + float(line)
total = total / 100
print "Total = $" + str(total) 