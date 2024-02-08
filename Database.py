Easy_prices =   ([1011, 1314, 1415,'Styczeń, Grudzień'],                      # Pszenica
                 [939, 1221, 1315,  'Styczeń Grudzień'],                      # Jęczmień
                 [1596, 2075, 2234,  'Styczeń Grudzień'],                     # Owies
                 [1809, 2352, 2533, 'Grudzień, Listopad'],                    # Rzepak
                 [1290, 1677, 1806, 'Styczeń, Luty'],                         # Sorgo
                 [1809, 2352, 2533, 'Maj, Czerwiec'],                         # Winogrona
                 [1809, 2352, 2533, 'Czerwiec, Lipiec'],                      # Oliwki
                 [2019, 2625, 2827, 'Marzec, Kwiecień'],                      # Słonecznik
                 [2333, 3033, 3266, 'Lipiec, Czerwiec'],                      # Soja
                 [1139, 1481, 1595, 'Styczeń, Lipiec'],                       # Kukurydza
                 [516, 671, 722, 'Styczeń, Luty'],                            # Ziemnkiaki
                 [366, 476, 512, 'Styczeń, Luty'],                            # Buraki cukrowe
                 [3756, 4883, 5258, 'Marzec, Luty'],                          # Bawełna
                 [357, 464, 500, 'Lipiec, Wrzesień, Sierpień, Październik'],  # Trzcina cukrowa
                 [126, 164, 176, 'Luty, Marzec'],                             # Topola
                 [135, 176, 189, 'Styczeń, Luty, Grudzień'],                  # Trawa
                 [123, 160, 172, 'Styczeń, Luty, Grudzień'])                  # Słoma

Normal_prices = ([607, 789, 850,'Styczeń, Grudzień'],                         # Pszenica
                 [563, 732, 788,  'Styczeń Grudzień'],                        # Jęczmień
                 [958, 1245, 1341,  'Styczeń Grudzień'],                      # Owies
                 [1085, 1411, 1519, 'Grudzień, Listopad'],                    # Rzepak
                 [773, 1006, 1084, 'Styczeń, Luty'],                          # Sorgo
                 [1085, 1411, 1519, 'Maj, Czerwiec'],                         # Winogrona
                 [1085, 1411, 1519, 'Czerwiec, Lipiec'],                      # Oliwki
                 [1211, 1574, 1695, 'Marzec, Kwiecień'],                      # Słonecznik
                 [1400, 1820, 1960, 'Lipiec, Czerwiec'],                      # Soja
                 [683, 888, 956, 'Styczeń, Lipiec'],                          # Kukurydza
                 [310, 403, 434, 'Styczeń, Luty'],                            # Ziemnkiaki
                 [220, 286, 308, 'Styczeń, Luty'],                            # Buraki cukrowe
                 [2254, 2930, 3156, 'Marzec, Luty'],                          # Bawełna
                 [214, 278, 300, 'Lipiec, Wrzesień, Sierpień, Październik'],  # Trzcina cukrowa
                 [76, 99, 106, 'Luty, Marzec'],                               # Topola
                 [81, 105, 113, 'Styczeń, Luty, Grudzień'],                   # Trawa
                 [74, 96,104, 'Styczeń, Luty, Grudzień'])                     # Słoma

Hard_prices =   ([337, 438, 472,'Styczeń, Grudzień'],                        # Pszenica
                 [313, 407, 438,  'Styczeń Grudzień'],                       # Jęczmień
                 [532, 692, 745,  'Styczeń Grudzień'],                       # Owies
                 [603, 784, 844, 'Grudzień, Listopad'],                      # Rzepak
                 [430, 559, 602, 'Styczeń, Luty'],                           # Sorgo
                 [603, 784, 844, 'Maj, Czerwiec'],                           # Winogrona
                 [603, 784, 844, 'Czerwiec, Lipiec'],                        # Oliwki
                 [673, 875, 942, 'Marzec, Kwiecień'],                        # Słonecznik
                 [778, 1011, 1089, 'Lipiec, Czerwiec'],                      # Soja
                 [380, 494, 532, 'Styczeń, Lipiec'],                         # Kukurydza
                 [172, 224, 241, 'Styczeń, Luty'],                           # Ziemnkiaki
                 [122, 159, 171, 'Styczeń, Luty'],                           # Buraki cukrowe
                 [1252, 1628, 1753, 'Marzec, Luty'],                         # Bawełna
                 [119, 155, 167, 'Lipiec, Wrzesień, Sierpień, Październik'], # Trzcina cukrowa
                 [42, 55, 59, 'Luty, Marzec'],                               # Topola
                 [45, 59, 63, 'Styczeń, Luty, Grudzień'],                    # Trawa
                 [41, 53, 57, 'Styczeń, Luty, Grudzień'])                    # Słoma

crop_yeld =     ([8900, 73447], #Pszenica
                 [9600, 73528], #Jęczmień
                 [5700, 73594], # Owies
                 [5800, 0],     # Rzepak
                 [8200, 0],     # Sorgo
                 [9200, 0],     # Winogrono
                 [9200, 0],     # Oliwki
                 [5200, 0],     # Słonecznik
                 [4500, 0],     # Soja
                 [9200, 0],     # Kukurydza
                 [41300, 0],    # Ziemniaki
                 [57800, 0],    # Buraki Cukrowe
                 [4970, 0],     # Bawełna
                 [113400, 0],   # Trzcina Cukrowa
                 [71760, 0],    # Topola
                 [32800, 0])    # Trawa

crop_data = ['Pszenica',
             'Jęczmień',
             'Owies',
             'Rzepak',
             'Sorgo',
             'Winogrono',
             'Oliwki',
             'Słonecznik',
             'Soja',
             'Kukurydza',
             'Ziemniaki',
             'Buraki Cukrowe',
             'Bawełna',
             'Trzcina Cukrowa',
             'Topola',
             'Trawa',
             'Słoma']