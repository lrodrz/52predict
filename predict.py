import csv
import numpy as np


# counting based on the high low system
def HiLo():
    #open file with all of the cards
    card_file = open('cards.csv','r')
    csv_read = csv.reader(card_file)
    count = 0

    print('\n','-'*20,'\n','Beginning Count: ',count,'\n','-'*20,'\n')

    
    
    lIst_fi_hilo = []
    for list in csv_read:
        for card in list:
            if card == 'ace':
                count = count - 1
                print('card:   ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count)
            elif card == 'queen':
                count = count - 1
                print('card: ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count)
            elif card == 'king':
                count = count - 1
                print('card:  ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count)
            elif card == 'jack':
                count = count - 1
                print('card:  ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count)
            elif card == '2':
                count = count + 1
                print('card:     ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count) 
            elif card == '3':
                count = count + 1
                print('card:     ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count)
            elif card == '4':
                count = count + 1
                print('card:     ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count) 
            elif card == '5':
                count = count + 1
                print('card:     ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count) 
            elif card == '6':
                count = count + 1
                print('card:     ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count)
            elif card == '7':
                count = count + 0
                print('card:     ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count)
            elif card == '8':
                count = count + 0
                print('card:     ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count)
            elif card == '9':
                count = count + 0
                print('card:     ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count)
            elif card == '10':
                count = count + 0
                print('card:    ',card,' | count: ' ,count)
                lIst_fi_hilo.append(count)
            else:
                print('error in card count')
        
    print('\n','-'*20,'\n','Final Count: ',count,'\n','-'*20,'\n')
       
    with open('count.csv','w') as count_fi:
        writer = csv.writer(count_fi)
        writer.writerow(lIst_fi_hilo)


    card_file.close()
    count_fi.close()
    

def CardRandomizer():
    cards = ['ace','king','queen','jack','10','9','8','7','6','5','4','3','2']
    is_this_your_card = np.random.choice(cards,size=1000)
    with open('cards.csv','w') as fi_gen_counts:
        writer = csv.writer(fi_gen_counts)
        writer.writerow(is_this_your_card)
        

    

    