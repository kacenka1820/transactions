import csv

transactions = []
total_transactions = 0
start_with_one = 0

with open('transactions.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) 
    for row in reader:
        transactions.append(row)
        total_transactions += 1
        
        if row [0].startswith('1'):
            start_with_one += 1
        

percentage = (start_with_one / total_transactions) * 100

print(f"Celkový počet transakcí: {total_transactions}")
print(f"Počet transakcí, které začínají hodnotou 1: {start_with_one}")
print(f"Procento těchto transakcí vzhledem k celkovému počtu transakcí: {percentage}%")
