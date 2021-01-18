import tkinter
from tkinter import messagebox
from tkinter import ttk


root = tkinter.Tk()
root.title('TicTacToe')
root.style = ttk.Style()

clicked = True
count = 0

def checkifwon():
	global winner
	winner = False

	if ((b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X")
	or(b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X")
	or(b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X")
	or(b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X")
	or(b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X")
	or(b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X")
	or(b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X")
	or(b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X")):
		winner = True
		messagebox.showinfo("Over, X wins")
	elif ((b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O")
	or(b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O")
	or(b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O")
	or(b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O")
	or(b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O")
	or(b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O")
	or(b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O")
	or(b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O")):
		winner = True
		messagebox.showinfo("Over, O wins")


def b_click(b):
	global clicked, count

	if b["text"] == " " and clicked == True:
		b["text"] = "X"
		clicked = False
		count += 1
		checkifwon()
	elif b["text"] == " " and clicked == False:
		b["text"] = "O"
		clicked = True
		count += 1
		checkifwon()
	else:
		messagebox.showerror("box already taken")



b1 = ttk.Button(root, text=" ", command=lambda: b_click(b1))
b2 = ttk.Button(root, text=" ", command=lambda: b_click(b2))
b3 = ttk.Button(root, text=" ", command=lambda: b_click(b3))

b4 = ttk.Button(root, text=" ", command=lambda: b_click(b4))
b5 = ttk.Button(root, text=" ", command=lambda: b_click(b5))
b6 = ttk.Button(root, text=" ", command=lambda: b_click(b6))

b7 = ttk.Button(root, text=" ", command=lambda: b_click(b7))
b8 = ttk.Button(root, text=" ", command=lambda: b_click(b8))
b9 = ttk.Button(root, text=" ", command=lambda: b_click(b9))

# show buttons

b1.grid(row=0, column=0, ipadx=3, ipady=6)
b2.grid(row=0, column=1, ipadx=3, ipady=6)
b3.grid(row=0, column=2, ipadx=3, ipady=6)

b4.grid(row=1, column=0, ipadx=3, ipady=6)
b5.grid(row=1, column=1, ipadx=3, ipady=6)
b6.grid(row=1, column=2, ipadx=3, ipady=6)

b7.grid(row=2, column=0, ipadx=3, ipady=6)
b8.grid(row=2, column=1, ipadx=3, ipady=6)
b9.grid(row=2, column=2, ipadx=3, ipady=6)


root.mainloop()