import random
print('')
print('')
nombre=input('Ingrese su nombre : ')
print('')
pais=['peruano','mexicano','boliviano','venezolano','colombiano','chileno']
print('Tu nombre es '+ nombre +' y eres ' +random.choice(pais)+'.')
#if random.choice(pais)=='peruano' : print('       \nHaha, orgullo peruano')