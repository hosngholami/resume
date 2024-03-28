from src.missing_value.save_file import save_file
from src.missing_value.load_data import load_data
import random

def remove_missingvalue_education(data):

    educations = set(data['رشته تحصیلی'])
    educations = list(educations)

    ## حذف داده های اضافی

    for i in range(len(educations)):
        educations[i] = str(educations[i]).replace("\n", "")
        educations[i] = str(educations[i]).replace("\u200c", "")


    if '0' in educations:
        educations.remove('0')

    if '-1' in educations:
        educations.remove('-1')

    ## اندیس سظر هایی که مقدار خالی دارند
    indexs = data[data['رشته تحصیلی'].isnull()].index

    ## مقداردهی سطر های خالی به صورت تصادقی از لیست تحصیلات
    for i in indexs:
        rand = random.randint(0, len(educations)-1)
        data.loc[i, 'رشته تحصیلی'] = educations[rand]


    save_file(data)


    data = load_data()

    return data