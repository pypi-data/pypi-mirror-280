# Importing Python Libraries
import json
import joblib 
import pyodbc
import warnings
import datetime
import itertools
import numpy as np
import pandas as pd

from timeit import time
from datetime import date

from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score



# Function for Displayting Performace Metrics
def performance_metrics(X_test, y_test, model):
  y_pred = model.predict(X_test)
  # len(y_pred)
  y_test = pd.Series(y_test)
  y_pred3 = pd.Series(y_pred)

  y_test.name = "target"
  y_pred3.name = "target"
  Classes = {0:"No",1:"Yes"}

  cm = confusion_matrix(y_test, y_pred)
  print("Accuracy: ", accuracy_score(y_test, y_pred)*100)
  print(f"Confusion Matrix:\n{cm}")

  for i in range(2):
    print("\n\nFor",Classes[i],"Class:\n")
    recall = recall_score(y_test, y_pred, pos_label=i)
    prec = precision_score(y_test, y_pred, pos_label=i)
    f1 = f1_score(y_test, y_pred, pos_label=i)


    # Print the results
    print(f"Recall: {recall:.4f}")
    print(f"Precision Score: {prec:.4f}")
    print(f"F1 Score: {f1:.4f}")

# Function to plot confusion matrix
def plot_confusion_matrix(cm, classes, normalize = False,
                          title='Confusion matrix',
                          cmap=plt.cm.Greens, date = datetime.datetime.today()): # can change color 
    plt.figure(figsize=(10, 10))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, size=24)
    plt.colorbar(aspect=4)
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45, size=14)
    plt.yticks(tick_marks, classes, size=14)
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    # Label the plot
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), 
             fontsize=20,
             horizontalalignment="center",
             color="white" if cm[i, j] > thresh else "black")
        plt.grid(None)
        plt.tight_layout()
        plt.ylabel('True label', size=18)
        plt.xlabel('Predicted label', size=18)
        # Save the plot
        plt.savefig(path['plots'] + '/{}'.format(date) + '_arr_confusion_matrix.png')

# Function to find rows matching the condition in data dataframe
def find_match_rows(pi ,pl ,pf ,hl1 ,hl2 ,dl1 ,dl2 ,pfhhl ,adv, data ):
    match = data[(data['PatientInvolvement'] == pi) & (data['ProductLine'] == pl) & (data['ProductFamily'] == pf) & (data['HazardLevel1'] == hl1) &
( data['HazardLevel2'] == hl2) & (data['DefectLevel1'] == dl1) & (data['DefectLevel2'] == dl2) & (data['PfhhlFamily'] == pfhhl) &
( data['AdvConsequences'] == adv)]
    return match

# Confidence Score Calculation
def awareness_date(today, latest_date):
    time_diff = (today - latest_date).days
    if (time_diff<180):
        return (0.4 + 0.6* (1- (time_diff/180)))
    elif (time_diff<1100):
        return (0.4 - 0.1* (time_diff/366))
    return 0.1

def randomness(data, decision):
    rep_dec = np.array(pd.Series(data).map({"No":0,"Yes":1}))

    val_count = {0:0,1:0}

    count = 0
    key_val = rep_dec[0]
    for i in range(1,len(rep_dec)):
        if rep_dec[i-1] == rep_dec[i]:
            count+=1
        else:
            if val_count[key_val]<count:
                val_count[key_val] = count
            count = 0
            key_val = rep_dec[i]

    if val_count[key_val]<count:
        val_count[key_val] = count

    max_con_val = 1 - max(val_count.values())/len(data)
    yes_no_ratio = pd.Series(data).value_counts()[decision]/(sum(pd.Series(data).value_counts().values))

    return ( max_con_val + yes_no_ratio) / 2

def last5_con( last_5, rd):
    if ((len(last_5) ==1) & (last_5.keys()[0]!=rd)):
        return 0
    return last_5[rd]/5

