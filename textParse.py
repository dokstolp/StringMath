A = str(input('Gimme a Value: '))
B = str(input('Gimme another Value: '))

def addStr(a,b):
	if len(a)==1 and len(b)==1:
		return str(int(a)+int(b))
	return '0'

def multStr(a,b):
	if len(a)==1 and len(b)==1:
		return str(int(a)*int(b))
	return '0'

def formatStr(a,b):
	a = a[::-1]
	b = b[::-1]
	toSum = max(len(a),len(b))+1
	a = a+('0'*(toSum-len(a)))
	b = b+('0'*(toSum-len(b)))
	return a,b

def deformatStr(a):
	return a.rstrip('0')[::-1]

def addFullStr(a,b):
	a,b = formatStr(a,b)
	tail = ''
	head = '0'
	for i in range(0,len(a)):
		outStr = addStr(a[i],b[i])[::-1]
		digit = addStr(head,outStr[0])[::-1]
		if len(outStr)==2 or len(digit)==2:
			head = '1'
		else:
			head = '0'
		tail = tail+digit[0]
	return deformatStr(tail)

def multFullStr(a,b):
	a = a[::-1]
	b = b[::-1]
	l = []
	for i in range(0,len(a)):
		for j in range(0,len(b)):
			l.append(multStr(a[i],b[j])+('0'*(i+j)))
	outval = '0'
	for b in l:
		outval = addFullStr(outval,b)
	return outval			


print multFullStr(A,B)

