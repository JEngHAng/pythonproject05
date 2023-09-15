#def order ( order1 ):
    #order1 = int(input("Input Order : "))
    #print (order1 + (order1 * 10 / 100))
#order1 = order
#order (order1)

def inputdata():
    product_name = input("Input Product Name : ")
    product_price = int(input("Input Pirce Product : "))
    return product_name , product_price

def cal_product_sale ( product_pirce ):
    product_sale = product_pirce + (product_pirce * 10 / 100)
    return product_sale

def output_cal_product(product_name , product_pirce , product_sale) :
    print (f"ชื่อสินค้า {product_name}")
    print (f"ราคาสินค้า (ต้นทุน) {product_pirce:.2f} บาท")
    print (f"ราคาขายสินค้า {product_sale:.2f} บาท")

print("-------------------------------------------------")
print("---------------** PRODUCT SALE **----------------")
print("-------------------------------------------------")
product_name , product_pirce = inputdata()
product_sale = cal_product_sale( product_pirce )
print("-------------------------------------------------")
output_cal_product( product_name , product_pirce , product_sale)
print("-------------------------------------------------")