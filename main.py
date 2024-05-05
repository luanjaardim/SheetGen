from functools import reduce
import customtkinter as tk
from tkcalendar import Calendar, DateEntry
import sys
import datetime as dt
from utils import ElementData, showObjs

showFinalized = True

elements = [
    ElementData("Galpao 1", [
        ElementData.Material("Material 1", "Description 1"),
        ElementData.Material("Material 2", "Description 2"),
        ElementData.Material("Material 3", "Description 3"),
    ]),
    ElementData("Galpao 2", [
        ElementData.Material("Material 4", "Description 4"),
        ElementData.Material("Material 5", "Description 5"),
        ElementData.Material("Material 6", "Description 6"),
    ], [
        dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        dt.datetime(2022, 12, 31).strftime("%d/%m/%Y %H:%M:%S"),
    ]),
    ElementData("Galpao 3", [
        ElementData.Material("Material 7", "Description 7"),
        ElementData.Material("Material 8", "Description 8"),
        ElementData.Material("Material 9", "Description 9"),
    ]),
    ElementData("Galpao 4", [
        ElementData.Material("Material 10", "Description 10"),
        ElementData.Material("Material 11", "Description 11"),
        ElementData.Material("Material 12", "Description 12"),
    ]),
]
elements[0].finalized = True

class PopUp(tk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Detalhes do projeto")
        self.geometry("600x400")
        self.resizable(False, False)

class Element(tk.CTkFrame):
    def __init__(self, master, data: ElementData, callback=None, width=200, height=200):
        super().__init__(master, corner_radius=10, border_width=2, width=200, height=200)
        self.data = data
        self.pack_propagate(False) # prevent the frame to resize to the label size

        callback = self.open_popup if callback is None else callback

        self.bind("<Button-1>", callback) # call a function when clicked
        self.label = tk.CTkLabel(self, text=data.name, font=("Arial", 20))
        self.label.bind("<Button-1>", callback) # call a function when clicked
        self.label.pack(pady=10, padx=10)

        self.reminder_frame = tk.CTkFrame(self, corner_radius=10, border_width=2)
        self.reminder_frame.bind("<Button-1>", callback) # call a function when clicked
        self.reminder_frame.pack(expand=True, fill='both', padx=10, pady=10)

        self.reminder = "Lembretes:\n" + "\n".join(data.reminders) if data.reminders else "Sem lembretes"
        self.description = tk.CTkLabel(self.reminder_frame, text=self.reminder, font=("Arial", 15))
        self.description.bind("<Button-1>", callback) # call a function when clicked
        self.description.pack(side='top', padx=5, pady=5, anchor='w')
        
    def open_popup(self, event):
        pop = PopUp(self)
        label = tk.CTkLabel(pop, text=self.data.name, font=("Arial", 20))
        label.pack(pady=10, padx=10, anchor='w')

        frame_reminder = tk.CTkFrame(pop, corner_radius=10, border_width=2)
        frame_reminder.pack(expand=True, fill='both', padx=10, pady=10)

        date = DateEntry(frame_reminder, width=12, background='darkblue', foreground='white', borderwidth=2)
        date.pack(pady=10, padx=10, anchor='ne', side='right')

        reminders = tk.CTkLabel(frame_reminder, text=self.reminder, font=("Arial", 17))
        reminders.pack(side='top', padx=5, pady=5)

        frame_materials = tk.CTkFrame(pop, corner_radius=10, border_width=2)
        frame_materials.pack(expand=True, fill='both', padx=10, pady=10)
        #show materials
        text = reduce(lambda x, y: x+"\n"+y, [f"{material.name}: {material.description}" for material in self.data.materials],"Materiais:")
        materials = tk.CTkLabel(frame_materials, text=text, font=("Arial", 17))
        materials.pack(side='top', padx=5, pady=5)
    
    def add_reminder(self):
        print('To implement')

class ElementsFrame(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.CTkLabel(self, text="Projetos", font=("Arial", 20))
        self.label.pack(pady=10, padx=10, anchor='w')

        self.elements = tk.CTkFrame(self, corner_radius=10, border_width=2)
        self.elements.pack(expand=True, fill='both', padx=10, pady=10)
        self.showElements(self.elements)

    def showElements(self, frame):
        elementWidth = 150
        elementHeight = 150
        
        maxAtOneRow = 4
        i = 0
        for e_data in elements:
            if not showFinalized and e_data.finalized: continue
            e = Element(frame, e_data, callback=None, width=elementWidth, height=elementHeight)
            e.grid(row=i//maxAtOneRow, column=i%maxAtOneRow, padx=5, pady=5, sticky='w')
            i += 1

class TopFrame(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        buttons = [
            {"text": "Ocultar projetos concluidos", "command": self.hideFinalized },
            {"text": "Criar novo projeto", "command": self.createNewElement },
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

    def hideFinalized(self):
        global showFinalized
        showFinalized = not showFinalized
        self.master.reload_elements()

    def createNewElement(self):
        pop = PopUp(self.master)
        label = tk.CTkLabel(pop, text="Criar novo projeto", font=("Arial", 20))
        label.pack(pady=10, padx=10, anchor='w')

        #make frame scrollable
        frame = tk.CTkScrollableFrame(pop, corner_radius=10, border_width=2)
        frame.pack(expand=True, fill='both', padx=10, pady=10)

        tk.CTkLabel(frame, text="Nome do projeto:", font=("Arial", 17)).pack(side='top', padx=5, pady=5, anchor='w')
        name = tk.CTkEntry(frame, font=("Arial", 15))
        name.pack(side='top', padx=5, pady=5, anchor='w')

        tk.CTkLabel(frame, text="Materiais:", font=("Arial", 17)).pack(side='top', padx=5, pady=5, anchor='w')
        materials = tk.CTkEntry(frame, font=("Arial", 15))
        materials.pack(side='top', padx=5, pady=5, anchor='w')

        def appendElement(name, materials):
            elements.append(ElementData(name, [ElementData.Material(material, "") for material in materials.split(",")]))
            pop.destroy()
            self.master.reload_elements()

        create_button = tk.CTkButton(frame, text="Criar", command=lambda: appendElement(name.get(), materials.get()))
        create_button.pack(side='top', padx=5, pady=5, anchor='w')

        cancel_button = tk.CTkButton(frame, text="Cancelar", command=pop.destroy)
        cancel_button.pack(side='top', padx=5, pady=5, anchor='w')

        showObjs(frame)

class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de projetos")
        self.geometry("860x600")

        self.top_frame = TopFrame(self)
        # self.top_frame.grid(row=0, column=0, sticky='nsew')
        self.top_frame.pack()

        self.elements_frame = ElementsFrame(self)
        # self.elements_frame.grid(row=1, column=0)
        self.elements_frame.pack(expand=True, fill='both')

    def reload_elements(self):
        self.elements_frame.destroy()
        self.elements_frame = ElementsFrame(self)
        self.elements_frame.pack(expand=True, fill='both')

tk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
tk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
app = App()
if(len(sys.argv) > 1): app.resizable(False, False)
app.mainloop()
