function solve(commands) {
    class Book {
        constructor(title, author, genre) {
            this.title = title;
            this.author = author;
            this.genre = genre;
        }

        print() {
            console.log(`--> ${this.title}: ${this.author}`);
        }
    }

    class Shelf {
        constructor(id, genre) {
            this.id = id;
            this.genre = genre;
            this.books = [];
        }

        addBook(book) {
            this.books.push(book);
        }

        print() {
            console.log(`${this.id} ${this.genre}: ${this.books.length}`)
            for (let book of this.books.sort((a, b) => a.title.localeCompare(b.title))) {
                book.print();
            }
        }
    }

    function isShelfIDFree(shelfID, shelfs) {
        for (let i = 0; i < shelfs.length; i++) {
            if (shelfID === shelfs[i].id) {
                return false;
            }
        }
        return true;
    }

    function getShelfIndexByGenre(genre, shelfs) {
        for (let i = 0; i < shelfs.length; i++) {
            if (genre === shelfs[i].genre) {
                return i;
            }
        }
        return -1;
    }

    let shelfs = [];

    for (let command of commands) {
        if (command.includes(" -> ")) {
            let [shelfId, shelfGenre] = command.split(" -> ");
            if (isShelfIDFree(shelfId, shelfs)) {
                shelfs.push(new Shelf(shelfId, shelfGenre));
            }
        } else {
            let [bookTitle, bookData] = command.split(": ");
            let [bookAuthor, bookGenre] = bookData.split(", ");
            let shelfIndex = getShelfIndexByGenre(bookGenre, shelfs);
            if (shelfIndex !== -1) {
                shelfs[shelfIndex].addBook(new Book(bookTitle, bookAuthor, bookGenre));
            }
        }
    }

    for (let shelf of shelfs.sort((a, b) => b.books.length - a.books.length)) {
        shelf.print();
    }
}

solve(['1 -> mystery', '2 -> sci-fi',
    'Child of Silver: Bruce Rich, mystery',
    'Lions and Rats: Gabe Roads, history',
    'Effect of the Void: Shay B, romance',
    'Losing Dreams: Gail Starr, sci-fi',
    'Name of Earth: Jo Bell, sci-fi']
);