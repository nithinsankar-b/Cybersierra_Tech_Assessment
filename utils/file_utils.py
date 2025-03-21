import pandas as pd

def read_excel_file(file):
    """Read Excel files with appropriate engine"""
    if file.name.endswith('.xlsx'):
        return pd.read_excel(file, engine='openpyxl')
    elif file.name.endswith('.xls'):
        return pd.read_excel(file, engine='xlrd')
    else:
        # For CSV or other file types
        return pd.read_csv(file)