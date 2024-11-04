rent=int(input("enter your hostel/flat rent ="))

food=int(input("enter the amount of food order ="))

electricity_spend=int(input("enter the electricity spent ="))

charge_per_unit=int(input("enter the charge per unit ="))


persons=int(input("enter the number of person living in room/flat ="))


total_bill = electricity_spend*charge_per_unit
output = (food + rent + total_bill) // persons


print("each person will pay = " , output )