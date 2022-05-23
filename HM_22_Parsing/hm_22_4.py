import json
import requests

# Получение списка авторов
all_authors = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Authors")
print(all_authors.json())

# Получение конкретного автора по его id
author_id = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Authors/5")
print(author_id.json())

# Добавить новую книгу
new_book = {
    "id": 1,
    "title": "Midnight Rain",
    "description": "A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world.",
    "pageCount": 285,
    "excerpt": "Do you remember the exact moment your childhood ended? 1977... Jimmy Carter is sworn in as America's 39th President. "
               "New York Police apprehend the Son of Sam. The King of Rock n' Roll permanently leaves the building. "
               "STAR WARS is the #1 film in the world. In a small town called Midnight, North Carolina, "
               "twelve-year-old Kyle Mackey couldn't care less about any of that. He has his own problems to deal with, "
               "as he ventures toward a strange new world called manhood... Kyle's older brother Dan is going away to college.",
    "publishDate": "2000-12-16T12:21:00.723Z"
}
add_new_book = requests.post(
    "https://fakerestapi.azurewebsites.net/api/v1/Books", json=new_book)
print(add_new_book.json())

# Добавить нового пользователя
new_user = {
    "id": 1,
    "userName": 'Pavel',
    "password": 'qwe1'
}
add_new_user = requests.post(
    "https://fakerestapi.azurewebsites.net/api/v1/Users", json=new_user)
print(add_new_user.json())

# Обновить данные для книги под номером 10
update_book = {
    "title": "Python для чайников",
    "description": "После этой книги вы станете крутыми python программистами.",
    "pageCount": 785,
    "publishDate": "2021-08-01T12:21:00.723Z"
}
upt_book = requests.put(
    "https://fakerestapi.azurewebsites.net/api/v1/Books/10", json=update_book)
print(upt_book.json())

# Удалить пользователя под номером 4
del_user = requests.delete(f"https://fakerestapi.azurewebsites.net/api/v1/Users/4")
print(del_user.status_code)