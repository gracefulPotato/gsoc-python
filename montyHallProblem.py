#Grace O'Hair-Sherman Monty Hall Problem C.P.2 Mods 4-5
import random
won=0
times=0
while times<1001:
    guess=(random.randint(1,3))
    car=(random.randint(1,3))
    if guess==car:
        won=won+1
    times=times+1
won1=0
times1=0
while times1<1001:
    guess1=(random.randint(1,3))
    car1=(random.randint(1,3))
    if guess1!=car1:
        won1=won1+1
    times1=times1+1
percent=won/10.0
percent1=won1/10.0
print "Unchanged: "+str(percent)+"%"
print "Changed: "+str(percent1)+"%"
