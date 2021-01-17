# Import pathlib
from pathlib import Path

# Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    csvpath = Path('../data/qualifying_loans.csv')  #data/qualifying_loans.csv
    bank_data = []
    header = []
    fileio.save_csv(csvpath, bank_data, header)
    assert csvpath.exists() == True

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    csvpath = Path('../data/daily_rate_sheet.csv') #data/daily_rate_sheet.csv
    bank_data = fileio.load_csv(csvpath)
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84
    
    filtered_bank_data = max_loan_size.filter_max_loan_size(loan, bank_data)
    filtered_bank_data = credit_score.filter_credit_score(current_credit_score, filtered_bank_data)
    filtered_bank_data = debt_to_income.filter_debt_to_income(monthly_debt_ratio, filtered_bank_data)
    filtered_bank_data = loan_to_value.filter_loan_to_value(loan_to_value_ratio, filtered_bank_data)

    assert len(filtered_bank_data) == 6

# Test the new save_csv code!
test_save_csv()