def last5_pred( last_5_pred, last_5_dec, rd):
    match = 0
    for i in range(min(len(last_5_pred),len(last_5_dec))):
        if (last_5_dec[i] == last_5_pred[i]) and (last_5_dec[i] == rd) :
            match+=1
    return match/5
# Note: to consider the scenario where the pred and decision length is different

def weightage(last_5 , aware, randomness_score, last_5_prediction):
    return (last_5 + aware + randomness_score + last_5_prediction)/4

def conf_score( pi ,pl ,pf ,hl1 ,hl2 ,dl1 ,dl2 ,pfhhl ,adv, rd, data):
    match = data[(data['PatientInvolvement'] == pi) & (data['ProductLine'] == pl) & (data['ProductFamily'] == pf) & (data['HazardLevel1'] == hl1) &
( data['HazardLevel2'] == hl2) & (data['DefectLevel1'] == dl1) & (data['DefectLevel2'] == dl2) & (data['PfhhlFamily'] == pfhhl) &
( data['AdvConsequences'] == adv)]
    
    if (len(match) == 1) and (match['Decision Type'].values[0] == 'S'):
        return 1

    if len(match) == 0:
        return -1
    
    
    last_5 = eval(match['Last 50 Decisions'].values[0])[-5:]
    last_5_pr = eval(match['Last 5 Prediction'].values[0])
    
    last_5_prediction = last5_pred(last_5_pr, last_5, rd)
    aware_score = awareness_date(pd.to_datetime(pred_date), 
                                 pd.to_datetime(match['Latest AwareData'].values[0]))    
    
    randomness_score = randomness(eval(match['Last 50 Decisions'].values[0]), rd)
    last5_score = last5_con( pd.Series(last_5).value_counts(), rd)
    # print((last5_score, aware_score, randomness_score, last_5_prediction))
    return weightage(last5_score, aware_score, randomness_score, last_5_prediction)
    # return weightage(last5_score, aware_score, randomness_score)

