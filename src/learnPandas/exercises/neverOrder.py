import pandas as pd
#see the problem leetcode 183: Customers who never order
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    neverOrderList=[]

    customers.set_index('id', inplace=True)
    for temp in customers.index:
        if (temp not in orders['customerId'].values): #use orders['customerId'] as a reference to check
            neverOrderList.append(customers.loc[temp, 'name'])

    ans=pd.DataFrame({
        'Customers': neverOrderList
    })

    return ans

#example taken from leetcode:
customers=pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
})

orders=pd.DataFrame({
    'id': [1, 2],
    'customerId': [3, 1]
})

ans=find_customers(customers, orders)
print(ans) #Henry and Max