e=2.718281828459045
pi=3.1415926535897932384626433

def tan(x):
    return ((e**(x*1j)-e**(x*-1j))/(1j*(e**(x*1j)+e**(x*-1j)))).real

def cos(x):
    return ((e**(x*1j)+e**(x*-1j))/2).real

def sin(x):
    return ((e**(x*1j)-e**(x*-1j))/2j).real

def sin_rad(x):
    return (1j**(4.0*x/(2*pi))).imag

def cos_rad(x):
    return (1j**(4.0*x/(2*pi))).real

def tan_rad(x):
    return (1j**(2.0*x/pi)).imag/(1j**(2.0*x/pi)).real

def sin_series(x):
    sin_list=[x,]
    sin_term=float(x)
    for k in range(2,300):
        sin_term=sin_term*x/k
        if k%2!=0:
            sin_list.append(sin_term)
    for k in range(1,150,2):
        sin_list[k]=-sin_list[k]
    return sum(sin_list)
         
def cos_series(x):
    cos_list=[1,]
    cos_term=float(x)
    for k in range(2,300):
        cos_term=cos_term*x/k
        if k%2==0:
            cos_list.append(cos_term)
    for k in range(1,150,2):
        cos_list[k]=-cos_list[k]
    return sum(cos_list)

def tan_series(x):
    sin_list=[x,]
    cos_list=[1,]
    sin_cos_term=float(x)
    for k in range(2,300):
        sin_cos_term=sin_cos_term*x/k
        if k%2==0:
            cos_list.append(sin_cos_term)
        elif k%2!=0:
            sin_list.append(sin_cos_term)
    for k in range(1,150,2):
        sin_list[k]=-sin_list[k]
        cos_list[k]=-cos_list[k]
    return sum(sin_list)/sum(cos_list)

def log(base,prod):
    if base==0 or prod==0 or base==1:
        return "error"
    if prod==1:
        return 0
    if base==prod:
        return 1
    base=float(abs(base))
    prod=float(abs(prod))
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
    for x in range(11):
        exp_add=10**-x
        base_x=base**exp_add
        while prod_x<prod:
            exp+=exp_add
            prod_x=base**exp
        if prod_x>prod:
            prod_x=prod_x/base_x
            exp-=exp_add
        if prod_x==prod:
            break
    if exp_state==True:
        exp=-exp
    return exp

def arctan(b,a):
    y=abs(float(b)/a)
    rad=0
    rad_add=0
    arctan_x=0
    last_arctan=0
    for x in range(11):
        rad_add=10**-x
        while arctan_x<y and rad<pi/2:
            last_arctan=arctan_x
            rad+=rad_add
            arctan_x=abs(((e**(rad*1j)-e**(rad*-1j))/(1j*(e**(rad*1j)+e**(rad*-1j)))).real)
        if arctan_x>y or rad>pi/2:
            rad-=rad_add
            arctan_x=last_arctan
    if a<0 and b>0:
        rad=pi-rad
    elif a<0 and b<0:
        rad=rad-pi
    elif a>0 and b<0:
        rad=-rad
    return rad

def arcsin(x):
    return arctan(x,(1-x**2)**0.5)

def arccos(x):
    return arctan((1-x**2)**0.5,x)

def atan(x):
    y=arctan(1,1.0/x)
    if x<0:
        y=-(pi-y)
    return y

