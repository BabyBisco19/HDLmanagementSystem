import booking as b
import Roomsinfo as ri
import Restaurant as rest
import payment as pay
import record as rec

# Home Function
def Home():
	
	print("\t\t WELCOME TO HOTEL DE LUNA\n")
	print("\t\t\t 1 Booking\n")
	print("\t\t\t 2 Rooms Info\n")
	print("\t\t\t 3 Room Service(Menu Card)\n")
	print("\t\t\t 4 Payment\n")
	print("\t\t\t 5 Record\n")
	print("\t\t\t 0 Exit\n")

	ch=int(input("->"))
	
	if ch == 1:
		print(" ")
		b.Booking()

	elif ch == 2:
		print(" ")
		ri.Rooms_Info()

	elif ch == 3:
		print(" ")
		rest.restaurant()

	elif ch == 4:
		print(" ")
		pay.Payment()
	
	elif ch == 5:
		print(" ")
		rec.Record()
	
	else:
		exit()

Home()