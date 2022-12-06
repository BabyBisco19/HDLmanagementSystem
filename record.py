import booking as b

# RECORD FUNCTION
def Record():
	
	# checks if any record exists or not
	if b.phno!=[]:
		print("	 * HOTEL RECORD ***\n")
		print("| Name	 | Phone No. | Address	 | Check-In | Check-Out	 | Room Type	 | Price	 |")
		print("----------------------------------------------------------------------------------------------------------------------")
		
		for n in range(0,b.i):
			print("|",b.name[n],"\t |",b.phno[n],"\t|",b.add[n],"\t|",b.checkin[n],"\t|",b.checkout[n],"\t|",b.room[n],"\t|",b.price[n])
		
		print("----------------------------------------------------------------------------------------------------------------------")
	
	else:
		print("No Records Found")
	n = int(input("0-BACK\n ->"))
	if n == 0:
		import home
		home.Home()
		
	else:
		exit()