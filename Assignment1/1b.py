inc = float(input("Gross income : "))
num = float(input("Number of dependents : "))

tax_rate = 0.2
std_deduction = 10000
dep_reduction = 3000


deduction = num*dep_reduction
tax = (inc- std_deduction - deduction)*tax_rate

print(tax)
