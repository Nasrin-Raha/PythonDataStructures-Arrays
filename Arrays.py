/*

Arrays Exercise
1.Let us say your expense for every month are listed below,

January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list

*/

//My Solution
monthly_expenses  = [2200, 2350, 2600, 2130, 2190]

january_expenses = monthly_expenses[0]
february_expenses = monthly_expenses[1]
march_expenses = monthly_expenses[2]
april_expenses = monthly_expenses[3]
may_expenses = monthly_expenses[4]

extra_spent_in_february  = january_expenses - february_expenses
print("Extra dollars spent in February compared to January:" , extra_spent_in_february )

total_expenses_first_qurter= january_expenses + february_expenses + march_expenses
print("Total expense in first quarter (first three months) of the year:", total_expenses_first_qurter)

for index, expense in enumerate(monthly_expenses):
    if expense == 2000:
        print("You spent exactly $2000 in the month of", index + 1)
        break
else:
    print("You did not spend exactly $2000 in any month.")

monthly_expenses.append(1980)
print("Monthly expenses including June:", monthly_expenses)
                       
refund_april = 200
april_index = 3
monthly_expenses[april_index] -= refund_april
print("Updated monthly expenses after the refund in April:", monthly_expenses)
    

