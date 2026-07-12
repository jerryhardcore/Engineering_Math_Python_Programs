def log_func(base,prod):
    base=float(base)
    prod=float(prod)
    exp=1
    prod_x=base
    exp_x=0
    base_x=0
    exp_add=0
    exp_state=False
    if prod<1:
        exp_state=True
        prod=1/prod
    for x in range(10):
        exp_add=10**-x  
        while prod_x<prod:
            exp+=exp_add
            prod_x=base**exp
        for y in range(10):
            exp_x=10**-y
            base_x=base**exp_x
            if prod_x>prod and exp_add==exp_x:
                prod_x=prod_x/base_x
                exp=exp-exp_add
    if exp_state==True:
        prod_x=1/prod_x
        exp=-exp
    return exp

ln_base=2.718281828459

def nest_log_func(base,prod):
    exp_list=[0,1,2]
    for b,p,e in zip((base,ln_base,ln_base),(prod,base,prod),(exp_list)):
        exp_list[e]=log_func(b,p)
    return exp_list

log_data={
    "single_variable_x":{
        "b":0,
        "x":0,
        "log(b)[x]":0,
        "derivative_log(b)[x]":0,
        "indefinite_integral_log(b)[x]":0
        },
    "double_variable_x":{
        "x2":0,
        "area_integral_log(b2)[x1->x2]":0
        }    
}       

def dict_reset():
    for x,key in log_data.items():
        for y in key:
            key[y]=0

def log_dict():
    print '\n'
    print "English"
    for x,key in log_data.items():
        print '\n'
        print x
        print '\n'
        for y in key:
            print y,":",key[y]

log_data_greek={
    "μονό_μεταβλητή_x":{
        "παράγωγο_log(b)[x]":0,
        "αόριστο_ολοκλήρωμα_log(b)[x]":0
        },
    "διπλό_μεταβλητή_x":{
        "εμβαδόν_ολοκλήρωμα_log(b2)[x1->x2]":0
        }    
}

def dict_copy():
    log_data_greek["μονό_μεταβλητή_x"]["παράγωγο_log(b)[x]"]=log_data["single_variable_x"]["derivative_log(b)[x]"]
    log_data_greek["μονό_μεταβλητή_x"]["αόριστο_ολοκλήρωμα_log(b)[x]"]=log_data["single_variable_x"]["indefinite_integral_log(b)[x]"]
    log_data_greek["διπλό_μεταβλητή_x"]["εμβαδόν_ολοκλήρωμα_log(b2)[x1->x2]"]=log_data["double_variable_x"]["area_integral_log(b2)[x1->x2]"]
        

def log_dict_greek():
    print '\n'
    print "Ελληνικά"
    for x,key in log_data_greek.items():
        print '\n'
        print x
        print '\n'
        for y in key:
            print y,":",key[y]
           
def log_deriv_func(base,prod):
    global user_exp,log_deriv,log_integ,base_final,prod_final
    base_final=base
    prod_final=prod
    user_exp,ln_exp,ln_exp_int=nest_log_func(base,prod)[0:3]
    log_deriv=1/(prod*ln_exp)
    log_integ=(prod/ln_exp)*(ln_exp_int-1)
    for x,y in zip(("b","x","log(b)[x]","derivative_log(b)[x]","indefinite_integral_log(b)[x]"),(base_final,prod_final,user_exp,log_deriv,log_integ)):
        log_data["single_variable_x"][x]=y
    return user_exp,log_deriv,log_integ

def area_find(base,prod1,prod2):
    global net_area,prod1_final,prod2_final,area_base
    area_base=base
    prod1_final=prod1
    prod2_final=prod2
    net_area=log_deriv_func(base,prod2)[2]-log_deriv_func(base,prod1)[2]
    for x,y in zip(("b","x","log(b)[x]","derivative_log(b)[x]","indefinite_integral_log(b)[x]"),(area_base,prod1_final,user_exp,log_deriv,log_integ)):
        log_data["single_variable_x"][x]=y
    for x,y in zip(("x2","area_integral_log(b2)[x1->x2]"),(prod2_final,net_area)):
        log_data["double_variable_x"][x]=y
    return net_area
    
def log_call(base,prod):
    dict_reset()
    log_deriv_func(base,prod)
    dict_copy()
    print "Ο λογάριθμος της βάσης",base_final,"και του προϊόνος",prod_final,"που δώσατε δίνει εκθέτη",user_exp
    print "The logarithm of the given base",base_final,"and product",prod_final,"gives exponent",user_exp
    
def derivative(base,prod):
    dict_reset()
    log_deriv_func(base,prod)
    dict_copy()
    print "Το παράγωγο του λογάριθμου",user_exp,"είναι",log_deriv
    print "The derivative of the logarithm",user_exp,"is",log_deriv 
    
def integral(base,prod):
    dict_reset()
    log_deriv_func(base,prod)
    dict_copy()
    print "Το αόριστο ολοκλήρωμα/αντιπαράγωγο του λογάριθμου",user_exp,"χωρίς σταθερά ολοκληρώσεως είναι",log_integ
    print "The indefinite integral of the logarithm",user_exp,"without the constant of integration is",log_integ

def integ_area(base,prod1,prod2):
    area_find(base,prod1,prod2)
    dict_copy()
    print "το εμβαδόν μέσα στα όρια των 2 τιμών",prod1_final,"και",prod2_final
    print "του μεταβλητή προϊόντος του ολοκληρώματος του λογάριθμου με βάση",area_base,"ειναι",net_area
    print "the area within the limit of 2 values",prod1_final,"and",prod2_final
    print "of the product variable of the integral of the logarithm with base",area_base,"is",net_area

class log_explain:
    def log(self,base,prod):
        return log_call(base,prod),log_dict(),log_dict_greek()
    
    def deriv(self,base,prod):
        return derivative(base,prod),log_dict(),log_dict_greek()
    
    def integ(self,base,prod):
        return integral(base,prod),log_dict(),log_dict_greek()
    
    def area(self,base,prod1,prod2):
        return integ_area(base,prod1,prod2),log_dict(),log_dict_greek()

fx=log_explain() 