def predict_decisions(pred_date,config_path):
    
    warnings.filterwarnings("ignore")
    path = json.load(open(config_path,'r'))
    day,month,year = [int(item) for item in pred_date.split('-')]

    if (((day>1) & (day<=31)) & ((month>1) & (month<=12)) & ((year>2019) & (day<=date.today().year))) != True:
        print("Please check the date format again")
        exit()

    read_sql_time = time.time()
    # Create function for querying MS SQL DB
    print('Reading SQL Data ...')
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

    # Loading SQL Training data
    sql_train = 'SELECT HazardId, AwarenessDate, PatientInvolvement, ProductLine, ProductFamily, HazardLevel1, HazardLevel2, DefectLevel1, DefectLevel2, PfhhlFamily, AdvConsequences, ReportabilityDecision FROM [MilesTestingDb].[python].[ArrReportabilityPred_TrainMv] ORDER BY AwarenessDate ASC'

    df = pd.DataFrame.from_records(
        data=qry_mssql(sql_train),
        columns=['HazardId', 'AwarenessDate', 'PatientInvolvement', 'ProductLine', 'ProductFamily', 'HazardLevel1','HazardLevel2', 'DefectLevel1', 'DefectLevel2', 'PfhhlFamily', 'AdvConsequences','ReportabilityDecision']
        )

    read_sql_end = time.time()
    # preprocessing, ensure no null values are present
    df.isnull().sum()

    # drop rows where data is null
    df.dropna(axis=0, inplace=True)

    # Data Description
    df1 = df.copy()

    # Split Awareness Date column into day, month, year using pandas
    df1['AwarenessDate'] = pd.to_datetime(df1['AwarenessDate'], yearfirst=True)
    df1['Aware_Day'] = df1['AwarenessDate'].dt.day
    df1['Aware_Month'] = df1['AwarenessDate'].dt.month
    df1['Aware_Year'] = df1['AwarenessDate'].dt.year
    df1.drop(columns=['AwarenessDate'], axis=1, inplace=True)

    # Selecting the date
    pred_date = datetime.date(year,month, day)

    # Columns that are used to make any prediction
    col = ['PatientInvolvement', 'ProductLine', 'ProductFamily', 'HazardLevel1', 'HazardLevel2', 'DefectLevel1', 'DefectLevel2', 'PfhhlFamily', 'AdvConsequences']

    main_df = pd.read_excel(path['trainingData'])


    # Load the model from the file 
    print("Loading the model ... ")
    pipe = joblib.load(path['model']) 

    # Extracting the data on prediction date
    data_on_pred_date = df1[(df1['Aware_Day'] == pred_date.day) & (df1['Aware_Month'] == pred_date.month) & (df1['Aware_Year'] == pred_date.year)]
    # data_on_pred_date = df1[(df1['Aware_Month'] == pred_date.month -1) & (df1['Aware_Year'] == pred_date.year)]

    # Prediction for data on Specified data

    # Prediction for case 2 and case 3
    print('Making the Prediction ...')
    y_pred = pipe.predict(data_on_pred_date[col])


    # Prediction for case 1 data
    for i in range(len(data_on_pred_date)):
        pi ,pl ,pf ,hl1 ,hl2 ,dl1 ,dl2 ,pfhhl ,adv = list(data_on_pred_date[col].iloc[i,:])
        temp = find_match_rows(pi ,pl ,pf ,hl1 ,hl2 ,dl1 ,dl2 ,pfhhl ,adv, main_df.copy())
        if (len(temp) == 1) and (temp['Decision Type'].values[0] == 'S'):
            y_pred[i] == eval(temp['Last 50 Decisions'].values[0])[-1]
        # print(i,y_pred[i])

    data_on_pred_date['Prediction'] = y_pred
    data_on_pred_date['Prediction'] = data_on_pred_date['Prediction'].map({0:"No",1:"Yes"})

    y_proba = pipe.predict_proba(data_on_pred_date[col])
    y_pr = [max(a) for a in y_proba]

    result = y_pr.copy()
    error = []
    dec_type = ['P'] * len(data_on_pred_date)
    for i in range(len(data_on_pred_date)):
        try:
            pi ,pl ,pf ,hl1 ,hl2 ,dl1 ,dl2 ,pfhhl ,adv, rd = list(data_on_pred_date[col+['ReportabilityDecision']].iloc[i,:])
            conf_temp = conf_score(pi ,pl ,pf ,hl1 ,hl2 ,dl1 ,dl2 ,pfhhl ,adv, rd, main_df.copy())
            if (conf_temp != -1): # if the value exist in the table
                result[i] = conf_temp
                if (int(conf_temp) == 1):
                    dec_type[i] = 'S'
                else:
                    dec_type[i] = 'A'
        except Exception as e:
            error.append({i:e})

    if(len(error) == 0):
        print("Predictions Finished Successfully")

    data_on_pred_date['Confidence Score'] = result
    data_on_pred_date['Prob Score'] = y_pr

    # Columns template for the data that need to shared in excel sheet
    col_ = ['HazardId', 'PatientInvolvement', 'ProductLine', 'ProductFamily',
        'HazardLevel1', 'HazardLevel2', 'DefectLevel1', 'DefectLevel2',
        'PfhhlFamily', 'AdvConsequences', 'ReportabilityDecision', 'Prediction', 'Confidence Score']

    data_on_pred_date[col_].to_excel(path['prediction'] + 'Prediction -'+str(pred_date)+'.xlsx',index=None)

    cm = confusion_matrix(data_on_pred_date['ReportabilityDecision'], data_on_pred_date['Prediction'])
    plot_confusion_matrix(cm, classes=['0 - Not Reportable', '1 - Reportable'],date=pred_date)

    print("Total time taken: ", time.time() - read_sql_time, "SQL read time taken: ", read_sql_end - read_sql_time)