def complex_arc(z):
    z=z/abs(z)
    if abs(z-1)<1 or abs(z-1)==1 and z!=0:
        terms_list=[0,]
        for n in range(1,201):
            terms_list.append((z-1)**n)
        for n in range(1,201,2):
            terms_list[n]=terms_list[n]*-2j/(n*pi)
        for n in range(2,201,2):
            terms_list[n]=terms_list[n]*1j/(n/2*pi)
        lnz1=(sum(terms_list)*2*pi/4).real
    elif abs(z-1)>1:
        terms_list2=[2,]
        for n in range(1,201):
            terms_list2.append(z**n)
        for n in range(1,201,2):
            terms_list2[n]=terms_list2[n]*2j/(n*pi)
        for n in range(2,201,2):
            terms_list2[n]=terms_list2[n]*1j/(n/2*pi)
        terms_list3=[0,]
        for n in range(1,201):
            terms_list3.append((z-1)**-n)
        for n in range(1,201,2):
            terms_list3[n]=terms_list3[n]*-2j/(n*pi)
        for n in range(2,201,2):
            terms_list3[n]=terms_list3[n]*1j/(n/2*pi)
        lnz1=((sum(terms_list2)+sum(terms_list3))*2*pi/4).real
    if z.real>0 and z.imag<0 and abs(lnz1)<1.5*pi:
        lnz1=2*pi-abs(lnz1)
    if z.real<0 and z.imag<0 or z.real>0 and z.imag<0:
        lnz1=-(2*pi-lnz1)
    return lnz1

def arccos_i(x):
    return complex_arc(x+(1-x**2)**0.5*1j)

def arcsin_i(x):
    return complex_arc((1-x**2)**0.5+x*1j)

def arctan_i(x):
    y=complex_arc(1.0/x+1j)
    if x<0:
        y=-(pi-y)
    return y

def log_i(z):
    z=z/abs(z)
    if z.imag<0 and z.real>0:
        z=-z.real+abs(z.imag)*1j
    terms_list=[1j*pi/2,]
    for n in range(1,161):
        terms_list.append((z-1j)**n)
    for n in range(1,161,4):
        terms_list[n]=terms_list[n]*1j/-n
    for n in range(3,161,4):
        terms_list[n]=terms_list[n]*1j/n
    for n in range(2,161,4):
        terms_list[n]=terms_list[n]/n
    for n in range(4,161,4):
        terms_list[n]=terms_list[n]/-n
    y=(sum(terms_list)*-1j).real
    if y>pi/2:
        y=-(pi-y)
    return y

def arctan_i2(x):
    interval_cond=False
    negative_cond=False
    if x<0:
        negative_cond=True
    if abs(x)<0.65:
        x=1./x
        interval_cond=True
    y=abs(log_i(1.0/x+1j))
    if interval_cond==True:
        y=pi/2-y
    if negative_cond==True:
        y=-y
    return y

def arccos_i2(x):
    y=log_i(x+(1-x**2)**0.5*1j)
    if y<0:
        y=pi-abs(y)
    return y

def arcsin_i2(x):
    interval_cond=False
    negative_cond=False
    if x<0:
        negative_cond=True
    if abs(x)<0.65:
        x=(1-x**2)**0.5
        interval_cond=True
    y=abs(log_i((1-x**2)**0.5+x*1j))
    if interval_cond==True:
        y=pi/2-y
    if negative_cond==True:
        y=-y
    return y

def new_arcsin(x):
    converge=False
    negative=False
    if x<0:
        negative=True
        x=abs(x)
    if x>0.5:
        converge=True
        x=(1-x**2)**0.5
    terms_list=[x,]
    for n in range(3,200,2):
        term=x**n/n
        coeff=0.5
        for k in range(3,n):
            if k%2!=0:
                coeff=coeff*k
            else:
                coeff=coeff/k
        terms_list.append(term*coeff)
    angle=sum(terms_list)
    if converge==True:
        angle=pi/2-angle
    if negative==True:
        angle=-angle
    return angle

def new_arctan(x):
    return new_arcsin(x/(1+x**2)**0.5)

def new_arccos(x):
    return pi/2-arcsin(x)

def factor():
    global multiple
    multiple=raw_input("1 for mega, 2 for kilo, ENTER key for standard unit, 3 for milli, 4 for micro:")
    while multiple!="1" and multiple!="2" and multiple!="3" and multiple!="4" and multiple!="":
        print "input error"
        multiple=raw_input("1 for mega, 2 for kilo, ENTER key for standard unit, 3 for milli, 4 for micro:")
    if multiple=="1":
        multiple=1000000
    elif multiple=="2":
        multiple=1000
    elif multiple=="3":
        multiple=0.001
    elif multiple=="4":
        multiple=0.000001
    else:
        multiple=1

