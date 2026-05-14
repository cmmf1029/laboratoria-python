##zadanie 1
import matplotlib.pyplot as plt
# x = [1, 3, 5, 7]
# y = [27, 30, 21, 29]
# plt.plot(x, y, color='green', marker='o')#rysowanie zielonej linijki
# plt.grid(True)# dodanie siatki
# plt.xlabel('day')
# plt.ylabel('temperature')
# plt.title('Temperature plot')#tytł wykresu
# plt.show()#wyświetlanie go
#
# #zadanie 2
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0, 5, 10)   # 10 punktów od 0 do 5
# y = np.linspace(0, 25, 10)  # 10 punktów od 0 do 25
# plt.scatter(x, y, color='red')# rysowanie scatter plot
# plt.xlabel('X')#podpis osi
# plt.ylabel('Y')#podpis osi
# plt.text(x[0], y[0], "(0,0)")#dodanie tekstu przy pierwszym i ostatnim pkt
# plt.text(x[-1], y[-1], "(5,25)")#to samo
# plt.show()

##zadanie 3
# import matplotlib.pyplot as plt
# labels = ['Horror', 'Comedy', 'Sci-Fi']
# sizes = [20, 30, 50]  # procentowy udział
# explode = [0, 0, 0.1]  # ranking (najlepsze)
# plt.pie(
#     sizes,
#     labels=labels,
#     explode=explode,
#     autopct='%1.1f%%',
#     shadow=True,
#     startangle=90
# )
# plt.title("Favourite film types")
# plt.show()

##zadanie 4
# import matplotlib.pyplot as plt
# import numpy as np
# data = np.random.randn(10000)
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))#tworzenie wykresow obok siebie
# ax1.hist(data, bins=10, color='skyblue', edgecolor='black')
# ax1.set_title("Histogram (10 bins)")
# ax1.set_xlabel("Value")
# ax1.set_ylabel("Frequency")
# ax1.grid(True)
# counts, bins = np.histogram(data, bins=10)
# bin_centers = 0.5 * (bins[:-1] + bins[1:])#środek przedziału
# ax2.bar(bin_centers, counts, width=(bins[1] - bins[0]), color='orange', edgecolor='black')
# ax2.set_title("Bar plot (10 bins)")
# ax2.set_xlabel("Value")
# ax2.set_ylabel("Count")
# ax2.grid(True)
# plt.tight_layout()
# plt.show()
