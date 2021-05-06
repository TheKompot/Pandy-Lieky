import pandas as pd 

def import_table(table,year):

    # assigning table name by the combination of table and year
    if table == 'all' and year == 2020:
        name = 'L01_L02_1_4Q_2020_rebricek_spotreba_humannych_liekov'
    elif table == 'insurance' and year == 2020:
        name = 'L02_1_4Q_2020_rebricek_vydane_na_recept_hradene_z_verejneho_poistenia'
    elif table == 'no prescription' and year == 2020:
        name ='L01_1_4Q_2020_vydaj_V_rebricek_predane_bez_receptu'
    elif table == 'no insurance' and year == 2020:
        name = 'L01_1_4Q_2020_vydaj_D_rebricek_vydane_na_recept_bez_uhrady_verejneho_poistenia'
    elif  table == 'detailed' and year == 2020:
        name = ['P_L01_L02_1Q_2020','P_L01_L02_2Q_2020','P_L01_L02_3Q_2020','P_L01_L02_4Q_2020']

    elif table == 'all' and year == 2019:
        name = 'L01_L02_1_4Q_2019_rebricek_spotreba_humannych_liekov'
    elif table == 'insurance' and year == 2019:
        name = 'L02_1_4Q_2019_rebricek_vydane_na_recept_hradene_verejneho_poistenia'
    elif table == 'no prescription' and year == 2019:
        name = 'L01_1_4Q_2019_vydaj_V_rebricek_predane_bez_receptu'
    elif table == 'no insurance' and year == 2019:
        name = 'L01_1_4Q_2019_vydaj_D_rebricek_vydane_na_recept_bez_uhrady_verejneho_poistenia'
    elif table == 'detailed' and year == 2019:
        name = 'PL01_L02_2019'

    elif table == 'all' and year == 2018:
        name = 'L01_L02_1_4Q_2018_rebricek'
    elif table == 'insurence' and year == 2018:
        name = 'L02_1_4Q_2018_rebricek'
    elif table == 'no prescription' and year == 2018:
        name = 'L01_1_4Q_2018_vydaj_V_rebricek'
    elif table == 'no insurance' and year == 2018:
        name = 'L01_1_4Q_2018_vydaj_D_rebricek'
    elif table == 'detailed' and year == 2018:
        name =  'PL01_L02_2018'

    elif table == 'detailed' and year == 2017:
        name = 'PL01_L02_2017'
    elif table == 'detailed' and year == 2016:
        name = 'PL01_L02_2016'
    elif table == 'detailed' and year == 2015:
        name = 'PL01_L02_2015'
    
    t = None # table that will be returned

    if year == 2020:
        if isinstance(name,list): # with the detailed option there are 3 tables associated -> creatingg a dict()
            t = {}
            for i,n in enumerate(name):
                t[f'Q{i+1}'] = pd.read_excel(f'data/{n}.xlsx',sheet_name='Dataset',header=0)
        else: # all other option are normal tables
            t = pd.read_excel(f'data/{name}.xlsx',sheet_name='Dáta',header=2).iloc[2:,:8].reset_index()
            t.pop('index')
            t = t.rename(columns={2020:'Spolu'})
    elif table == 'detailed' and year == 2019:
        t = pd.read_excel(f'data/{name}.xlsx',sheet_name='Dáta',header=1)
    elif table == 'detailed':
        t = pd.read_excel(f'data/{name}.xlsx',sheet_name='Dataset',header=0)
        t.dropna(how='all', axis=1, inplace=True)
    elif year == 2018 or year == 2019: # in year 2018, 2019 and with any opton except detailed there are a lot of information about every quarter 
                                       # so from one table it creates 5 of them for every quarter and all together in to a dict()
        temp = pd.read_excel(f'data/{name}.xlsx',sheet_name='T1',header=4)
        rename_columns = ('Počet balení','Úhrada_ZP','Úhrada_PAC','Úhrada_SPOLU',
        'POCET_BALENI','UHRADA_ZP','UHRADA_PAC','UHRADA_SP','CENA')  # Columns that are duplicated in the table
        for c in temp.columns: # renaming the diplicated columns by adding Qx 
            if c in rename_columns:
                temp = temp.rename(columns={c:f'{c}_Q1'})
            elif c[:-2] in rename_columns:
                index = int(c[-1])
                if index == 4:
                    temp = temp.rename(columns={c:f'{c[:-2]}'})
                else:
                    temp = temp.rename(columns={c:f'{c[:-2]}_Q{index+1}'})
        # because tables varry in the number of collumns there are different constants with you should divide the table
        if year == 2019 and (table == 'no_prescription' or table == 'no insurance'):
            mult = 2
            add=-2
        elif year == 2018 and (table == 'no_prescription' or table == 'no insurance'):
            mult = 3
            add = -1
        elif year == 2019:
            mult = 4
            add = 0
        else:
            mult = 5
            add = 1

        t = {'SPOLU' :  temp.iloc[:,:3].join(temp.iloc[:,mult*4+3:]) }
        for i in range(4):
            t[f'Q{i+1}'] =  temp.iloc[:,:3].join(temp.iloc[:,i*mult+3:i*mult+7+add]) 
    # removing potencial spaces in column names
    if isinstance(t,dict):
        for i in t:
            for c in t[i].columns:
                t[i] = t[i].rename(columns={c:c.strip()})
    else:       
        for c in t.columns:
            t = t.rename(columns={c:c.strip()})
    return t