def s_or_p():
    global series_or_parallel
    series_or_parallel=raw_input("enter 1 for series rlc circuit or 2 for parallel rlc circuit:")
    while series_or_parallel!="1" and series_or_parallel!="2" and series_or_parallel!="":
        print "input error"
        series_or_parallel=raw_input("enter 1 for series rlc circuit or 2 for parallel rlc circuit:")

def impedance():
    global imped_mag
    imped_mag=raw_input("Enter magnitude of impedance:")
    while imped_mag.replace('.','',1).isdigit()==False and imped_mag.isdigit()==False and imped_mag.replace('-','',1).isdigit()==False and imped_mag.replace('.','',1).replace('-','',1).isdigit()==False and imped_mag!="" or imped_mag=="0" or imped_mag=="0.0" or "-" in imped_mag and imped_mag.index('-')!=0:
        print "input error"
        imped_mag=raw_input("Enter magnitude of impedance:")
    if imped_mag!="":
        print "unit of measurement for impedance in Ohms"
        factor()
        imped_mag=abs(float(imped_mag))*multiple
        
def reactance():
    global net_react,react_processed
    react_processed=False
    net_react=raw_input("Enter net reactance:")
    while net_react.replace('.','',1).isdigit()==False and net_react.isdigit()==False and net_react.replace('-','',1).isdigit()==False and net_react.replace('.','',1).replace('-','',1).isdigit()==False and net_react!="" or net_react=="0" or net_react=="0.0" or "-" in net_react and net_react.index('-')!=0:
        print "input error"
        net_react=raw_input("Enter net reactance:")
    if net_react!="":
        print "unit of measurement for net reactance in Ohms"
        factor()
        net_react=float(net_react)*multiple
    else:
        induct_react=raw_input("Enter inductive reactance:")
        while induct_react.replace('.','',1).isdigit()==False and induct_react.isdigit()==False and induct_react.replace('-','',1).isdigit()==False and induct_react.replace('.','',1).replace('-','',1).isdigit()==False and induct_react!="" or induct_react=="0" or induct_react=="0.0" or "-" in induct_react and induct_react.index('-')!=0:
            print "input error"
            induct_react=raw_input("Enter inductive reactance:")
        capac_react=raw_input("Enter capacitive reactance:")
        while capac_react.replace('.','',1).isdigit()==False and capac_react.isdigit()==False and capac_react.replace('-','',1).isdigit()==False and capac_react.replace('.','',1).replace('-','',1).isdigit()==False and capac_react!="" or capac_react=="0" or capac_react=="0.0" or "-" in capac_react and capac_react.index('-')!=0:
            print "input error"
            capac_react=raw_input("Enter capacitive reactance:")
        if capac_react!="" and induct_react!="":
            react_processed=True
            capac_react,induct_react=abs(float(capac_react)),abs(float(induct_react))
            print "unit of measurement for inductive reactance in Ohms"
            factor()
            induct_react=induct_react*multiple
            print "unit of measurement for capacitive reactance in Ohms"
            factor()
            capac_react=capac_react*multiple
            if series_or_parallel=="1":
                net_react=induct_react-capac_react
                if abs(net_react)<0.005:
                    print "net reactance cannot be zero"
                    net_react=""
            elif series_or_parallel=="2":
                if abs(1./induct_react-1./capac_react)>0.05:
                    net_react=1./(1./induct_react-1./capac_react)
                else:
                    print "error: divide by zero"
                    net_react==""
        else:
            induct=raw_input("Enter inductance:")
            while induct.replace('.','',1).isdigit()==False and induct.isdigit()==False and induct.replace('-','',1).isdigit()==False and induct.replace('.','',1).replace('-','',1).isdigit()==False and induct!="" or induct=="0" or induct=="0.0" or "-" in induct and induct.index('-')!=0:
                print "input error"
                induct=raw_input("Enter inductance:")
            if induct!="":
                print "unit of measurement for inductance in Henries"
                factor()
                induct=abs(float(induct))*multiple
            capac=raw_input("Enter capacitance:")
            while capac.replace('.','',1).isdigit()==False and capac.isdigit()==False and capac.replace('-','',1).isdigit()==False and capac.replace('.','',1).replace('-','',1).isdigit()==False and capac!="" or capac=="0" or capac=="0.0" or "-" in capac and capac.index('-')!=0:
                print "input error"
                capac=raw_input("Enter capacitance:")
            if capac!="":
                print "unit of measurement for capacitance in Farads"
                factor()
                capac=abs(float(capac))*multiple
            if type(induct)==float and type(capac)==float:
                freq=raw_input("Enter frequency:")
                while freq.replace('.','',1).isdigit()==False and freq.isdigit()==False and freq.replace('-','',1).isdigit()==False and freq.replace('.','',1).replace('-','',1).isdigit()==False and freq!="" or freq=="0" or freq=="0.0" or "-" in freq and freq.index('-')!=0:
                    print "input error"
                    freq=raw_input("Enter frequency:")
                ang_or_hz=raw_input("1 for frequency in Hertz, 2 for angular frequency in rad/s:")
                while ang_or_hz!="1" and ang_or_hz!="2" and ang_or_hz!="":
                    print "input error"
                    ang_or_hz=raw_input("1 for frequency in Hertz, 2 for angular frequency in rad/s:")
                if freq!="" and ang_or_hz!="":
                    react_processed=True
                    print "unit of measurment for frequency"
                    factor()
                    freq=abs(float(freq))*multiple
                    if ang_or_hz=="2":
                        freq=freq/(2*pi)
                    if series_or_parallel=="1":
                        net_react=2*pi*freq*induct-1/(2*pi*freq*capac)
                        if abs(net_react)<0.05:
                            print "error: net reactance cannot be zero"
                            net_react=""
                    elif series_or_parallel=="2":
                        if abs(1./(2*pi*freq*induct)-2*pi*freq*capac)>0.05:
                            net_react=1./(1./(2*pi*freq*induct)-2*pi*freq*capac)
                        else:
                            net_react=""
                            print "error: divide by zero"
                          
