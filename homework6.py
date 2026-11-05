# Summer Time - Activity PLanner
temp = float(input("Enter the temperature in degree celsius: "))
print()

if temp >= 35:
   print("It'ss very hot! Stay indooors and drink lots of water.")
elif temp >= 28:
   print("It's warm. Go to the beach or swimming pool.")
elif temp >= 20:
   print("Nice weather! You can play outside or have a picnic.")
elif temp >= 10:
   print("It's a bit cool. Wear a light jacket if you go out.")
else:
   print("It's cold for summer. Stay warm indoors.")

day = input("Is it weekend? (yes/no): ")
if day == "yes":
   print("Since it's a weekend, ypu have more time for fun!")
else:
   print("It's a weekday, so don't forget your summer homework!")