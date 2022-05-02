 #“Friday Project: Printing Receipts.”

#created a product and price for the three items
from  email import message

# created products and prices
product1,price1 = "coffee", 1.5
product2, price2 = "computer", 5
product3, price3 = "moninter", 200

#  created the comapny and adress
company_name ="Amd , inc"
company_address ="283 Franklin, St"
company_city ="Boston,Ma"

# declare for end shopping
message = "Thank for shopping today"

# create top border
print("*" * 50)

#printing company and address firt  using format
print("\t\t {}".format(company_name.title()) )
print("\t\t {}".format(company_address.title()))
print("\t\t {}".format(company_city.title()))

#created section border
print("=" * 50)

#print out of header for sections items
print("\tProduct name \tProduct price")

# created stamtement for for each product
print("\t{}\t\t\t${}".format(product1.title(),price1))
print("\t{}\t\t${}".format(product2.title(),price2))
print("\t{}\t\t${}".format(product3.title(),price3))

#print a line between section
print("=" * 50)

# print out of header for section total
print("\t\t\t\tTotal")

#  calculate total price and print out
total = price1 + price2 + price3
print("\t\t\t\t${}\n".format(total))



#  end message
print("\t{}\n".format(message))

print("*" * 50)