def resistance():
    global resist
    resist=raw_input("Enter resistance:")
    while resist.replace('.','',1).isdigit()==False and resist.isdigit()==False and resist.replace('-','',1).isdigit()==False and resist.replace('.','',1).replace('-','',1).isdigit()==False and resist!="" or resist=="0" or resist=="0.0" or "-" in resist and resist.index('-')!=0:
        print "input error"
        resist=raw_input("Enter resistance:")
    if resist!="":
        print "unit of measurement for resistance in Ohms"
        factor()
        resist=abs(float(resist))*multiple

def phase_angle():
    global phase
    deg_or_rad=raw_input("phase angle: enter 1 for degrees or 2 for radians:")
    while deg_or_rad!="1" and deg_or_rad!="2" and deg_or_rad!="":
        print "input error"
        deg_or_rad=raw_input("phase angle: enter 1 for degrees or 2 for radians:")
    if deg_or_rad!="":
        phase=raw_input("Enter phase angle:")
        while phase.replace('.','',1).isdigit()==False and phase.isdigit()==False and phase.replace('-','',1).isdigit()==False and phase.replace('.','',1).replace('-','',1).isdigit()==False and phase!="" or phase=="0" or phase=="0.0" or "-" in phase and phase.index('-')!=0:
            print "input error"
            phase=raw_input("Enter phase angle:")
        if phase!="":
            phase=float(phase)
            if deg_or_rad=="1":
                if abs(phase)%90>=0 and abs(phase)%90<=0.005:
                    phase+=0.005
                phase=phase*pi/180
            elif deg_or_rad=="2" and abs(phase)%(pi/2)>=0 and abs(phase)%(pi/2)<=0.005:
                phase+=0.005
    else:
        phase=""

