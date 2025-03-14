 ## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)

""" bruh = []
for row in data[1:]:
    start = row[0]
    sales = list(map(int, row[1:]))
    total = sum(sales)
    average = total / len(sales)  
    bruh.append((average, start)) 
bruh.sort(reverse=True)  
print(bruh) """

""" bruh = []
for row in data[1:]:
    start = row[0]
    sales = list(map(int, row[1:]))
    total = sum(sales)
    bruh.append((start, total))
print(bruh) """

""" def rowtotal():
    total_sales_sum = 0  # Sum of all sales
    total_sales_count = 0  # Total number of sales entries (all days)
    store_averages = {}
    good_stores = []
    bad_stores = []
    for row in data[1:]:
        start = row[0] # why row 0 duh its called the store name
        sales = list(map(int, row[1:]))  
        average = sum(sales) / len(sales) 
        store_averages[start] = average  
        sales = list(map(int, row[1:])) 
        total_sales_sum += sum(sales)  
        total_sales_count += len(sales) # u have to loop through all values

    
    overall_average = total_sales_sum / total_sales_count if total_sales_count > 0 else 0
    for key, value in store_averages.items(): #using this means key (name) value(num) in dict.items(pairs)
        if value * 0.8 >= overall_average:  
            good_stores.append((key, value))
        else:  
            bad_stores.append((key, value))

    # Print the results
    print(f"Good:", good_stores)
    print(f"Bad stores:", bad_stores)
    print(overall_average)

rowtotal() """
""" def rowtotal():
    averages = []  
    WEWANTYOU = []
    GETOUT = []
    for row in data[1:]:  

        sales = list(map(int, row[1:])) 
        row_total = sum(sales) 
        average = row_total / len(sales) 
        averages.append(average)  
        totalsum = sum(sales)
        totalsum = totalsum / len(row)
    for i in averages:
        if i * 0.8 >= totalsum:
            WEWANTYOU.append(i)
        else:
            GETOUT.append(i)
    print(f"i want {WEWANTYOU}, get out {GETOUT}")
rowtotal() """

""" def rowtotal():
    store_averages = {}
    
    for row in data[1:]:
        start = row[0]  # Store name
        sales = list(map(int, row[1:]))  # Convert to list to calculate average
        average = sum(sales) / len(sales) 
        store_averages[start] = average
    total_sales_sum = 0
    total_sales_sum += sum(sales)  # Sum of all sales
    total_sales_count = 0  # Total number of sales entries (all days)
    total_sales_count += len(sales)  # Count the number of sales entries (days)

    # Calculate the overall average sales across all stores and days
    overall_average = total_sales_sum / total_sales_count if total_sales_count > 0 else 0
    
    print(f"Total sales across all stores: {total_sales_sum}")
    print(f"Overall average sales across all stores: {overall_average}")
rowtotal() """


""" def rowtotal():
    for row in data[1:]: 
        start = row[0]  
        sales = list(map(int, row[1:])) 
        row_total = sum(sales) 
        average = row_total / len(sales)
        
        print(f"Store: {start}, Total sales: {row_total}, Average sales: {average}")

rowtotal() """
"""     
def rowtotal():
    averages = []  # List to store all averages
    
    for row in data[1:]:  # Loop through each row (excluding header)
        sales = list(map(int, row[1:]))  # Convert sales to integers
        row_total = sum(sales)  # Total sales for this store
        average = row_total / len(sales)  # Average sales for this store
        averages.append(average)  # Add individual average to the list
        totalsum = sum(sales)
        totalsum = totalsum / len(row)
    print(totalsum)
    print(averages)  # Print all averages at the end
rowtotal()
 """

""" def rowtotal():
    row_totals = {}
    averages = [] 
    store_names = []  
    
    for row in data[1:]: 
        start = row[0]  
        sales = list(map(int, row[1:]))  #

        row_totals[start] = sum(sales)  
        average = sum(sales) / len(sales)  
        averages.append(average)  
        store_names.append(start)  

    # Sort the averages and store names together
    sorted_averages = sorted(zip(averages, store_names), reverse=True) #ZIP PAIRS BOTH ELEEMNTS YAY FIRST STRAIGHT FORWARD ONE

    # Print the store names and their averages
    print(sorted_averages)

rowtotal()
 """


""" 
numbers = [1, 2, 3, 4, 5]
#make ur own function 
def double(x):
    return x * 2
# Use map() to double the numbers
doubled_numbers = map(double, numbers) #map = (function, what ur iterating)

print(list(doubled_numbers))
    

 """

""" #skipping loops

data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row (skip this)
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]

for row in data[1:2:]:  # Skip the first AND row 
    print(row) """

""" sales_data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]

def rowtotal():

    row_totals={}
    def skibidi():
        for i in sales_data:
            return i
        skibidi()
    sales = map(int, sales_data[1:])
    row_totals["store_name"] = sum(sales)  # Sum up sales for the store
    return row_totals
rowtotal()
 """

""" def calcRow(data):
    row_totals = {}

    for row in data[1:]:  # Skipping the first row
        sales = map(int, row[1:])  # Convert sales to numbers
        row_totals[row[0]] = sum(sales)  # Sum up sales for the store #aka u add 

    return row_totals

# Example Data
sales_data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]

totals = calcRow(sales_data)
print(totals)
 """
""" sales_data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]

row_totals = {}
for row in sales_data[1:]:
    sales = map(int, row[1:])
    row_totals[row[0]] = sum(sales)
print(row_totals)

#returns the sum of all integers iterated over any row except the first bc its the names of them how would u even add them???? ??? like?? ?? """

""" numbers = [2,4,6,8]
doubled = [num **2**2**2 for num in numbers]
print(doubled) """

#complex list, turn a list into another list'

""" sales_data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]

def calcRowLC(data):
    row_totals = {row[0]: sum([int(x) for x in row[1:]]) for row in data[1:]}
    return row_totals """

""" print(calcRowLC(sales_data))
 """

""" temperatures = ["Label", 32, 50, 77, 104]

def fahrenheit_to_celsius(f):
    return float((f - 32) * 5 / 9)

for f in temperatures:
    celsius = list(map(fahrenheit_to_celsius, temperatures[1:]))

print(celsius) """