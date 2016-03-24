#Grace O'Hair-Sherman
#Demo script testing out possible data structures for strace
#structured output filter
class Line:

        def __init__(self,call,arguments):
                self.syscall = call
                self.args = arguments

def main():
	callArr = []
	for i in range(0,3):
		myLine = Line("brk",i)
		callArr.append(myLine)
	
	printJSON(callArr)

def printJSON(arr):
	for i in arr:
		print("{\"syscall\":\""+i.syscall+"\"args\":\""+str(i.args)+"\"}");

main()
