molecule = str(input("Type the organic molecule as SMILES: "))

nCarbons = molecule.count('C')

if nCarbons == 1:
    prefix = 'Met'
elif nCarbons == 2:
    prefix = 'Et'
elif nCarbons == 3:
    prefix = 'Prop'
elif nCarbons == 4:
    prefix = 'But'
elif nCarbons == 5:
    prefix = 'Pent'
elif nCarbons == 6:
    prefix = 'Hex'
elif nCarbons == 7:
    prefix = 'Hept'
elif nCarbons == 8:
    prefix = 'Oct'
    
dbond = molecule.count('=')

if '(C=O)OH' in molecule:
    sufix = 'oic acid'
    dbond = dbond - 1
elif '(C=O)H' in molecule:
    sufix = 'al'
    dbond = dbond - 1
elif 'OH' in molecule:
    sufix = 'ol'
else:
    sufix = 'e'
    
    
if dbond == 0:
    infix = 'an'
elif dbond == 1:
    infix = 'en'
elif dbond == 2:
    infix == 'adien'
    
print(f"The name of the organic compound is {prefix + infix + sufix}")