import streamlit as st
import pandas as pd
from datetime import datetime, date
import sqlite3
import io
import matplotlib.pyplot as plt
import seaborn as sns

# ตั้งค่าฟอนต์ภาษาไทยเบื้องต้นให้ matplotlib (ถ้ามี)
plt.rcParams['font.family'] = 'Tahoma'

# --- ส่วนจัดการฐานข้อมูล SQLite ---
def init_db():
    conn = sqlite3.connect('blood_bank.db')
    cursor = conn.cursor()
    # ตารางสต็อกเลือด
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blood_stock (
            Bag_ID TEXT PRIMARY KEY,
            Blood_Group TEXT,
            Component TEXT,
            Receive_Date TEXT,
            Expire_Date TEXT,
            Status TEXT
        )
    ''')
    # ตารางผู้บริจาค
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS donors (
            Donor_ID TEXT PRIMARY KEY,
            Name TEXT,
            Phone TEXT,
            Blood_Group TEXT,
            Last_Donation TEXT
        )
    ''')
    # ตารางผู้ใช้งานระบบ
    cursor.execute('''
        CREATE TABLE IF NOT EX...
