import csv
import locale

class Departments:

    department: str
    actual_spent: int

    def __init__(self, department, actual_spent):
        self.department = department
        self.actual_spent = actual_spent

class Parse:

    def parse(self, fileName):
        audit = []

        with open(fileName, "r") as file:

            expenditures = csv.reader(file, delimiter=",")
            next(expenditures)

            for row in expenditures:
                dept_spending = Departments(row[0], row[3])
                audit.append(dept_spending)
        
        return(audit)

parse = Parse()
seattle_audit = parse.parse("city-of-seattle-2012-expenditures-dollars.csv")
# for dept_spending in seattle_audit:
#     print(dept_spending.department, dept_spending.actual_spent)

department_spending = {}
for item in seattle_audit:
    department = item.department
    actual_spent = int(item.actual_spent or 0)

    if not department:
        continue

    if department in department_spending:
        department_spending[department] += actual_spent
    else:
        department_spending[department] = actual_spent

locale.setlocale(locale.LC_ALL, 'C')

def format_currency(amount):
    return '${:,.2f}'.format(amount)

complete_total = 0

for department, spending in department_spending.items():
    total_spent = format_currency(spending)
    complete_total += spending
    print(department, total_spent)
print("City of Seattle total 2012 spending: " + format_currency(complete_total))
print("-----Audit Complete-----")




