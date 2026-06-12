def bernoulli(number=""):
    global bernoulli_result
    bernoulli_value=""
    print "bernoulli function only shows iterative visualization triangle(Akiyama-Tanigawa) for B(n) values"
    print "greater >2 and <11 for screen readability and educational aid."
    print "note:values quickly lose accuracy with this method after B(16)"
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
    row_1_list=[]
    bernoulli_result=None
    if type(bernoulli_value)==int and bernoulli_value>2:
        B=bernoulli_value
        bernoulli_value+=1
        if B<11:
            print "first row of Bernoulli triangle for B(",B,")"
            print '\n'
        for n in range(1,bernoulli_value+1):
            row_1_list.append(1./n)
        if B<11:
            print row_1_list
            print '\n'
        terms=bernoulli_value-1
        while terms>=1:
            terms-=1
            for n in range(bernoulli_value):
                if n<=terms:
                    row_1_list[n]=(n+1)*(row_1_list[n]-row_1_list[n+1])
                    if abs(row_1_list[n])<1e-8:
                        row_1_list[n]=0
                elif n>terms:
                    row_1_list[n]=0
            if B<11:
                print "row",abs(terms-bernoulli_value),"of Bernoulli triangle for B(",B,")"
                print '\n'
                print row_1_list
                print '\n'
        bernoulli_result=row_1_list[0]
        if B%2!=0 and B>2:
            bernoulli_result=0
    elif bernoulli_value==0:
        bernoulli_result=1
    elif bernoulli_value==1:
        bernoulli_result=-0.5
    elif bernoulli_value==2:
        bernoulli_result=1./6
    print "bernoulli_result=",bernoulli_result
    
            
        
        
    
    
        
            
                
        
            
        
    




                   
        
        



    
            
    
