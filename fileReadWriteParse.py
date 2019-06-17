def rec (lis):
	strr=''
	varList=[]
	next=''
	#print(lis)
	for i in range(0,len(lis)):
		word = lis[i]
		#print(str(i)+' Current Word = '+word)
		if '"' in word :
			if next in strr:
				strr+=word.replace('"','')		
		else:
			if (i+1) <len(lis):
				next = lis[i+1]
			else:
				next = lis[len(lis)-1]
			varList.append(word)
			if '"' in next:
				quoteindex = next.index('"')
				strr += (next[:quoteindex+1]+'{}'+next[quoteindex+1:]).replace('"','')
			else:
				strr+='{}'
			#print(' next Word = '+next)
		#print(strr)
	return '("'+strr+'", '+ str(varList).replace('[','').replace(']','').replace('\'','')+');'

def finishLine (indx, lines):		
	for line in lines[indx:]:		
		if';' in line:
			return line
		else:
			return line.strip().replace('\n','')+finishLine(indx+1,lines).strip()
		
fileName = 'BusinessTransTestBase.java'
lineStartWith = 'APMUtils.btmLogger.debug'
lineStartWith = 'APMUtils.btmLogger'
line = 	'APMUtils.btmLogger.debug(loggerDispStr + " isSourceTableFromTempCompID : " + isSourceTableFromTempCompID);'
#with open(fileName) as file :
with open('newFile.txt','w') as f1:
#		lines = file.readlines()
#		totlLines = len(lines)-1
#		for indx in range(0,totlLines):	
#			#if(indx<151):
#				line = lines[indx]
	if lineStartWith in line:
		if(line.endswith(';')):
			pass
		else:
			line= finishLine(indx,lines)			
		finalStr = line.split('(')[0]
		modStr = line.split('(')[1].replace(');','')
		print('Writing')
		f1.write(finalStr+rec(modStr.split('+')))
				
