from functools import reduce
import customtkinter as tk
import sys
from utils import ElementData

elements = [
    ElementData("Element 1", [
        ElementData.Material("Material 1", "Description 1"),
        ElementData.Material("Material 2", "Description 2"),
        ElementData.Material("Material 3", "Description 3"),
    ]),
    ElementData("Element 2", [
        ElementData.Material("Material 4", "Description 4"),
        ElementData.Material("Material 5", "Description 5"),
        ElementData.Material("Material 6", "Description 6"),
    ]),
    ElementData("Element 3", [
        ElementData.Material("Material 7", "Description 7"),
        ElementData.Material("Material 8", "Description 8"),
        ElementData.Material("Material 9", "Description 9"),
    ]),
    ElementData("Element 4", [
        ElementData.Material("Material 10", "Description 10"),
        ElementData.Material("Material 11", "Description 11"),
        ElementData.Material("Material 12", "Description 12"),
    ]),
]

class PopUp(tk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("PopUp")
        self.geometry("200x200")
        self.label = tk.CTkLabel(self, text="PopUp", font=("Arial", 20))
        self.label.pack(expand=True, fill='both')

class Element(tk.CTkFrame):
    def __init__(self, master, data: ElementData, callback=None, width=200, height=200):
        super().__init__(master, corner_radius=10, border_width=2, width=200, height=200)
        self.data = data
        self.pack_propagate(False) # prevent the frame to resize to the label size

        self.bind("<Button-1>", callback) # call a function when clicked
        self.label = tk.CTkLabel(self, text=data.name, font=("Arial", 20))
        self.label.bind("<Button-1>", callback) # call a function when clicked
        self.label.pack(pady=10, padx=10)

        materials = data.materials if len(data.materials) < 4 else data.materials[:3]
        text = reduce(lambda x, y: x+"\n"+y, [f"{material.name}: {material.description}" for material in materials],"Materiais:")
        self.description = tk.CTkLabel(self, text=text, font=("Arial", 15))
        self.description.bind("<Button-1>", callback) # call a function when clicked
        self.description.pack(side='top', padx=5, pady=5)

class ElementsFrame(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.CTkLabel(self, text="ElementsFrame", font=("Arial", 20))
        self.label.pack(pady=10, padx=10, anchor='w')

        self.elements = tk.CTkFrame(self, corner_radius=10, border_width=2)
        self.elements.pack(expand=True, fill='both', padx=10, pady=10)
        self.showElements(self.elements)

    def showElements(self, frame):
        elementWidth = 150
        elementHeight = 150
        maxAtOneRow = 4
        callback = lambda event: print("Element clicked")
        for i, element in enumerate(elements):
            e = Element(frame, element, callback, width=elementWidth, height=elementHeight)
            e.grid(row=i//maxAtOneRow, column=i%maxAtOneRow, padx=5, pady=5, sticky='w')
        
    def open_popup(self):
        PopUp(self)

class TopFrame(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        buttons = [
            {"text": "Ocultar projetos concluidos", "command": lambda: print("Button 1")},
            {"text": "Criar novo projeto", "command": lambda: print("Button 2")},
            {"text": "Outro comando...", "command": lambda: print("To implement")},
            {"text": "Mais um comando...", "command": lambda: print("To implement")},
        ]
        for button in buttons:
            tk.CTkButton(self,
                text=button["text"],
                command=button["command"],
                width=30,
                height=15,
            ).pack(side='left', padx=5, pady=5)

class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("860x600")

        self.top_frame = TopFrame(self)
        # self.top_frame.grid(row=0, column=0, sticky='nsew')
        self.top_frame.pack()

        self.elements_frame = ElementsFrame(self)
        # self.elements_frame.grid(row=1, column=0)
        self.elements_frame.pack(expand=True, fill='both')

tk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
tk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
app = App()
if(len(sys.argv) > 1): app.resizable(False, False)
app.mainloop()
