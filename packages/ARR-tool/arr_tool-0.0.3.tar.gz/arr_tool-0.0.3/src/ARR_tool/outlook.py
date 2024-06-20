import json
import pythoncom
import win32com.client as win32

def send_mail(mail_to,subject,body,config_dir):
    pythoncom.CoInitialize()  # Initialize the COM library
    try:
        outlook = win32.Dispatch('outlook.application')

        mail = outlook.CreateItem(0)
        path = json.load(open(config_dir,'r'))

        mail.To = mail_to # 'himanshu.kumar2022@outlook.com'
        mail.Subject = subject # 'Weekly Report'
        mail.Body = body # 'Please find the weekly report attached.'
        
        excel_path = path['dir'] + '//prediction//Prediction.xlsx'
        mail.Attachments.Add(excel_path)

        image_path = path['dir'] + '//plots//arr_confusion_matrix.png'
        mail.Attachments.Add(image_path)

        mail.Send()
        print("Mail sent successfully")
    except Exception as e:
        print(f"Failed to send mail: {e}")
    finally:
        pythoncom.CoUninitialize()  # Uninitialize the COM library

