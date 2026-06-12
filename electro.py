e,q="e","q"
def electro(e_or_q,eq1,eq1_deci,eq2,eq2_deci,d):
    coeff=1
    k=8.9875517923*10**9
    eq1,eq2,d=float(eq1),float(eq2),float(d)
    if e_or_q=="e":
        eq1,eq2=eq1*10**eq1_deci*d**2/k,eq2*10**eq2_deci*d**2/k
    elif e_or_q=="q":
        eq1,eq2=eq1*10**eq1_deci,eq2*10**eq2_deci
    factor1,factor2=(abs(eq1))**0.5,(abs(eq2)/abs(eq1))**0.5
    if eq1>0 and eq2<0 or eq1<0 and eq2>0:
        coeff=-1
        factor1,factor2=-factor1,-factor2
    return d*(abs(eq1))**0.5/((abs(eq2))**0.5+factor1),coeff*d/(1+factor2)
    
    
    
    
    
        
        
