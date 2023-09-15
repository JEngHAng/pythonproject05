def inputdata ():
    user_pass = int(input("ป้อนรหัสพนักงาน : "))
    user_name = input("ป้อนชื่อพนักงาน : ")
    user_money = int(input("ป้อนเงินเดือนพนักงาน : "))
    return user_money , user_name , user_pass
def addtax_money (user_money):
    Additional_taxes = user_money * 0.07
    return Additional_taxes
def sso_money (user_money):
    have_user = user_money - 500 
    return have_user
def vat_user (have_user , Additional_taxes):
    use_money = have_user - Additional_taxes
    return use_money
def output_vat (Additional_taxes ,vat_user):
    print (f"ภาษีเป็นเงิน : {Additional_taxes:.2f} บาท")
    print (f"เงินเดือนสุทธิเป็นเงิน : {vat_user:.2f} บาท")

print ("--------------------------------------------")
print ("--------------คำนวณเงินเดือนพนักงาน------------")
print ("--------------------------------------------")
user_money , user_name , user_pass = inputdata ()
print ("--------------------------------------------")
output_vat (addtax_money (user_money) ,vat_user (sso_money (user_money), addtax_money (user_money)))
print ("--------------------------------------------")
