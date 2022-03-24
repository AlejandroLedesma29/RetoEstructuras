import io
class singleLinkedList:
    #Creamos una clase anidada
    
    class Node:
        #Creamos el inicializador
         
        def __init__ (self, value):
            #Definimos la estructura de nodo 
            self.value = value
            self.next_node = None

    #Metodo inicializador de la clase SingleLinkedList        
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    
    def menu2(self):
        while True:
            option = int(input('\nIngrese la opcion a realizar:\n     ---1.Insertar un nuevo nodo\n     ---2.Eliminar un nodo\n     ---3.Consultar el valor de un nodo en especifico\n     ---4.Editar el valor de un nodo existente en la lista\n     ---5.Invertir el contenido de la lista\n     ---6.Vaciar la lista\n     ---7.Salir del sistema\n     >>>'))
            if option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 6 and option != 7:
                print('La opcion es incorrecta, intenta de nuevo')
            elif option == 1 :
                while True:
                    try:
                        option1 = int(input('\nIngrese donde desea insertar el nodo:\n     ---1.Al inicio\n     ---2.Al final\n     ---3.En una posición específica\n     >>>'))
                        if option1 != 1 and option1 != 2 and option1 != 3 :
                            print('\nLa opcion es incorrecta, intenta de nuevo')
                        elif option1 == 1 :
                            valor = str(input('Ingrese el valor del nuevo nodo\n     >>>'))
                            self.add_node_head(valor)
                            self.show_nodes_list()
                            self.update_txt()
                            input('\n Pulse enter para continuar')
                            break
                        elif option1 == 2 :
                            valor = str(input('Ingrese el valor del nuevo nodo\n     >>>'))
                            self.add_node_tail(valor)
                            self.show_nodes_list()
                            self.update_txt()
                            input('\n Pulse enter para continuar')
                            break
                        elif option1 == 3 :
                            valor = str(input('Ingrese el valor del nuevo nodo\n     >>>'))
                            while True:
                                try:
                                    indice = int(input('Ingrese el indice del nuevo nodo\n     >>>'))
                                    if indice <= 0 and indice > self.length-1 :
                                        print('El indice no esta en el rango de longitud de la lista\n')
                                    else :
                                        break
                                except ValueError:
                                    print('Se esperaba un numero\n')
                            self.insert(indice,valor)
                            self.update_txt()
                            self.show_nodes_list()
                            input('\n Pulse enter para continuar')
                            break
                    except ValueError:
                        print("\n     >>>Se espera un valor numerico<<<\n")
                        input('\n Pulse enter para continuar')
            elif option == 2 :
                while True:
                    try:
                        option1 = int(input('\nIngrese donde desea eliminar el nodo:\n     ---1.Al inicio\n     ---2.Al final\n     ---3.En una posición específica\n     >>>'))
                        if option1 != 1 and option1 != 2 and option1 != 3 :
                            print('\nLa opcion es incorrecta, intenta de nuevo')
                        elif option1 == 1 :
                            self.delete_node_head()
                            self.show_nodes_list()
                            self.update_txt()
                            input('\n Pulse enter para continuar')
                            break
                        elif option1 == 2 :
                            self.delete_node_tail()
                            self.show_nodes_list()
                            self.update_txt()
                            input('\n Pulse enter para continuar')
                            break
                        elif option1 == 3 :
                            while True:
                                try:
                                    indice = int(input('Ingrese el indice del nodo a eliminar\n     >>>'))
                                    if indice <= 1 and indice > self.length() :
                                        print('El indice no esta en el rango de longitud de la lista')
                                    else :
                                        break
                                except ValueError:
                                    print('Se esperaba un numero\n')
                            self.remove(indice)
                            self.update_txt()
                            self.show_nodes_list()
                            input('\n Pulse enter para continuar')
                            break
                    except ValueError:
                        print("\n     >>>Se espera un valor numerico<<<\n")
                        input('\n Pulse enter para continuar')
            elif option == 3 :
                while True:
                    try:
                        indice = int(input('Ingrese el indice del nodo que desea saber su valor\n     >>>'))
                        if indice <= 1 or indice > self.length :
                            print('El indice no esta en el rango de longitud de la lista\n')
                        else :
                            break
                    except ValueError:
                        print('Se esperaba un numero\n')
                        
                print(f'El valor del nodo es\n        '+(self.get(indice-1).value))
                input('\n Pulse enter para continuar')
            
            elif option == 4 :
                valor = str(input('Ingrese el nuevo valor del nodo\n     >>>'))
                while True:
                    try:
                        indice = int(input('Ingrese el indice del nodo a actualizar\n     >>>'))
                        if indice <= 0 or indice > self.length :
                            print('El indice no esta en el rango de longitud de la lista\n')
                        else:
                            break
                    except ValueError:
                        print('Se esperaba un numero\n')
                self.update(indice,valor)
                self.update_txt()
                self.show_nodes_list()
                input('\n Pulse enter para continuar')

            elif option == 5 :
                self.reverse()
                self.show_nodes_list()
                input('\n Pulse enter para continuar')
            
            elif option == 6 :
                self.empty_list()
                self.show_nodes_list()
                self.update_txt()
                input('\n Pulse enter para continuar')
            elif option == 7:
                print('\nAsi quedo la lista de nodos finalmente')
                self.show_nodes_list()
                print('\nAdios :) <3')
                break
            else:
                print('Se esperaba un valor numerico')
        
    def show_nodes_list(self):
        print('\n')
        node_list = []
        current_node = self.head
        #Recoremos la lista hasta que no existan nodos
        while (current_node != None):
            #A la lista node_list le agregamos al final el value del nodo visitado
            node_list.append(current_node.value)
            current_node = current_node.next_node
        print(f"{node_list} La cantidad de nodos es :{self.length}")
    
    def update_txt(self):
        node_list = []
        current_node = self.head
        while (current_node != None):
            node_list.append(current_node.value)
            current_node = current_node.next_node
        for item in range(len(node_list)):
            if item != len(node_list)-1:
                node_list[item] = node_list[item]+'\n'
        data_file = io.open('data.txt','w',encoding='utf-8')
        if len(node_list) == 0:
            data_file.write('')
        data_file.writelines(node_list)
        data_file.close
    
    
    #Metodo que agrega un nodo nuevo al inicio de la lista
    def add_node_head (self, value):
        new_node = self.Node(value)
        #Conslutar si la lista no tiene head y tail
        if self.head == None and self.tail==None:
            #En este caso la lista esta vacia, no contiene nodos
            self.head = new_node
            self.tail = new_node
        else:
            #En este caso, la lista contiene almenos un nodo
            #Para este caso habria que enlazar el nodo nuevo con la cabeza de la lista
            new_node.next_node = self.head
            #Actuaizar la cabeza de la lista
            self.head = new_node
        self.length+=1
    
    #Metodo que agrega un nodo nuevo al final de la lista
    def add_node_tail (self, value):
        new_node = self.Node(value)
        #Conslutar si la lista no tiene head y cola
        if self.head == None and self.tail==None:
            #En este caso la lista esta vacia, no contiene nodos
            self.head = new_node
            self.tail = new_node
        else:
            #En este caso, la lista contiene almenos un nodo
            #Para este caso habria que enlazar el nodo nuevo con la cola de la lista
            self.tail.next_node = new_node
            #Actuaizar la cabeza de la lista
            self.tail = new_node
        self.length+=1
        
    #Eliminar primer nodo de la lista
    def delete_node_head(self):
        if self.length == 0 :
            self.head = None
            self.tail = None
        else :
            #Eliminar la cabeza de la lista
            remove_node = self.head
            #El nodo que seguia sera la cabeza
            self.head = remove_node.next_node
            #Eliminamos el enlace del nodo con la lista
            remove_node.next_node = None
            self.length-=1
            print(f"El valor del nodo eliminado es {remove_node.value}")
    
    #Eliminamos el ultimo nodo de la lista 
    def delete_node_tail(self):
        if self.length == 0 :
            self.head = None
            self.tail = None
        else :
            #Eliminar la cola de la lista
            current_node = self.head
            #El nodo anterior seria la cola
            new_tail = current_node
            while (current_node.next_node != None):
                new_tail = current_node
                current_node = current_node.next_node
            self.tail = new_tail
            self.tail.next_node = None            
            self.length-=1
            print(f"El valor del nodo eliminado es {current_node.value}")
    
    # Consultar el value de determinado nodo       
    def get(self, index):
        # Obtiene un nodo dado un index
        # Si el indice es el último nodo de la lista, nos referimos a la cola
        if index == self.length - 1:
            #print(self.tail.value)
            return self.tail
        #Si el indice es el primer value de la lista, devolvemos el value de la cabeza
        elif index == 0:
            #print(self.head.value)
            return self.head
        #De lo contrario, es porque el indice esta en una posición intermedia de la lista
        #Validar que el indice se encuentre entre los rangos permitidos de la lista
        elif not (index >= self.length or index < 0):
            current_node = self.head
            contador = 0
            #Recorremos la lista siempre y cuando el contador sea diferente al nodo a buscar
            while contador != index:
                #Incrementamos en uno el while pasando a visitar el siguiente nodo
                current_node = current_node.next_node
                contador  += 1
            #print(current_node.value)
            return current_node
        else:
            return None
        
        
    #Método que nos permite actualizar el valor del nodo
    def update (self,index,value):
        index = index-1
        #Cambia el value de un nodo dado un index
        nodo_objetivo = self.get(index)
        if nodo_objetivo != None:
            #Reemplazamos el valor actual del nodo por el suministrado por el usuario
            nodo_objetivo.value = value
        else: 
            return None 
        
        
    # Agrega un elemento en donde sea en la linkedlist dado el index
    def insert(self, index, value):
        #Siempre que se desee crear un nuevo nodo es necesario solicitar el valor
        #Si el usuario quiere añadir el nodo al final de la lista, se llama la función append_node()
        if index == self.length + 1:
            return self.add_node_tail(value)
        #Se valida si el nodo se quiere insertar en la cabeza de la lista
        elif index == 1:
            return self.add_node_head(value)
        #Se valida si el indice esta entre los rangos de la lista
        elif not (index >= self.length+1 or index <= 0):
            new_node = self.Node(value)
            previous_node = self.get(index-2)
            nodos_siguientes = previous_node.next_node
            #Generamos los enlaces del nuevo nodo con el anterior y el siguiente
            previous_node.next_node = new_node
            new_node.next_node = nodos_siguientes
            self.length += 1
        else:
            return None
        
    #Eliminar un nodo de una posicion en especifico   
    def remove (self, index):
        if index == self.length:
            return self.delete_node_tail()
        elif index == 1:
            return self.delete_node_head()
        elif not(index >= self.length or index <0) :
            nodos_anteriores = self.get(index-2)
            node_remove = nodos_anteriores.next_node
            nodos_anteriores.next_node = node_remove.next_node
            node_remove.next_node = None
            self.length -=1
        else:
            return None  
    
    #Poner la lista al reves
    def reverse (self):
        reverse_nodes = None
        current_node = self.head
        self.tail = current_node
        while (current_node != None):
            next_node = current_node.next_node
            current_node.next_node = reverse_nodes
            reverse_nodes = current_node
            current_node = next_node
        self.head = reverse_nodes
        return self.head
    
    #Vaciar lista
    def empty_list(self):
        self.head = None
        self.tail = None
        self.length = 0
        
        
    