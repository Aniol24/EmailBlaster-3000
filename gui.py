import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ttkthemes import ThemedTk
import csv
import os
import ssl
import smtplib
import random
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()




# ------------------------------
# SEND EMAIL FUNCTION
# ------------------------------
def send_email(to_email, to_name, subject, body, sender, password, sender_name, attachment_path=None):
    msg = EmailMessage()
    msg["From"] = f"{sender_name} <{sender}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body.replace("{name}", to_name if to_name else "bro"))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)


# ------------------------------
# MAIN WINDOW
# ------------------------------
root = ThemedTk(theme="default", themebg=True, toplevel=True)
root.title("Email Blaster 3000")
root.geometry("950x700")
root.configure(bg="black")
root.resizable(False, False)

FONT = ("Terminal", 12)

# ------------------------------
# STYLING
# ------------------------------
style = ttk.Style()
style.configure("TFrame", background="black")
style.configure("TLabel", background="black", foreground="#00ff66")

style.configure("TNotebook", background="black", borderwidth=0)
style.configure("TNotebook.Tab",
                background="black",
                foreground="#00ff66",
                padding=[10, 5],
                font="Terminal 10") 
style.map("TNotebook.Tab",
          background=[("selected", "gray20"), ("active", "black"), ("!active", "black")],
          foreground=[("selected", "#00ff66"), ("active", "#00ff66")],
)
root.after(10, lambda: root.tk.eval('ttk::style configure TNotebook -background black'))

style.configure("Dark.TButton",
                background="black",
                foreground="#00ff66",
                borderwidth=1,
                padding=6,
                focusthickness=0,
                focuscolor="black",
                font="Terminal 10") 
style.map("Dark.TButton",
          background=[("active", "#002200"), ("disabled", "gray20")],
          foreground=[("active", "#00ff66")])

# ------------------------------
# HEADER ASCII
# ------------------------------
header_frame = tk.Frame(root, bg="black", highlightthickness=0, bd=0)
header_frame.pack(fill="x")

ascii_art = r"""
[ MAIL BLASTER 3000 ]
                                                                                                                        
@@@@@@@@  @@@@@@@@@@    @@@@@@   @@@  @@@          @@@@@@@   @@@        @@@@@@    @@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@   
@@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@  @@@          @@@@@@@@  @@@       @@@@@@@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@  
@@!       @@! @@! @@!  @@!  @@@  @@!  @@!          @@!  @@@  @@!       @@!  @@@  !@@         @@!    @@!       @@!  @@@  
!@!       !@! !@! !@!  !@!  @!@  !@!  !@!          !@   @!@  !@!       !@!  @!@  !@!         !@!    !@!       !@!  @!@  
@!!!:!    @!! !!@ @!@  @!@!@!@!  !!@  @!!          @!@!@!@   @!!       @!@!@!@!  !!@@!!      @!!    @!!!:!    @!@!!@!   
!!!!!:    !@!   ! !@!  !!!@!!!!  !!!  !!!          !!!@!!!!  !!!       !!!@!!!!   !!@!!!     !!!    !!!!!:    !!@!@!    
!!:       !!:     !!:  !!:  !!!  !!:  !!:          !!:  !!!  !!:       !!:  !!!       !:!    !!:    !!:       !!: :!!   
:!:       :!:     :!:  :!:  !:!  :!:   :!:         :!:  !:!   :!:      :!:  !:!      !:!     :!:    :!:       :!:  !:!  
 :: ::::  :::     ::   ::   :::   ::   :: ::::      :: ::::   :: ::::  ::   :::  :::: ::      ::     :: ::::  ::   :::  
: :: ::    :      :     :   : :  :    : :: : :     :: : ::   : :: : :   :   : :  :: : :       :     : :: ::    :   : :
"""

tk.Label(header_frame, text=ascii_art, font=("Terminal", 8),
         fg="#00ff66", bg="black", justify="left").pack(padx=5, pady=5)


# ------------------------------
# NOTEBOOK
# ------------------------------
notebook = ttk.Notebook(root, style="TNotebook")
notebook.pack(fill="both", expand=True)


# ------------------------------
# CONSOLE LOG
# ------------------------------
console = tk.Text(root, height=10, bg="#0c0c0c", fg="#00ff66",
                  insertbackground="#00ff66", font=("Terminal", 10),
                  bd=0, relief="flat", highlightthickness=0)
console.pack(fill="x", side="bottom")
console.insert("end", "[*] EMAIL BLASTER READY...\n")

def log(msg):
    console.insert("end", msg + "\n")
    console.see("end")


# ------------------------------
# TAB 1 - CONTACTS
# ------------------------------
tab_contacts = ttk.Frame(notebook, style="TFrame")
notebook.add(tab_contacts, text="DJs List")

contacts = []

empty_label = ttk.Label(tab_contacts, text="No contacts loaded.\nPlease load a CSV file.",
                        font=("Terminal", 10), foreground="#00ff66", background="black", justify="center")
empty_label.pack(pady=20)

contact_frame = ttk.Frame(tab_contacts, style="TFrame")
contact_frame.pack()

scroll_contacts = ttk.Scrollbar(contact_frame, orient="vertical")
scroll_contacts.pack(side="right", fill="y")

listbox = tk.Listbox(contact_frame, width=150, height=22,
                     font=("Terminal", 10), bg="#0f0f0f", fg="#00ff66",
                     selectbackground="#003300", relief="flat",
                     highlightthickness=0, yscrollcommand=scroll_contacts.set)

