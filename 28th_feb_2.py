"""
Calculate income tax for the given income by adhering to the below rules
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.

"""

def TaxCalculation(Amount):
    tax_amount = 0
    Tax_amount = 0
    Tax_amount_total = 0
    if Amount < 10000:
        tax_amount = tax_amount
    elif Amount >= 10000 and Amount <= 20000:
            tax_amount = 0.1*Amount
            print (tax_amount)
    else:
        if Amount > 20000:
            tax_amount = 0.1* 10000
            Tax_amount = (Amount - 20000)*0.2
            Tax_amount_total = tax_amount + Tax_amount

            print("Tax is ", Tax_amount_total)






if __name__ == '__main__':

    Amount = input("Input the gross amount for tax collection: ")
    Amount = int(Amount)

    TaxCalculation(Amount)