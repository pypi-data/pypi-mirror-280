# Import necessary python libraries
import json
import joblib
import warnings
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

def label_stats(df):
    stats = df['ReportabilityDecision'].value_counts()
    print('"No" Percentage', stats[0]*100/(stats[0]+stats[1]),"% \t Count: ", stats[0])
    print('"yes" Percentage', stats[1]*100/(stats[0]+stats[1]),"% \t Count: ", stats[1])

    plt.figure(figsize=(5, 4))
    df['ReportabilityDecision'].value_counts().plot(kind='bar')
    plt.xlabel('Categories')
    plt.ylabel('Count')
    plt.title('ReportabilityDecision')
    plt.show()

def performance_metrics(X_test, y_test, model):
  y_pred = model.predict(X_test)
  # len(y_pred)
  y_test = pd.Series(y_test)
  y_pred3 = pd.Series(y_pred)

  y_test.name = "target"
  y_pred3.name = "target"
  Classes = {0:"No",1:"Yes"}

  cm = confusion_matrix(y_test, y_pred)
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

def train(config_path):
    # Ignore all warnings
    warnings.filterwarnings("ignore")
    path = json.load(open(config_path,"r"))
    #  Data Preprocessing
    print("Loading Training Data ...")

    # Extracted the decisions which have split decisions in the past
    df = pd.read_excel(path['trainingData'])

    # Extracting the count of decision with the same description from historical data
    dec_len = []
    for i in range(len(df)):
        dec_len.append(len(eval(df['Last 50 Decisions'].values[i])))

    df['Decisions Length'] = dec_len

    # print(df['Decisions Length'].value_counts().head(5))

    print('Extracting Case 1 data ... ')
    case1_data = df[df['Decision Type'] == 'S']
    decision = case1_data['Last 50 Decisions']
    decision = [eval(item)[-1] for item in decision]
    case1_data['ReportabilityDecision'] = decision

    print('Extracting Case 2 data ... ')
    # For 3 consecutive entries
    case2_data = df[(df['Decision Type'] == 'A') & (df['Decisions Length'] >= 5)]
    decs = ['NF'] * len(case2_data)
    for i in range(len(case2_data)):
        temp_decs = eval(case2_data['Last 50 Decisions'].values[i])[-3:]
        if len(pd.Series(temp_decs).value_counts()) == 1:
            decs[i] = temp_decs[-1]

    # print("Total Values: ",len(case2_data), "\nValue Counts:")
    # print(pd.Series(decs).value_counts())

    # For 5 consecutive entries
    case2_data = df[(df['Decision Type'] == 'A') & (df['Decisions Length'] >= 5)]
    decs = ['NF'] * len(case2_data)
    for i in range(len(case2_data)):
        temp_decs = eval(case2_data['Last 50 Decisions'].values[i])[-5:]
        if len(pd.Series(temp_decs).value_counts()) == 1:
            decs[i] = temp_decs[-1]


    case2_data['ReportabilityDecision'] = decs
    case2_data = case2_data[case2_data['ReportabilityDecision'] != 'NF']

    df_temp = pd.concat([case1_data,case2_data],ignore_index=True)
    if 'Unnamed: 0' in df_temp.columns:
        df_temp.drop(columns=['Unnamed: 0'],inplace=True)

    df = df_temp
    rep_desc_map = {'Yes': 1, 'No': 0}
    df['ReportabilityDecision'] = df['ReportabilityDecision'].map(rep_desc_map)

    temp = df[df["ReportabilityDecision"]==1]
    temp1 = df[df["ReportabilityDecision"]==0]
    temp = pd.concat([temp]*7, ignore_index=True)
    df = pd.concat([temp, df], ignore_index=True)

    ## Split the training data into X and y
    X = df[['PatientInvolvement', 'ProductLine', 'ProductFamily', 'PfhhlFamily', 'HazardLevel1', 'HazardLevel2','DefectLevel1', 'DefectLevel2', 'AdvConsequences']]
    y = df['ReportabilityDecision'] # y is the decision that we want to predict for

    seed = 50
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=seed
        )

    # Fill NaN (NULL) values with "na"
    X_train = X_train.fillna('na')
    X_test = X_test.fillna('na')

    # Create a list of categorical variables
    features_to_encode = list(X_train.select_dtypes(include=['object']).columns)


    # Create a constructor to handle categorical features
    # this constructor will automatically handle the categorical variables and leave numeric variables untouched (this solution does not have numerica variablesll)
    # pandas get_dummies() get also be used to encode categorical data

    col_trans = make_column_transformer(
                            (OneHotEncoder(handle_unknown='ignore'), 
                            features_to_encode),
                            remainder='passthrough'
                            )

    # the remainder = 'passthrough' allows the constructor to ignore those variables that are not included in features_to_encode

    #  Train the Random Forest Classifier

    # Train the RF classifier
    # This set uses the hyper parameter tuning results
    print('Setting parameter for Random Foest Model ...')
    rf_classifier = RandomForestClassifier(
                        min_samples_leaf=1,
                        min_samples_split=2,
                        n_estimators=210,
                        bootstrap=True,
                        oob_score=True,
                        n_jobs=-1,
                        random_state=seed,
                        max_features='log2'
                        )

    # I would recommend to always start with the model where oob_score = True because it is better to use out-of-bag samples to estimate the generalization accuracy. 
    # An oob error estimate is almost identical to that obtained by k-fold cross-validation. 
    # Unlike many other nonlinear estimators, random forests can be fit in one sequence, with cross-validation being performed along the way.

    # Combine classifier and the constructor by using pipeline
    print('Training the model ... ')
    pipe = make_pipeline(col_trans, rf_classifier)
    pipe.fit(X, y)

    # Note: Here entire data is used for training and new data is used for checking the efficiency of model
    # This could be changed to the X_train and y_train for cheking the prediction efficiency in this notebook

    # pipe is a new black box created with 2 components:
    # 1, a constructor to handle inputs with categorical variables and transform into a corret type
    # 2, a classifier that recieves those newly transformed inputs from the constructor

    y_pred = pipe.predict(X_test)

    #  Evaluate the Classifier

    # model accurracy
    accuracy_score(y_test, y_pred)
    print("\n\nThe accuracy of the model is", round(accuracy_score(y_test, y_pred), 3) * 100,"%")

    performance_metrics(X_test, y_test, pipe)

    # Save the model as a pickle in a file 
    joblib.dump(pipe, path['model']) 