scroll_contacts.config(command=listbox.yview)


def update_contact_view():
    if contacts:
        empty_label.pack_forget()
        contact_frame.pack()
        listbox.pack(side="left", fill="both", pady=10)
    else:
        contact_frame.pack_forget()
        empty_label.pack(pady=20)


def load_csv():
    global contacts
    path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not path:
        return
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            contacts = [(r.get("email","").strip(), r.get("name","").strip()) for r in reader]
    except Exception as e:
        messagebox.showerror("Error", f"Could not read CSV:\n{e}")
        return

    listbox.delete(0, tk.END)
    for email, name in contacts:
        listbox.insert(tk.END, f"{email} | {name}")
    update_contact_view()
    log(f"[+] Loaded {len(contacts)} contacts")


def clear_contacts():
    contacts.clear()
    listbox.delete(0, tk.END)
    update_contact_view()
    log("[*] Contact list wiped")


update_contact_view()

frame_buttons = ttk.Frame(tab_contacts, style="TFrame")
frame_buttons.pack()

ttk.Button(frame_buttons, text="Load CSV", style="Dark.TButton", command=load_csv).grid(row=0, column=0, padx=10)
ttk.Button(frame_buttons, text="Clear", style="Dark.TButton", command=clear_contacts).grid(row=0, column=1, padx=10)


# ------------------------------
# TAB 2 - EMAIL CONTENT
# ------------------------------
tab_msg = ttk.Frame(notebook, style="TFrame")
notebook.add(tab_msg, text="Email")

frame_msg = ttk.Frame(tab_msg, style="TFrame")
frame_msg.pack(pady=15)

ttk.Label(frame_msg, text="Subject:", font=FONT).pack(pady=5)
entry_subject = tk.Entry(frame_msg, width=45, font=FONT,
                         bg="#1a1a1a", fg="#00ff66", insertbackground="#00ff66",
                         relief="flat", highlightthickness=1, highlightbackground="#003300")
entry_subject.pack()
entry_subject.insert(0, "Subject goes here...")

ttk.Label(frame_msg, text="Message:", font=FONT).pack(pady=10)

text_frame = ttk.Frame(frame_msg, style="TFrame")
text_frame.pack()

scrollbar = ttk.Scrollbar(text_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

text_body = tk.Text(text_frame, width=60, height=15, font=FONT,
                    bg="#0f0f0f", fg="#00ff66", insertbackground="#00ff66",
                    relief="flat", highlightthickness=1, highlightbackground="#003300",
                    yscrollcommand=scrollbar.set)

scrollbar.config(command=text_body.yview)
text_body.pack(side="left", fill="both")

text_body.insert("1.0",
                 "Hey {name},\n\n"
                 "Message body goes here...\n\n")


def generate_fake_serial():
    return "-".join("".join(random.choice("0123456789ABCDEF") for _ in range(4)) for _ in range(4))


def send_all():
    sender = entry_email.get().strip()
    password = entry_password.get().strip()
    sender_name = entry_sender_name.get().strip()
    subject = entry_subject.get().strip()
    body = text_body.get("1.0", tk.END)

    if not sender or not password:
        messagebox.showwarning("Warning", "Fill email + app password in config tab.")
        return
    if not contacts:
        messagebox.showwarning("Warning", "Select CSV first!")
        return

    log("[*] Initiating mass email session...")
    ok = 0
    fails = 0

    for email, name in contacts:
        serial = generate_fake_serial()
        log(f"[+] Serial for {email}: {serial}")
        try:
            send_email(email, name, subject, body, sender, password, sender_name)
            ok += 1
            log(f"[OK] {email}")
        except Exception as e:
            fails += 1
            log(f"[ERR] {email}: {e}")

    messagebox.showinfo("Completed", f"OK: {ok}\nFAILED: {fails}")
    log("[DONE] Session complete")

ttk.Button(tab_msg, text="BLAST!", style="Dark.TButton", command=send_all).pack(pady=20)


# ------------------------------
# TAB 3 - CONFIG
# ------------------------------
tab_config = ttk.Frame(notebook, style="TFrame")
notebook.add(tab_config, text="Config")

config_frame = ttk.Frame(tab_config, style="TFrame")
config_frame.pack(pady=25)

ttk.Label(config_frame, text="Your Email:", font=FONT).pack(pady=5)
entry_email = tk.Entry(config_frame, width=30, font=FONT,
                       bg="#1a1a1a", fg="#00ff66", insertbackground="#00ff66",
                       relief="flat", highlightthickness=1, highlightbackground="#003300")
entry_email.pack()

ttk.Label(config_frame, text="Google App Password:", font=FONT).pack(pady=10)
entry_password = tk.Entry(config_frame, width=30, font=FONT, show="•",
                          bg="#1a1a1a", fg="#00ff66", insertbackground="#00ff66",
                          relief="flat", highlightthickness=1, highlightbackground="#003300")

entry_password.pack()

ttk.Label(config_frame, text="Sender Display Name:", font=FONT).pack(pady=5)
entry_sender_name = tk.Entry(config_frame, width=30, font=FONT,
                             bg="#1a1a1a", fg="#00ff66", insertbackground="#00ff66",
                             relief="flat", highlightthickness=1, highlightbackground="#003300")
entry_sender_name.pack()
entry_sender_name.insert(0, "Your Name")


root.mainloop()
