import tkinter
import tkinter.messagebox
import customtkinter
from Database import *
# from tkinter import ttk

customtkinter.set_appearance_mode("System")     # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        # configure window
        self.title("Farming 2022 Field-Yeald Calc :3")
        self.geometry(f"{1100}x{600}")


        # configure grid layout (3x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 2), weight=1)


        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Poziom Trudności", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text='Łatwy', command=self.sidebar_button_easy)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text='Średni', command=self.sidebar_button_medium)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text='Trudny', command=self.sidebar_button_hard)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Wygląd:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Skalowanie UI:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250, state='normal')
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")


        # # earning and losss progress bar
        self.progressbar_frame = customtkinter.CTkFrame(self)
        self.progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 10), sticky="new")
        self.progressbar_frame.grid_columnconfigure(0, weight=1)

        self.progressbar_loss = customtkinter.CTkProgressBar(self.progressbar_frame,progress_color='indianred4')
        self.progressbar_loss.grid(row=0, column=0, padx=(10, 10), pady=(20, 10), sticky="new")
        self.progressbar_earning = customtkinter.CTkProgressBar(self.progressbar_frame)
        self.progressbar_earning.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="new")


        # create frame, main entry & spinbox,and button
        self.entry_frame = customtkinter.CTkFrame(self)
        self.entry_frame.grid(row=2, column=1, padx=(20, 0), pady=(0, 10), sticky="nsew")

        self.entry_frame.grid_columnconfigure(0, weight=1)
        self.entry = customtkinter.CTkEntry(self.entry_frame, placeholder_text="Wprowadź wielkość pola")
        self.entry.grid(row=1, column=0, columnspan=1, padx=(20, 0), pady=(10, 20), sticky="nwe")

        self.main_button_1 = customtkinter.CTkButton(master=self.entry_frame, fg_color="transparent", text='Oblicz', border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=1, column=1, padx=(20, 10), pady=(10, 20), sticky="ne")


        # price frame
        self.price_frame = customtkinter.CTkFrame(self.entry_frame)
        self.price_frame.grid(row=2, column=0,columnspan=2, padx=(10, 10), pady=(0, 10), sticky="nsew")
        self.price_frame.grid_columnconfigure((0, 1, 2),weight=1)

        self.label_price_frame = customtkinter.CTkLabel(master=self.price_frame, text="Cena")
        self.label_price_frame.grid(row=0, column=1, columnspan=1, padx=10, pady=(10,0), sticky="n")

        self.price_button_1 = customtkinter.CTkButton(self.price_frame, text='Średnia',
                                                        command=self.sidebar_button_average)
        self.price_button_1.grid(row=1, column=0, padx=(5, 5), pady=10, sticky='new')

        self.price_button_2 = customtkinter.CTkButton(self.price_frame, text='Dobra',
                                                      command=self.sidebar_button_good)
        self.price_button_2.grid(row=1, column=1, padx=(5, 5), pady=10, sticky='new')

        self.price_button_3 = customtkinter.CTkButton(self.price_frame, text='Najlepsza',
                                                      command=self.sidebar_button_best)
        self.price_button_3.grid(row=1, column=2, padx=(5, 5), pady=10, sticky='new')


        # Log box entry savestate

        self.log_save_frame = customtkinter.CTkFrame(self.entry_frame, bg_color='transparent',)
        self.log_save_frame.grid(row=3, column=0, columnspan=1, padx=(10, 0), pady=(0, 10), sticky="nsew")
        self.log_save_frame.grid_columnconfigure((0, 2), weight=1)

        self.entry = customtkinter.CTkEntry(self.log_save_frame, placeholder_text="Wprowadź wielkość pola")
        self.entry.grid(row=0, column=0, padx=(5, 0), pady=(10, 10), sticky="nwe")

        self.log_price_entry = customtkinter.CTkEntry(self.log_save_frame, placeholder_text="Wprowadź cenę sprzedaży")
        self.log_price_entry.grid(row=0, column=2, padx=(10, 10), pady=(10, 10), sticky="nwe")

        self.log_save_button = customtkinter.CTkButton(master=self.entry_frame, fg_color="transparent", text='Zapisz LOG',
                                                     border_width=2, text_color=("gray10", "#DCE4EE"))
        self.log_save_button.grid(row=3, column=1, padx=(10, 10), pady=(10, 20), sticky="ne")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(2, 0), sticky="nsew")
        self.tabview.add("Uprawa")
        self.tabview.add("Nawóz")
        self.tabview.tab("Uprawa").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Nawóz").grid_columnconfigure(0, weight=1)


        #combobox
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Uprawa"), command=self.optionmenu_event(), dynamic_resizing=False,
                                                                                    values=['Pszenica', 'Jęczmień', 'Owies', 'Rzepak', 'Sorgo',
                                                                                            'Winogrono', 'Oliwki', 'Słonecznik', 'Soja', 'Kukurydza',
                                                                                            'Ziemniaki', 'Buraki Cukrowe', 'Bawełna', 'Trzcina Cukrowa',
                                                                                            'Topola', 'Trawa'])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.tabview.tab("Uprawa"),text='Pszczoły  +5%')
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="nw")

        self.radio_var0 = tkinter.IntVar(value=0)
        self.radio_button_0 = customtkinter.CTkRadioButton(master=self.tabview.tab("Uprawa"),text='Herbicyd  -15%', variable=self.radio_var0, value=0)
        self.radio_button_0.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="nw")

        self.radio_button_01 = customtkinter.CTkRadioButton(master=self.tabview.tab("Uprawa"),text='Pielnik  +0%', variable=self.radio_var0, value=1)
        self.radio_button_01.grid(row=3, column=0, pady=20, padx=20, sticky="nw")


        # Tab 2 configuration

        self.scrollable_frame1 = customtkinter.CTkScrollableFrame(self.tabview.tab("Nawóz"))
        self.scrollable_frame1.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.scrollable_frame1.grid_columnconfigure(0, weight=1)


        # First fertilizing
        self.first_fertilizing = customtkinter.CTkFrame(self.scrollable_frame1)
        self.first_fertilizing.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        self.label_first_fertilizing = customtkinter.CTkLabel(master=self.first_fertilizing, text="Pierwsze nawożenie")
        self.label_first_fertilizing.grid(row=0, column=0, padx=60, pady=(10, 0), sticky="nsew")

        self.radio_var1 = tkinter.IntVar(value=0)

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.first_fertilizing, text='Rzodkiew oleista', variable=self.radio_var1, value=0)
        self.radio_button_1.grid(row=1, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.first_fertilizing,text='Nawóz płynny', variable=self.radio_var1, value=1)
        self.radio_button_2.grid(row=2, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.first_fertilizing,text='Nawóz stały', variable=self.radio_var1, value=2)
        self.radio_button_3.grid(row=3, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_4 = customtkinter.CTkRadioButton(master=self.first_fertilizing,text='Gnojówka', variable=self.radio_var1, value=3)
        self.radio_button_4.grid(row=4, column=0, pady=10, padx=20, sticky="nw")


        # second fertilizing
        self.second_fertilizing = customtkinter.CTkFrame(self.scrollable_frame1)
        self.second_fertilizing.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        self.label_second_fertilizing = customtkinter.CTkLabel(master=self.second_fertilizing, text="Drugie nawożenie")
        self.label_second_fertilizing.grid(row=0, column=0, padx=60, pady=(10, 0), sticky="nsew")

        self.radio_var2 = tkinter.IntVar(value=0)

        self.radio_button_5 = customtkinter.CTkRadioButton(master=self.second_fertilizing,text='Nawóz płynny', variable=self.radio_var2, value=0)
        self.radio_button_5.grid(row=1, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_6 = customtkinter.CTkRadioButton(master=self.second_fertilizing,text='Nawóz stały', variable=self.radio_var2, value=1)
        self.radio_button_6.grid(row=2, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_7 = customtkinter.CTkRadioButton(master=self.second_fertilizing,text='Gnojówka', variable=self.radio_var2, value=2)
        self.radio_button_7.grid(row=3, column=0, pady=10, padx=20, sticky="nw")


        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Ulepszenia pola")
        self.scrollable_frame.grid(row=1,rowspan=2, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        switch1 = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"1 Nawożenie +22,5%").grid    (row=1, column=0, padx=10, pady=(0, 20), sticky='w')
        switch2 = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"2 Nawożenie +22,5%").grid    (row=2, column=0, padx=10, pady=(0, 20), sticky='w')
        switch3 = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"Oranie +15%").grid           (row=3, column=0, padx=10, pady=(0, 20), sticky='w')
        switch4 = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"Wapnowanie +15%").grid       (row=4, column=0, padx=10, pady=(0, 20), sticky='w')
        switch5 = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"Odchwaszczanie +15%").grid   (row=5, column=0, padx=10, pady=(0, 20), sticky='w')
        switch6 = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"Wałowanie +2,5%").grid       (row=6, column=0, padx=10, pady=(0, 20), sticky='w')
        switch7 = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"Mulczowanie +2,5%").grid     (row=7, column=0, padx=10, pady=(0, 20), sticky='w')


        # events


        # set default values

        self.checkbox_1.select()
        # self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("Uprawa")

        self.progressbar_earning.set(.3)
        self.textbox.insert("0.0", "Command Window\n\n" + "Tu będzie output programu.\n\n")

# Apperance mode
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
# Scaling Change
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

# Option menu
    def optionmenu_event(self):
        pass

# Radio Buttton

# scrolable bar switches
    def switch1(value):
        print(f'{value}')



# Sidebar

    def sidebar_button_easy(self):
        print("Wybrano Łatwy poziom trudności")
    def sidebar_button_medium(self):
        print("Wybrano Średni poziom trudności")
    def sidebar_button_hard(self):
        print("Wybrano Trudny trudności")
    def sidebar_button_average(self):
        print("Wybrano średnią cenę")
    def sidebar_button_good(self):
        print("Wybrano dobrą cenę")
    def sidebar_button_best(self):
        print("Wybrano najlepszą cenę")

if __name__ == "__main__":
    app = App()
    app.mainloop()