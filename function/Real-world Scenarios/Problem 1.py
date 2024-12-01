# Write a function that takes a list of employee salaries and calculates the average salary.

def avg_salary(salaries):
    if not salaries:
        return 0
    return sum(salaries) / len(salaries)

salaries = [50000, 60000, 55000, 70000, 65000]
avg = avg_salary(salaries)
print(f"Average salary: {avg}")