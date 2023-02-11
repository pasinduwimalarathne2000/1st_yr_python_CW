# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1868270 
 
# Date: 07/12/2021

#===========Progression outcomes and validation=======================
count=0
count1=0
Progress=0
Trailer=0
Retriever=0
Exclude=0
while True:
    
    try:
        user_input1 = int(input('Please enter your credits at pass: '))
        
        if user_input1 not in range(0,121,20):
            print('out of range')             #checking out of range
            
            continue
        
    except ValueError:
        print('Integer required')
        continue

    
    try:
        user_input2 = int(input('Please enter your credit at defer: '))
        if user_input2 not in range(0,121,20):
            print('out of range')
            continue
       
            
    except ValueError:
        print('Integer required')
        continue

    try:
        user_input3 = int(input('Please enter your credit at fail : ' ))
        if user_input3 not in range(0,121,20):
            print('out of range')
            
            continue
        
            
    except ValueError:
        print('Integer required')
        continue
    import os
    if os.path.exists('My List File.txt'):
        file=open("My List File.txt","r")
        lines=file.readlines()

    total= user_input1 + user_input2 + user_input3
    if total !=120:
        print('Total incorrect')
        continue   
    #Check progression outcome and print.
    if user_input1==120 and user_input2==0 and user_input3==0:
         print('Progress')
         count+=1
         Progress+=1
         count1+=1
    
    elif user_input1==100 and user_input2==0 and user_input3==20:
        print('Progress (module trailer) ')
        count+=1
        Trailer+=1
        count1+=1
    elif user_input1==100 and user_input2==20 and user_input3==0:
        print('Progress (module trailer) ') 
        count+=1
        Trailer+=1
        count1+=1
    elif user_input1<=80 and user_input2<=120 and user_input3<=60:
        print('Do not Progress – module retriever')
        count+=1
        Retriever+=1
        count1+=1
    elif user_input1<=40 and user_input2<=40 and user_input3<=120 :
        print('Exclude')
        count+=1
        Exclude+=1
        count1+=1
    print("\n")
    #check for user wants to add another set of data.
    text=input("Would you like to enter another set of data?,\n,Enter 'y' for yes or 'q' to quit and view results: ")
    if text=='y':
        print("\n")
        continue

    #================Vertical Histogram============
    elif text=='q':
        print('- '*35)
        print('Vertical Histogram')
        #Reference(https://stackoverflow.com)
        print(F"\n-----------------------------\nProgress {Progress}   |   Trailer {Trailer}   |   Retriever {Retriever}   |   Excluded {Exclude}\n")
        while (count1>0):
            if Progress>0:
                print("    * \t\t",end="")
                Progress -=1
            else:
                print("     \t\t",end="")

            if Trailer>0:
                print("     *\t\t",end="")
                Trailer -= 1
            else:
                print("     \t\t",end="")
            if Retriever>0:
                print("      *\t\t",end="")
                Retriever-= 1
            else:
                print("      \t\t",end="")
            if Exclude>0:
                print("       *")
                Exclude -= 1
            else:
                print(" ")
                count1=Progress+Trailer+Retriever+Exclude
        print(count,"outcomes in total")
        print("_ "*35)
        
    break


        
   
