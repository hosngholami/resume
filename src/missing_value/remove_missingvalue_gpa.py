from src.missing_value.save_file import save_file
from src.missing_value.load_data import load_data

def remove_missingvalue_gpa(data):
    data['معدل'].fillna(data['معدل'].mean(), inplace=True)
    save_file(data)

    data = load_data()

    return data