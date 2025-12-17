# 🎓 Exam Scheduler GUI (Tkinter Learning Project)

This project is a **learning-oriented GUI application** built with **Python’s Tkinter** library.  
It simulates a simplified **Exam Scheduler** to practice GUI design, event handling, and multi-tab layouts in Python.

---

## 🧩 Overview
The application provides:
- A **menu bar** with options to open, save, and exit  
- Two main tabs:
  - **Import Tab** — allows importing `.csv` files (Classrooms, Lessons, Students)
  - **Results Tab** — displays a generated exam schedule table (dummy data)
- Configurable **exam start date** and **exam period (days)**
- Dynamic **time slot management** (add/remove slots)
- **Treeview** table for visualizing schedule data
- **Log panel** that records all actions in real time

---

## 🧠 Purpose
This project was developed **for learning and experimentation purposes**.  
It was designed to explore and understand:
- Tkinter GUI structure and widget hierarchy  
- Event-driven programming in Python  
- Notebook (tab-based) interfaces with `ttk.Notebook`  
- Table displays with `ttk.Treeview`  
- Input widgets such as `DateEntry`, `Spinbox`, and `Listbox`

The app currently uses **dummy data generation** for demonstration, but it serves as a solid foundation for future database integration and real exam scheduling logic.

---

## 🚀 How to Run
1. Ensure you have **Python 3.x** installed.
2. Install the required dependency:
   ```bash
   pip install tkcalendar
