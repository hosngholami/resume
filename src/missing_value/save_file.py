def save_file(data):
    file_name = "data/resume.csv"
    try:
        data.to_csv(file_name)
    except:
        return "ذخیره با خطا مواجه شد"
    
    else:
        return "با موفقیت ذخیره شده"