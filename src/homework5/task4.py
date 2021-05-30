# В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
# a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# b. Найдите ТОП250 фильмов и извлеките заголовки.
# c. Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt – гистограмма рейтингов,
# years.txt – гистограмма годов.

lst_films = []
try:
    # open file ratings.list
    with open("./ratings.list") as fh:
        fh.seek(830)
        for line in fh.readlines():
            lst_films.append(line.strip().split("  "))
except FileNotFoundError:
    print("File not found!")


top250_films = lst_films[0:250]
movie_titles_list = [film[-1] for film in top250_films]
# create and write to top250_movies.txt names of the top 250 films
with open("top250_movies.txt", "w") as fh:
    number = 0
    for movie in movie_titles_list:
        number += 1
        fh.writelines("{a} {b}\n".format(a=number, b=movie))


ratings_list = [ratings[2] for ratings in top250_films]
dct = {}
for rating in ratings_list:
    dct[rating] = dct.get(rating, 0) + 1
# create and write to ratings.txt ratings histogram
with open("ratings.txt", "w") as fh:
    for el in dct:
        fh.writelines("{} {}\n".format(el, "=" * dct[el]))


years_list = [movie.split()[-1] for movie in movie_titles_list]
result_years_list = [year[1:5] for year in years_list]
result_years_list.sort()
dct = {}
for year in result_years_list:
    dct[year] = dct.get(year, 0) + 1
# create and write to years.txt years histogram
with open("years.txt", "w") as fh:
    for el in dct:
        fh.writelines("{} {}\n".format(el, "=" * dct[el]))
