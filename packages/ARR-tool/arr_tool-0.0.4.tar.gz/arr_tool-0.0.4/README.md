To execute the Python code on your system, first activate the environment:

1. Open the command prompt in the directory where the Python scripts are stored.
2. Start the virtual environment:
   - Command: `venv\Scripts\activate`
   - This creates a virtual environment where the Python libraries used in the scripts are installed.

Files and Their Functions:

- config.json: Contains the paths for the model, and the destination where the predicted Excel sheet needs to be stored.

- updateTable: Compares our table's latest awareness date with the latest awareness date of the SQL data and updates our excel sheet 'training_data.xlsx'.
  - Command for importing : 
      - from ARR_tool import updateTable
      - updateTable.update(config_path)

- modelTraining: Trains the model on the data prepared in the Excel sheet.
  - Command for importing :  
      - from ARR_tool import modelTraining
      - modelTraining.train(config_path)

- generate_prediction: Makes predictions for all the data on a specified date.
  - Command for importing :  
      - from ARR_tool import generate_prediction
      - generate_prediction.predict_decisions(pred_date,config_path)

- outlook: Sends the prepared predicted Excel sheet to the designated person.
  - Command for importing :  
      - from ARR_tool import outlook
      - outlook.send_mail(mail_to,subject,body,config_path)

This forms a cycle where, after some days, the model is updated. First, run `updateTable.py` to load all new data and update the `training_data.xlsx` Excel sheet, followed by model training and other processes.










