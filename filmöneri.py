import pandas as pd

# Veri setini yükle
movies = pd.read_csv("movies.csv")

# Verileri incele
print(movies.head())
# Kullanıcının seçtiği film
secilen_film = "Toy Story (1995)"

# Benzerlik ölçüsü olarak Pearson korelasyon katsayısı kullanacağız
from scipy.spatial.distance import correlation

# Kullanıcının seçtiği film puanları
secilen_film_puanlari = movies[movies["title"] == secilen_film]["rating"].values

# Tüm filmlerle seçilen film arasındaki benzerlikleri hesapla
benzerlik_olculeri = []
for i in range(len(movies)):
    puanlar = movies.iloc[i, 3:].values
    benzerlik = correlation(puanlar, secilen_film_puanlari)
    if pd.isna(benzerlik):
        continue
    else:
        benzerlik_olculeri.append((movies.iloc[i]["title"], benzerlik))

# Benzerlik ölçüsüne göre en iyi sonuçları al
