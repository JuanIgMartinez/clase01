# Juan I. Martinez, Número de legajo 57018


def roman_to_decimal(roman_number):
    decimal_number = 0
    ant = ''
    #import ipdb; ipdb.set_trace()          #instalar la libreria para probar esto
    for letter in roman_number:
        if letter == "I":
            decimal_number += 1
    
        elif letter == "V":
            decimal_number += 5
            if ant == 'I':
                decimal_number -= 2

        elif letter == "X":
            decimal_number += 10
            if ant == 'I':
                decimal_number -= 2

        elif letter == "L":
            decimal_number += 50
            if ant == 'X':
                decimal_number -= 20

        elif letter == "C":
            decimal_number += 100
            if ant == 'X':
                decimal_number -= 20

        elif letter == "D":
            decimal_number += 500
            if ant == 'C':
                decimal_number -= 200           

        elif letter == "M":
            decimal_number += 1000
            if ant == 'C':
                decimal_number -= 200 

        ant = letter
        
    return decimal_number



