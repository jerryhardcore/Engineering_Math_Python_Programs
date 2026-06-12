def bernoulli(number=""):
    global bernoulli_result
    bernoulli_value=""
    print "The bernoulli function only shows iterative visualization triangle(Akiyama-Tanigawa) for B(n) values"
    print "greater >2 and <17 for screen readability and educational aid."
    print "The program fails past B(36) due to overflow."
    if number=="":
        repeat=True
        count=2
        while repeat==True and count>0:
            try:
                x=input("enter number:")
            except:
                print "input error: input must be number:"
            else:
                if type(x) is int and x>=0:
                    repeat=False
                    bernoulli_value=x
                else:
                    print "input error: invalid number, number must be zero or positive integer:"
            count-=1
    else:
        if type(number) is int and number>=0:
            bernoulli_value=number
        else:
            print "error: invalid function parameter, number must be zero or positive integer"     
    bernoulli_result=None
    row_1_list=[]
    row_1_denom=[]
    bernoulli_print=[]
    if type(bernoulli_value)==int and bernoulli_value>2:
        if bernoulli_value>36:
            bernoulli_value=36
            print "you bernoulli parameter is too high and reduced to the 36 limit to prevent crashing"
        B=bernoulli_value
        bernoulli_value+=1
        for n in range(1,bernoulli_value+1):
            row_1_list.append(1)
            row_1_denom.append(n)
        if B<17:
            print '\n'
            print "first row of Bernoulli triangle for B(",B,")"
            print '\n'
            bernoulli_print.append(":")
            for i in range(bernoulli_value):
                bernoulli_print.append(row_1_list[i])
                bernoulli_print.append("/")
                bernoulli_print.append(row_1_denom[i])
                bernoulli_print.append(":")
            print bernoulli_print
            bernoulli_print=[]
            print '\n'
        for m in range(bernoulli_value-1,0,-1):
            for n in range(m):
                numer_1=row_1_list[n]*row_1_denom[n+1]
                numer_2=row_1_denom[n]*row_1_list[n+1]
                denom_1_2=row_1_denom[n]*row_1_denom[n+1]
                row_1_list[n]=(n+1)*(numer_1-numer_2)
                row_1_denom[n]=denom_1_2 
                for repeat in range(4):
                    if abs(row_1_list[n])>1 and row_1_denom[n]!=0:
                        highest_comm_fact=1
                        for i in range(2,400):
                            if i>row_1_list[n]/2 and row_1_list[n]>=4 and abs(row_1_list[n])<abs(row_1_denom[n]):
                                break
                            elif i>row_1_denom[n]/2 and row_1_denom[n]>=4 and abs(row_1_list[n])>abs(row_1_denom[n]):
                                break
                            if row_1_list[n]%i==0 and row_1_denom[n]%i==0:
                                highest_comm_fact=i
                        row_1_list[n],row_1_denom[n]=row_1_list[n]/highest_comm_fact,row_1_denom[n]/highest_comm_fact
                if len(str(row_1_list[n]))>20 or len(str(row_1_denom[n]))>20:
                    row_1_list[n],row_1_denom[n]=1,float(row_1_denom[n])/row_1_list[n]
            row_1_list.pop()
            row_1_denom.pop()      
            if B<17:
                print "row",abs(bernoulli_value+1-m),"of Bernoulli triangle for B(",B,")"
                print '\n'
                bernoulli_print.append(":")
                for i in range(m):
                    if row_1_list[i]!=0 and row_1_denom[i]!=0:
                        bernoulli_print.append(row_1_list[i])
                        bernoulli_print.append("/")
                        bernoulli_print.append(row_1_denom[i])
                        bernoulli_print.append(":")
                    else:
                        bernoulli_print.append(0)
                        bernoulli_print.append(":")
                print bernoulli_print
                bernoulli_print=[]
                print '\n'
        if B%2==0:
            bernoulli_result=float(row_1_list[0])/row_1_denom[0]
        else:
            bernoulli_result=0 
    elif bernoulli_value==0:
        bernoulli_result=1
    elif bernoulli_value==1:
        bernoulli_result=-0.5
    elif bernoulli_value==2:
        bernoulli_result=1./6
    print "bernoulli_result=",bernoulli_result
    
            
        
        
    
    
        
            
                
        
            
        
    




                   
        
        



    
            
    
