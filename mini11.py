from tkinter import *

root = Tk()
root.title("Scrolling News Reader")


headlines = [f"News Headline {i}" for i in range(1, 25)]

listbox_frame = Frame(root)
listbox_frame.pack()

news_listbox = Listbox(listbox_frame, width=50, height=10)
news_listbox.pack(side=LEFT)

scroll = Scrollbar(listbox_frame)
scroll.pack(side=RIGHT, fill=Y)
news_listbox.config(yscrollcommand=scroll.set)
scroll.config(command=news_listbox.yview)

for headline in headlines:
    news_listbox.insert(END, headline)


def show_details(event):
    selected = news_listbox.get(ACTIVE)
    detail_win = Toplevel(root)
    Label(detail_win, text=selected, wraplength=300).pack(padx=10, pady=10)

news_listbox.bind("<Double-Button-1>", show_details)


def refresh_news():
    news_listbox.delete(0, END)
    new_headlines = [f"Updated Headline {i}" for i in range(1, 25)]
    for item in new_headlines:
        news_listbox.insert(END, item)

Button(root, text="Refresh News", command=refresh_news).pack(pady=5)


def auto_scroll():
    current = news_listbox.yview()[0]
    news_listbox.yview_moveto(current + 0.01)
    root.after(100, auto_scroll)


auto_scroll()

root.mainloop()
