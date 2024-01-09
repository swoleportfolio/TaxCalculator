# Step 1: Get Input
wages = int(input("Enter wages: "))
taxable_interest = int(input("Enter taxable interest: "))
unemployment_compensation = int(input("Enter unemployment compensation: "))
status = int(input("Enter status (1 for single, 2 for married): "))
taxes_withheld = int(input("Enter taxes withheld: "))

# Step 2: Combine for AGI
agi = wages + taxable_interest + unemployment_compensation

# AGI max threshold
if agi > 120_000:
    print("Error: AGI is above $120,000")
    exit()

# step 3: Get a deduction Amount
if status == 1:  # Single
    deduction = 12_000
else:
    deduction = 24_000  #Married

# Calculate taxable income
taxable_income = agi - deduction

# Set taxable income to zero when its negative
if taxable_income < 0:
    taxable_income = 0

# Step4 calculate taxable income
if status == 1:  # Single
    if taxable_income <= 10_000:
        tax = taxable_income * 0.10
    elif taxable_income <= 40_000:
        tax = 1_000 + (taxable_income - 10_000) * 0.11
    elif taxable_income <= 85_000:
        tax = 4_600 + (taxable_income - 40_000) * 0.21
    else:
        tax = 14_500 + (taxable_income - 85_000) * 0.25
else:  # Married
    if taxable_income <= 20_000:
        tax = taxable_income * 0.10
    elif taxable_income <= 80_000:
        tax = 2_000 + (taxable_income - 20_000) * 0.11
    else:
        tax = 9_200 + (taxable_income - 80_000) * 0.21


tax = round(tax)

#Step 5: calculate Tax Due or Refund
tax_due_or_refund = tax - taxes_withheld

# output
print(f"Deduction: ${deduction:,}")
print(f"Taxable Income: ${taxable_income:,}")
print(f"Tax: ${tax:,}")
print(f"Tax Due or Refund: ${abs(tax_due_or_refund):,}")