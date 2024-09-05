import pandas as pd
from functions import generate_email

#load the Excel file
file_a_df =pd.read_excel('C:/Users/User/PycharmProjects/pythonProject11/ComputerGraphics/data/TestFiles.xlsx')
file_b_df =pd.read_excel('C:/Users/User/PycharmProjects/pythonProject11/ComputerGraphics/data/TestFiles.xlsx')

#generate email
def process_file(df):
    df['Email Address']=df['Student Name'].apply(generate_email)
    return print(df[['Student Name','Email Address']])

print("Processing file_A")
process_file(file_a_df)

print("Processing file_B")
process_file(file_b_df)