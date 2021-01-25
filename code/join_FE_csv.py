import pandas as pd
pd.set_option('display.max_columns', None)

df1 = pd.read_csv("risultati/fermoelucia/fet1c1.csv", header= 0)

#print(df1)
headers = df1.iloc[0]
new_df  = pd.DataFrame(df1.values[1:], columns=headers)
print(new_df)


df2 = pd.read_csv("risultati/fermoelucia/fet1c2.csv", header= 0)

df3 = pd.read_csv("risultati/fermoelucia/fet1c3.csv", header= 0)

df4 = pd.read_csv("risultati/fermoelucia/fet1c4.csv", header= 0)

df5 = pd.read_csv("risultati/fermoelucia/fet1c5.csv", header= 0)

df6 = pd.read_csv("risultati/fermoelucia/fet1c6.csv", header= 0)

df7 = pd.read_csv("risultati/fermoelucia/fet1c7.csv", header= 0)

df8 = pd.read_csv("risultati/fermoelucia/fet1c8.csv", header= 0)

df1 = df1.rename({'Frequency':'Chapter I'}, axis=1)
df2 = df2.rename({'Frequency':'Chapter II'}, axis=1)
df3 = df3.rename({'Frequency':'Chapter III'}, axis=1)
df4 = df4.rename({'Frequency':'Chapter IV'}, axis=1)
df5 = df5.rename({'Frequency':'Chapter V'}, axis=1)
df6 = df6.rename({'Frequency':'Chapter VI'}, axis=1)
df7 = df7.rename({'Frequency':'Chapter VII'}, axis=1)
df8 = df8.rename({'Frequency':'Chapter VIII'}, axis=1)



from functools import reduce
df = reduce(lambda x,y: pd.merge(x,y, on=['Category 1', 'Category 2', 'Category 3'], how='outer'), [df1, df2, df3, df4, df5, df6, df7, df8])

df.loc[df['Category 3'] == 'prima', 'Complexity'] = 'IC 1'
df.loc[df['Category 3'] == 'corpo minore', 'Complexity'] = 'IC 1'
df.loc[df['Category 3'] == 'faseprima 1234T', 'Complexity'] = 'IC 4'
df.loc[df['Category 3'] == 'faseprima 123T', 'Complexity'] = 'IC 3'
df.loc[df['Category 3'] == 'faseprima 12345T', 'Complexity'] = 'IC 5'
df.loc[df['Category 3'] == 'faseprima 123456T', 'Complexity'] = 'IC 6'
df.loc[df['Category 3'] == 'faseprima 12345678T', 'Complexity'] = 'IC 8'
df.loc[df['Category 3'] == 'fasericavataprima 123T', 'Complexity'] = 'IC 3'
df.loc[df['Category 3'] == 'fasericavataprima 1234T', 'Complexity'] = 'IC 4'
df.loc[df['Category 3'] == 'fasericavataprima 1234567T', 'Complexity'] = 'IC 7'


df.loc[df['Category 3'] == 'da', 'Complexity'] = 'LC 1'
df.loc[df['Category 3'] == 'su', 'Complexity'] = 'LC 1'
df.loc[df['Category 3'] == 'corr.in', 'Complexity'] = 'LC 1'

df.loc[df['Category 3'] == 'sps.', 'Complexity'] = 'LC 1'
df.loc[df['Category 3'] == 'segue', 'Complexity'] = 'IC 1'

df.loc[df['Category 3'] == 'as.', 'Complexity'] = 'LC 1'

df.loc[df['Category 3'] == 'ins.', 'Complexity'] = 'INS 1'#????? CONTROLLA

df.loc[df['Category 3'] == 'fasericavata 12T', 'Complexity'] = 'LC 2'
df.loc[df['Category 3'] == 'fasericavata T', 'Complexity'] = 'LC 2'

df.loc[df['Category 3'] == 'fasericavata 123T', 'Complexity'] = 'LC 3'
df.loc[df['Category 3'] == 'fasericavata 123456T', 'Complexity'] = 'LC 6'
df.loc[df['Category 3'] == 'fasericavata 1234T', 'Complexity'] = 'LC 4'
df.loc[df['Category 3'] == 'fasericavata 12345T', 'Complexity'] = 'LC 5'
df.loc[df['Category 3'] == 'fasericavata 123456T', 'Complexity'] = 'LC 6'

df.loc[df['Category 3'] == 'fase 12T', 'Complexity'] = 'LC 2'

df.loc[df['Category 3'] == 'fase 123T', 'Complexity'] = 'LC 3'
df.loc[df['Category 3'] == 'fase 1234T', 'Complexity'] = 'LC 4'
df.loc[df['Category 3'] == 'fase 12345T', 'Complexity'] = 'LC 5'
df.loc[df['Category 3'] == 'fase 123456T', 'Complexity'] = 'LC 6'
#print(df)

#group_data = df.groupby(['level_3','Complexity'])['Value'].sum()
#group_data = group_data.to_frame().reset_index()
#print(df)
#df['Date']='02/02/2000'
df.to_csv('risultati/df_uniti_fermoelucia2.csv', index=False)
