import csv
import sys
team_list = []
f = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        team_list.append(row)
finally:
    f.close()
team_list.pop(0)
target = open("results.txt", 'w')
quote = str('"')
for i in range(0,len(team_list)):
	line1 = quote+str(team_list[i][0])+'" => ["'+str(team_list[i][0])+'" , "'+str(team_list[i][2])+'" , "'+str(team_list[i][3])+'" , "'+str(team_list[i][3]+" "+team_list[i][2])+'" ],\n'
	target.write(line1)
print "closing file"
target.close()
#print team_list

