import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
import requests
import hashlib
from tkinter import messagebox
import sqlite3
#pawned password counter
cnt = -1

def req_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching:{res.status_code},check again')
    return res


def get_password_leak_cnt(hashes, hash_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, cnt in hashes:
        if h == hash_check:
            return cnt
    return 0


def check_pwned(password):
    # check pass word if exists in API
    sha1passwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chars, tail = sha1passwd[:5], sha1passwd[5:]
    respose = req_api_data(first5_chars)
    return get_password_leak_cnt(respose, tail)


def low():
    entry.delete(0, END)

    lent = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, lent):
            password += random.choice(lower)
        return password
    elif var.get() == 2:
        for i in range(0, lent):
            password += random.choice(upper)
        return password
    elif var.get() == 3:
        for i in range(0, lent):
            password += random.choice(digits)
        return password
    else:
        popup(-1, -1)

def generate():
    paswd = low()
    cnt = check_pwned(paswd)
    if cnt > -1:
        popup(cnt,0)
    entry.insert(10, paswd)


def cpy():
    rnp = entry.get()
    pyperclip.copy(rnp)


def popup(cnt,err):
    if err == 0:
        messagebox.showinfo("Passward Breach info", "This password has been pawned " + str(cnt) + " times")
    elif err == -1:
        messagebox.showerror("Error","Please select option !!")


# main function
root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Password Generator")
root.iconbitmap('./Icons_python.ico')

Random_password = Label(root, text='Password')
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

# create Label for length
c_label = Label(root, text="Length")
c_label.grid(row=1)

copy_button = Button(root, text="Copy", command=cpy)
copy_button.grid(row=0, column=2)

genreate_button: Button = Button(root, text="Generate", command=generate)
genreate_button.grid(row=0, column=3)

radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')

radio_med = Radiobutton(root, text="Medium", variable=var, value=2)
radio_med.grid(row=1, column=3, sticky='E')

radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')

combo = Combobox(root, textvariable=var1)
combo['values'] = (8, 10, 12, 16, 32)

combo.current(0)
combo.bind('<<ComboBox>>')
combo.grid(column=1, row=1)

root.mainloop()
