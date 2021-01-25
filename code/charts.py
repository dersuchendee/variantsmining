import pandas as pd
pd.set_option('display.max_columns', None)

df_unito = pd.read_csv("risultati/df_uniti_fermoelucia2.csv", header= 0)

df_unito.drop('Complexity', axis=1, inplace=True)
#df_unito.drop('Category 2', axis=1, inplace=True)
#df_unito.drop('Category 3', axis=1, inplace=True)

df = df_unito.set_index(['Category 1', 'Category 2' ,'Category 3']).stack().rename('Value').reset_index()


#df = df_unito.T


df.loc[df['level_3'] == 'Chapter I', 'Date'] = 'Chapter I'

df.loc[df['level_3'] == 'Chapter II', 'Date'] = 'Chapter II'
df.loc[df['level_3'] == 'Chapter III', 'Date'] = 'Chapter III'
df.loc[df['level_3'] == 'Chapter IV', 'Date'] = 'Chapter IV'
df.loc[df['level_3'] == 'Chapter V', 'Date'] = 'Chapter V'
df.loc[df['level_3'] == 'Chapter VI', 'Date'] = 'Chapter VI'
df.loc[df['level_3'] == 'Chapter VII', 'Date'] = 'Chapter VII'
df.loc[df['level_3'] == 'Chapter VIII', 'Date'] = 'Chapter VIII'
df.reset_index(drop=True, inplace=True)
df.insert(loc = 4, column='Complexity', value=['' for i in range(df.shape[0])])

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

group_data = df.groupby(['level_3','Complexity'])['Value'].sum()
group_data = group_data.to_frame().reset_index()

group_data['Datee']='02/02/2000'
group_data.loc[group_data['level_3'] == 'Chapter II', 'Datee'] = '02/02/2001'
group_data.loc[group_data['level_3'] == 'Chapter III', 'Datee'] = '02/02/2002'
group_data.loc[group_data['level_3'] == 'Chapter VI', 'Datee'] = '02/02/2003'
group_data.loc[group_data['level_3'] == 'Chapter V', 'Datee'] = '02/02/2004'
group_data.loc[group_data['level_3'] == 'Chapter VI', 'Datee'] = '02/02/2005'
group_data.loc[group_data['level_3'] == 'Chapter VII', 'Datee'] = '02/02/2006'
group_data.loc[group_data['level_3'] == 'Chapter VIII', 'Datee'] = '02/02/2007'
group_data.reset_index(drop=True, inplace=True)

group_data = group_data.pivot('Complexity', 'level_3', 'Value')
#df = group_data.T
#print(group_data)
df = group_data.T
print(df)

df.to_csv('provo2.csv')
group_data.to_csv('pergrafico_alluvial2_fermoelucia.csv')



