"""
JSON XML [Python]
Ejercicio de hackerrank
---------------------------
Autor: Inove Coding School
Version: 1.1
"""

__author__ = "Torres Molina Emmanuel O."
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


import requests
import re
from matplotlib import pyplot as plt


def fetch(page_number, location_id):
    url = 'https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page={}'.format(page_number)
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json().get('data')
        filter_json_response = [{'userId': user.get('userId'), 'amount': user.get('amount')} 
                                for user in json_response if user.get('location').get('id') == location_id]
    
    return filter_json_response
    

def transform (dataset):
    data = []
    user_id_repeat = []
    user_id_not_repeat = []
    amount_id_repeat = 0
    amount = 0

    if dataset != []:  # Pregunto si la lista no está vacía.
        user_id_copy = [user.get('userId') for user in dataset] # Creo una Lista con todos los userId
        for user in dataset:
            if user_id_copy.count(user.get('userId')) > 1:  # Pregunto si el userId está repetido ==> > 1
               amount_id_repeat += float(re.sub(r'[^\d\-.]', '', user.get('amount'))) 
               user_id_repeat = [user.get('userId'), amount_id_repeat]
            else:
                amount = float(re.sub(r'[^\d\-.]', '', user.get('amount'))) 
                user_id_not_repeat.append([user.get('userId'), amount])
    
        if len(user_id_not_repeat) == 1:
            user_id_not_repeat = [user_id_not_repeat[0][0], user_id_not_repeat[0][1]]
        
        if user_id_repeat == []:
            data = user_id_not_repeat
        else:
            if user_id_not_repeat == []:
                data = user_id_repeat
            else: 
                data.extend([user_id_not_repeat, user_id_repeat])

    return data


def transform_2 (dataset):
    data = {}
    
    for user in dataset:
        user_id = user.get('userId')
        amount = float(re.sub(r'[^\d\-.]', '', user.get('amount')))
        accumulated_amount = data.get(user_id)
        if accumulated_amount is not None:
            amount += accumulated_amount
        data[user_id] = amount

        data1 = [key for key in data.keys()]
        data2 = [value for value in data.values()]

    data_user = [[id, amount] for id, amount in zip(data1, data2)]

    return data_user


def report(data, page_number, location_id):
    x = ['user_Id {}'.format(id[0]) for id in data]
    y = [amount[1] for amount in data]

    #Plot:
    fig1 = plt.figure('Figura 1')
    fig1.suptitle('Usuarios y sus Consumos', fontsize=20)
    ax = fig1.add_subplot(1,1,1)
    ax.set_title('Page_Number: {} - Location_Id: {}'.format(page_number, location_id), fontsize=15)
    ax.bar(x, y, color=['darkcyan', 'darkgreen'])
    ax.set_facecolor('lightyellow')
    plt.show()



if __name__ == "__main__":
    page_number = 1
    location_id = 1
    dataset = fetch(page_number, location_id)
    #data = transform(dataset)
    data = transform_2(dataset)
    print(data)
    report(data, page_number, location_id)
    print('\n\n{}\n\n{}\n\n'.format(dataset, data))