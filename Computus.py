# Grace O'Hair-Sherman Computus C.P.1 Mods 4-5
print("Please type a year.")
year = raw_input()
y=int(year)
a=y%19
b=y/100
c=y%100
d=b/4
e=b%4
g=(8*b+13)/25
h=(19*a+b-d-g+15)%30
j=c/4
k=c%4
m=(a+11*h)/319
r=(2*e+2*j-k-h+m+32)%7
n=(h-m+r+90)/25
p=(h-m+r+n+19)%32
if n==3:
    month ="March"
else:
    month="April"
if y<2013:
    copula="was"
elif y>2013:
    copula="will be"
else:
    copula="is"
print("In "+year+", Easter Sunday "+copula+" on "+month+" "+str(p)+".")
