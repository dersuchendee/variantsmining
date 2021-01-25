import pandas as pd
pd.set_option('display.max_columns', None)

df1 = pd.read_csv("risultati/sposipromessi/spt1c1.csv", header= 0)

#print(df1)
headers = df1.iloc[0]
new_df  = pd.DataFrame(df1.values[1:], columns=headers)
print(new_df)


df2 = pd.read_csv("risultati/sposipromessi/spt1c2.csv", header= 0)

df3 = pd.read_csv("risultati/sposipromessi/spt1c3.csv", header= 0)

df4 = pd.read_csv("risultati/sposipromessi/spt1c4.csv", header= 0)

df5 = pd.read_csv("risultati/sposipromessi/spt1c5.csv", header= 0)

df6 = pd.read_csv("risultati/sposipromessi/spt1c6.csv", header= 0)

df7 = pd.read_csv("risultati/sposipromessi/spt1c7.csv", header= 0)

df8 = pd.read_csv("risultati/sposipromessi/spt1c8.csv", header= 0)

df1 = df1.rename({'Frequency':'Chapter I'}, axis=1)
df2 = df2.rename({'Frequency':'Chapter II'}, axis=1)
df3 = df3.rename({'Frequency':'Chapter III'}, axis=1)
df4 = df4.rename({'Frequency':'Chapter IV'}, axis=1)
df5 = df5.rename({'Frequency':'Chapter V'}, axis=1)
df6 = df6.rename({'Frequency':'Chapter VI'}, axis=1)
df7 = df7.rename({'Frequency':'Chapter VII'}, axis=1)
df8 = df8.rename({'Frequency':'Chapter VIII'}, axis=1)








from functools import reduce
df = reduce(lambda x,y: pd.merge(x,y, on=['Category 1', 'Category 2', 'Category 3', 'Complexity'], how='outer'), [df1, df2, df3, df4, df5, df6, df7, df8])

#print(df)
#df['Date']='02/02/2000'
#df.to_csv('risultati/df_uniti_sposipromessi.csv', index=False)
