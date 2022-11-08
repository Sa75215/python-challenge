import os
import csv
#Find the budget file
csvpath = os.path.join('Resources', 'budget_data.csv')

csvpath_write = os.path.join('analysis', 'code.txt' )
#save the file within variable csvreader in python
with open(csvpath_write, 'w') as Pybank_out:
    with open(csvpath, newline = '') as csv_file:
        csvreader = csv.reader(csv_file, delimiter = ',')
        print(csvreader)
        #Designate first row as header
        csv_header = next(csvreader)
        print(f' CSV Header: {csv_header}')
    
        #counts the number of rows which represent different months and stores as variable
        month_count = 0

        #empty table that will contain all the budget values
        budget_pl = []
    
        #variable that will hold the sum the budget values.
        net_pl = 0

        months = []

        for row in csvreader:
         #If we save the rows into a variable then print that variable, why do we get a None at the end?
            month_count +=1
            budget_pl.append(row[1])
            months.append(row[0])

        for values in budget_pl:
            net_pl += int(values)
            round(net_pl,)    
    
            #Why are we dividing by 85 instead of 86?
        budget_text = round(net_pl)
        pl_change = round((int(budget_pl[len(budget_pl)-1]) - int(budget_pl[0]))/int(len(budget_pl)-1),2)
    
        current_number = 0
        next_number = 0
        profit_change_tracker = []

        for p in budget_pl:
            next_number+=1
            if (next_number < len(budget_pl)):
                number_current = budget_pl[current_number]
                number_next = budget_pl[next_number]
                row_profit = int(number_next) - int(number_current)
                profit_change_tracker.append(row_profit)
                current_number +=1
        

        max_row_profit = round(max(profit_change_tracker),)
        min_row_profit = round(min(profit_change_tracker),)    
        max_profit_month = profit_change_tracker.index(max_row_profit)+1
        min_profit_month = profit_change_tracker.index(min_row_profit)+1
        max_month = months[max_profit_month]
        min_month = months[min_profit_month]

    print('--------------------------')
    print(f'Total Months: {month_count}')
    print(f'Total:  ${net_pl}')
    print(f'Average Change: ${pl_change}')
    print(f'Greatest Increase in Profits: {max_month} ${max_row_profit}')
    print(f'Greatest Decrease in Profits: {min_month} ${min_row_profit}')

    text_1 = f'Financial Analysis\n-----------------------------\nTotal Months: {month_count}'
    text_2 = f'\nTotal: ${budget_text}\nAverage Change ${pl_change}'
    text_3 = f'\nGreatest Increase in Profits: {max_month} (${max_row_profit})\nGreatest Decrease in Profits: {min_month} ${min_row_profit})'

    Pybank_out.write(text_1)
    Pybank_out.write(text_2)
    Pybank_out.write(text_3)
Pybank_out.close()