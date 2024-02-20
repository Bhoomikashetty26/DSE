import pandas as pd
data={
    'name':['john','emma','sam','lisa','tom'],
    'age':[25,30,28,32,27],
    'country':['usa','canada','australia','uk','german'],
    'salary':[50000,60000,55000,70000,52000]
}
df=pd.DataFrame(data)
print("original data frame")
print(df)
name_age=df[['name','age']]
print("\n name and age column")
print(name_age)
filtered_df=df[df['country']=='usa']
print("\n filtered  DataFrame(country='usa'):")
print(filtered_df)
sorted_df=df.sort_values('salary',ascending=False)
print("\n sorted DataFrame(by salary in descending order)")
print(sorted_df)
average_salary=df['salary'].mean()
print("\n average salary",average_salary)
df['experience']=[3,6,4,8,5]
print("\n DataFrame with added experiece column:")
print(df)
df.loc[df['name']=='emma','salary']=65000
print("\n data frame  after updating emmas salary:")
print(df)
df=df.drop('experience',axis=1)
print("\n data frame after deleting experience column:")
print(df)
#OUTPUT
# original data frame
#    name  age    country  salary
# 0  john   25        usa   50000
# 1  emma   30     canada   60000
# 2   sam   28  australia   55000
# 3  lisa   32         uk   70000
# 4   tom   27     german   52000

#  name and age column
#    name  age
# 0  john   25
# 1  emma   30
# 2   sam   28
# 3  lisa   32
# 4   tom   27

#  filtered  DataFrame(country='usa'):
#    name  age country  salary
# 0  john   25     usa   50000

#  sorted DataFrame(by salary in descending order)
#    name  age    country  salary
# 3  lisa   32         uk   70000
# 1  emma   30     canada   60000
# 2   sam   28  australia   55000
# 4   tom   27     german   52000
# 0  john   25        usa   50000

#  average salary 57400.0

#  DataFrame with added experiece column:
#    name  age    country  salary  experience
# 0  john   25        usa   50000           3
# 1  emma   30     canada   60000           6
# 2   sam   28  australia   55000           4
# 3  lisa   32         uk   70000           8
# 4   tom   27     german   52000           5

#  data frame  after updating emmas salary:
#    name  age    country  salary  experience
# 0  john   25        usa   50000           3
# 1  emma   30     canada   65000           6
# 2   sam   28  australia   55000           4
# 3  lisa   32         uk   70000           8
# 4   tom   27     german   52000           5

#  data frame after deleting experience column:
#    name  age    country  salary
# 0  john   25        usa   50000
# 1  emma   30     canada   65000
# 2   sam   28  australia   55000
# 3  lisa   32         uk   70000
# 4   tom   27     german   52000
