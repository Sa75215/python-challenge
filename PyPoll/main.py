import os
import csv


candidate_tracker = {}
c_list = []

tot_votes = 0
win_votes = 0


elect_csv = os.path.join('Resources', 'election_data.csv')
elect_csv_text = os.path.join('analysis', 'code.txt')

    # with open(elect_csv_text, 'w') as Pybank_out:
print(f'-----------------------\nElection Results\n-----------------------')

with open(elect_csv_text, 'w') as elect_out:
    with open(elect_csv, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        
        for row in csvreader:
            # Question - what is candidate_tracker[row]
            if row[2] not in c_list:
                candidate_tracker[row[2]] = 0
                # print(candidate_tracker[row[2]])
                c_list.append(row[2])
            candidate_tracker[row[2]]+=1
            tot_votes += 1
        print(f'Total Votes {tot_votes}\n-----------------------')
        
        for candidate in c_list:
            
            if win_votes < candidate_tracker[candidate]:
                win_votes = candidate_tracker[candidate]
                winner = candidate
        # print(winner)
                pct_of_votes = round(((candidate_tracker[candidate]/tot_votes)*100),2)
            print(f'{candidate} {str(pct_of_votes)}% ({str(candidate_tracker[candidate])})')
            
        print('-----------------------')
        print(f'Winner: {winner}')

    text1 = f'-----------------------\nElection Results\n-----------------------\n'
    text2 = f'Total Votes: {tot_votes}\n-----------------------\n'
    text3 = (f'{candidate} {str(pct_of_votes)}% ({str(candidate_tracker[candidate])})')
    elect_out.write(text1)
    elect_out.write(text2)
    #I can't get the output to the text file to read all the names. Can you explain how to code that?
    elect_out.write(text3)
elect_out.close()



