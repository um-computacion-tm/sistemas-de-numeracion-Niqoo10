#SISTEMA DE NUMERACIÓN DE DECIMAL A BINARIO

def decimal_a_binario(decimal):
    return bin(decimal)[2:]

#SISTEMA DE NUMERACIÓN DE BINARIO A DECIMAL

def binario_a_decimal(binario):
    return int(binario, 2)
