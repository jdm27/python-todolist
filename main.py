import pandas as pd


def add_task():
    new_task = input(">Add a task:")
    new_description= input(">Add a description:")
    df= pd.read_csv('data.csv')
    df= df.append({"Description":new_description,"Task":new_task,"Status": "Pending"}, ignore_index=True)
    df.to_csv('data.csv',index=False )


def read_tasks(search_text=None):
    df = pd.read_csv('data.csv')
    if search_text:
        df = df[df['Task'].str.contains(search_text,case=False,na=False)]

    print(df)

def modify_status(index_task):
    df = pd.read_csv('data.csv')
    status =df.at[index_task,"Status"]

    if status== "Pending":
        df.at[index_task,"Status"] = "Complete"
    elif status == "Complete":
        df.at[index_task,"Status"] = "Pending"
    else: print("It not posible change the status...")
    
    df.to_csv('data.csv',index=False )
    print(df)

def modify_task(index_task,new_title_task):
    df = pd.read_csv('data.csv')
    df.at[index_task,'Task']  = new_title_task     
    df.to_csv('data.csv',index=False )

def modify_description(index_task,new_description):
    df = pd.read_csv('data.csv')
    df.at[index_task,'Description']  = new_description  
    df.to_csv('data.csv',index=False )


def delete_task(index):
    df = pd.read_csv('data.csv')
    df = df.drop(index)
    df.to_csv('data.csv',index=False )


while (True):
    print('*******TO***DO***LIST*******')
    read_tasks()
    print("_____________________________")
    print("|1.New task                  |")
    print("|2.Modify status             |")
    print("|3.Modify title task         |")
    print("|4.Modify description        |")
    print("|5.Search task               |")
    print("|6.Delete task               |")
    print("|7.Exit                      |")
    print("|____________________________|")
    
    choice= input(">")

    if choice=="7":
        print("See you soon!")
        break

    if choice=="1":
        add_task()
    elif choice=="2":
        modify_status(int(input(">Select index: ")))
    elif choice=="3":
        modify_task(int(input(">Select index: ")),input(">Write your new title: "))
    elif choice=="4":
        modify_description(int(input(">Select index: ")),input(">Write your new description: "))
    elif choice=="5":
        read_tasks(input(">Write title to search: "))
    elif choice =="6":
        delete_task(int(input(">Select index task to delete: ")))
        



