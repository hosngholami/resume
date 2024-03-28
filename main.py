from src.missing_value.load_data import load_data
from src.missing_value.get_missing_value import get_missing_value
from src.missing_value.clean_dataset import clean_dataset
from src.missing_value.remove_missingvalue_name import remove_missingvalue_name
from src.missing_value.remove_missingvalue_sex import remove_missingvalue_sex
from src.missing_value.remove_missingvalue_family import remove_missingvalue_family
from src.missing_value.remove_missingvalue_gpa import remove_missingvalue_gpa
from src.missing_value.remove_missingvalue_level import remove_missingvalue_level
from src.missing_value.remove_missingvalue_experince_of_year import remove_missingvalue_experince_of_year
from src.missing_value.remove_missingvalue_experince import remove_missingvalue_experince
from src.missing_value.remove_missingvalue_education import remove_missingvalue_education


def main():


    ### Missing value ###

    data = load_data()

    missing_value = get_missing_value(data)
    print(missing_value)

    print('****** remove white space ********')

    data = clean_dataset(data)

    missing_value = get_missing_value(data)
    print(missing_value)

    data = remove_missingvalue_name(data)
    data = remove_missingvalue_family(data)
    data = remove_missingvalue_sex(data)
    data = remove_missingvalue_gpa(data)
    data = remove_missingvalue_level(data)
    data = remove_missingvalue_education(data)
    data = remove_missingvalue_experince_of_year(data)
    data = remove_missingvalue_experince(data)

    missing_value = get_missing_value(data)
    print(missing_value)
    



    


if __name__ == '__main__':
    main()