def input_decibel():
    global db_input
    db_input=raw_input("Enter input voltage or power:")
    while db_input.replace('.','',1).isdigit()==False and db_input.isdigit()==False and db_input.replace('-','',1).isdigit()==False and db_input.replace('.','',1).replace('-','',1).isdigit()==False and db_input!="" or db_input=="0" or db_input=="0.0" or "-" in db_input and db_input.index('-')!=0:
        print "input error"
        db_input=raw_input("Enter input voltage or power:")
    if db_input!="":
        print "unit of measurement for input voltage in Volts or power in Watts"
        factor()
        db_input=abs(float(db_input))*multiple

def output_decibel():
    global db_output
    db_output=raw_input("Enter output voltage or power:")
    while db_output.replace('.','',1).isdigit()==False and db_output.isdigit()==False and db_output.replace('-','',1).isdigit()==False and db_output.replace('.','',1).replace('-','',1).isdigit()==False and db_output!="" or db_output=="0" or db_output=="0.0" or "-" in db_output and db_output.index('-')!=0:
        print "input error"
        db_output=raw_input("Enter output voltage or power:")
    if db_output!="":
        print "unit of measurement for output voltage in Volts or power in Watts"
        factor()
        db_output=abs(float(db_output))*multiple
        
def input_impedance():
    global imped_in
    imped_in=raw_input("Enter input impedance for mismatch correction:")
    while imped_in.replace('.','',1).isdigit()==False and imped_in.isdigit()==False and imped_in.replace('-','',1).isdigit()==False and imped_in.replace('.','',1).replace('-','',1).isdigit()==False and imped_in!="" or imped_in=="0" or imped_in=="0.0" or "-" in imped_in and imped_in.index('-')!=0:
        print "input error"
        imped_in=raw_input("Enter input impedance for mismatch correction:")
    if imped_in!="":
        print "unit of measurement for input impedance in Ohms for mismatch correction"
        factor()
        imped_in=abs(float(imped_in))*multiple
        
def output_impedance():
    global imped_out
    imped_out=raw_input("Enter output impedance for mismatch correction:")
    while imped_out.replace('.','',1).isdigit()==False and imped_out.isdigit()==False and imped_out.replace('-','',1).isdigit()==False and imped_out.replace('.','',1).replace('-','',1).isdigit()==False and imped_out!="" or imped_out=="0" or imped_out=="0.0" or "-" in imped_out and imped_out.index('-')!=0:
        print "input error"
        imped_out=raw_input("Enter output impedance for mismatch correction:")
    if imped_out!="":
        print "unit of measurement for output impedance in Ohms for mismatch correction"
        factor()
        imped_out=abs(float(imped_out))*multiple

phase_angle_1,phase_angle_2,phase_angle_3,phase_angle_4=0,0,0,0
log_coeff=0

solve=raw_input("1: solve for impedance, 2: solve for resistance, 3: solve for reactance, 4: decibel gain/attenuation, 0 to end program:")
if solve=="0":
    print "program ended"
