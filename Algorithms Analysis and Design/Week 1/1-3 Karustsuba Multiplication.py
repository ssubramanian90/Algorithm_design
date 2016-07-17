"""Karatsuba Multiplication"""




def karatsuba(anumber1, anumber2):
        
        length1=len(str(anumber1))
        length2=len(str(anumber2))
        if length1==1 and length2==1:
                return anumber1*anumber 2
        else:
                maxlen=max(length1, length2)
                a=anumber1/(10**(maxlen/2))
                b=anumber1%(10**(maxlen/2))
                c=anumber2/(10**(maxlen/2))
                d=anumber2%(10**(maxlen/2))
                step1=karatsuba(a,c)
                step2=karatsuba(b,d)
                step3=karatsuba(a+b,c+d)
                step4=step3-step1-step2
                product=step1*(10**(maxlen*2))+step2+step4*(10**maxlen)
        return product

