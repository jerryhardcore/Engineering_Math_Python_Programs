pi=3.1415936535897932384626433

def B(number=None):
    if type(number) is int and number>=0 and number<=36:
        if number==0:
            return 1
        elif number==1:
            return -0.5
        elif number==2:
            return 1./6
        elif number>2:
            if number%2!=0:
                return 0
            else:
                bernoulli_value=number+1     
                row_1_list=[]
                row_1_denom=[]
                for n in range(1,bernoulli_value+1):
                    row_1_list.append(1)
                    row_1_denom.append(n)
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
                return float(row_1_list[0])/row_1_denom[0]
    else:                                   
        return None

def factorial(x=None):
    if type(x) is int and x>=0:
        if x==0:
            return 1.0
        if x==1:
            return 1.0
        if x==2:
            return 2.0
        if x>=3:
            y=2
            for n in range(3,x+1):
                y=y*n
            return float(y)
    else:
        return None
        
def Btan(x=None):
    if x is not None:
        tan_list=[]
        if x>0 and x<=(pi/4):
            for n in range(1,19):
                y=(-1)**(n-1)*2**(2*n)*(2**(2*n)-1)*B(2*n)*x**(2*n-1)/factorial(2*n)
                tan_list.append(y)
            return sum(tan_list)
        elif x>(pi/4) and x<(pi/2):
            for n in range(1,19):
                y=(-1)**(n-1)*2**(2*n)*(2**(2*n)-1)*B(2*n)*(pi/2-x)**(2*n-1)/factorial(2*n)
                tan_list.append(y)
            return 1./sum(tan_list)  
    else:
        return None


        
    
   

   

                           
