function solve(movieDataList) {
    class Movie {
        constructor(name, director, date) {
            this.name = name;
            this.director = director;
            this.date = date;
        }

        isValid() {
            return this.name !== "" && this.director !== "" && this.date !== "";
        }
    }

    function getMovieByName(movieName, movies) {
        for (let movie of movies) {
            if (movie.name === movieName) {
                return movie;
            }
        }
        return "";
    }

    let movies = [];

    for (let movieData of movieDataList) {
        let movieDataList = movieData.split(" ");
        if (movieDataList[0] === "addMovie") {
            let movieName = movieDataList.slice(1).join(" ").trim();
            movies.push(new Movie(movieName, "", ""));
        } else if (movieDataList.includes("directedBy")) {
            let index = movieDataList.indexOf("directedBy");
            let movieName = movieDataList.slice(0, index).join(" ").trim();
            let movie = getMovieByName(movieName, movies);
            if (movie !== "") {
                movie.director = movieDataList.slice(index + 1).join(" ").trim();
            }
        } else if (movieDataList.includes("onDate")) {
            let index = movieDataList.indexOf("onDate");
            let movieName = movieDataList.slice(0, index).join(" ").trim();
            let movie = getMovieByName(movieName, movies);
            if (movie !== "") {
                movie.date = movieDataList.slice(index + 1).join(" ").trim();
            }
        }
    }

    for (let movie of movies) {
        if (movie.isValid()) {
            console.log(JSON.stringify(movie));
        }
    }
}

solve([
    'addMovie The Avengers',
    'addMovie Superman',
    'The Avengers directedBy Anthony Russo',
    'The Avengers onDate 30.07.2010',
    'Captain America onDate 30.07.2010',
    'Captain America directedBy Joe Russo'
]

)