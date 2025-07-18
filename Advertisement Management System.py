import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from collections import Counter
import pdfplumber
import re

# Database connection
connection = sqlite3.connect("management.db")

TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

# Create table if it doesn't exist (Do not drop it)
connection.execute(f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    student_name TEXT, 
    student_college TEXT, 
    student_address TEXT, 
    student_phone INTEGER
);
""")
connection.commit()

# Main application window
root = tk.Tk()
root.title("Advertisement Management System")

# App header
appLabel = tk.Label(root, text="Advertisement Management System", fg="#06a099", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10, 10), pady=(30, 0))

nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                font= ("Sylfaen",12)).grid(row=1, column=0, padx=(10,0),
                pady=(30,0))

collegeLabel = tk.Label(root, text="Enter your project name", width=40, anchor='w',
                font= ("Sylfaen",12)).grid(row=2, column=0, padx=(10,0),
                pady=(30,0))

phoneLabel = tk.Label(root, text="Enter your phone", width=40, anchor='w',
                font= ("Sylfaen",12)).grid(row=3, column=0, padx=(10,0),
                pady=(30,0))

addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                font= ("Sylfaen",12)).grid(row=4, column=0, padx=(10,0),
                pady=(30,0))

# Input fields
nameEntry = tk.Entry(root, width=30)
nameEntry.grid(row=1, column=1, padx=(0, 10), pady=(30, 20))

collegeEntry = tk.Entry(root, width=30)
collegeEntry.grid(row=2, column=1, padx=(0, 10), pady=20)

phoneEntry = tk.Entry(root, width=30)
phoneEntry.grid(row=3, column=1, padx=(0, 10), pady=20)

addressEntry = tk.Entry(root, width=30)
addressEntry.grid(row=4, column=1, padx=(0, 10), pady=20)

def takeNameInput():
    username = nameEntry.get()
    collegeName = collegeEntry.get()
    phone = int(phoneEntry.get())
    address = addressEntry.get()

    connection.execute(f"INSERT INTO {TABLE_NAME} ({STUDENT_NAME}, {STUDENT_COLLEGE}, {STUDENT_ADDRESS}, {STUDENT_PHONE}) VALUES (?, ?, ?, ?);",
                       (username, collegeName, address, phone))
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")
    nameEntry.delete(0, tk.END)
    collegeEntry.delete(0, tk.END)
    phoneEntry.delete(0, tk.END)
    addressEntry.delete(0, tk.END)

def displayAnalytics():
    cursor = connection.execute(f"SELECT {STUDENT_COLLEGE}, {STUDENT_ADDRESS} FROM {TABLE_NAME};")
    colleges = []
    addresses = []
    for row in cursor:
        colleges.append(row[0])
        addresses.append(row[1])

    # Count data for analytics
    college_counts = Counter(colleges)
    address_counts = Counter(addresses)

    # Plot college distribution
    plt.figure(figsize=(10, 5))
    plt.bar(college_counts.keys(), college_counts.values(), color='skyblue')
    plt.title("Number of Buyers per project")
    plt.xlabel("Location")
    plt.ylabel("Number of Buyer")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    # Plot address distribution
    plt.figure(figsize=(10, 5))
    plt.pie(address_counts.values(), labels=address_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Address Distribution")
    plt.tight_layout()
    plt.show()

def extract_pdf_data(file_path):
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            print("Extracted Text from Page:")
            print(text)  # Print extracted text to inspect structure
            process_pdf_text(text)

def process_pdf_text(text):
    print("Processing Extracted Text:")
    lines = text.split("\n")

    # Skip the header and blank lines
    lines = [line.strip() for line in lines if line.strip() and line.lower() not in ["name", "college", "address", "phone"]]

    print("Processed Lines:")
    for line in lines:
        print(f"Line: '{line}'")  # Print each line to inspect
        # Adjust regex for more flexible matching of fields (e.g., with spaces or multiple separators)
        match = re.match(r"^(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d{10})$", line)
        if match:
            name, college, address, phone = match.groups()
            connection.execute(f"INSERT INTO {TABLE_NAME} (student_name, student_college, student_address, student_phone) VALUES (?, ?, ?, ?) ",
                               (name.strip(), college.strip(), address.strip(), int(phone.strip())))
        else:
            print(f"Skipping invalid line: {line}")
    connection.commit()
    print("PDF Data Imported Successfully!")

def importPDF():
    extract_pdf_data("student_details.pdf")
    messagebox.showinfo("Success", "PDF Data Imported Successfully!")

# Buttons
button = tk.Button(root, text="Save Data", command=takeNameInput)
button.grid(row=5, column=0, pady=20)

analyticsButton = tk.Button(root, text="Analyze Data", command=displayAnalytics)
analyticsButton.grid(row=5, column=1)

importButton = tk.Button(root, text="Import PDF", command=importPDF)
importButton.grid(row=6, column=0, pady=20)

root.mainloop()
