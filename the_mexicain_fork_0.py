from input_number_between_0 import input_number_between
from random import randrange

ZERO = 0

def play(start_sum):
    print "At any time, bet 0 to quit."
    capital = start_sum
    
    
    while capital != ZERO:
        print "You have %s." % capital
        d1 = randrange(6) + 1
        d2 = randrange(6) + 1
        d_bet = randrange(6) + 1
        if d1 > d2:
            aux = d1
            d1 = d2
            d2 = aux
        bet = "Your bet that the next draw is between %s and %s? " % (d1, d2)    
        amount = (input_number_between(bet, ZERO, capital))
        if amount == ZERO:
            return "You quit with %s." % capital
        print "I draw %s." % d_bet
        if d1 <= d_bet <= d2:
            capital += amount               
        else:
            capital -= amount        
    return "You lose all your money."  

play(100) 
