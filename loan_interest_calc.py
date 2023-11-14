def main():
    print("Monthly loan payment calculator ")
    print("")


    principal = float(input("Enter the loan amount: "))
    interest = float(input("Enter annual interest rate: "))
    years = int(input("Enter the number of years: "))


    monthly_interest_rate = interest / 1200
    number_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_of_months))



    print("The monthly payment for this loan is: %.2f " % monthly_payment)

main()