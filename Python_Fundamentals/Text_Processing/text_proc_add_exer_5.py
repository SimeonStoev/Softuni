html_article = ""

title = input()
html_article += "<h1>\n\t" + title + "\n</h1>\n"
content = input()
html_article += "<article>\n\t" + content + "\n</article>\n"

while True:
    comment = input()

    if comment == "end of comments":
        break
    html_article += "<div>\n\t" + comment + "\n</div>\n"

print(html_article)
