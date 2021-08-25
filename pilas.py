import collections

# Para implementar colas como listas
# agregamos con append, pero retiramos pop(0)
# despues agrego con append y
# retiramos con popleft()
#
# Para implementar pilas con listas
# agregamos con append, pero retiramos con pop
# despues agregamos con append() y
# retiramos con pop

####### Con Deque #######
pila_con_deque = collections.deque()
for _ in range(5):
    pila_con_deque.append(input("Dime el nombre a agregar: "))
    
# Sacar elementos de la pila
while pila_con_deque:
    print(pila_con_deque.pop())