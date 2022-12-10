
#Klaudene Aclan
# #Baby C. Bisco
#Jinky F. Gayeta
#BS IT 2103
class hotel(): 
     def Name(self):
         print("===========================================================")
         print("***************WELCOME TO HOTEL DE LUNA***************")
         print("===========================================================")
     def location(self): 
       print("Location: Bry. Pinili Sitio Iniwan Umiyak City") 
     def Safety(self):
         print("Safety: ")
         print("Access Control ")
         print("Vehicle Security")
         print("Key Management")
         print("Video Surveillance")
         print("Building Identification and Accessibility")
     def Floor(self):
       print("Floor: 5TH FLOOR")  
     def ContactInfo(self):
       print("Contact Information: 0912345678") 
     def Hotelemail(self):
       print("Hotel Email: HotelDeLuna@g.hotel.ph ") 
     def HotelAward(self):
         print("Hotel Award:") 
         print("Luxury Art Boutique Hotel in 2019")
         print("Luxury Design Boutique Hotel in 2019")
         print("Best Golf Hotel in 2020")
         print("Best Country Hotel in 2021")
         print("Luxury Concept Hotel in 2021")
     def Owner(self):
       print("Ms. Klaudene Aclan, Ms. Baby Bisco and Ms. Jinky Gayeta") 
    


obj_manage =hotel()

def success():
  print("DO YOU WANT TO CHECK IN!!!")
  answer = str(input("Enter yes or no:"))
  while 1:
    if answer == "yes" or answer == "Yes":
        print("SIGN IN BELOW!!!")
        print("===========================================================")
        print("")
        print("")
        import home as dl
        print(dl.Home())
        break
    elif answer == "no" or answer == "No":
          print(" You need to enter yes to continue.")
          answer = str(input("Do you want to continue and Checkin."))
          if answer == "yes":
                obj_manage.Name()
                obj_manage.location()
                obj_manage.Safety()
                obj_manage.Floor()
                obj_manage.ContactInfo()
                obj_manage.Hotelemail()
                obj_manage.HotelAward()
                obj_manage.Owner()
          print("DO YOU WANT TO CHECK IN!!!")
          answer = str(input("Enter yes or no:"))
          
    else:
        print("You may exit.")

for  luna in (obj_manage, ):
    luna.Name()
    luna.location()
    luna.Safety()
    luna.Floor()
    luna.ContactInfo()
    luna.Hotelemail()
    luna.HotelAward()
    luna.Owner()

success()
