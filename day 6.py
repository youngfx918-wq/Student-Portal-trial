print ("Atm Balance Checker")
name = input ("name:")
pin = int(input ("pin:"))
if pin == 1244:
	print ("welcome" , name,)
	balance = int(input ("balance"))
	with_amt = int(input("withdraw_amt"))
	if with_amt <= balance:
		print ("withdrawal approved")
		choice = balance - with_amt
		input ("would you like to continue? (yes/no): ")
		if choice  == "yes":
			print("unto the next")	
		else:
			print ("thanks for banking with us")
	else:
			print("insufficient balance")
else:
	print ("incorrect Pin")
	print ("Access Denied")
	