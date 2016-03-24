#Grace O'Hair-Sherman Square root function C.P.2 Mods 4-5 
def main ():
    print "Enter a positive number (or a negative number to quit)."
    n=raw_input()
    n=float(n)
    if n<0:
        print "Quitting, good bye!"
    else:
        sqrt(n)
def sqrt (n):
        oldGuess = n/2.0
        counter = 0
        while counter<10:
            newGuess = ((n/oldGuess) + oldGuess) / 2.0
            oldGuess = newGuess
            counter = counter+1
        print "Square root is: "+str(newGuess)
        print "Difference is: "+str(newGuess - n**0.5)
main()

