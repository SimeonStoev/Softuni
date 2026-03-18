import re

head_pattern = r"(?<=<title>).+(?=<\/title>)"
body_pattern = r"(?<=<body>).+(?=<\/body>)"
replace_newline_pattern = r"\\n"
replace_tags_pattern = r"<[^>]+>"

html_text = input()

title = re.search(head_pattern, html_text).group()
title = re.sub(replace_newline_pattern, "", title)
title = re.sub(replace_tags_pattern, "", title)
content = re.search(body_pattern, html_text).group()
content = re.sub(replace_newline_pattern, "", content)
content = re.sub(replace_tags_pattern, "", content)
print(f"Title: {title}")
print(f"Content: {content}")
