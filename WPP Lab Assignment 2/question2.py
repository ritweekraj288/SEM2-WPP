#DICTIONARY TO STORE PRODUCT NAME AND PRICE IN FORM KEY VALUE PAIR

n=int(input("enter th number of products\t"))
product={}

#USER ENTRY TO MAKE DICTIONARY OF PRODUCTS

for i in range(n):
    name=input("enter the product name\t")
    price=float(input("enter the price\t"))
    product[name]=price

#PRINTING DICTIONARY
    
print("dictionary of product details is ",product)  

#USER ENTRY TO FIND PRICE FOR A PRODUCT

find=input("enter the product whose price you want to know\t")

#CHECKING AND PRINTING FINAL RESULT

if find in product.keys():
    print("price of",find,"=",product[find])
else:
    print("sorry! this product is currently not available")    