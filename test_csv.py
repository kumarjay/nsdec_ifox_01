import pandas as pd

# dict = {'name':['Jay'],
#         'enrollment':['dmk']}
#
# df1 = pd.DataFrame(dict)

# data = pd.read_csv('enrollments.csv')
#
# print(data.head())
# df2 = {'name': ['Anup'],
#        'enrollment': ['DME/5442']}
#
# df2 = pd.DataFrame(df2)
#
# data = [data, df2]
# data = pd.concat(data, axis=0, ignore_index=True)
#
# print(data.head())
# data.to_csv('enrollments.csv', index=False)


def get_name_enrollment(name, enrollment):
    data = pd.read_csv('enrollments.csv')
    # print(data.shape)
    entry = False
    branch = False
    year = False
    for ind in range(data.shape[0]):
        if data.iloc[ind]['name'].upper() == name.upper() and data.iloc[ind]['enrollment'] == enrollment:
            # entry = True
            branch = data.iloc[ind]['branch']
            year = data.iloc[ind]['year']
    print(branch, '  ', year)
    return branch, year

# get_name_enrollment('aa', 'bb')