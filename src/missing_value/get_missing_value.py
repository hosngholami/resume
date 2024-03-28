def get_missing_value(data):

    missing_Value = data.isnull().sum()

    return missing_Value