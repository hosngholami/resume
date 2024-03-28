from src.missing_value.load_data import load_data
from src.missing_value.save_file import save_file
import random
def remove_missingvalue_experince(data):

    experince = set(data['مهارت'])
    experince = list(experince)

    for i in range(len(experince)):
        experince[i] = str(experince[i]).replace("\n", "")


    if 'nan' in experince:
        experince.remove('nan')

    if '0' in experince:
        experince.remove('0')

    if '-1' in experince:
        experince.remove('-1')



    index = data[data['مهارت'].isnull()].index
    for i in index:
        rand = random.randint(0, len(experince)-1)
        data.loc[i, 'مهارت'] = experince[rand]


    save_file(data)

    data = load_data()


    return data