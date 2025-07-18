# 📊 Advertisement Management System

This is a beginner-friendly desktop application built with **Python**, **Tkinter**, **SQLite**, and **Matplotlib** to manage advertisement-related buyer data. It supports manual entry, PDF import, and basic analytics visualization.

---

## 🚀 Features

- ✅ Add new buyer details manually
- 📥 Import data from a structured PDF file
- 📊 Analyze buyer distribution:
  - Bar chart by project name
  - Pie chart by address
- 💾 Store all data securely in an SQLite database
- 🖥️ GUI-based interaction using Tkinter

---

## 🛠️ Tech Stack

| Tool           | Purpose                         |
|----------------|---------------------------------|
| Python         | Core programming language       |
| Tkinter        | GUI framework                   |
| SQLite3        | Embedded database               |
| Matplotlib     | Data visualization              |
| pdfplumber     | PDF text extraction             |
| re (Regex)     | Pattern matching for parsing    |

---

## 🧾 How to Use

### 🔧 Requirements

Install dependencies (if not already installed):

```bash
pip install matplotlib pdfplumber
```

### 🖥️ Run the App

```bash
python your_file_name.py
```

### 📥 Importing from PDF

Make sure your `student_details.pdf` follows this format:

```
Name | Project Name | Address | 10-digit Phone
Shivam Singh | SmartAds | Thane | 9876543210
Riya Mehta   | SmartAds | Mumbai | 9123456789
John Roy     | QuickReach | Pune | 9988776655
Anaya Kapoor | QuickReach | Mumbai | 9876543201
```

> Each field should be separated by a vertical bar `|` and follow the exact order.

### 📈 Data Visualization

- **Bar Chart**: Shows number of buyers per project
- **Pie Chart**: Shows buyer distribution by address

---

## 🗃️ Database Info

**Database File**: `management.db`  
**Table**: `management_table`

**Columns:**

- `student_id` (Primary Key)
- `student_name`
- `student_college` *(used here as Project Name)*
- `student_address`
- `student_phone`

---
---

## 📌 Future Improvements

- 🔍 Add data search/filtering with Treeview
- 📤 Export data to CSV/Excel
- 🔐 Login system for admin access
- 🤖 Better PDF auto-detection and parsing

---

## 👨‍💻 Author

**Shivam Singh**  
🎓 BSc Data Science @ BK Birla College  
💡 Passionate about AI, Data, and Building Cool Stuff 🚀

---

## 📝 License

This project is open source and free to use.
