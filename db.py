import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS students(
            id Integer Primary Key,
            code text,
            name text,
            email text,
            gender text,
            phone text,
            city text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, code, name, email, gender, phone, city):
        self.cur.execute("insert into students values (NULL,?,?,?,?,?,?)",
                         (code, name, email, gender, phone, city))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from students")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from students where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, code, name, email, gender, phone, city):
        self.cur.execute(
            "update students set code=?, name=?, email=?, gender=?, phone=?, city=? where id=?",
            (code, name, email, gender, phone, city, id))
        self.con.commit()
