# input areał w Ha, output zbiór z pola w litrach
# output pół produktu na podstawie areału i wybranej uprawy + ceny
# output pół porduktu z uwzględnieniem nawożenia + ceny
# ilość wyjściowa produktów z ilości półporduktu + cena i zarobek procent względem półproduktu
# output cena za sprzedany produkt, słoma
# output sprzednaych produktów zapisywany do oddzielnego pliku txt.
# wybieranie zbioru z listy numerycznej jako przenica 1 ect
# koszt nawozu, nasion,

ver = 0.0

from Database import *

print(f'Witaj w kalkulatorze do "Farming Simulator 20" {ver} !\n')

area = float(input('Wprowadź wielkość pola w Ha: '))
while True:
    crop = int(input('Wprowadź numer odpowiadający uprawie:\n'
                     '\033[1;32m[\033[1;37;m1\033[1;32m] - Pszenica\n'
                     '[\033[1;37;m2\033[1;32m] - Jęczmień\n'
                     '[\033[1;37;m3\033[1;32m] - Owies\n'
                     '[\033[1;37;m4\033[1;32m] - Rzepak\n'
                     '[\033[1;37;m5\033[1;32m] - Sorgo\n'
                     '[\033[1;37;m6\033[1;32m] - Winogrono\n'
                     '[\033[1;37;m7\033[1;32m] - Oliwki\n'
                     '[\033[1;37;m8\033[1;32m] - Słonecznik\n'
                     '[\033[1;37;m9\033[1;32m] - Soja\n'
                     '[\033[1;37;m10\033[1;32m] - Kukurydza\n'
                     '[\033[1;37;m11\033[1;32m] - Ziemniaki\n'
                     '[\033[1;37;m12\033[1;32m] - Buraki Cukrowe\n'
                     '[\033[1;37;m13\033[1;32m] - Bawełna\n'
                     '[\033[1;37;m14\033[1;32m] - Trzcina Cukrowa\n'
                     '[\033[1;37;m15\033[1;32m] - Topola\n'
                     '[\033[1;37;m16\033[1;32m] - Trawa\n'
                     'Numer uprawy:\033[1;37;m '))

    if 0 < crop <=3:
        print(f'\n\033[1;32m{crop_data[crop - 1]}\033[1;37;m na polu \033[1;32m{area} Ha\033[1;37;m, da urobek: \033[1;32m{crop_yeld[crop - 1][0] * area} l\033[1;37;m, oraz \033[1;32m{round(crop_yeld[crop - 1][1] * area, 2)} l\033[1;37;m słomy')
        print(f'+ 22,5% z nawożenia (1) {round(crop_yeld[crop - 1][0] * area * 0.225, 2)}'
              f'\n+ 45% z nawożenia (2) {round(crop_yeld[crop - 1][0] * area * 0.45, 2)}')
        print(f'+ 20% z odchwaszczania {round(crop_yeld[crop - 1][0] * area * 0.225, 2)}')
        print(f'+ 15% z wapnowania {round(crop_yeld[crop - 1][0] * area * 0.15, 2)}')
        print(f'+ 15% z orania {round(crop_yeld[crop - 1][0] * area * 0.15, 2)}')
        print(f'+ 2,5% z mulczowania {round(crop_yeld[crop - 1][0] * area * 0.25, 2)}')
        print(f'+ 2,5% z wałowania {round(crop_yeld[crop - 1][0] * area * 0.25, 2)}')
        print(f'+ 100% z wszystkimi bonusami {round(crop_yeld[crop - 1][0] * area, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 2), 2)}')

        print(f'\nŚrednia cena za "\033[1;32m{crop_data[crop - 1]}\033[1;37;m" \033[1;32m{Normal_prices[crop - 1][0]}\033[1;37;m.'
              f'\nDochód z pola \033[1;32m{area} Ha\033[1;37;m po średniej cenie: \033[1;32m{round(crop_yeld[crop - 1][0] * area / 1000 * Normal_prices[crop - 1][0], 2)}\033[1;37;m'
              f'\nPlus Dochód z słomy po średniej cenie: \033[1;32m{round(crop_yeld[crop - 1][1] * area / 1000 * Normal_prices[16][0], 2)}\033[1;37;m')
        # print()
        # print(f'+ 22,5% z nawożenia (1) {round(crop_yeld[crop - 1][0] * area * 0.225, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.225)  / 1000 * Normal_prices[crop - 1][0], 2)}'
        #     f'\n+ 45% z nawożenia (2) {round(crop_yeld[crop - 1][0] * area * 0.45, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.45) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 20% z odchwaszczania {round(crop_yeld[crop - 1][0] * area * 0.225, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.225) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 15% z wapnowania {round(crop_yeld[crop - 1][0] * area * 0.15, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.15) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 15% z orania {round(crop_yeld[crop - 1][0] * area * 0.15, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.15) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 2,5% z mulczowania {round(crop_yeld[crop - 1][0] * area * 0.25, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.25) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 2,5% z wałowania {round(crop_yeld[crop - 1][0] * area * 0.25, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.25) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'100% - z wszystkimi bonusami {round(crop_yeld[crop - 1][0] * area, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area) / 1000 * Normal_prices[crop - 1][0], 2)}')
        # full_yeald = round(crop_yeld[crop - 1][0] * area / 1000 * 2 * Normal_prices[crop - 1][0], 2)
        # straw_yeald = round(crop_yeld[crop - 1][1] * area / 1000 * Normal_prices[16][0], 2)
        # print(f'Dochód za sprzedaż 100% + słoma: {full_yeald + straw_yeald} ')


        print(f'\nDobra cena za "\033[1;32m{crop_data[crop - 1]}\033[1;37;m" \033[1;32m{Normal_prices[crop - 1][1]}\033[1;37;m.'
              f'\nDochód z pola \033[1;32m{area} Ha\033[1;37;m po dobrej cenie: \033[1;32m{round(crop_yeld[crop - 1][0] * area / 1000 * Normal_prices[crop - 1][1], 2)}\033[1;37;m'
              f'\nPlus Dochód z słomy po dobrej cenie: \033[1;32m{round(crop_yeld[crop - 1][1] * area / 1000 * Normal_prices[16][1], 2)}\033[1;37;m')
        # print()
        # print(f'+ 22,5% z nawożenia (1) {round(crop_yeld[crop - 1][0] * area * 0.225, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.225)  / 1000 * Normal_prices[crop - 1][0], 2)}'
        #     f'\n+ 45% z nawożenia (2) {round(crop_yeld[crop - 1][0] * area * 0.45, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.45) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 20% z odchwaszczania {round(crop_yeld[crop - 1][0] * area * 0.225, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.225) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 15% z wapnowania {round(crop_yeld[crop - 1][0] * area * 0.15, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.15) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 15% z orania {round(crop_yeld[crop - 1][0] * area * 0.15, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.15) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 2,5% z mulczowania {round(crop_yeld[crop - 1][0] * area * 0.25, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.25) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 2,5% z wałowania {round(crop_yeld[crop - 1][0] * area * 0.25, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.25) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'100% - z wszystkimi bonusami {round(crop_yeld[crop - 1][0] * area, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area) / 1000 * Normal_prices[crop - 1][0], 2)}')
        # full_yeald = round(crop_yeld[crop - 1][0] * area / 1000 * 2 * Normal_prices[crop - 1][0], 2)
        # straw_yeald = round(crop_yeld[crop - 1][1] * area / 1000 * Normal_prices[16][0], 2)
        # print(f'Dochód za sprzedaż 100% + słoma: {full_yeald + straw_yeald} ')

        print(f'\nNajlepsza cena za "\033[1;32m{crop_data[crop - 1]}\033[1;37;m" \033[1;32m{Normal_prices[crop - 1][2]}\033[1;37;m.'
              f'\nDochód z pola \033[1;32m{area} Ha\033[1;37;m po najlepszej cenie: \033[1;32m{crop_yeld[crop - 1][0] * area / 1000 * Normal_prices[crop - 1][2]}\033[1;37;m.'
              f'\nMiesiące występowania najlepszej ceny: \033[1;32m{Normal_prices[crop - 1][3]}\033[1;37;m'
              f'\n\nPlus Dochód z słomy po najlepszej cenie: \033[1;32m{crop_yeld[crop - 1][1] * area/ 1000  * Normal_prices[16][2]}\033[1;37;m'
              f'\nMiesiące występowania najlepszej ceny: \033[1;32m{Normal_prices[16][3]}\033[1;37;m')
        # print()
        # print(f'+ 22,5% z nawożenia (1) {round(crop_yeld[crop - 1][0] * area * 0.225, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.225)  / 1000 * Normal_prices[crop - 1][0], 2)}'
        #     f'\n+ 45% z nawożenia (2) {round(crop_yeld[crop - 1][0] * area * 0.45, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.45) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 20% z odchwaszczania {round(crop_yeld[crop - 1][0] * area * 0.225, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.225) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 15% z wapnowania {round(crop_yeld[crop - 1][0] * area * 0.15, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.15) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 15% z orania {round(crop_yeld[crop - 1][0] * area * 0.15, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.15) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 2,5% z mulczowania {round(crop_yeld[crop - 1][0] * area * 0.25, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.25) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'+ 2,5% z wałowania {round(crop_yeld[crop - 1][0] * area * 0.25, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area * 0.25) / 1000  * Normal_prices[crop - 1][0], 2)}')
        # print(f'100% - z wszystkimi bonusami {round(crop_yeld[crop - 1][0] * area, 2)}, w sumie: {round((crop_yeld[crop - 1][0] * area) / 1000 * Normal_prices[crop - 1][0], 2)}')
        # full_yeald = round(crop_yeld[crop - 1][0] * area / 1000 * 2 * Normal_prices[crop - 1][0], 2)
        # straw_yeald = round(crop_yeld[crop - 1][1] * area / 1000 * Normal_prices[16][0], 2)
        # print(f'Dochód za sprzedaż 100% + słoma: {full_yeald + straw_yeald} ')


    elif 3 < crop <=16:
        print(f'\n\033[1;32m{crop_data[crop - 1]}\033[1;37;m na polou \033[1;32m{area} Ha\033[1;37;m, da urobek: \033[1;32m{crop_yeld[crop - 1][0] * area} l\033[1;37;m.')
        print(f'\nŚrednia cena za "\033[1;32m{crop_data[crop - 1]}\033[1;37;m" \033[1;32m{Normal_prices[crop - 1][0]}\033[1;37;m.'
              f'\nDochód z pola \033[1;32m{area} Ha\033[1;37;m po średniej cenie: \033[1;32m{crop_yeld[crop - 1][0] * area / 1000 * Normal_prices[crop - 1][0]}\033[1;37;m')
        print(f'\nDobra cena za "\033[1;32m{crop_data[crop - 1]}\033[1;37;m" \033[1;32m{Normal_prices[crop - 1][1]}\033[1;37;m.'
              f'\nDochód z pola \033[1;32m{area} Ha\033[1;37;m po dobrej cenie: \033[1;32m{crop_yeld[crop - 1][0] * area/ 1000  * Normal_prices[crop - 1][1]}\033[1;37;m')
        print(f'\nNajlepsza cena za "\033[1;32m{crop_data[crop - 1]}\033[1;37;m" \033[1;32m{Normal_prices[crop - 1][2]}\033[1;37;m.'
              f'\nDochód z pola \033[1;32m{area} Ha\033[1;37;m po najlepszej cenie: \033[1;32m{crop_yeld[crop - 1][0] * area / 1000 * Normal_prices[crop - 1][2]}\033[1;37;m.'
              f'\nMiesiące występowania najlepszej ceny: \033[1;32m{Normal_prices[crop - 1][3]}\033[1;37;m')


    else:
        print('Wybierz właściwy numer uprawy')

    price_data = ['Średnia', 'Dobra', 'Najlepsza']
    price = input(f'\nPo jakiej cenie chcesz sprzedać "{crop_data[crop - 1]}"?'
                  f'\n\033[1;32m[\033[1;37;m1\033[1;32m] - Średnia\n'
                  f'[\033[1;37;m2\033[1;32m] - Dobra\n'
                  f'[\033[1;37;m3\033[1;32m] - Najlepsza\n')
    break
