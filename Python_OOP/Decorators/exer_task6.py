def tags(tag):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"

        return wrapper

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
