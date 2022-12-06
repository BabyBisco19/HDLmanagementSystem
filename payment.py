
import booking as b

# PAYMENT FUNCTION			
def Payment():
	
	ph=str(input("Phone Number: "))
	i=b.i
	f=0
	
	for n in range(0,i):
		if ph==b.phno[n] :
			
			# checks if payment is
			# not already done
			if b.p[n]==0:
				f=1
				print(" Payment")
				print(" --------------------------------")
				print(" MODE OF PAYMENT")
				
				print(" 1- Credit/Debit Card")
				print(" 2- Paytm/PhonePe")
				print(" 3- Using UPI")
				print(" 4- Cash")
				x=int(input("-> "))
				print("\n Amount: ",(b.price[n]*b.day[n])+b.rc[n])
				print("\n		 Pay For AnCasa")
				print(" (y/n)")
				ch=str(input("->"))
				
				if ch=='y' or ch=='Y':
					print("\n\n --------------------------------")
					print("		 Hotel AnCasa")
					print(" --------------------------------")
					print("			 Bill")
					print(" --------------------------------")
					print(" Name: ",b.name[n],"\t\n Phone No.: ",b.phno[n],"\t\n Address: ",b.add[n],"\t")
					print("\n Check-In: ",b.checkin[n],"\t\n Check-Out: ",b.checkout[n],"\t")
					print("\n Room Type: ",b.room[n],"\t\n Room Charges: ",b.price[n]*b.day[n],"\t")
					print(" Restaurant Charges: \t",b.rc[n])
					print(" --------------------------------")
					print("\n Total Amount: ",(b.price[n]*b.day[n])+b.rc[n],"\t")
					print(" --------------------------------")
					print("		 Thank You")
					print("		 Visit Again 🙂")
					print(" --------------------------------\n")
					b.p.pop(n)
					b.p.insert(n,1)
					
					# pops room no. and customer id from list and
					# later assigns zero at same position
					b.roomno.pop(n)
					b.custid.pop(n)
					b.roomno.insert(n,0)
					b.custid.insert(n,0)
					
			else:
				
				for j in range(n+1,i):
					if ph==b.phno[j] :
						if b.p[j]==0:
							pass
						
						else:
							f=1
							print("\n\tPayment has been Made :)\n\n")
	if f==0:	
		print("Invalid Customer Id")
		
	n = int(input("0-BACK\n ->"))
	if n == 0:
		import home
		home.Home()
	else:
		exit()