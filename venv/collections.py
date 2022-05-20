

from models import container 
from asyncio import FastChildWatcher


def generate_test_cases():
    test_1=[True,False,False,False]
    test_2=[False,True,False,False]
    test_3=[False,False,True,False]
    test_4=[False,False,False,True]
    test_cases=[test_1,test_2,test_3,test_4]

    return test_cases



def generate_default_shakers():
    shaker_1= container.Shaker("Sugar")
    shaker_2= container.Shaker("Sugar")
    shaker_3= container.Shaker("Salt")
    shaker_4= container.Shaker("Sugar")
    shakers=[shaker_1,shaker_2,shaker_3,shaker_4]
    return shakers
    test_cases=generate_test_cases()
    def print_senario(shakers):
        for shaker in shakers:
            print(shaker)




