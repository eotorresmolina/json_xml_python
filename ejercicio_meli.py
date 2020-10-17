"""
JSON XML [Python]
Ejercicio de MELI
---------------------------
Autor: Inove Coding School
Version: 1.1
"""

__author__ = "Torres Molina Emmanuel O."
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


import requests
from matplotlib import pyplot as plt


def fetch (ciudad):
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20{}%20&limit=50'.format(ciudad)

    response = requests.get(url)
    if response.status_code == 200:
        dataset = response.json().get('results')
        filter_json_response = [{'price': dpto.get('price'), 'condition': dpto.get('condition')} 
                    for dpto in dataset if dpto.get('currency_id') == 'ARS']
    return filter_json_response


def transform (dataset, min, max):
    
    dpto_min = [int(dpto.get('price')) for dpto in dataset if dpto.get('price') < min]
    dpto_min_max = [int(dpto.get('price')) for dpto in dataset if min<=dpto.get('price')<=max]
    dpto_max = [int(dpto.get('price')) for dpto in dataset if dpto.get('price') > max]

    min_count = len(dpto_min)
    min_max_count = len(dpto_min_max)
    max_count = len(dpto_max)

    return [min_count, min_max_count, max_count]


def report (data, ciudad):
    data.sort()
    explode = [0.0, 0.0, 0.1]

    fig = plt.figure('Figura 1')
    fig.suptitle('Porcentaje de Alquileres en {} Según el Rango de Precio:'.format(ciudad), fontsize=18)
    ax = fig.add_subplot(1,1,1)
    ax.pie(data, labels=['Alquileres < Mín', 'Mín <= Alquileres <= Máx', 'Alquileres > Máx'],
            shadow=True, autopct='%1.2f%%', explode=explode, startangle=90)
    ax.axis('equal')
    plt.show()



if __name__ == "__main__":
    
    ciudad = 'Mendoza'
    min = 2500
    max = 10000
    dataset = fetch(ciudad)
    data = transform(dataset, min, max)
    #print('\n\n{}\n\n'.format(data))
    report(data, ciudad)