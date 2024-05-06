import tkinter.messagebox
import customtkinter
from Database_dictionary import *
import datetime

customtkinter.set_appearance_mode("System")     # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    def __init__(self):
        super(App, self).__init__()

        self.title("UnOfficial Farming 2022 Calculator CLASS")
        self.geometry(f"{1100}x{600}")
        self.minsize(1100, 600)

        # configure grid layout (3x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="Trudność\nGospodarcza",
            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        sidebar_var = customtkinter.StringVar(value='Normal_prices')

        def sidebar_button_1_event():
            sidebar_var.set(value='Easy_prices')
            # textbox.insert('end', f'\n\nŁatwy {sidebar_var.get()}')
            # textbox.see('end')
            self.sidebar_button_1.configure(state='disable', fg_color='#2FA572')
            self.sidebar_button_2.configure(state='normal', fg_color='grey')
            self.sidebar_button_3.configure(state='normal', fg_color='grey')

        self.sidebar_button_1 = customtkinter.CTkButton(
            self.sidebar_frame,
            text='Łatwa',
            command=sidebar_button_1_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        def sidebar_button_2_event():
            sidebar_var.set(value='Normal_prices')
            # textbox.insert('end', f'\n\nŚredni {sidebar_var.get()}')
            # textbox.see('end')
            self.sidebar_button_1.configure(state='normal', fg_color='grey')
            self.sidebar_button_2.configure(state='disable', fg_color='#2FA572')
            self.sidebar_button_3.configure(state='normal', fg_color='grey')

        self.sidebar_button_2 = customtkinter.CTkButton(
            self.sidebar_frame,
            text='Średnia',
            command=sidebar_button_2_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        def sidebar_button_3_event():
            sidebar_var.set(value='Hard_prices')
            # textbox.insert('end', f'\n\nTrudny {sidebar_var.get()}')
            # textbox.see('end')
            self.sidebar_button_1.configure(state='normal', fg_color='grey')
            self.sidebar_button_2.configure(state='normal', fg_color='grey')
            self.sidebar_button_3.configure(state='disable', fg_color='#2FA572')

        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame,
            text='Trudna',
            command=sidebar_button_3_event)

        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        def appearance_mode_change(value):
            customtkinter.set_appearance_mode(value)

        appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="Wygląd:",
            anchor="w")
        appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        appearance_mode_option_menu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=appearance_mode_change)

        appearance_mode_option_menu.grid(row=6, column=0, padx=20, pady=(10, 10))

        def change_scaling_event(new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            customtkinter.set_widget_scaling(new_scaling_float)

        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="Skalowanie UI:",
            anchor="w")

        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_option_menu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=change_scaling_event)

        self.scaling_option_menu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self,
                                                width=250,
                                                state='normal',
                                                wrap='word')

        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # earning and loss progress bar
        self.progressbar_frame = customtkinter.CTkFrame(self)
        self.progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 10), sticky="new")
        self.progressbar_frame.grid_columnconfigure(0, weight=1)

        progressbar_loss_variable = customtkinter.DoubleVar(value=0)
        self.progressbar_loss = customtkinter.CTkProgressBar(
            self.progressbar_frame,
            progress_color='indianred4',
            variable=progressbar_loss_variable)

        self.progressbar_loss.grid(row=0, column=0, padx=(10, 10), pady=(20, 10), sticky="new")

        progressbar_earning_variable = customtkinter.DoubleVar(value=0)
        self.progressbar_earning = customtkinter.CTkProgressBar(
            self.progressbar_frame,
            variable=progressbar_earning_variable)

        self.progressbar_earning.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="new")

        # create frame, main entry & spinbox,and button
        self.entry_frame = customtkinter.CTkFrame(self)
        self.entry_frame.grid(row=2, column=1, padx=(20, 0), pady=(0, 0), sticky="nsew")
        self.entry_frame.grid_columnconfigure(0, weight=1)

        entry_var = tkinter.DoubleVar(value=0.5)

        self.entry = customtkinter.CTkEntry(
            self.entry_frame,
            placeholder_text="Wprowadź wielkość pola",
            textvariable=entry_var)

        self.entry.grid(row=1, column=0, columnspan=1, padx=(20, 0), pady=(10, 20), sticky="nwe")

        def main_button_1_event():
            calculate()

        self.main_button_1 = customtkinter.CTkButton(
            master=self.entry_frame,
            command=main_button_1_event,
            fg_color="transparent",
            text='Oblicz', border_width=2,
            text_color=("gray10", "#DCE4EE"))

        self.main_button_1.grid(row=1, column=1, padx=(20, 10), pady=(10, 20), sticky="ne")

        # price frame
        self.price_frame = customtkinter.CTkFrame(self.entry_frame)
        self.price_frame.grid(row=2, column=0, columnspan=2, padx=(10, 10), pady=(0, 10), sticky="nsew")
        self.price_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.label_price_frame = customtkinter.CTkLabel(
            master=self.price_frame,
            text="Cena",
            font=customtkinter.CTkFont(size=20, weight='bold'))

        self.label_price_frame.grid(row=0, column=1, columnspan=1, padx=10, pady=(10, 0), sticky="n")

        price_var = customtkinter.IntVar(value=0)

        def price_button_1_event():
            price_var.set(value=0)
            self.price_button_1.configure(state='disable', fg_color='#2FA572')
            self.price_button_2.configure(state='normal', fg_color='grey')
            self.price_button_3.configure(state='normal', fg_color='grey')

        self.price_button_1 = customtkinter.CTkButton(self.price_frame, text='Średnia', command=price_button_1_event)
        self.price_button_1.grid(row=1, column=0, padx=(5, 5), pady=10, sticky='new')

        def price_button_2_event():
            price_var.set(value=1)
            self.price_button_1.configure(state='normal', fg_color='grey')
            self.price_button_2.configure(state='disable', fg_color='#2FA572')
            self.price_button_3.configure(state='normal', fg_color='grey')

        self.price_button_2 = customtkinter.CTkButton(self.price_frame, text='Dobra', command=price_button_2_event)
        self.price_button_2.grid(row=1, column=1, padx=(5, 5), pady=10, sticky='new')

        def price_button_3_event():
            price_var.set(value=2)
            self.price_button_1.configure(state='normal', fg_color='grey')
            self.price_button_2.configure(state='normal', fg_color='grey')
            self.price_button_3.configure(state='disable', fg_color='#2FA572')

        self.price_button_3 = customtkinter.CTkButton(
            self.price_frame,
            text='Najlepsza',
            command=price_button_3_event)

        self.price_button_3.grid(row=1, column=2, padx=(5, 5), pady=10, sticky='new')

        # Log box entry savestate
        self.log_save_frame = customtkinter.CTkFrame(
            self.entry_frame,
            fg_color='transparent')

        self.log_save_frame.grid(row=3, column=0, columnspan=1, padx=(10, 0), pady=(0, 10), sticky="nsew")
        self.log_save_frame.grid_columnconfigure((0, 2), weight=1)

        self.entry = customtkinter.CTkEntry(
            self.log_save_frame,
            placeholder_text="Wprowadź wielkość pola",
            textvariable=entry_var)
        self.entry.grid(row=0, column=0, padx=(5, 0), pady=(10, 10), sticky="nwe")

        log_price_entry_var = tkinter.IntVar(value=0)
        log_price_entry = customtkinter.CTkEntry(self.log_save_frame,
                                                 placeholder_text="Wprowadź cenę sprzedaży",
                                                 textvariable=log_price_entry_var)
        log_price_entry.grid(row=0, column=2, padx=(10, 10), pady=(10, 10), sticky="nwe")

        def log_save_button_event():
            log_save()
            self.textbox.insert('end', f'\n\nLog zapisany')
            self.textbox.see('end')

        self.log_save_button = customtkinter.CTkButton(master=self.entry_frame,
                                                       fg_color="transparent",
                                                       text='Zapisz LOG',
                                                       command=log_save_button_event,
                                                       border_width=2,
                                                       text_color=("gray10", "#DCE4EE"))
        self.log_save_button.grid(row=3, column=1, padx=(10, 10), pady=(10, 20), sticky="ne")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(2, 0), sticky="nsew")
        self.tabview.add("Uprawa")
        self.tabview.add("Nawóz")
        self.tabview.tab("Uprawa").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Nawóz").grid_columnconfigure(0, weight=1)
        self.tabview.tab('Nawóz').grid_rowconfigure(0, weight=1)

        # combobox
        def self_option_menu_1_event(value):
            check_bees()
            check_straw()

        option_menu_1_var = customtkinter.StringVar(value='Pszenica')
        self.option_menu_1 = customtkinter.CTkOptionMenu(
            self.tabview.tab("Uprawa"),
            variable=option_menu_1_var,
            dynamic_resizing=False,
            command=self_option_menu_1_event,
            values=['Pszenica', 'Jęczmień', 'Owies', 'Rzepak', 'Sorgo',
                    'Winogrono', 'Oliwki', 'Słonecznik', 'Soja', 'Kukurydza',
                    'Ziemniaki', 'Buraki cukrowe', 'Bawełna', 'Trzcina cukrowa', 'Topola', 'Trawa'])
        self.option_menu_1.grid(row=0, column=0, padx=20, pady=(20, 10))

        def checkbox_1_event():
            check_bees()

        checkbox_1_text_var = customtkinter.StringVar(value='Pszczoły +5%')
        checkbox_1_var = customtkinter.IntVar(value=0)
        self.checkbox_1 = customtkinter.CTkCheckBox(
            master=self.tabview.tab("Uprawa"),
            textvariable=checkbox_1_text_var,
            command=checkbox_1_event,
            offvalue=0,
            onvalue=1,
            variable=checkbox_1_var)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="nw")

        def checkbox_2_event():
            check_straw()

        checkbox_2_var = customtkinter.IntVar(value=0)
        self.checkbox_2 = customtkinter.CTkCheckBox(
            master=self.tabview.tab("Uprawa"),
            text='Słoma',
            command=checkbox_2_event, offvalue=0, onvalue=1, variable=checkbox_2_var)
        self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="nw")

        def radio_button_0_event():
            pass

        radio_var0 = tkinter.IntVar(value=0)

        self.radio_button_0 = customtkinter.CTkRadioButton(
            master=self.tabview.tab("Uprawa"),
            command=radio_button_0_event,
            text='Herbicyd  -15%',
            variable=radio_var0, value=1)
        self.radio_button_0.grid(row=3, column=0, pady=(20, 0), padx=20, sticky="nw")

        self.radio_button_01 = customtkinter.CTkRadioButton(
            master=self.tabview.tab("Uprawa"),
            command=radio_button_0_event,
            text='Pielnik  +0%', variable=radio_var0, value=0)
        self.radio_button_01.grid(row=4, column=0, pady=20, padx=20, sticky="nw")

        # Tab 2 configuration
        self.scrollable_frame1 = customtkinter.CTkScrollableFrame(self.tabview.tab("Nawóz"))
        self.scrollable_frame1.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        # First fertilizing
        self.first_fertilizing = customtkinter.CTkFrame(self.scrollable_frame1)
        self.first_fertilizing.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        self.label_first_fertilizing = customtkinter.CTkLabel(master=self.first_fertilizing, text="Pierwsze nawożenie")
        self.label_first_fertilizing.grid(row=0, column=0, padx=60, pady=(10, 0), sticky="nsew")

        def radio_button_1_event():
            pass

        radio_var1 = tkinter.StringVar(value='Nawóz płynny')

        self.radio_button_1 = customtkinter.CTkRadioButton(
            master=self.first_fertilizing,
            command=radio_button_1_event,
            text='Rzodkiew oleista',
            variable=radio_var1,
            value='Rzodkiew oleista')
        self.radio_button_1.grid(row=1, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_2 = customtkinter.CTkRadioButton(
            master=self.first_fertilizing,
            command=radio_button_1_event,
            text='Nawóz płynny',
            variable=radio_var1,
            value='Nawóz płynny')
        self.radio_button_2.grid(row=2, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_3 = customtkinter.CTkRadioButton(
            master=self.first_fertilizing,
            command=radio_button_1_event,
            text='Nawóz stały',
            variable=radio_var1,
            value='Nawóz stały')
        self.radio_button_3.grid(row=3, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_4 = customtkinter.CTkRadioButton(
            master=self.first_fertilizing,
            command=radio_button_1_event,
            text='Gnojówka',
            variable=radio_var1,
            value='Gnojówka')
        self.radio_button_4.grid(row=4, column=0, pady=10, padx=20, sticky="nw")

        # second fertilizing
        self.second_fertilizing = customtkinter.CTkFrame(self.scrollable_frame1)
        self.second_fertilizing.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        self.label_second_fertilizing = customtkinter.CTkLabel(
            master=self.second_fertilizing,
            text="Drugie nawożenie")
        self.label_second_fertilizing.grid(row=0, column=0, padx=60, pady=(10, 0), sticky="nsew")

        def radio_button_2_event():
            pass

        radio_var2 = tkinter.StringVar(value='Nawóz płynny')

        self.radio_button_5 = customtkinter.CTkRadioButton(
            master=self.second_fertilizing,
            command=radio_button_2_event,
            text='Nawóz płynny',
            variable=radio_var2,
            value='Nawóz płynny')
        self.radio_button_5.grid(row=1, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_6 = customtkinter.CTkRadioButton(
            master=self.second_fertilizing,
            command=radio_button_2_event,
            text='Nawóz stały',
            variable=radio_var2,
            value='Nawóz stały')
        self.radio_button_6.grid(row=2, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_7 = customtkinter.CTkRadioButton(
            master=self.second_fertilizing,
            command=radio_button_2_event,
            text='Gnojówka',
            variable=radio_var2,
            value='Gnojówka')
        self.radio_button_7.grid(row=3, column=0, pady=10, padx=20, sticky="nw")

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Ulepszenia pola")
        self.scrollable_frame.grid(row=1, rowspan=2, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        def switch1_event():
            pass

        switch1_var = customtkinter.IntVar(value=1)
        self.switch1 = (customtkinter.CTkSwitch(
            master=self.scrollable_frame,
            text=f"1 Nawożenie +22,5%",
            onvalue=1,
            offvalue=0,
            variable=switch1_var,
            command=switch1_event).grid(row=1, column=0, padx=10, pady=(0, 20), sticky='w'))

        def switch2_event():
            pass

        switch2_var = customtkinter.IntVar(value=1)
        self.switch2 = (customtkinter.CTkSwitch(
            master=self.scrollable_frame,
            text=f"2 Nawożenie +22,5%",
            onvalue=1,
            offvalue=0,
            variable=switch2_var,
            command=switch2_event).grid(row=2, column=0, padx=10, pady=(0, 20), sticky='w'))

        def switch3_event():
            pass

        switch3_var = customtkinter.IntVar(value=1)
        self.switch3 = (customtkinter.CTkSwitch(
            master=self.scrollable_frame,
            text=f"Oranie +15%",
            onvalue=1,
            offvalue=0,
            variable=switch3_var,
            command=switch3_event).grid(row=3, column=0, padx=10, pady=(0, 20), sticky='w'))

        def switch4_event():
            pass

        switch4_var = customtkinter.IntVar(value=1)
        self.switch4 = (customtkinter.CTkSwitch(
            master=self.scrollable_frame,
            text=f"Wapnowanie +15%",
            onvalue=1,
            offvalue=0,
            variable=switch4_var,
            command=switch4_event).grid(row=4, column=0, padx=10, pady=(0, 20), sticky='w'))

        def switch5_event():
            pass

        switch5_var = customtkinter.IntVar(value=1)
        self.switch5 = (customtkinter.CTkSwitch(
            master=self.scrollable_frame,
            text=f"Odchwaszczanie +15%",
            onvalue=1,
            offvalue=0,
            variable=switch5_var,
            command=switch5_event).grid(row=5, column=0, padx=10, pady=(0, 20), sticky='w'))

        def switch6_event():
            pass

        switch6_var = customtkinter.IntVar(value=0)
        self.switch6 = (customtkinter.CTkSwitch(
            master=self.scrollable_frame,
            text=f"Wałowanie +2,5%",
            onvalue=1,
            offvalue=0,
            variable=switch6_var,
            command=switch6_event).grid(row=6, column=0, padx=10, pady=(0, 20), sticky='w'))

        def switch7_event():
            pass

        switch7_var = customtkinter.IntVar(value=0)
        self.switch7 = (customtkinter.CTkSwitch(
            master=self.scrollable_frame,
            text=f"Mulczowanie +2,5%",
            onvalue=1,
            offvalue=0,
            variable=switch7_var,
            command=switch7_event).grid(row=7, column=0, padx=10, pady=(0, 20), sticky='w'))

        # Values check
        def check_bees():
            bee_plant = option_menu_1_var.get()
            if bee_plant == 'Słonecznik':
                self.checkbox_1.configure(state='normal')
                checkbox_1_text_var.set('Pszczoły +5%')
            elif bee_plant == 'Rzepak':
                self.checkbox_1.configure(state='normal')
                checkbox_1_text_var.set('Pszczoły +2,5%')
            elif bee_plant == 'Ziemniaki':
                self.checkbox_1.configure(state='normal')
                checkbox_1_text_var.set('Pszczoły +2,5%')
            else:
                checkbox_1_var.set(value=0)
                self.checkbox_1.configure(state='disabled')

        def check_straw():
            straw_plant = option_menu_1_var.get()
            if straw_plant == 'Pszenica':
                self.checkbox_2.configure(state='normal')
            elif straw_plant == 'Jęczmień':
                self.checkbox_2.configure(state='normal')
            elif straw_plant == 'Owies':
                self.checkbox_2.configure(state='normal')
            else:
                checkbox_2_var.set(value=0)
                self.checkbox_2.configure(state='disabled')

        def bees_force():
            check_bees()
            if checkbox_1_text_var.get() == 'Pszczoły +5%' and checkbox_1_var.get() == 1:
                bees_fo = 0.05
                return bees_fo
            elif checkbox_1_text_var.get() == 'Pszczoły +2,5%' and checkbox_1_var.get() == 1:
                bees_fo = 0.025
                return bees_fo
            else:
                bees_fo = 0.0
                return bees_fo

        def difficulty_price():
            if sidebar_var.get() == 'Easy_prices':
                price1 = Easy_prices
                return price1
            elif sidebar_var.get() == 'Normal_prices':
                price1 = Normal_prices
                return price1
            else:
                price1 = Hard_prices
                return price1

        # Obliczanie zarobku oraz strat, wartości progress barów
        def calculate():

            difficulty_price()
            plant = option_menu_1_var.get()  # zboże
            area = entry_var.get()  # areał
            harvest = crop_harvest[plant]  # wielkość zbioru z Ha
            price = difficulty_price()[plant][price_var.get()]  # cena zboża
            bees = checkbox_1_var.get()  # wartość pszczół
            herb = radio_var0.get()  # herbicyd 0 / pielnik 1
            bees_f = bees_force()  # ''.join(map(str, bees_force()))
            seeds = seed_usage[plant]  # zużycie nasion za 1Ha
            used_manure2 = manure[radio_var2.get()][0]  # Drugie nawożenie, zużycie na 1 Ha
            used_manure_price2 = manure[radio_var2.get()][1]  # Drugie nawożenie, zużycie na 1 Ha

            lime = manure['Wapno'][0]
            lime_price = manure['Wapno'][1]

            # Przypisanie ceny z obliczeń do log save
            log_price_entry_var.set(value=price)

            if radio_var1.get() == 'Rzodkiew oleista':
                used_manure = seed_usage['Rzodkiew oleista']
                used_manure_price = 0.9  # Pierwsze nawożenie, cena za 1 Ha

            else:
                used_manure = manure[radio_var1.get()][0]  # Pierwsze nawożenie, zużycie na 1 Ha
                used_manure_price = manure[radio_var1.get()][1]  # Pierwsze nawożenie, cena za 1 Ha

            max_price = round(((harvest[0] * area / 1000 * price) +
                               (harvest[0] * price * 0.225 * area / 1000) +
                               (harvest[0] * price * 0.225 * area / 1000) +
                               (harvest[0] * price * 0.15 * area / 1000) +
                               (harvest[0] * price * 0.15 * area / 1000) +
                               (harvest[0] * price * 0.15 * area / 1000) +
                               (harvest[0] * price * 0.025 * area / 1000) +
                               (harvest[0] * price * 0.025 * area / 1000) +
                               (harvest[0] * price * area / 1000 * float(bees_f)) -
                               (harvest[0] * price * 0.15 * area / 1000) +
                               (harvest[1] * area / 1000 * Normal_prices['Słoma'][1])), 2)

            together1 = round(((harvest[0] * area / 1000 * price) +
                               (harvest[0] * price * 0.225 * area / 1000 * switch1_var.get()) +
                               (harvest[0] * price * 0.225 * area / 1000 * switch2_var.get()) +
                               (harvest[0] * price * 0.15 * area / 1000 * switch3_var.get()) +
                               (harvest[0] * price * 0.15 * area / 1000 * switch4_var.get()) +
                               (harvest[0] * price * 0.15 * area / 1000 * switch5_var.get()) +
                               (harvest[0] * price * 0.025 * area / 1000 * switch6_var.get()) +
                               (harvest[0] * price * 0.025 * area / 1000 * switch7_var.get()) +
                               (harvest[0] * price * area / 1000 * float(bees_f) * bees) -
                               (harvest[0] * price * 0.15 * area / 1000 * herb) +
                               (harvest[1] * area / 1000 * Normal_prices['Słoma'][1] * checkbox_2_var.get())), 2)

            together2 = round(area * seeds +
                              used_manure * area * used_manure_price * switch1_var.get() +
                              manure[1][0] * area * manure[1][1] * switch2_var.get() +
                              manure[1][0] * area * manure[1][1] * switch4_var.get(), 2)

            # Progressbar
            progressbar_loss_variable.set(value=together2 / max_price)
            progressbar_earning_variable.set(value=(together1 - together2) / max_price)

            # textbox.configure(font=customtkinter.CTkFont(size=18))
            self.textbox.insert(
                'end', '\n' * 13 +
                f'{plant} na polu {area} Ha, da urobek: \t\t\t\t'
                f'{round(((harvest[0] * area) + (harvest[0] * 0.225 * area * switch1_var.get()) + 
                          (harvest[0] * 0.225 * area * switch2_var.get()) +
                          (harvest[0] * 0.15 * area * switch3_var.get()) +
                          (harvest[0] * 0.15 * area * switch4_var.get()) +
                          (harvest[0] * 0.15 * area * switch5_var.get()) +
                          (harvest[0] * 0.025 * area * switch6_var.get()) +
                          (harvest[0] * 0.025 * area * switch7_var.get()) +
                          (harvest[0] * area / 1000 * float(bees_f) * bees) -
                          (harvest[0] * 0.15 * area / 1000 * herb)), 2)} l ' +
                f'oraz \t\t\t\t{harvest[1] * area} l słomy' * checkbox_2_var.get() +

                f'\nCena za "{plant}" to: \t\t\t\t{price} euro' +
                f'\n\nMiesiące najwyższych cen to: {difficulty_price()[plant][3]}' +
                f'\n\nDochód z pola {area} Ha wyniesie: '
                f'\t\t\t\t{round((harvest[0]) * area / 1000 * price, 2)} euro' +
                f'\n+ 22,5% za pierwsze nawożenie: '
                f'\t\t\t\t{round((harvest[0]) * price * 0.225 * area / 1000, 2)} euro'
                * switch1_var.get() + f'\n+ 22,5% za drugie nawożenie: '
                f'\t\t\t\t{round((harvest[0]) * price * 0.225 * area / 1000, 2)} euro'
                * switch2_var.get() + f'\n+ 15% za oranie: '
                f'\t\t\t\t{round((harvest[0]) * price * 0.15 * area / 1000, 2)} euro'
                * switch3_var.get() +
                f'\n+ 15% za wapnowanie: '
                f'\t\t\t\t{round((harvest[0]) * price * 0.15 * area / 1000, 2)} euro'
                * switch4_var.get() +
                f'\n+ 15% za odchwaszczanie: '
                f'\t\t\t\t{round((harvest[0]) * price * 0.15 * area / 1000, 2)} euro'
                * switch5_var.get() +
                f'\n+ 2,5% za wałowanie: '
                f'\t\t\t\t{round((harvest[0]) * price * 0.025 * area / 1000, 2)} euro'
                * switch6_var.get() +
                f'\n+ 2,5% za mulczowanie: '
                f'\t\t\t\t{round((harvest[0]) * price * 0.025 * area / 1000, 2)} euro'
                * switch7_var.get() +
                f'\n+ {bees_f * 100}% za pszczoły: '
                f'\t\t\t\t{round((harvest[0]) * price * area / 1000 * bees_f, 2)} euro'
                * bees +
                f'\n-15% za użycie herbicydu: '
                f'\t\t\t\t-{round((harvest[0]) * price * 0.15 * area / 1000, 2)} euro'
                * herb +
                f'\nDochód z słomy po {price} cenie: '
                f'\t\t\t\t{round(harvest[1] * area / 1000 * Normal_prices['Słoma'][1], 2)} euro'
                * checkbox_2_var.get() +
                f'\n' +
                f'-' * 80 +
                f'\nZysk w sumie: \t\t\t\t{together1} euro')

            self.textbox.insert(
                'end',
                f'\n\n\nWydatki wyniosą:\nZużyte nasiona: \t\t\t\t-{area * seeds} euro \nKoszt pierwszego nawożenia:'
                f' \t\t\t\t-{round(used_manure * area * used_manure_price, 2)} euro' * switch1_var.get() +
                f'\nKoszt drugiego nawożenia: \t\t\t\t-{round(used_manure2 * area * used_manure_price2, 2)} euro'
                * switch2_var.get() + f'\nKoszt Wapnowania:'
                                      f' \t\t\t\t-{round(lime * area * lime_price, 2)} euro'
                * switch4_var.get() + f'\nKoszt użycia herbicydu:'
                                      f' \t\t\t\t-{round(manure[1][0] * area * manure[1][1], 2)} euro'
                * herb + '\n' + '-' * 80 + f'\nWydatki w sumie: \t\t\t\t{together2} euro')

            self.textbox.insert(
                'end',
                f'\n' + '=' * 46 + f'\nDochód w sumie: \t\t\t\t{round(together1 - together2, 2)} euro')
            self.textbox.see('end')
            return area, together2, together1

        def log_save():
            e = datetime.datetime.now()
            difficulty_price()
            plant = option_menu_1_var.get()  # zboże
            area = entry_var.get()  # areał
            harvest = crop_harvest[plant]  # wielkość zbioru z Ha
            price = difficulty_price()[plant][price_var.get()]  # cena zboża
            bees = checkbox_1_var.get()  # wartość pszczół
            herb = radio_var0.get()  # herbicyd 0 / pielnik 1
            bees_f = bees_force()  # ''.join(map(str, bees_force()))
            seeds = seed_usage[plant]  # zużycie nasion za 1Ha
            used_manure2 = manure[radio_var2.get()][0]  # Drugie nawożenie, zużycie na 1 Ha
            used_manure_price2 = manure[radio_var2.get()][1]  # Drugie nawożenie, zużycie na 1 Ha

            lime = manure['Wapno'][0]
            lime_price = manure['Wapno'][1]

            if radio_var1.get() == 'Rzodkiew oleista':
                used_manure = seed_usage['Rzodkiew oleista']
                used_manure_price = 0.9  # Pierwsze nawożenie, cena za 1 Ha

            else:
                used_manure = manure[radio_var1.get()][0]  # Pierwsze nawożenie, zużycie na 1 Ha
                used_manure_price = manure[radio_var1.get()][1]  # Pierwsze nawożenie, cena za 1 Ha

            together1 = round(((harvest[0] * area / 1000 * price) +
                               (harvest[0] * price * 0.225 * area / 1000 * switch1_var.get()) +
                               (harvest[0] * price * 0.225 * area / 1000 * switch2_var.get()) +
                               (harvest[0] * price * 0.15 * area / 1000 * switch3_var.get()) +
                               (harvest[0] * price * 0.15 * area / 1000 * switch4_var.get()) +
                               (harvest[0] * price * 0.15 * area / 1000 * switch5_var.get()) +
                               (harvest[0] * price * 0.025 * area / 1000 * switch6_var.get()) +
                               (harvest[0] * price * 0.025 * area / 1000 * switch7_var.get()) +
                               (harvest[0] * price * area / 1000 * float(bees_f) * bees) -
                               (harvest[0] * price * 0.15 * area / 1000 * herb) +
                               (harvest[1] * area / 1000 * Normal_prices['Słoma'][1] * checkbox_2_var.get())), 2)

            together2 = round(area * seeds +
                              used_manure * area * used_manure_price * switch1_var.get() +
                              manure[1][0] * area * manure[1][1] * switch2_var.get() +
                              manure[1][0] * area * manure[1][1] * switch4_var.get(), 2)

            profit = together1 - together2
            print("%s/%s/%s" % (e.day, e.month, e.year))
            print("%s:%s:%s" % (e.hour, e.minute, e.second))
            with open('Log_book.csv', 'a') as file1:
                content = file1
                file1.write("%s/%s/%s," % (e.day, e.month, e.year))
                file1.write("%s:%s:%s," % (e.hour, e.minute, e.second))
                file1.write(f'{area},')
                file1.write(f'{together1},')
                file1.write(f'{together2},')
                file1.write(f'{profit}\n')
            print(content)

        # set default values
        bees_force()
        difficulty_price()
        check_bees()
        check_straw()

        # Difficulty default values
        self.sidebar_button_1.configure(state='normal', fg_color='grey')
        self.sidebar_button_2.configure(state='disable', fg_color='#2FA572')
        self.sidebar_button_3.configure(state='normal', fg_color='grey')
        sidebar_var.set(value='Normal_prices')

        # Price default values
        price_var.set(value=0)
        self.price_button_1.configure(state='disable', fg_color='#2FA572')
        self.price_button_2.configure(state='normal', fg_color='grey')
        self.price_button_3.configure(state='normal', fg_color='grey')

        # Appearance default values
        appearance_mode_option_menu.set("Dark")

        # Scaling default value
        self.scaling_option_menu.set("100%")

        # Version
        ver = "0.1.1"
        # Textbox Welcome Message
        self.textbox.insert(
            "0.0", "Command Window - tu możesz zapisać notatki!\n\n"
            + f'Witaj w kalkulatorze do "Farming Simulator 22" version: {ver} !\n\n' +
            'Wybierz poziom trudności,'
            '\n\nWprowadź wielkość pola w Ha,'
            '\n\nWybierz uprawę, dostępne bonusy oraz cenę, po której będziesz chciał sprzedać urobek')
        self.textbox.see('end')


# Main Loop
App().mainloop()
