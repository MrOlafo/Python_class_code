#Asing the prices for the 5 kind of products and set the variable total in 0
productA=1000
productB=500
productC=250
productD=100
productE=50
total=0
#With this try we are avoiding that the users use letters instead of numbers
try:
#The program starts runnig. The user should press 1 to continue or 0 to leave		
	start=input('Welcome. Press 1 to start or to leave 0 the system: ')
	start=(int(start))
#Verify that the user did not write down a invalid value for the program. Only 1 or 0 are valid.	
	while start!=1 and start!=0:
		start=input('Please, press 1 to start or to leave 0 the system: ')
		start=(int(start))
#If the variable start is equal to 1, the system starts the products sales		
	if start==1:
#While start is equal to 1, the system stays in the products sales		
		while start==1:
			product=input('What kind of product are the customer buying? Product a=1, Producto b=2, Producto c=3, Producto d=4, Product e=5: ')
			product=(int(product))
#Verify that the users write down a valid product. If not, the system will continue asking for a valid product kind			
			while product!=1 and product!=2 and product!=3 and product!=4 and product!=5:
				product=input('Please write down one of the available categories for the products. Product a=1, Producto b=2, Producto c=3, Producto d=4, Product e=5: ')
				product=(int(product))
#Begins the product sales, 1=Product A, 2=Product B, 3=Product C, 4=Product D, 5=Product E				
			if product==1:
				print('The A products price is $',productA,'. They have a 75%  discount. Final price: $',productA-(productA*0.75),'.  Write down the amount of them that the client wants: ')
				amount=input()
				amount=(int(amount))
				print('Total to pay for ',amount,'A products is $',amount*(productA-(productA*0.75)))
#Assigning to the current total value the amount for this sale				
				total=total+(amount*(productA-(productA*0.75)))
			else:
				if product==2:
					print('The B products price is $',productB,'. They have a 50%  discount. Final price: $',productB-(productB*0.50),'.  Write down the amount of them that the client wants: ')
					amount=input()
					amount=(int(amount))
					print('Total to pay for ',amount,' B products is $',amount*(productB-(productB*0.50)))
#Assigning to the current total value the amount for this sale					
					total=total+(amount*(productB-(productB*0.50)))
				else:
					if product==3:
						print('The C products price is $',productC,'. They have a 25%  discount. Final price: $',productC-(productC*0.25),'.  Write down the amount of them that the client wants: ')
						amount=input()
						amount=(int(amount))
						print('Total to pay for ',amount,' C products is $',amount*(productC-(productC*0.25)))
#Assigning to the current total value the amount for this sale						
						total=total+(amount*(productC-(productC*0.25)))
					else:
						if product==4:
							print('The D products price is $',productD,'. They have no discount. Final price: $',productD,'.  Write down the amount of them that the client wants: ')
							amount=input()
							amount=(int(amount))
							print('Total to pay for ',amount,' D products is $',amount*productD)
#Assigning to the current total value the amount for this sale							
							total=total+(amount*productD)
						else:
							print('The E products price is $',productE,'. They have no discount. Final price: $',productE,'.  Write down the amount of them that the client wants: ')
							amount=input()
							amount=(int(amount))
							print('Total to pay for ',amount,' E products is $',amount*productE)
#Assigning to the current total value the amount for this sale							
							total=total+(amount*productE)
			print('By now the total to pay is: $',total)
#The system ask the user to continue with the sales or leave the program					
			start=input('Press 1 to continue or  press 0  to end the sale: ')
			start=(int(start))
#Verify that the user did not write down a invalid value for the program. Only 1 or 0 are valid.			
			while start!=1 and start!=0:
				start=input('Please, press 1 to continue or to leave 0 the end the sale: ')
				start=(int(start))
	print('The total to pay is: $',total)
	print('Thanks for using our system. Bye')
except:
	print('Use numbers, not letters')