#!/usr/bin/env python
'''
JSON XML [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Torres Molina Emmanuel O."
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


import json
import requests
from matplotlib import pyplot as plt
import xml.etree.ElementTree as ET


def obt_titulos_completados (data, nro_user):
    titles_completed = [id.get('completed') for id in data if id.get('userId') == nro_user 
                        and id.get('completed') is True]

    return titles_completed


def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado
    
    json_data = {
                    'Nombre': 'Emmanuel Oscar',
                    'Apellido': 'Torres Molina',
                    'DNI': 38404200,
                    'Vestimenta': [
                                    {
                                        'prenda': 'zapatillas',
                                        'cantidad': 6
                                    },
                                    {
                                        'prenda': 'remeras',
                                        'cantidad': 15
                                    },
                                    {
                                        'prenda': 'pantalones',
                                        'cantidad': 18
                                    },
                                    {
                                        'prenda': 'camisas',
                                        'cantidad': 10
                                    }
                    ]

    }

    print('\nImprimo el objeto JSON como un diccionario:\n\n{}\n\n'.format(json_data))
    json_data_string = json.dumps(json_data, indent=4)
    print('Imprimo el Objeto JSON:\n\n{}\n\n'.format(json_data_string))

    with open('data.json', 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)


def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1
    
    with open('data.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)

    print('\nImprimo el objeto JSON como un diccionario ==> JSON Deserialize:\n\n{}\n\n'.format(json_data))
    json_data_string = json.dumps(json_data, indent=4)
    print('Imprimo el Objeto JSON Serialize:\n\n{}\n\n'.format(json_data_string))


def ej3():
    # Ejercicio de XML
    # Basado en la estructura de datos del ejercicio 1,
    # crear a mano un archivo ".xml" y generar una estructura
    # lo más parecida al ejercicio 1.
    # El objectivo es que armen un archivo XML al menos
    # una vez para que entiendan como funciona.
    pass

    # Archivo: datos_personales.xml


def ej4():
    # XML Parser
    # Tomar el archivo realizado en el punto anterior
    # e iterar todas las tags del archivo e imprimirlas
    # en pantalla tal como se realizó en el ejemplo de clase.
    # El objectivo es que comprueben que el archivo se realizó
    # correctamente, si la momento de llamar al ElementTree
    # Python lanza algún error, es porque hay problemas en el archivo.
    # Preseten atención al número de fila y al mensaje de error
    # para entender que puede estar mal en el archivo.
    
    print('\n\n')
    
    tree = ET.parse('datos_personales.xml')
    root = tree.getroot() # Obtengo la Etiqueta de Mayor Jerarquía.

    # Recorro el root:
    for child in root:
        print('Tag:', child.tag, 'Attrib:', child.attrib, 'Text:', child.text)
        for child2 in child:
            print('Tag:', child2.tag, 'Attrib:', child2.attrib, 'Text:', child2.text)

    print('\n\n')

def ej5():
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    response = requests.get(url)
    if response.status_code == 200:
        # Una forma de hacerlo:
        #data = json.loads(response.text)

        # Otra Forma:
        data = response.json()
        json_data = json.dumps(data, indent=4)
        print('Objeto JSON Obtenido de la URL: "{}"\n\n{}\n\n'.format(url, json_data))
        
        users = ['User '+str(nro_user) for nro_user in range(1, 11)]
        user_id_titles = [obt_titulos_completados(data, user) for user in range(1, 11)]
        cant_titulos_completados = [int(sum(user)) for user in user_id_titles]

        # Plot:
        fig1 = plt.figure('Figura 1')
        fig1.suptitle('Títulos de Libros Leídos por Usuarios')
        ax = fig1.add_subplot(1,1,1)
        ax.pie(cant_titulos_completados, labels=users, shadow=True, autopct='%1.2f%%', startangle=90)
        ax.axis('equal')
        plt.show()


if __name__ == '__main__':
    print("\n\nBienvenidos a otra clase de Inove con Python\n\n")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
