import mysql.connector
from tabulate import tabulate

con=mysql.connector.connect(host="localhost",user="root",password="root",database="python_db")

def insert(name,age,city):
    res=con.cursor()
    sql="insert into users(name,age,city) values (%s,%s,%s);"
    res.execute(sql,(name,age,city))
    con.commit()
    print("Data insert success")
def update(name,age,city,id):
    res=con.cursor()
    sql="update users set name=%s,age=%s,city=%s where id=%s;"
    res.execute(sql,(name,age,city,id))
    con.commit()
    print("Data Update success")

def select():
    res=con.cursor()
    sql="select * from users;"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["Id","Name","Age","City"]))
def delete(id):
    res=con.cursor()
    sql="delete from users where id=%s;"
    res.execute(sql,(id,))
    con.commit()
    print("Data Delete Success")

while True:
    print("1.Insert Data ")
    print("2.Update Data ")
    print("3.Select Data ")
    print("4.Delete Data ")
    print("5.Exit ")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        name = input("Enter your Name :")
        age = input("Enter your age :")
        city = input("Enter your city :")
        insert(name, age, city)
    elif ch == 2:
        id = input("Enter your Id :")
        name = input("Enter your Name :")
        age = input("Enter your age :")
        city = input("Enter your city :")
        update(name, age, city, id)
    elif ch == 3:
        select()
    elif ch == 4:
        id = input("Enter your Id :")
        delete(id)
    elif ch==5:
        quit()
    else:
        print("Invalid selection")