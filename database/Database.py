import sqlite3

class Database:
    """Database class"""

    def __init__(self):
        self.conn = sqlite3.connect('subjects.db')
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def __repr__(self):
        return "Database: subjects.db"

    def create_table(self):
        self.cur.execute("""CREATE TABLE subjects (
                            code text primary key,
                            name text,
                            description text,
                            ECTS real
                            )""")
    def insert_subject(self, subject):
        with self.conn:
            self.cur.execute("INSERT INTO subjects VALUES (:code, :name, :description, :ECTS)", {'code': subject.code, 'name': subject.name, 'description': subject.description, 'ECTS': subject.ECTS})

    def get_subjects_by_code(self, code):
        code = "%" + code + "%"
        self.cur.execute("SELECT * FROM subjects WHERE code LIKE :code ORDER BY code", {'code':code})
        return self.cur.fetchall()

    def show_all_subjects(self):
        self.cur.execute("SELECT * FROM subjects ORDER BY code")
        return self.cur.fetchall()

    def remove_subject(self, code):
        with self.conn:
            self.cur.execute("DELETE from subjects WHERE code = :code",
                    {'code': code})

    def get_number_of_subjects(self):
        return (self.cur.execute("SELECT COUNT(*) FROM subjects").fetchone()[0])

    def get_number_of_subjects_by_code(self, code):
        return (self.cur.execute("SELECT COUNT(*) FROM subjects WHERE code LIKE :code", {'code':code}).fetchone()[0])
