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

def rowtotal():
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