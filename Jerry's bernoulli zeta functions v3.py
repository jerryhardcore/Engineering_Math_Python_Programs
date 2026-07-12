pi=3.1415936535897932384626433

def zeta(s=None):
    dirichlet_series=[]
    if type(s) is int and s>=0:
        if s==0:
            return 0
        elif s==1:
            return 0
        elif s==2:
            return 1.6449340668482264
        elif s==3:
            return 1.2020569031595943
        elif s==4:
            return 1.0823232337111381
        elif s==5:
            return 1.0369277551433699
        elif s==6:
            return 1.0173430619844491
        elif  s>=7 and s<45:
            if s>=7 and s<21:
                precision=1200
            elif s>=21 and s<45:
                precision=500
            for n in range(1,precision):
                dirichlet_series.append(n**-s)
            return sum(dirichlet_series)
        elif s>=45:
            return 1.0
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

zeta_list=[]
for n in range(141):
    zeta_list.append(zeta(n))

def B(index=None):
    if type(index) is int and index>=0:
        if index==0:
            return 1
        elif index==1:
            return -0.5
        elif index==2:
            return 1./6
        elif index>2:
            if index%2!=0:
                return 0
            else:
                return 2*(-1)**(index/2+1)*factorial(index)*zeta_list[index]/((2*pi)**index)
    else:
        return None

bernoulli_list=[]
factorial_list=[]
for n in range(141):
    bernoulli_list.append(B(n))
    factorial_list.append(factorial(n))
quotient_list=[]
for bern,fact in zip((bernoulli_list),(factorial_list)):
    quotient_list.append(bern/fact)

def Btan(x=None):
    if x is not None and x>0 and x<pi/2:
        tan_list=[]
        if x>0 and x<=pi/4:
            for n in range(1,70):
                y=(-1)**(n-1)*2**(2*n)*(2**(2*n)-1)*x**(2*n-1)*quotient_list[2*n]
                tan_list.append(y)
            return sum(tan_list)
        elif x>pi/4 and x<pi/2:
            for n in range(1,70):
                y=(-1)**(n-1)*2**(2*n)*(2**(2*n)-1)*(pi/2-x)**(2*n-1)*quotient_list[2*n]
                tan_list.append(y)
            return 1./sum(tan_list)  
    else:
        return None

def Bcot(x=None):
    if x is not None and x>0 and x<pi/2:
        cot_list=[]
        for n in range(1,70):
            y=(-1)**(n-1)*2**(2*n)*x**(2*n-1)*quotient_list[2*n]
            cot_list.append(y)
        return 1./x-sum(cot_list)
    else:
        return None

def Bcosec(x=None):
    if x is not None and x>0 and x<pi:
        cosec_list=[]
        for n in range(1,70):
            y=(-1)**(n-1)*2*(2**(2*n-1)-1)*x**(2*n-1)*quotient_list[2*n]
            cosec_list.append(y)
        return 1./x+sum(cosec_list)
    else:
        return None



