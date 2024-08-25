import datetime

def get_user_input():
    principal = float(input("Enter the loan amount: "))
    rate = float(input("Enter the annual interest rate (%): "))
    term = int(input("Enter the loan term in years: "))
    return principal, rate, term

def calculate_monthly_payment(principal, annual_rate, term_years):
    monthly_rate = annual_rate / 100 / 12
    total_payments = term_years * 12
    return principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)

def calculate_payoff_date(start_date, term_years):
    return start_date + datetime.timedelta(days=365 * term_years)

def display_results(principal, rate, term, monthly_payment, payoff_date):
    print(f"Loan amount: {principal}")
    print(f"Interest rate: {rate}%")
    print(f"Loan term: {term} years")
    print(f"Monthly payment: {monthly_payment:.2f}")
    print(f"Payoff date: {payoff_date.strftime('%Y-%m-%d')}")

def main():
    principal, rate, term = get_user_input()
    monthly_payment = calculate_monthly_payment(principal, rate, term)
    payoff_date = calculate_payoff_date(datetime.datetime.now(), term)
    display_results(principal, rate, term, monthly_payment, payoff_date)

if __name__ == "__main__":
    main()
