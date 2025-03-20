import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data_credits = pd.read_csv("C:/Users/Ayhan/PycharmProjects/pythonProject1/tmdb_5000_credits.csv", encoding='iso-8859-1')
data_movies = pd.read_csv("C:/Users/Ayhan/PycharmProjects/pythonProject1/tmdb_5000_movies.csv", encoding='iso-8859-1')

data_movies = data_movies.rename(columns={"id": "movie_id"})

data_all = pd.merge(data_movies, data_credits, on='movie_id')

V = data_all['vote_count']
R = data_all['vote_average']
C = data_all['vote_average'].mean()
m = data_all['vote_count'].quantile(0.75)

data_all['weighted_average'] = (V/(V+m) * R) + (m/(m+V) * C)
movies_ranked = data_all.sort_values('weighted_average', ascending=False)
#movies_ranked[['original_title','vote_count','vote_average','weighted_average','popularity']].head(100)

plt.figure(figsize=(16, 5))
ax = sns.barplot(x=movies_ranked['weighted_average'].head(10),y=movies_ranked['original_title'].head(10))

plt.xlim(6.75, 8.35)
plt.title('Oylarla Seçilen En İyi Filmler', weight='bold'),
plt.xlabel('Alınan Ortalama Skor', weight='bold')
plt.ylabel('Film Adı',weight='bold')

plt.savefig('en_iyi_filmler.png')

data_all['overview'] = data_all['overview'].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data_all['overview'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(data_all.index, index=data_all['original_title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    #Bu filmin diğer tüm filmlerele olan benzerlik puanlarını listele
    sim_scores = list(enumerate(cosine_sim[idx]))
    #filmleri benzerlik puanlarına göre listele
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    #En çok benzeyen 10 filmin skorunu al
    sim_scores = sim_scores[1:11]

    #film indexlerini al
    movie_indices = [i[0] for i in sim_scores]

    #En çok benzeyen 10 filmi döndür
    return data_all['original_title'].iloc[movie_indices]

