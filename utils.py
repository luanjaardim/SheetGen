class ElementData:
    class Material:
        def __init__(self, name: str, description: str):
            self.name = name
            self.description = description
            self.quantity = 0
            self.price = 0.0

        def totalPrice(self) -> float:
            return self.quantity * self.price

    def __init__(self, name: str, materials: list[Material] = [], reminders: list[str] = []):
        self.name = name
        self.materials = materials
        self.finalized = False
        self.reminders = reminders

# temporary function to show the objects
def showObjs(frame):
    import customtkinter as tk

    progressbar_1 = tk.CTkProgressBar(master=frame)
    progressbar_1.pack(pady=10, padx=10)

    button_1 = tk.CTkButton(master=frame, command=lambda: print("Button click", combobox_1.get()))
    button_1.pack(pady=10, padx=10)

    slider_1 = tk.CTkSlider(master=frame, command=lambda: print("sla"), from_=0, to=1)
    slider_1.pack(pady=10, padx=10)
    slider_1.set(0.5)

    entry_1 = tk.CTkEntry(master=frame, placeholder_text="CTkEntry")
    entry_1.pack(pady=10, padx=10)

    optionmenu_1 = tk.CTkOptionMenu(frame, values=["Option 1", "Option 2", "Option 42 long long long..."])
    optionmenu_1.pack(pady=10, padx=10)
    optionmenu_1.set("CTkOptionMenu")

    combobox_1 = tk.CTkComboBox(frame, values=["Option 1", "Option 2", "Option 42 long long long..."])
    combobox_1.pack(pady=10, padx=10)
    combobox_1.set("CTkComboBox")

    checkbox_1 = tk.CTkCheckBox(master=frame)
    checkbox_1.pack(pady=10, padx=10)

    radiobutton_var = tk.IntVar(value=1)

    radiobutton_1 = tk.CTkRadioButton(master=frame, variable=radiobutton_var, value=1)
    radiobutton_1.pack(pady=10, padx=10)

    radiobutton_2 = tk.CTkRadioButton(master=frame, variable=radiobutton_var, value=2)
    radiobutton_2.pack(pady=10, padx=10)

    switch_1 = tk.CTkSwitch(master=frame)
    switch_1.pack(pady=10, padx=10)

    text_1 = tk.CTkTextbox(master=frame, width=200, height=70)
    text_1.pack(pady=10, padx=10)
    text_1.insert("0.0", "CTkTextbox\n\n\n\n")

    segmented_button_1 = tk.CTkSegmentedButton(master=frame, values=["CTkSegmentedButton", "Value 2"])
    segmented_button_1.pack(pady=10, padx=10)

    tabview_1 = tk.CTkTabview(master=frame, width=300)
    tabview_1.pack(pady=10, padx=10)
    tabview_1.add("CTkTabview")
    tabview_1.add("Tab 2")
