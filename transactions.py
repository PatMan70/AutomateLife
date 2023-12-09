import csv

# Save a CSV file of your transactions in the same folder as this project and put the name below
FILE_NAME = ''

def finance_manager(file_name):
    total_sum = 0 
    transactions = []

    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

        for row in csv_reader:
            # Extract relevant information from the row
            name = row[4]
            amount = float(row[7])
            date = row[1]

            # Create a tuple representing the transaction and add it to the list
            transaction = (date, name, amount)
            transactions.append(transaction)

            # Update the total sum
            total_sum += amount

    # Print the total sum of transactions for the month
    print(f"The sum of your transactions this month is {total_sum}")
    print('')

    return transactions

# Example usage
print(finance_manager(FILE_NAME))
