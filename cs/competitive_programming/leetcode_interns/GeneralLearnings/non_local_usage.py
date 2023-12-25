#!/usr/bin/python3


def func1():
    murali,adi = 0,0
    def func2():
        nonlocal murali
        
        murali = 30+6
        adi = 30+6
    
    func2()
    return murali,adi

murali,adi = func1()
print("murali is {}".format(murali))
print("adi is {}".format(adi))

#ANSWER - good usuage of non local
"""
murali is 36
adi is 0
"""