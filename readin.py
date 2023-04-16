from PIL import Image
from pytesseract import pytesseract
from readreceipt import ConvertImage
import sqlite3

class ReadIn:
    def __init__(self,filename):
        self.receipt_text = ConvertImage(filename)
        self.receipt = self.receipt_text.return_text()
        self.itemized_information = self.receipt.split()
        self.total = 0
        self.conn = sqlite3.connect("receipts.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS receipts (amount real)")

    def findtotal(self):
        
        index = self.itemized_information.index("TOTAL")
        try:
            self.total = float(self.itemized_information[index + 1])
        except ValueError:
            self.itemized_information.pop(index)
            self.findtotal()

    def add_to_db(self):
        total = self.total
        self.c.execute("INSERT INTO receipts VALUES (?)", (total,))
        self.conn.commit()
    def print_db(self):
        self.c.execute("SELECT * FROM receipts")
        items = self.c.fetchall()
        for ele in items:
            print(ele[0])

    def run(self):
        self.findtotal()
        self.add_to_db()
        self.print_db()