from src.missing_value.save_file import save_file
from src.missing_value.load_data import load_data



def remove_missingvalue_experince_of_year(data):
    data['تجربه کاری(به سال)'].fillna(data['تجربه کاری(به سال)'].mean(), inplace=True)

    save_file(data)

    data = load_data()

    return data