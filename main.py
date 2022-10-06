from bs4 import BeautifulSoup
import requests
import re
# import pandas as pd


# Downloading imdb top 250 movie's data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
# print(response);
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.find_all('a'))
# for a in soup.find_all('a'):
#     print(a.attrs.get('title'))
movies = soup.select('td.titleColumn')
# print(movies)
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
# print(crew)
# ratings = [b.attrs.get('data-value')
# 		for b in soup.select('td.posterColumn span[name=ir]')]




# create a empty list for storing
# movie information
list = []

# Iterating over movies to extract
# each movie's details

word_dict = dict()
n = int(input("enter number of top movies details you want to see"))
for index in range(0, n):
        movie_string = movies[index].a.get_text()
        print(movie_string)
        star_cast = movies[index].a.attrs.get('title');
        print(star_cast)

        # for star in range(0, len(star_cast)):
        star = 0
        while (star < len(star_cast)):
            # print(star)
            name = ""
            while(star< len(star_cast) and star_cast[star]!=','):
                # if(star_cast[star] != " "):
                name = name + star_cast[star]
                star+=1;
            # print(name)
            star+=1
            # print(name)
           
            if(name[0] == " "):
                name = name[1:]
            # if(name == "Brad Pitt"):
            #     print("yes")
            # word_dict[name] = set()
            if(word_dict.get(name)== None):
                word_dict[name] = set()
            word_dict[name].add(movie_string)
# Brad Pitt
# Inglourious Basterds
# Snatch
# Fight Club
# Se7en
query_star = input("Enter your actor name: ")
# query_star = "Morgan Freeman"
m = int(input("Enter the number of top movies you want to see for the given actor"))
# m = 1
for i in word_dict :
    if(i == query_star ):
        print(query_star)
        j = 0
        for val in word_dict[i]:
            if(m == 0):
                break
            print(val)
            m = m-1
            
        # movie = (' '.join(movie_string.split()).replace('.', ''))
        # movie_title = movie[len(str(index))+1:-7]
        # print(movie_title)
        # print(crew[index]);
        # print(len(crew[index]))
        # for i in range(0, len(crew[index])):
        #     # print(crew[index])
        #     star = ""
        #     j = i
        #     while(j < len(crew[index]) and crew[index][j]!=','):
        #         star = star + crew[index][j];
        #         j = j + 1;
        #     # print(star)
        #     # print(i)
        #     i = j
        #     word_dict[star] = set()
        #     word_dict[star].add(movie_title)


# for i in word_dict :
#     print(i, word_dict[i])
	# Separating movie into: 'place',
	# 'title', 'year'
	# movie_string = movies[index].get_text()
	# movie = (' '.join(movie_string.split()).replace('.', ''))
	# movie_title = movie[len(str(index))+1:-7]
	# year = re.search('\((.*?)\)', movie_string).group(1)
	# place = movie[:len(str(index))-(len(movie))]
# print(place)
# print(crew[index]);
    # word_dict[crew[index]] = set()
    # word_dict

	# data = {"place": place,
	# 		"movie_title": movie_title,
	# 		"rating": ratings[index],
	# 		"year": year,
	# 		"star_cast": crew[index],
	# 		}
	# list.append(data)

# printing movie details with its rating.

# for movie in list:
# 	print(movie['place'], '-', movie['movie_title'], 'CAST :', movie['star_cast'])


# ##.......##
# df = pd.DataFrame(list)
# df.to_csv('imdb_top_250_movies.csv',index=False)
