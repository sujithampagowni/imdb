## IMDB Movies

####	Hey! We here have the list of movies with IMBD score, Director name, its Genre and 99Popularity from which one authenticated user can search by its relative name, director and id. We also provide create, update and delete options for an Admin. 

######	Using Chrome browser for accessing the below URL's is most recommended.

### User Registration

#####	We allow user to register with the below URL which accepts POST request.

##### URL

```json
https://new-imdb.herokuapp.com/register/
```

##### Payload

```json
{
"username" : "George",
"email" : "george@gmail.com",
"password" : "bchsdgc678"
}
```

### User Login

##### Using the below endpoint user can login and proceed further.

##### URL

```json
https://new-imdb.herokuapp.com/api-auth/login/
```

### GET List of Movies

##### Using the below URL user can get the list of all the movies with specified details of each with default pagination of 10 per each page.

##### URL

```json
https://new-imdb.herokuapp.com/movie/
```

##### Response

```json
{
    "count": 248,
    "next": "https://new-imdb.herokuapp.com/movie/?limit=10&offset=10",
    "previous": null,
    "results": [
        {
            "id": 41,
            "name": "The Tin Man",
            "imdb_score": 4.6,
            "director": "James Parrott",
            "genre": [
                "Short",
                " Adventure",
                " Comedy"
            ],
            "popularity_99": 46.0
        },
        {
            "id": 119,
            "name": "His Trust Fulfilled",
            "imdb_score": 4.7,
            "director": "D.W. Griffith",
            "genre": [
                "Short",
                " Drama"
            ],
            "popularity_99": 47.0
        },
        {
            "id": 153,
            "name": "Swing Your Lady",
            "imdb_score": 4.8,
            "director": "Ray Enright",
            "genre": [
                "Comedy",
                " Music",
                " Romance",
                " Sport"
            ],
            "popularity_99": 48.0
        },
        {
            "id": 212,
            "name": "American Idol : The Search for a Superstar",
            "imdb_score": 4.8,
            "director": "Bruce Gowers",
            "genre": [
                "Game-Show",
                " Music",
                " Reality-TV"
            ],
            "popularity_99": 48.0
        },
        {
            "id": 227,
            "name": "Baywatch",
            "imdb_score": 4.9,
            "director": "Gregory J. Bonann",
            "genre": [
                "Drama",
                " Action",
                " Adventure"
            ],
            "popularity_99": 49.0
        },
        {
            "id": 214,
            "name": "Revenge of the Creature",
            "imdb_score": 5.1,
            "director": "Jack Arnold",
            "genre": [
                "Horror",
                " Sci-Fi"
            ],
            "popularity_99": 51.0
        },
        {
            "id": 179,
            "name": "Deep Throat",
            "imdb_score": 5.2,
            "director": "Gerard Damiano",
            "genre": [
                "Adult",
                " Comedy"
            ],
            "popularity_99": 52.0
        },
        {
            "id": 37,
            "name": "The Wizard of Oz",
            "imdb_score": 5.3,
            "director": "Larry Semon",
            "genre": [
                "Comedy",
                " Family",
                " Fantasy",
                " Adventure"
            ],
            "popularity_99": 53.0
        },
        {
            "id": 120,
            "name": "His Trust",
            "imdb_score": 5.3,
            "director": "D.W. Griffith",
            "genre": [
                "Short",
                " Drama",
                " War"
            ],
            "popularity_99": 53.0
        },
        {
            "id": 95,
            "name": "The Bangville Police",
            "imdb_score": 5.5,
            "director": "Henry Lehrman",
            "genre": [
                "Comedy",
                " Short"
            ],
            "popularity_99": 55.0
        }
    ]
}
```

### 

### Search and Filter

##### Search and Filters are also possible using below URL with movie name or director name or both.

##### URL

```json
https://new-imdb.herokuapp.com/movie/?name=The&director=James
```

