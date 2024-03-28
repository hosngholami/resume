from src.missing_value.load_data import load_data
from src.missing_value.save_file import save_file

def clean_dataset(data):
    import re
    pattern = r"\A\s*\Z" ## پیدا کردن سطر هایی که فقط space ذخیره شده اند
    for i in range(len(data)-1):

        if (re.search(pattern ,str(data.loc[i, 'نام'])) != None ):
            data.loc[i, 'نام'] = re.sub(re.compile(pattern), '', data.loc[i, 'نام'])
            
        if (re.search(pattern ,str(data.loc[i, 'نام خانوادگی'])) != None ):
            data.loc[i, 'نام خانوادگی'] = re.sub(re.compile(pattern), '', data.loc[i, 'نام خانوادگی'])
            
        if (re.search(pattern ,str(data.loc[i, 'آدرس'])) != None ):
            data.loc[i, 'آدرس'] = re.sub(re.compile(pattern), '', data.loc[i, 'آدرس'])

        if (re.search(pattern ,str(data.loc[i, 'جنسیت'])) != None ):
            data.loc[i, 'جنسیت'] = re.sub(re.compile(pattern), '', data.loc[i, 'جنسیت'])

        if (re.search(pattern ,str(data.loc[i, 'معدل'])) != None ):
            data.loc[i, 'معدل'] = re.sub(re.compile(pattern), '', data.loc[i, 'معدل'])

        if (re.search(pattern ,str(data.loc[i, 'مقطع تحصیلی'])) != None ):
            data.loc[i, 'مقطع تحصیلی'] = re.sub(re.compile(pattern), '', data.loc[i, 'مقطع تحصیلی'])
        
        if (re.search(pattern ,str(data.loc[i, 'رشته تحصیلی'])) != None ):
            data.loc[i, 'رشته تحصیلی'] = re.sub(re.compile(pattern), '', data.loc[i, 'رشته تحصیلی'])

        if (re.search(pattern ,str(data.loc[i, 'سن'])) != None ):
            data.loc[i, 'سن'] = re.sub(re.compile(pattern), '', data.loc[i, 'سن'])
        
        if (re.search(pattern ,str(data.loc[i, 'مهارت'])) != None ):
            data.loc[i, 'مهارت'] = re.sub(re.compile(pattern), '', data.loc[i, 'مهارت'])

        if (re.search(pattern ,str(data.loc[i, 'تجربه کاری(به سال)'])) != None ):
            data.loc[i, 'تجربه کاری(به سال)'] = re.sub(re.compile(pattern), '', data.loc[i, 'تجربه کاری(به سال)'])
    # write chnages to csv file
    print(save_file(data))
    
    data = load_data()
    return data