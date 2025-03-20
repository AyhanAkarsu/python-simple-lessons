import numpy as np
from scipy.spatial.distance import pdist, squareform

data = [    ['movieId', 'title', 'genres', 'rating'],
    [1, 'Toy Story (1995)', 'Adventure|Animation|Children|Comedy|Fantasy', 6],
    [2, 'Jumanji (1995)', 'Adventure|Children|Fantasy', 7],
    [3, 'Grumpier Old Men (1995)', 'Comedy|Romance', 8],
    [4, 'Waiting to Exhale (1995)', 'Comedy|Drama|Romance', 9],
    [5, 'Father of the Bride Part II (1995)', 'Comedy', 6],
    [6, 'Heat (1995)', 'Action|Crime|Thriller', 7],
    [7, 'Sabrina (1995)', 'Comedy|Romance', 8],
    [8, 'Tom and Huck (1995)', 'Adventure|Children', 5],
    [9, 'Sudden Death (1995)', 'Action', 7],
    [10, 'GoldenEye (1995)', 'Action|Adventure|Thriller', 8],
    [11,'The Lion King (1994)','Animation|Adventure|Drama|Family|Musical',9],
    [12,'Fight Club (1999)','Drama',7],
    [13,'The Matrix (1999)','Action|Sci-Fi',8],
    [14,'Forrest Gump (1994)','Comedy|Drama|Romance',9],
    [15,'Pulp Fiction (1994)','Crime|Drama',7],
    [16,'The Silence of the Lambs (1991)','Crime|Drama|Thriller',7],
    [17,'Goodfellas (1990)','Crime|Drama',8],
    [18,'The Shawshank Redemption (1994)','Drama',8],
    [19,'The Godfather (1972)','Crime|Drama',7]
]

# Dizi boyutları (satır, sütun) şeklinde yazdırılır
print("Dizinin boyutu: ", np.array(data).shape)

data_arr = np.array(data[1:])
# 4. sütunu float tipine dönüştür
data_arr[:, 3] = data_arr[:, 3].astype(float)

# Hesaplanan mesafe matrisi dizi boyutları yazdırılır
dist_mat = squareform(pdist(data_arr[:, 3:], metric='euclidean'))
print("Mesafe matrisinin boyutu: ", dist_mat.shape)

print(dist_mat)
