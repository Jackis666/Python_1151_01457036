import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def cov():
    try:
        val=float(tmp.get())
        if mode.get()=="c2f":
            ans=val*9/5+32
            anss.config(text=f"轉換結果：{ans:.2f} °F")
        else:
            ans=(val-32)*5/9
            anss.config(text=f"轉換結果：{ans:.2f} °C")
    except ValueError:
        messagebox.showerror("WA", "WA")
def clear():
    tmp.delete(0, tk.END)
    anss.config(text="轉換結果：")
root=tk.Tk()
root.title("溫度轉換器")
ttk.Label(root,text="請輸入溫度:").grid(row=0,column=0,sticky="w",padx=8,pady=8,columnspan=2)
tmp = ttk.Entry(root, width=36)
tmp.grid(row=1, column=0, padx=8, pady=6,columnspan=2)
mode = tk.StringVar(value="c2f")
ttk.Radiobutton(root, text="攝氏 → 華氏", variable=mode, value="c2f").grid(row=2, column=0, sticky="w", columnspan=2, padx=8)
ttk.Radiobutton(root, text="華氏 → 攝氏", variable=mode, value="f2c").grid(row=3, column=0, sticky="w", columnspan=2, padx=8)
ttk.Button(root, text="轉換", command=cov).grid(row=4, column=0, sticky="ew", padx=4, pady=8)
ttk.Button(root, text="清除", command=clear).grid(row=4, column=1, sticky="ew", padx=4, pady=8)
anss=ttk.Label (root, text="轉換結果：")
anss.grid(row=5, column=0, columnspan=2, sticky="w", padx=8, pady=6)
root.geometry("300x210")
root.mainloop()