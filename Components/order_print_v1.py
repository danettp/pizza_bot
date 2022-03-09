#list to store ordered pizzas
order_list = ["Margherita","Hawaiian", "Vegan", "BBQ Chicken Deluxe"]
#list to store pizza prices
order_cost = [8.50, 8.50, 8.50, 13.50]


count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1 