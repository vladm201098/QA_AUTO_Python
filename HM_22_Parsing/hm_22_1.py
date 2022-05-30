import xml.etree.ElementTree as ET

tree = ET.parse("library.xml")
root = tree.getroot()

# Поиск книги по автору, частичное совпадение имени
for book in root.findall('book'):
    for author in book.findall('author'):
        book_author = author.text
        if "Eva" in book_author:
            print(book.attrib)
            for child in book:
                print(child.tag, child.text)

# Поиск книги по цене
for book in root.findall('book'):
    for price in book.findall('price'):
        book_price = price.text
        if "36.75" in book_price:
            print(book.attrib)
            for child in book:
                print(child.tag, child.text)

# Поиск книги по заголовку
for book in root.findall('book'):
    for title in book.findall('title'):
        book_title = title.text
        if "Learn Python 3 the Hard Way" in book_title:
            print(book.attrib)
            for child in book:
                print(child.tag, child.text)

# Поиск книги по описанию
for book in root.findall('book'):
    for description in book.findall('description'):
        book_description = description.text
        if "A former architect" in book_description:
            print(book.attrib)
            for child in book:
                print(child.tag, child.text)