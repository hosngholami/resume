import random
from src.missing_value.save_file import save_file
from src.missing_value.load_data import load_data
def remove_missingvalue_level(data):

    ## گرفتن لیست مقطع تحصیلی و حذف موارد اضافی
    condition =  {'-1', '0', 'ندارد', None}
    education = ['سیکل', 'دیپلم', 'کاردانی', 'فوق دیپلم', 'لیسانس', 'کارشناسی', 'فوق لیسانس', 'کارشناسی ارشد', 'دکترا', 'فوق دکترا']
    index = data[data['مقطع تحصیلی'].isnull()].index

    for i in index:
        
        age = data.loc[i, 'سن']

        if (age > 30):
            rand = random.randint(0, len(education)-1)    
            data.loc[i, 'مقطع تحصیلی'] = education[rand]

        elif (age > 25):
            rand = random.randint(0, 7)
            data.loc[i, 'مقطع تحصیلی'] = education[rand]

        elif (age > 20):
            rand = random.randint(0, 5)
            data.loc[i, 'مقطع تحصیلی'] = education[rand]
        else:
            rand = random.randint(0, 1)
            data.loc[i, 'مقطع تحصیلی'] = education[rand]


    save_file(data)
    data = load_data()

    return data
        

    

