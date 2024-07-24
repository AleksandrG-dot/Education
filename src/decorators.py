from functools import wraps


def log(filename=""):
    """Декоратор для создания логов функций в файл или в терминал"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                error_msg = ""
            except Exception as e:
                log_message = f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                error_msg = e
            finally:
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)
                if error_msg:
                    raise error_msg
                return result

        return wrapper

    return decorator
