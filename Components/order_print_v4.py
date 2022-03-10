#list to store ordered pizzas
order_list = ["Margherita","Hawaiian", "Vegan", "BBQ Chicken Deluxe"]
#list to store pizza prices
order_cost = [8.50, 8.50, 8.50, 13.50]

customer_details= {'name':'Dan','phone':'08102312','house':'45','street':'Harry','suburb':'Howick'}

def print_order():
    total_cost = sum(order_cost)
    print("Customer Details")
    print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1 
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")

print_order()