while solve!="0":
    while solve!="1" and solve!="2" and solve!="3" and solve!="4" and solve!="0":
        print "input error"
        solve=raw_input("1: solve for impedance, 2: solve for resistance, 3: solve for reactance, 4: decibel gain/attenuation, 0 to end program:")
    if solve=="1":
        s_or_p()
        if series_or_parallel!="":
            resistance()
            reactance()
            if type(resist)==float and type(net_react)==float:
                if series_or_parallel=="1":
                    print "impedance magnitude is",abs(resist+net_react*1j),"Ohms"
                    phase_angle_1=atan(net_react/resist) 
                    phase_angle_2=arctan_i(net_react/resist)
                    phase_angle_3=arctan_i2(net_react/resist)
                    phase_angle_4=new_arctan(net_react/resist)
                    print "impedance phase angle for series rlc circuit:"
                elif series_or_parallel=="2":
                    print "impedance magnitude is",1./abs((1./resist)+(1./net_react)*1j),"Ohms"
                    phase_angle_1=atan(resist/net_react)
                    phase_angle_2=arctan_i(resist/net_react)
                    phase_angle_3=arctan_i2(resist/net_react)
                    phase_angle_4=new_arctan(resist/net_react)
                    print "impedance phase angle for series rlc circuit:"
                print "impedance phase angle from 1st arctan function is",phase_angle_1,"radians or",phase_angle_1*180/pi,"degrees"
                print "impedance phase angle from 2nd arctan function is",phase_angle_2,"radians or",phase_angle_2*180/pi,"degrees"
                print "impedance phase angle from 3rd arctan function is",phase_angle_3,"radians or",phase_angle_3*180/pi,"degrees"
                print "impedance phase angle from 4th arctan function is",phase_angle_4,"radians or",phase_angle_4*180/pi,"degrees"
            elif type(resist)==float and react_processed==False:
                phase_angle()
                if type(phase)==float:
                    if series_or_parallel=="1":
                        print "impedance for series rlc circuit:"
                        print "impedance from 1st cos function is",resist/cos(phase),"Ohms"
                        print "impedance from 2nd cos function is",resist/cos_rad(phase),"Ohms"
                        print "impedance from 3rd cos function is",resist/cos_series(phase),"Ohms"
                    elif series_or_parallel=="2":
                        print "impedance for parallel rlc circuit:"
                        print "impedance from 1st cos function is",resist*cos(phase),"Ohms"
                        print "impedance from 2nd cos function is",resist*cos_rad(phase),"Ohms"
                        print "impedance from 3rd cos function is",resist*cos_series(phase),"Ohms"
                else:
                    print "insufficient data"
            elif type(net_react)==float:
                phase_angle()
                if type(phase)==float:
                    if series_or_parallel=="1":
                        print "impedance for series rlc circuit:"
                        print "impedance from 1st sin function is",net_react/sin(phase),"Ohms"
                        print "impedance from 2nd sin function is",net_react/sin_rad(phase),"Ohms"
                        print "impedance from 3rd sin function is",net_react/sin_series(phase),"Ohms"
                    elif series_or_parallel=="2":
                        print "impedance for parallel rlc circuit:"
                        print "impedance from 1st sin function is",net_react*sin(phase),"Ohms"
                        print "impedance from 2nd sin function is",net_react*sin_rad(phase),"Ohms"
                        print "impedance from 3rd sin function is",net_react*sin_series(phase),"Ohms"
                else:
                    print "insufficient data"
            else:
                print "insufficient data"
        else:
            print "insufficient data"   
    elif solve=="2":
        s_or_p()
        if series_or_parallel!="":
            impedance()
            reactance()
            if type(net_react)==float and type(imped_mag)==float:
                if abs(net_react/imped_mag)<0.995 and series_or_parallel=="1" or abs(imped_mag/net_react)<0.995 and series_or_parallel=="2":
                    if series_or_parallel=="1":
                        phase_angle_1=arcsin(net_react/imped_mag)
                        phase_angle_2=arcsin_i(net_react/imped_mag)
                        phase_angle_3=arcsin_i2(net_react/imped_mag)
                        phase_angle_4=new_arcsin(net_react/imped_mag)
                        print "phase angle and resistance for series rlc circuit:"
                        print "resistance from 1st cos function is",imped_mag*cos(phase_angle_1),"Ohms"
                        print "resistance from 2nd cos function is",imped_mag*cos_rad(phase_angle_1),"Ohms"
                        print "resistance from 3rd cos function is",imped_mag*cos_series(phase_angle_1),"Ohms"
                    elif series_or_parallel=="2":
                        phase_angle_1=arcsin(imped_mag/net_react)
                        phase_angle_2=arcsin_i(imped_mag/net_react)
                        phase_angle_3=arcsin_i2(imped_mag/net_react)
                        phase_angle_4=new_arcsin(imped_mag/net_react)
                        print "phase angle and resistance for parallel rlc circuit:"
                        print "resistance from 1st cos function is",imped_mag/cos(phase_angle_1),"Ohms"
                        print "resistance from 2nd cos function is",imped_mag/cos_rad(phase_angle_1),"Ohms"
                        print "resistance from 3rd cos function is",imped_mag/cos_series(phase_angle_1),"Ohms"
                    print "impedance phase angle from 1st arcsin function is",phase_angle_1,"radians or",phase_angle_1*180/pi,"degrees"
                    print "impedance phase angle from 2nd arcsin function is",phase_angle_2,"radians or",phase_angle_2*180/pi,"degrees"
                    print "impedance phase angle from 3rd arcsin function is",phase_angle_3,"radians or",phase_angle_3*180/pi,"degrees"
                    print "impedance phase angle from 4th arcsin function is",phase_angle_4,"radians or",phase_angle_4*180/pi,"degrees"
                else:
                    print "error: reactance/impedance ratio exceeded arcsin domain"
            elif type(net_react)==float:
                phase_angle()
                if type(phase)==float:
                    if series_or_parallel=="1":
                        print "resistance in series rlc circuit:"
                        print "resistance from 1st tan function is",net_react/tan(phase),"Ohms"
                        print "resistance from 2nd tan function is",net_react/tan_rad(phase),"Ohms"
                        print "resistance from 3rd tan function is",net_react/tan_series(phase),"Ohms"
                    elif series_or_parallel=="2":
                        print "resistance in parallel rlc circuit:"
                        print "resistance from 1st tan function is",net_react*tan(phase),"Ohms"
                        print "resistance from 2nd tan function is",net_react*tan_rad(phase),"Ohms"
                        print "resistance from 3rd tan function is",net_react*tan_series(phase),"Ohms"
                else:
                    print "insufficient data"
            elif type(imped_mag)==float and react_processed==False:
                phase_angle()
                if type(phase)==float:
                    if series_or_parallel=="1":
                        print "resistance in series rlc circuit:"
                        print "resistance from 1st cos function is",imped_mag*cos(phase),"Ohms"
                        print "resistance from 2nd cos function is",imped_mag*cos_rad(phase),"Ohms"
                        print "resistance from 3rd cos function is",imped_mag*cos_series(phase),"Ohms"
                    elif series_or_parallel=="2":
                        print "resistance in parallel rlc circuit:"
                        print "resistance from 1st cos function is",imped_mag/cos(phase),"Ohms"
                        print "resistance from 2nd cos function is",imped_mag/cos_rad(phase),"Ohms"
                        print "resistance from 3rd cos function is",imped_mag/cos_series(phase),"Ohms"
                else:
                    print "insufficient data"
            else: 
                print "insufficient data"
        else:
            print "insufficient data"
    elif solve=="3":
        s_or_p()
        if series_or_parallel!="":
            impedance()
            resistance()
            if type(resist)==float and type(imped_mag)==float:
                if abs(resist/imped_mag)<0.995 and series_or_parallel=="1" or series_or_parallel=="2" and abs(imped_mag/resist)<0.995:
                    if series_or_parallel=="1":
                        phase_angle_1=arccos(resist/imped_mag)
                        phase_angle_2=arccos_i(resist/imped_mag)
                        phase_angle_3=arccos_i2(resist/imped_mag)
                        phase_angle_4=new_arccos(resist/imped_mag)
                        print "reactance for series rlc circuit:"
                        print "reactance from 1st sin function is",imped_mag*sin(phase_angle_1),"Ohms"
                        print "reactance from 2nd sin function is",imped_mag*sin_rad(phase_angle_1),"Ohms"
                        print "reactance from 3rd sin function is",imped_mag*sin_series(phase_angle_1),"Ohms"
                    elif series_or_parallel=="2":
                        phase_angle_1=arccos(imped_mag/resist)
                        phase_angle_2=arccos_i(imped_mag/resist)
                        phase_angle_3=arccos_i2(imped_mag/resist)
                        phase_angle_4=new_arccos(imped_mag/resist)
                        print "reactance for parallel rlc circuit:"
                        print "reactance from 1st sin function is",imped_mag/sin(phase_angle_1),"Ohms"
                        print "reactance from 2nd sin function is",imped_mag/sin_rad(phase_angle_1),"Ohms"
                        print "reactance from 3rd sin function is",imped_mag/sin_series(phase_angle_1),"Ohms"
                    print "impedance phase angle from 1st arccos function is",phase_angle_1,"radians or",phase_angle_1*180/pi,"degrees"
                    print "impedance phase angle from 2nd arccos function is",phase_angle_2,"radians or",phase_angle_2*180/pi,"degrees"
                    print "impedance phase angle from 3rd arccos function is",phase_angle_3,"radians or",phase_angle_3*180/pi,"degrees"
                    print "impedance phase angle from 4th arccos function is",phase_angle_4,"radians or",phase_angle_4*180/pi,"degrees"
                else:
                    print "error: resistance/impedance ratio exceeded arccos domain"
            elif type(resist)==float:
                phase_angle()
                if type(phase)==float:
                    if series_or_parallel=="1":
                        print "reactance for series rlc circuit:"
                        print "reactance from 1st tan function is",resist*tan(phase),"Ohms"
                        print "reactance from 2nd tan function is",resist*tan_rad(phase),"Ohms"
                        print "reactance from 3rd tan function is",resist*tan_series(phase),"Ohms"
                    elif series_or_parallel=="2":
                        print "reactance for parallel rlc circuit:"
                        print "reactance from 1st tan function is",resist/tan(phase),"Ohms"
                        print "reactance from 2nd tan function is",resist/tan_rad(phase),"Ohms"
                        print "reactance from 3rd tan function is",resist/tan_series(phase),"Ohms"
                else:
                    print "insufficient data"
            elif type(imped_mag)==float:
                phase_angle()
                if type(phase)==float:
                    if series_or_parallel=="1":
                        print "reactance for series rlc circuit:"
                        print "reactance from 1st sin function is",imped_mag*sin(phase),"Ohms"
                        print "reactance from 2nd sin function is",imped_mag*sin_rad(phase),"Ohms"
                        print "reactance from 3rd sin function is",imped_mag*sin_series(phase),"Ohms"
                    elif series_or_parallel=="2":
                        print "reactance for parallel rlc circuit:"
                        print "reactance from 1st sin function is",imped_mag/sin(phase),"Ohms"
                        print "reactance from 2nd sin function is",imped_mag/sin_rad(phase),"Ohms"
                        print "reactance from 3rd sin function is",imped_mag/sin_series(phase),"Ohms"
                else:
                    print "insufficient data"
            else:
                print "insufficient data"
        else:
            print "insufficient data"
    elif solve=="4":
        volt_or_pow=raw_input("1 for power ratio or 2 for voltage ratio:")
        while volt_or_pow!="1" and volt_or_pow!="2" and volt_or_pow!="":
            print "input error"
            volt_or_pow=raw_input("1 for power ratio or 2 for voltage ratio:")
        if volt_or_pow!="":
            if volt_or_pow=="1":
                log_coeff=10
            elif volt_or_pow=="2":
                log_coeff=20
            input_decibel()
            output_decibel()
            if type(db_input)==float and type(db_output)==float:
                input_impedance()
                output_impedance()
                if type(imped_in)==float and type(imped_out)==float:
                    print "the corrected decibel gain/attenuation from the voltage/power ratio is",log_coeff*log(10,db_output/db_input)+10*log(10,imped_in/imped_out)
                else:
                    print "the decibel gain/attenuation from the voltage/power ratio without impedance mismatch correction for is",log_coeff*log(10,db_output/db_input)
            else:
                print "insufficient data"
        else:
            print "insufficient data"
    if solve!="0":
        solve=raw_input("1: solve for impedance, 2: solve for resistance, 3: solve for reactance, 4: decibel gain/attenuation, 0 to end program:")
    if solve=="0":
        print "program ended"






