import customtkinter as tk
import tkinterDnD

tk.set_ctk_parent_class(tkinterDnD.Tk)

tk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
tk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = tk.CTk()
app.geometry("400x780")
app.title("CustomTkinter simple_example.py")

print(type(app), isinstance(app, tkinterDnD.Tk))

def button_callback():
    print("Button click", combobox_1.get())


def slider_callback(value):
    progressbar_1.set(value)


frame_1 = tk.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = tk.CTkLabel(master=frame_1, justify=tk.LEFT)
label_1.pack(pady=10, padx=10)

progressbar_1 = tk.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=10, padx=10)

button_1 = tk.CTkButton(master=frame_1, command=button_callback)
button_1.pack(pady=10, padx=10)

slider_1 = tk.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=10, padx=10)
slider_1.set(0.5)

entry_1 = tk.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
entry_1.pack(pady=10, padx=10)

optionmenu_1 = tk.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("CTkOptionMenu")

combobox_1 = tk.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("CTkComboBox")

checkbox_1 = tk.CTkCheckBox(master=frame_1)
checkbox_1.pack(pady=10, padx=10)

radiobutton_var = tk.IntVar(value=1)

radiobutton_1 = tk.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
radiobutton_1.pack(pady=10, padx=10)

radiobutton_2 = tk.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
radiobutton_2.pack(pady=10, padx=10)

switch_1 = tk.CTkSwitch(master=frame_1)
switch_1.pack(pady=10, padx=10)

text_1 = tk.CTkTextbox(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "CTkTextbox\n\n\n\n")

segmented_button_1 = tk.CTkSegmentedButton(master=frame_1, values=["CTkSegmentedButton", "Value 2"])
segmented_button_1.pack(pady=10, padx=10)

tabview_1 = tk.CTkTabview(master=frame_1, width=300)
tabview_1.pack(pady=10, padx=10)
tabview_1.add("CTkTabview")
tabview_1.add("Tab 2")

app.mainloop()
