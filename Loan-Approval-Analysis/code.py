# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank_data = pd.read_csv(path)

#Code starts here
bank = pd.DataFrame(bank_data)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

banks = pd.DataFrame(bank_data)
banks.drop('Loan_ID', inplace=True, axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode()

for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)

print(banks.head(12))
print(banks.shape)

avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc='mean')
print(avg_loan_amount)

a = banks['Self_Employed']=='Yes'
b = banks['Self_Employed']=='No'
c = banks['Loan_Status']=='Y'
Loan_Status_c = 614

loan_approved_se = len(banks[ a & c ])
loan_approved_nse = len(banks[ b & c ])
percentage_se = (loan_approved_se/Loan_Status_c) * 100
percentage_nse = (loan_approved_nse/Loan_Status_c) * 100
print( percentage_se, percentage_nse )

loan_term = banks['Loan_Amount_Term'].apply( lambda x: x/12 )
big_loan_term = loan_term[loan_term >= 25.0]
print(len(big_loan_term))

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values)



