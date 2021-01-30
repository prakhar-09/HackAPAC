import tkinter as tk 
import mysql.connector  
from tkinter import * 
import PIL 
   
  
def submitact(): 
      
    user = Username.get() 
    passw = password.get() 
   
    print(f"The name entered by you is {user} {passw}") 
   
    logintodb(user, passw) 
   
   
def logintodb(user, passw): 
      
    # If paswword is enetered by the  
    # user 
    if passw: 
        db = mysql.connector.connect(host ="localhost", 
                                     user = user, 
                                     password = passw, 
                                     db ="College") 
        cursor = db.cursor() 
          
    # If no password is enetered by the 
    # user 
    else: 
        db = mysql.connector.connect(host ="localhost", 
                                     user = user, 
                                     db ="College") 
        cursor = db.cursor() 
          
    # A Table in the database 
    savequery = "select * from STUDENT"
      
    try: 
        cursor.execute(savequery) 
        myresult = cursor.fetchall() 
          
        # Printing the result of the 
        # query 
        for x in myresult: 
            print(x) 
        print(" your Query Excecuted successfully") 
          
    except: 
        db.rollback() 
        print("Error occured") 
   
   
root = tk.Tk() 
root.geometry("300x300") 
root.title("Study Aid") 
   
C = Canvas(root, bg ="brown", height = 250, width = 300) 
  
# Definging the first row 
lblfrstrow = tk.Label(root, text ="Username -", ) 
lblfrstrow.place(x = 50, y = 20) 
  
Username = tk.Entry(root, width = 35) 
Username.place(x = 151, y = 21, width = 100) 
   
lblsecrow = tk.Label(root, text ="Password -") 
lblsecrow.place(x = 50, y = 50) 
  
password = tk.Entry(root, width = 35) 
password.place(x = 150, y = 50, width = 100) 
  
submitbtn = tk.Button(root, text ="Login here",  
                      bg ='green', command = submitact) 
submitbtn.place(x = 150, y = 135, width = 55) 
  
root.mainloop() 
