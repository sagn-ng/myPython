import pandas as pd
#see the problem leetcode 175
def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    firstName=person['firstName']

    lastName=person['lastName']

    city=[]
    state=[]

    address.set_index('personId', inplace=True)

    for ID in person['personId']:
        if (ID in address.index):
            city.append(address.loc[ID, 'city'])
            state.append(address.loc[ID, 'state'])
        
        else:
            city.append(None)
            state.append(None)

    res=pd.DataFrame({
        'firstName': firstName,
        'lastName': lastName,
        'city': city,
        'state': state
    })

    return res

#example (taken from leetcode):
person=pd.DataFrame({
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
})
person.set_index('personId')
print("The 'person' table before combining:")
print(person)

address=pd.DataFrame({
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
})
address.set_index('addressId')

print("\nThe 'address' table before combining:")
print(address)

print("\nThe result table:")
res=combine_two_tables(person, address)
print(res)