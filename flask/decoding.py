decoding(int1):
	lis1 = []
	int2 = 0
	lis2 = []
	for i in range(len(int1)):
    	if int1[i] == '0':
        	lis1.append(0)
    	elif int1[i] == '1':
        	lis1.append(1)
    	elif int1[i] == '2':
        	lis1.append(2)
    	elif int1[i] == '3':
        	lis1.append(3)
    	elif int1[i] == '4':
        	lis1.append(4)
    	elif int1[i] == '5':
        	lis1.append(5)
    	elif int1[i] == '6':
        	lis1.append(6)
    	elif int1[i] == '7':
        	lis1.append(7)
    	elif int1[i] == '8':
        	lis1.append(8)
    	elif int1[i] == '9':
        	lis1.append(9)
    	elif int1[i] == 'A':
        	lis1.append(10)
    	elif int1[i] == 'B':
        	lis1.append(11)
    	elif int1[i] == 'C':
        	lis1.append(12)
    	elif int1[i] == 'D':
        	lis1.append(13)
    	elif int1[i] == 'E':
        	lis1.append(14)
    	elif int1[i] == 'F':
        	lis1.append(15)
    	elif int1[i] == 'G':
        	lis1.append(16)

	lis1.reverse()


	for i in range(0, len(lis1)):
    	int2 = int2 + lis1[i]*(17**i)
	
	if int2 % 3 == 0:
		return True
	else:
		return False