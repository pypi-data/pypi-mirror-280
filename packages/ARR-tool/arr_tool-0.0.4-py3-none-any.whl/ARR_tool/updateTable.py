# Import necessary python libraries
import json
import pyodbc
import joblib
import warnings
import numpy as np
import pandas as pd
from timeit import time
# Create function for querying MS SQL DB
def qry_mssql(sql):
    # Connection string
    # Trusted_connection=yes will use credentials of the currently logged in user
    cnxn = pyodbc.connect(r"""
        DRIVER={ODBC Driver 17 for SQL Server};
        SERVER=kzo00031252d.strykercorp.com\sqlra2012;
        DATABASE=MilesTestingDb;
        UID=MilesUser;
        PWD=Stryker1;
        """
        )
    # Query database
    mycursor = cnxn.cursor()
    mycursor.execute(sql)
    qry = mycursor.fetchall()
    # Close the cursor and connection
    mycursor.close()
    cnxn.close()
    # Return query results
    return qry

def find_match_rows(pi ,pl ,pf ,hl1 ,hl2 ,dl1 ,dl2 ,pfhhl ,adv, data ):
    match = data[(data['PatientInvolvement'] == pi) & (data['ProductLine'] == pl) & (data['ProductFamily'] == pf) & (data['HazardLevel1'] == hl1) &
( data['HazardLevel2'] == hl2) & (data['DefectLevel1'] == dl1) & (data['DefectLevel2'] == dl2) & (data['PfhhlFamily'] == pfhhl) &
( data['AdvConsequences'] == adv)]
    return match

def update(config_path):
    warnings.filterwarnings('ignore')
    start = time.time()
    # Load the config.json file which consists of all the paths
    path = json.load(open(config_path))

    # Reading the training data
    train_data = pd.read_excel(path['trainingData'])

    # Loading the model
    pipe = joblib.load(path['model'])

    # Loading SQL Training data
    sql_train = 'SELECT HazardId, AwarenessDate, PatientInvolvement, ProductLine, ProductFamily, HazardLevel1, HazardLevel2, DefectLevel1, DefectLevel2, PfhhlFamily, AdvConsequences, ReportabilityDecision FROM [MilesTestingDb].[python].[ArrReportabilityPred_TrainMv] ORDER BY AwarenessDate ASC'

    print('Loading SQL data ...')
    sql_data = pd.DataFrame.from_records(
        data=qry_mssql(sql_train),
        columns=['HazardId', 'AwarenessDate', 'PatientInvolvement', 'ProductLine', 'ProductFamily', 'HazardLevel1','HazardLevel2', 'DefectLevel1', 'DefectLevel2', 'PfhhlFamily', 'AdvConsequences','ReportabilityDecision']
        )

    # preprocessing, ensure no null values are present
    sql_data.isnull().sum()

    # drop rows where data is null
    sql_data.dropna(axis=0, inplace=True)

    last_update_date = list(pd.to_datetime(train_data['Latest AwareDate']).sort_values().values)[-1]
    last_update_date = pd.to_datetime(last_update_date)

    # Split Awareness Date column into day, month, year using pandas
    sql_data['AwarenessDate'] = pd.to_datetime(sql_data['AwarenessDate'], yearfirst=True)
    sql_data['Aware_Day'] = sql_data['AwarenessDate'].dt.day
    sql_data['Aware_Month'] = sql_data['AwarenessDate'].dt.month
    sql_data['Aware_Year'] = sql_data['AwarenessDate'].dt.year

    data_to_update = sql_data[
                        (sql_data['Aware_Year']>=last_update_date.year) &
                        (sql_data['Aware_Month']>=last_update_date.month) &
                        (sql_data['Aware_Day']>last_update_date.day)
                    ]

    col = ['PatientInvolvement', 'ProductLine', 'ProductFamily', 'HazardLevel1', 'HazardLevel2', 
        'DefectLevel1', 'DefectLevel2', 'PfhhlFamily', 'AdvConsequences']

    pred = pipe.predict(data_to_update[col])

    data_to_update["prediction"] = pred
    data_to_update["prediction"] = data_to_update["prediction"].map({0:"No",1:"Yes"})

    error = []
    case1_data =pd.DataFrame(columns=['PatientInvolvement', 'ProductLine', 'ProductFamily', 'HazardLevel1',
        'HazardLevel2', 'DefectLevel1', 'DefectLevel2', 'PfhhlFamily',
        'AdvConsequences', 'Last 5 Prediction', 'Latest AwareDate',
        'Decision Type', 'Last 50 Decisions'])

    print('Updating the table ...')
    for i in range(len(data_to_update)):
        try:
            pi ,pl ,pf ,hl1 ,hl2 ,dl1 ,dl2 ,pfhhl ,adv = list(data_to_update[col].iloc[i,:])
            df_temp = find_match_rows(pi ,pl ,pf ,hl1 ,hl2 ,dl1 ,dl2 ,pfhhl ,adv, train_data )
            if(len(df_temp)>0):
                train_data.loc[df_temp.index,'Latest AwareDate'] = data_to_update[['AwarenessDate']].iloc[i,:].values
                train_data.loc[df_temp.index,'Last 5 Prediction'] = np.array([str(eval(list(df_temp['Last 5 Prediction'].values)[0])[-4:] + list(data_to_update[['prediction']].iloc[i,:].values))])
                train_data.loc[df_temp.index,'Last 50 Decisions'] = np.array([str(eval(list(df_temp['Last 50 Decisions'].values)[0])[-49:] + list(data_to_update[['ReportabilityDecision']].iloc[i,:].values))])
            else:
                new_entry = pd.DataFrame({
                        'PatientInvolvement': pi,
                        'ProductLine': pl, 
                        'ProductFamily': pf, 
                        'HazardLevel1': hl1,       
                        'HazardLevel2': hl2, 
                        'DefectLevel1': dl1, 
                        'DefectLevel2': dl2, 
                        'PfhhlFamily': pfhhl,       
                        'AdvConsequences': adv, 
                        'Last 5 Prediction': str([data_to_update[['prediction']].iloc[i,:].values[0]]), 
                        'Latest AwareDate': data_to_update[['AwarenessDate']].iloc[i,:].values[0],       
                        'Decision Type': 'A', 
                        'Last 50 Decisions': str([data_to_update[['ReportabilityDecision']].iloc[i,:].values[0]])
                                        })
                
                case1_data = pd.concat([case1_data,new_entry])
                
        except Exception as e:
            error.append(i)

    before_new_hazard = len(train_data)
    train_data = pd.concat([train_data, case1_data], ignore_index=True)
    print("Total new addition:",len(train_data) - before_new_hazard, case1_data['Decision Type'])

    print('Writing the data in the main table ...')
    train_data.to_excel(path['trainingData'],index=None)
    print("Total time taken:", time.time() - start)