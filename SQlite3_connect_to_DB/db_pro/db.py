import sqlite3

con=sqlite3.connect('users.db')

def insertData(name,age,city):
    qry="insert into users(name,age,city) values (?,?,?);"
    con.execute(qry,(name,age,city))
    con.commit()
    print("User Details Added")
    
def updateData(name,age,city,id):
    qry="update users set name=?,age=?,city=? where id=?;"
    con.execute(qry,(name,age,city,id))
    con.commit()
    print("User Details Updated")
    
def deleteData(id):
    qry="delete from users where id=?;"
    con.execute(qry,(id))
    con.commit()
    print("User Details Deleted")
    
def selectData():
    qry="select * from users;"
    result=con.execute(qry)
    for row in result:
        print(row)


print("""
1.Insert
2.Update
3.Delete
4.Select
""")

ch=1
while ch==1:
    c=int(input("Select Your Choice : "))
    if(c==1):
        print("Add New Record")
        name=input("Enter your Name :")
        age=input("Enter your age :")
        city=input("Enter your city :")
        insertData(name,age,city)
    elif(c==2):
        print("Edit New Record")
        id=input("Enter your Id :")
        name=input("Enter your Name :")
        age=input("Enter your age :")
        city=input("Enter your city :")
        updateData(name,age,city,id)
    elif(c==3):
        print("Delete New Record")
        id=input("Enter your Id :")
        deleteData(id)
    elif(c==4):
        print("Print All Record")
        selectData()
    else:
        print("Invalid selection")
    ch=int(input("Enter 1 to continue : "))
print("Thank You")