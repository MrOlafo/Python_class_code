pa=750
pb=1500
pc=500
pd=250
p=0
Total=0
try:
	Start=input('Welcome to the store. If you want to start shopping press 1, else, press 0 to leave: ')
	Start=(int(Start))
	if Start/1 == Start:
		while Start!=1 and Start!=0:
			Start=input('Please press 1 to start shopping or 0 to leave: ')
			Start=(int(Start))
		if Start==1:
			while Start==1:
				p=input('Choose the product you want to buy: 1=a, 2=b, 3=c o 4=d: ')
				p=(int(p))
				if p/1 == p:
					if p==1 or p==2 or p==3 or p==4:
						if p==1:
							Amount=input('Write down the amount you want to buy: ')
							Amount=(int(Amount))
							print('Regular price: ',pa,'. Product have a 75% Of. Total price for ',Amount,' is: ',Amount*(pa-(pa*0.75)))
							Total=Total+(Amount*(pa-(pa*0.75)))
						else:
							if p==2:
								Amount=input('Write down the amount you want to buy: ')
								Amount=(int(Amount))
								print('Regular price: ',pb,'. Product have a 25% Of. Total price for ',Amount,' is: ',Amount*(pb-(pb*0.25)))
								Total=Total+(Amount*(pb-(pb*0.25)))	
							else:
								if p==3:
									Amount=input('Write down the amount you want to buy: ')
									Amount=(int(Amount))
									print('Regular price: ',pc,'. Product have no discount. Total price for ',Amount,' is: ',Amount*pc)
									Total=Total+(Amount*pc)
								else:
									if p==4:
										Amount=input('Write down the amount you want to buy: ')
										Amount=(int(Amount))
										print('Regular price: ',pd,'. Product have no discount. Total price for ',Amount,' is: ',Amount*pd)
										Total=Total+(Amount*pd)
					else:
						print('Please write down a valid product')
				else:
					print('Please write down a valid product')
				print('Total to pay: ',Total)
				Start=input('Continue shopping? 1=Yes, 0=No: ')
				Start=(int(Start))
		print('Total to pay: ',Total,'. Thanks for shopping')	
	else:
		print('Please start again the system and write down a numeric value')
except:
	print("Use numbers, not letters")