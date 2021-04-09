from tkinter import *

def ok():
    screen2.destroy()
    screen3.destroy()

def ucet():
    global screen3
    screen3 = Tk()
    screen3.geometry("500x150")
    screen3.title("Ucet")
    
    Label(screen3, text = "Ucet", font = "Arial 10").pack()
    Label(screen3, text = "").pack()
    k_p_k = kpk.get()
    k_p_t = kpt.get()
    k_z_k = kzk.get()
    k_z_t = kzt.get()
    u_cet = (4.10 * int(k_p_k) + 4.50 * int(k_p_t) + 3.80 * int(k_z_k) + 4.10 * int(k_z_t))
    Label(screen3, text = round(u_cet, 2)).pack()
    Label(screen3, text = "").pack()
    Button(screen3, text = "ok", width = 10, command = ok).pack()

def kebab():
    global screen2, kpk, kpt, kzk, kzt
    screen2 = Tk()
    screen2.geometry("500x300")
    screen2.title("Pocitanie kebabov")
    
    Label(screen2, text = "Zadaj pocet kebabov", font = "Arial 15").pack()
    Label(screen2, text = "").pack
    Label(screen2, text = "Kebab v placke kuraci").pack()
    kpk = Entry(screen2, width = 5)
    kpk.pack()
    Label(screen2, text = "Kebab v placke telaci").pack()
    kpt = Entry(screen2, width = 5)
    kpt.pack()
    Label(screen2, text = "Kebab v zemli kuraci").pack()
    kzk = Entry(screen2, width = 5)
    kzk.pack()
    Label(screen2, text = "Kebab v zemli telaci").pack()
    kzt = Entry(screen2, width = 5)
    kzt.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Ucet", command = ucet).pack()
    
def uvod():
    screen = Tk()
    screen.geometry("500x200")
    screen.title("Kebab Kalkulacka")
    
    Label(text = "Kebab kalkulacka", font = "Arial 20", width = 500).pack()
    Label(text = "").pack()
    Button(text = "Pocitanie kebabov", width = 20, command = kebab).pack()
    Label(text = "").pack()
    Button(text = "Pocitanie sumy", width = 20).pack()
    
uvod()
