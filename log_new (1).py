e=2.718281828459045
precision=0
log_array=["calculation_history:",]

def log(base,prod,accur):
    global precision
    if base==0 or prod==0 or base==1:
        return "error"
    if prod==1:
        return 0
    if base==prod:
        return 1
    base=float(abs(base))
    prod=float(abs(prod))
    if accur>11:
        accur=11
    tol=10**-accur
    exp=1
    exp_x=0
    base_x=0
    exp_add=0
    exp_state=False
    if base<1 and prod<1:
        base=1/base
        prod=1/prod
    if prod<1:
        exp_state=True
        prod=1/prod
    if base<1:
        exp_state=True
        base=1/base
    prod_x=base
    for x in range(accur+4):
        exp_add=10**-x
        base_x=base**exp_add
        while prod_x<prod:
            exp+=exp_add
            prod_x=base**exp
        if prod_x>prod:
            prod_x=prod_x/base_x
            exp=exp-exp_add
        if prod-prod_x <tol or prod_x==prod:
            precision=x,tol
            break
    if exp_state==True:
        exp=-exp
    return exp
        
def log1(base,prod,accur):
    log1_list=["log_and_derivative","input:",["constant_base_b=",],["product_variable_x=",],"output:",["precision_error_margin=",],["log(b)[x]=",],["derivative=",]] 
    logbx=log(base,prod,accur)
    deriv=1/(prod*log(e,base,accur))
    for x,y in zip((2,3,5,6,7),(base,prod,precision,logbx,deriv)):
        log1_list[x].append(y)
    log_array.append(log1_list)
    for x in range(8):
        print log1_list[x]
    print '\n'
    return logbx,deriv

def log2(base,prod1,prod2,accur):
    log2_list=["integral_area_and_arc_length","input:",["constant_base_b=",],["product_variable_x1=",],["product_variable_x2=",],"output:",["precision_error_margin=",],["integral_area=",],["arc_length=",]]
    lnbase=log(e,base,accur)
    x1lnb=((prod1*lnbase)**2+1)**0.5
    x2lnb=((prod2*lnbase)**2+1)**0.5
    area=abs((prod2/lnbase)*(log(e,prod2,accur)-1)-(prod1/lnbase)*(log(e,prod1,accur)-1))
    length=abs(((x2lnb-x1lnb)+log(e,prod2*(1+x1lnb)/(prod1*(1+x2lnb)),accur))/lnbase)
    for x,y in zip((2,3,4,6,7,8),(base,prod1,prod2,precision,area,length)):
        log2_list[x].append(y)
    log_array.append(log2_list)
    for x in range(9):
        print log2_list[x]
    print '\n'
    return area,length
           
def log3(a,x1,x2,accur):
    log3_list=["integral_area_","input:",["numerator_a=",],["denominator_variable_x1=",],["denominator_variable_x2=",],"output:",["precision_error_margin=",],["integral_area_under_a/x=",]]
    area=a*log(e,float(x2)/x1,accur)
    for x,y in zip((2,3,4,6,7),(a,x1,x2,precision,area)):
        log3_list[x].append(y)
    log_array.append(log3_list)
    for x in range(8):
        print log3_list[x]
    print '\n'
    return area

def history():
    print log_array[0]
    for x in range(1,len(log_array)):
        print '\n'
        for y in range(len(log_array[x])):
            print log_array[x][y]


       









    