##### Response

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 41,
            "name": "The Tin Man",
            "imdb_score": 4.6,
            "director": "James Parrott",
            "genre": [
                "Short",
                " Adventure",
                " Comedy"
            ],
            "popularity_99": 46.0
        },
        {
            "id": 26,
            "name": "The Terminator",
            "imdb_score": 8.1,
            "director": "James Cameron",
            "genre": [
                "Action",
                " Sci-Fi",
                " Thriller"
            ],
            "popularity_99": 81.0
        }
    ]
}
```

1. ##### Search by name of the movie or relevent name or complete name.

   ##### URL

   ```
   https://new-imdb.herokuapp.com/movie/?name=The
   ```

   ##### Response

   ```
   {
       "count": 93,
       "next": "https://new-imdb.herokuapp.com/movie/?limit=10&name=The&offset=10",
       "previous": null,
       "results": [
           {
               "id": 41,
               "name": "The Tin Man",
               "imdb_score": 4.6,
               "director": "James Parrott",
               "genre": [
                   "Short",
                   " Adventure",
                   " Comedy"
               ],
               "popularity_99": 46.0
           },
           {
               "id": 212,
               "name": "American Idol : The Search for a Superstar",
               "imdb_score": 4.8,
               "director": "Bruce Gowers",
               "genre": [
                   "Game-Show",
                   " Music",
                   " Reality-TV"
               ],
               "popularity_99": 48.0
           },
           {
               "id": 214,
               "name": "Revenge of the Creature",
               "imdb_score": 5.1,
               "director": "Jack Arnold",
               "genre": [
                   "Horror",
                   " Sci-Fi"
               ],
               "popularity_99": 51.0
           },
           {
               "id": 37,
               "name": "The Wizard of Oz",
               "imdb_score": 5.3,
               "director": "Larry Semon",
               "genre": [
                   "Comedy",
                   " Family",
                   " Fantasy",
                   " Adventure"
               ],
               "popularity_99": 53.0
           },
           {
               "id": 95,
               "name": "The Bangville Police",
               "imdb_score": 5.5,
               "director": "Henry Lehrman",
               "genre": [
                   "Comedy",
                   " Short"
               ],
               "popularity_99": 55.0
           },
           {
               "id": 221,
               "name": "The Pride and the Passion",
               "imdb_score": 5.5,
               "director": "Stanley Kramer",
               "genre": [
                   "Action",
                   " Adventure",
                   " Drama",
                   " Romance",
                   " War"
               ],
               "popularity_99": 55.0
           },
           {
               "id": 50,
               "name": "His Majesty, the Scarecrow of Oz",
               "imdb_score": 6.0,
               "director": "L. Frank Baum",
               "genre": [
                   "Family",
                   " Fantasy",
                   " Adventure",
                   " Comedy"
               ],
               "popularity_99": 60.0
           },
           {
               "id": 93,
               "name": "The Oprah Winfrey Show",
               "imdb_score": 6.0,
               "director": "Joseph C. Terry",
               "genre": [
                   "Talk-Show"
               ],
               "popularity_99": 60.0
           },
           {
               "id": 117,
               "name": "5 Against the House",
               "imdb_score": 6.0,
               "director": "Phil Karlson",
               "genre": [
                   "Drama",
                   " Crime",
                   " Film-Noir"
               ],
               "popularity_99": 60.0
           },
           {
               "id": 239,
               "name": "It! The Terror from Beyond Space",
               "imdb_score": 6.0,
               "director": "Edward L. Cahn",
               "genre": [
                   "Horror",
                   " Sci-Fi"
               ],
               "popularity_99": 60.0
           }
       ]
   }
   ```

2. ##### Search using director name.

   ##### URL

   ```	json
   https://new-imdb.herokuapp.com/movie/?dirctor=D.W. 20Griffith
   ```

   ##### Response

   ```json
   {
       "count": 248,
       "next": "https://new-imdb.herokuapp.com/movie/?dirctor=D.W.+Griffith&limit=10&offset=10",
       "previous": null,
       "results": [
           {
               "id": 41,
               "name": "The Tin Man",
               "imdb_score": 4.6,
               "director": "James Parrott",
               "genre": [
                   "Short",
                   " Adventure",
                   " Comedy"
               ],
               "popularity_99": 46.0
           },
           {
               "id": 119,
               "name": "His Trust Fulfilled",
               "imdb_score": 4.7,
               "director": "D.W. Griffith",
               "genre": [
                   "Short",
                   " Drama"
               ],
               "popularity_99": 47.0
           },
           {
               "id": 153,
               "name": "Swing Your Lady",
               "imdb_score": 4.8,
               "director": "Ray Enright",
               "genre": [
                   "Comedy",
                   " Music",
                   " Romance",
                   " Sport"
               ],
               "popularity_99": 48.0
           },
           {
               "id": 212,
               "name": "American Idol : The Search for a Superstar",
               "imdb_score": 4.8,
               "director": "Bruce Gowers",
               "genre": [
                   "Game-Show",
                   " Music",
                   " Reality-TV"
               ],
               "popularity_99": 48.0
           },
           {
               "id": 227,
               "name": "Baywatch",
               "imdb_score": 4.9,
               "director": "Gregory J. Bonann",
               "genre": [
                   "Drama",
                   " Action",
                   " Adventure"
               ],
               "popularity_99": 49.0
           },
           {
               "id": 214,
               "name": "Revenge of the Creature",
               "imdb_score": 5.1,
               "director": "Jack Arnold",
               "genre": [
                   "Horror",
                   " Sci-Fi"
               ],
               "popularity_99": 51.0
           },
           {
               "id": 179,
               "name": "Deep Throat",
               "imdb_score": 5.2,
               "director": "Gerard Damiano",
               "genre": [
                   "Adult",
                   " Comedy"
               ],
               "popularity_99": 52.0
           },
           {
               "id": 37,
               "name": "The Wizard of Oz",
               "imdb_score": 5.3,
               "director": "Larry Semon",
               "genre": [
                   "Comedy",
                   " Family",
                   " Fantasy",
                   " Adventure"
               ],
               "popularity_99": 53.0
           },
           {
               "id": 120,
               "name": "His Trust",
               "imdb_score": 5.3,
               "director": "D.W. Griffith",
               "genre": [
                   "Short",
                   " Drama",
                   " War"
               ],
               "popularity_99": 53.0
           },
           {
               "id": 95,
               "name": "The Bangville Police",
               "imdb_score": 5.5,
               "director": "Henry Lehrman",
               "genre": [
                   "Comedy",
                   " Short"
               ],
               "popularity_99": 55.0
           }
       ]
   }
   ```

##### Create, Edit and Delete is only possible for an Admin who can login with the below credentials

```"username" : "admin"
{
"username" : "admin",
"password" : "otocapital"
}
```

##### To perform RUD operations on a perticular movie, search by its ID as below

##### URL

```json
https://new-imdb.herokuapp.com/movie/41/
```

##### To Create new data use below URL.

##### URL

```json
https://new-imdb.herokuapp.com/movie/
```

Payload

```json
{
    "name": "new movie",
    "imdb_score": 9.1,
    "director": "Cristopher Nolon",
    "popularity_99": 91.0
}	
```

