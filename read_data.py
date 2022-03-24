import io
from SingleLinkedList import singleLinkedList
class ReadData:
    def __init__(self):
        self.file = open('data.txt','r+')
        self.linkedLi = singleLinkedList()
        self.menu()
    
    def menu(self):
            while True:
                try:
                    option = int(input('\nIngrese la opcion a realizar:\n     ---1.Leer el archivo existente\n     ---2.Añadir lineas al archivo ya existente\n     ---3.Sobreescribir sobre el archivo\n     ---4.Salir de la edicion del archivo a la edicion de nodos\n     >>>'))
                    if option != 1 and option != 2 and option != 3 and option != 4:
                        print('\nLa opcion es incorrecta, intenta de nuevo')
                    elif option == 1 :
                        self.show_file_content_v2()
                        input('\n Pulse enter para continuar')
                    elif option == 2 :
                        self.write_in_file()
                        input('\n Pulse enter para continuar')
                    elif option == 3 :
                        self.overwrite_in_file()
                        input('\n Pulse enter para continuar')
                    elif option == 4 :
                        self.lines_nodes()
                        break
                except ValueError:
                    print("\n     >>>Se espera un valor numerico<<<\n")
            
    
    '''    
    def show_file_content(self):
        with io.open('data.txt','r+', encoding='utf-8') as data_file:
            file_line = data_file.readline()
            while (file_line != ''):
                print(file_line, end='')
                file_line = data_file.readline()
        data_file.close()
    '''
    #Imprimir contenido del texto  
    def show_file_content_v2(self):
        print('El texto es el siguiente :')
        with io.open('data.txt','r+', encoding='utf-8') as data_file:
            for line in data_file.readlines():
                print(line, end='')
        data_file.close()

    
    #Volver todas las lineas a nodos
    def lines_nodes(self):
        with io.open('data.txt','r+', encoding='utf-8') as data_file:
            for line in data_file.readlines():
                new_node = singleLinkedList.Node(line.rstrip('\n'))
                self.linkedLi.add_node_tail(new_node.value)
        data_file.close()
        self.linkedLi.show_nodes_list()
        self.linkedLi.menu2()

    #Escribir una nueva linea en el archivo de texto
    def write_in_file(self):
        line_write = input('\nIngresa el texto que desea añadir al texto: \n     >>>')
        with io.open('data.txt','a',encoding='utf-8') as data_file:
            data_file.write('\n'+ line_write)
        self.file.close()
        self.show_file_content_v2()

    #Sobreescribir en el archivo de texto
    def overwrite_in_file(self):
        line_write = input('\nIngresa lo que desea poner en el archivo : \n     >>>')
        with io.open('data.txt','w',encoding='utf-8') as data_file:
            data_file.write(line_write)
        self.file.close()
        self.show_file_content_v2()