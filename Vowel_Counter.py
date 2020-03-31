def count():
	
	countA=0;
	countE=0;
	countI=0;
	countO=0;
	countU=0;
	
	list=['a','e','i','o','u']
	
	sentence = input("Please Enter a sentence : ")
	
	for i in sentence:
		if(i=='a' or i=='A'):
			countA=countA+1
			#sentence2 = input("Do you wish to enter another sentence?(Yes/No)")
			
			
		if(i=='e' or i=='E'):
			countE=countE+1
			
		
		if(i=='i' or i=='I'):
			countI=countI+1
			
		
		if(i=='o' or i=='O'):
			countO=countO+1
			
		
		if(i=='u' or i=='U'):
			countU=countU+1
			
	#Adding values to a dictionary.

	Vowelsdict={"a":countA,"e":countE,"i":countI,"o":countO,"u":countU}


	#Printing values from a dictionary.
	print(Vowelsdict)


			
	sentence2 = input("Do you wish to enter another sentence?(Yes/No)")
	if(sentence2=='Yes' or sentence2=='yes' or sentence2=='YES'):
		count()
	else:
		exit()

			
count()




