import pandas as pd
#see the problem leetcode 181: employees earning more than their manages
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    emplList=[]

    employee.set_index('id', inplace=True)

    for i in employee.index:
        if (employee['managerId'][i]==None): continue

        t=employee['managerId'][i]
        if (t not in employee.index): continue

        if (employee['salary'][i]>employee['salary'][t]):
            emplList.append(employee['name'][i])
        
    ans=pd.DataFrame({
        'Employee': emplList
    })

    return ans

#example (taken from leetcode)
employee=pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]
})

ans=find_employees(employee)
print(ans)