""" ## This function opens the CSV for You!
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
print(data)  # Output the list



 """

numbers = [1, 2, 3, 4, 5]
#make ur own function 
def double(x):
    return x * 2
# Use map() to double the numbers
doubled_numbers = map(double, numbers) #map = (function, what ur iterating)

print(list(doubled_numbers))
    

