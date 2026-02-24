import tkinter as tk
from datetime import datetime
from lunardate import LunarDate

CHINESE_MONTHS = [
    "正月", "二月", "三月", "四月", "五月", "六月",
    "七月", "八月", "九月", "十月", "冬月", "腊月"
]

CHINESE_DAYS = [
    "初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
    "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十",
    "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"
]

def get_chinese_date(date):
    lunar = LunarDate.fromSolarDate(date.year, date.month, date.day)
    month_str = ("闰" if lunar.isLeapMonth else "") + CHINESE_MONTHS[lunar.month - 1]
    day_str = CHINESE_DAYS[lunar.day - 1]
    return f"{lunar.year}年 {month_str}{day_str}"

def show_info():
    now = datetime.now()
    gregorian = now.strftime("%A, %d %B %Y")
    time_str = now.strftime("%H:%M:%S")
    chinese = get_chinese_date(now)

    time_label.config(text=f"Time:  {time_str}")
    gregorian_label.config(text=f"Gregorian:  {gregorian}")
    chinese_label.config(text=f"Chinese:  {chinese}")

root = tk.Tk()
root.title("Date & Time")
root.geometry("420x220")
root.resizable(False, False)

tk.Label(root, text="Date & Time Info", font=("Arial", 16, "bold")).pack(pady=10)

time_label = tk.Label(root, text="Time:  —", font=("Arial", 12))
time_label.pack(anchor="w", padx=20)

gregorian_label = tk.Label(root, text="Gregorian:  —", font=("Arial", 12))
gregorian_label.pack(anchor="w", padx=20, pady=4)

chinese_label = tk.Label(root, text="Chinese:  —", font=("Arial", 12))
chinese_label.pack(anchor="w", padx=20)

tk.Button(root, text="Get Date & Time", command=show_info, font=("Arial", 12)).pack(pady=16)

root.mainloop()
