#search for records with values that contain val
def locator(df, col, val):
    '''
    This is used a function to create unique
    filters to return all records where a column
    has a matching val for any poassed dataframe.
    Use the returned list as the .iloc filter
    '''
    a_list=[]
    for i in range(len(df[col])):
        if type(df[col].iloc[i])==list:
            if val in df[col].iloc[i]:
                a_list.append(i)
        else:
            if val == df[col].iloc[i]:
                a_list.append(i)
    #return the list of locations to be used as a .iloc filter
    return a_list

#create a list of unique possible values based on a column
#with lists or not
def pos_values(df,col):
    '''
    This will reveal to you all relevant or possible values
    from a data frame (a distinct function) for cols with lists
    and non list items mixed.
    '''
    p_list=[]
    for i in range(len(df[col])):
        if type(df[col].iloc[i])==list:
            s=df[col].iloc[i]
            for j in s:
                p_list.append(j)
        else:
            p_list.append(df[col].loc[i])
            
    p_list=list(set(p_list))
    p_list.sort()
    return p_list

#converst list objects to strings for presentation convenience
def stringConvert (df,col):
    '''
    This is utilized to call a df frame and column
    and is useful for creating string dummy columns
    that play nice for streamlit in there crisp dataframe box
    '''
    a_list = []
    for i in range(len(df[col])):
        if type(df[col].iloc[i])==list:
            a_list.append(', '.join(j for j in df[col].iloc[i]))
        else:
            a_list.append(str(df[col].iloc[i]))
    #return the list of locations to be used as a .iloc filter
    return a_list

def hour_sort(list):
    h_dict = {
        "monday": '',"tuesday": '', "wednesday": '', "thursday": '', "friday": '', "saturday": '', "sunday": ''
        }   
    try:
        for j in list.keys():
            h_dict[j]=list[j]
    except:
        pass
    return h_dict
