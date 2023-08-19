products = []
while True:
    selection = int(input("1. Add New Product\n"
                          "2. Print Product Details\n"
                          "3. Buy Product\n"
                          "4. Delete Product\n"
                          "5. Exit"))

    if selection == 1:
        product_number = input("Enter Product Number: ")
        product_name = input("Enter Product Name: ")
        product_price = input("Enter Product Price: ")
        product_qty = int(input("Enter Product Quantity: "))
        product = {
            "id": product_number,
            "name": product_name,
            "price": product_price,
            "qty": product_qty
        }
        products.append(product)
        print("Product Added Successfully.\n")

    elif selection == 2:
        product_number = input("Enter Product Number: ")
        for i in products:
            if i.get('id') == product_number:
                print(i, "\n")
                break
        else:
            print("Product not found.\n")

    elif selection == 3:
        product_number = input("Enter Product Number: ")
        product_qty = int(input("Enter Product Quantity: "))
        for i in products:
            if i.get('id') == product_number:
                if i.get('qty') >= product_qty:
                    i['qty'] = i['qty'] - product_qty
                    print("Purchase Successful, Remaining quantity:", i['qty'], "\n")
                else:
                    print("Insufficient quantity available.\n")
                break
        else:
            print("Product not found.\n")

    elif selection == 4:
        product_number = input("Enter Product Number: ")
        for i in products:
            if i.get('id') == product_number:
                products.remove(i)
                print("Product Deleted Successfully.\n")
                break
        else:
            print("Product not found.\n")

    elif selection == 5:
        exit()
    else:
        print("Invalid Input.\n")
