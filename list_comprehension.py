i=int(input())				#input for X
j=int(input())				#input for Y
k=int(input())				#input for Z
n=int(input())				#input for N

new_list=[]			#default checking list

list_main=[]				#main list to display the output 

for i1 in range(0,i+1):			#values of i from 0 to X
	for j1 in range(0,j+1):		#values of j from 0 to Y
		for k1 in range(0,k+1):		#values of k from 0 to Z
			if i1+j1+k1!=n:				#checking condition whether the sum of i,j,k is not equal to n
				new_list=[i1,j1,k1]		#creating new list to insert in a new list 
				list_main.append(new_list)		#inserting list inside list 

print(list_main)			#displaying output
