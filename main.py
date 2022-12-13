username ="suresh"
password ='1234'

custmer_name =input("enter your name:")
custmer_password =str(input("enter your password"))
if custmer_name ==username and custmer_password ==password:
    print('''
    1. deposit
    2.withdraw
    3.ministatement
    4.exit
    ''')
    amount =50000
    option =int(input("select your option:"))
    if option ==1:
        deposite =int(input("enter youe amount:"))
        amount+=deposite
        print("total amount:",amount)
    elif option ==2:
        withdraw =int(input("enter amount:"))
        amount -=withdraw
        print("with draw amount:",amount)
    elif option ==3:
        print("=====STATE BANK OF INDIA=====")
        print("user name:",username)
        print("total amount",amount)
        print("thanks for visiting")
else:
    print("PLEASE ENTER CORRECT LOGIN PIN")

