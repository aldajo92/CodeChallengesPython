def middle_salary(salaries_raw, case):
    salaries = [int(x) for x in salaries_raw.split(" ")]
    salaries.sort()
    return "Case {}: {}".format(case, salaries[1])


for i in range(int(input())):
    print(middle_salary(input(), i + 1))
