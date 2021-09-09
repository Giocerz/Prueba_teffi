# -*- coding: utf-8 -*-
import random

def contraAzar():
    valores={0:"k",1:"A",2:"5",3:"@",4:"i",5:"0",
         6:"%", 7:"m", 8:"1", 9:"S"}
    llave=random.randint(0, 9)
    contra=valores[llave]
    for i in range(3):
        llave=random.randint(0, 9)
        contra+=valores[llave]
    return contra    
