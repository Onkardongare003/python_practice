    # Tax is charged on the annual salary on the following basis
    # Income <300000 → no tax
    # Income between 3 lacs and 5 lacs → 10% of the amount exceeding 3 lacs
    # Income between 5 lacs and 7 lacs  → 20% of the amount exceeding 5 lacs+10000
    # if(salary>=500000 and salary<700000):
    # Income above 7 lacs → 30% of amount exceeding 7 lacs+25000






salary = int(input("Enter Your Salary = "))

if salary <= 300000:
    print("No Tax")

elif salary < 500000:
    tax = (salary - 300000) * 10 / 100
    print("Your Tax is =", tax)
