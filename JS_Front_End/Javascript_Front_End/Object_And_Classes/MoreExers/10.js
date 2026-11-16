function solve(commands) {
    class Article {
        constructor(name) {
            this.name = name;
            this.comments = [];
        }

        addComment(comment) {
            this.comments.push(comment);
        }

        print() {
            console.log(`Comments on ${this.name}`);
            for (let comment of this.comments.sort((a, b) => a.username.localeCompare(b.username))) {
                comment.print();
            }
        }
    }

    class Comment {
        constructor(username, title, content) {
            this.username = username;
            this.title = title;
            this.content = content;
        }

        print() {
            console.log(`--- From user ${this.username}: ${this.title} - ${this.content}`);
        }
    }

    function isUserExists(searchUser, users) {
        for (let user of users) {
            if (user === searchUser) {
                return true;
            }
        }
        return false;
    }

    function getArticleIndex(searchArticle, articles) {
        for (let i = 0; i < articles.length; i++) {
            if (articles[i].name === searchArticle) {
                return i;
            }
        }
        return -1;
    }

    let users = [];
    let articles = [];

    for (let command of commands) {
        if (command.includes("user")) {
            let username = command.split(" ")[1];
            users.push(username);
        } else if (command.includes("article")) {
            let arr = command.split(" ");
            let article = arr.slice(1).join(" ");
            if (getArticleIndex(article, articles) === -1) {
                articles.push(new Article(article));
            }
        } else {
            let arr = command.split(": ");
            let [userName, articleName] = arr[0].split(" posts on ");
            let [commentTitle, commentContent] = arr[1].split(", ");
            let articleIndex = getArticleIndex(articleName, articles);
            if (isUserExists(userName, users) && articleIndex !== -1) {
                articles[articleIndex].addComment(new Comment(userName, commentTitle, commentContent));
            }
        }
    }

    for (let article of articles.sort((a, b) => -a.comments.length + b.comments.length)) {
        article.print();
    }
}

solve(['user Mark',
    'Mark posts on someArticle: NoTitle, stupidComment',
    'article Bobby',
    'article Steven',
    'user Liam',
    'user Henry',
    'Mark posts on Bobby: Is, I do really like them',
    'Mark posts on Steven: title, Run',
    'someUser posts on Movies: Like']);