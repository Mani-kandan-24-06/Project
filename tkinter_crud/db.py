import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        Create table if not exists employee(
            id integer primary key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
            )
        """
        self.cur.execute(sql)
        self.con.commit()


    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute("insert into employee values (NULL,?,?,?,?,?,?,?)",
                         (name,age,doj,email,gender,contact,address))
        self.con.commit()

    def fetch(self):
        self.cur.execute("select * from employee")
        row=self.cur.fetchall()
        # print(row)
        return row

    def remove(self,id):
        self.cur.execute("delete from employee where id=?",(id,))
        self.con.commit()

    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cur.execute("update employee set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?",
                         (name,age,doj,email,gender,contact,address,id))
# o=Database("Employee.db")
# o.insert("Mani","21","23-2-23","manikandanrv2@gmail.com","Male","9929323322","s.n.chavadi,cuddalore")
# o.fetch()
# o.remove("5")
# o.update("2","")
