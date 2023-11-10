#TASK1: make a 2d array to store sales of 5 salespersons' sales for 12 months

Sales = [[0 for col in range(12)]for row in range(5)]

#TASK2: ask user to enter sales for each sales person for each month
#TASK3: calculate the average sales for each sales person and average sales of all salespersons

from random import randint

grandTotal = 0

for row in range(5):
    indTotal = 0
    for col in range(12):
        Sales[row][col] = randint(0,100)
        grandTotal += Sales[row][col]
        indTotal += Sales[row][col]
    indAvg = indTotal/12
    print()
    print(f"Average sales of salesperson {row+1}: ", indAvg)
grandAvg = grandTotal/60
print()
print("Average sales overall:", grandAvg)

#TASK4: find the highest and Lowest sales month for each sales person

for row in range(5):
    highMonth = 1
    lowMonth = 1
    highest = Sales[row][0]
    lowest = Sales[row][0]
    for col in range(12):
        if Sales[row][col] > highest:
            highMonth = col + 1
        elif Sales[row][col] < lowest:
            lowMonth = col + 1


    print()
    print(f"highest sales of salesperson {row+1} were in month {highMonth}")
    print()
    print(f"lowest sales for salesperson {row+1} were in month {lowMonth}")

#TASK5: make a 1d array bonus, that calculates bonus for each sales person based on the formulo
#total of 10% of (sales for the month * month number)

Bonus = [0 for row in range(5)]
for row in range(5):
    totalBonus = 0
    for col in range(12):
        totalBonus += Sales[row][col] * col * 10 /100
    Bonus[row] = totalBonus
print()
for row in range(5):
    print(f"Bonus for salesperson {row+1}: {Bonus[row]}")