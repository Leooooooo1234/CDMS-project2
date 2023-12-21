from init_db.ConnectDB import Book
from sqlalchemy import create_engine,ForeignKey, func
from sqlalchemy.orm import sessionmaker



class BookDB:
    def __init__(self):
        engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5433/bookstore', encoding='utf-8',
                               echo=True)
        db_session_class = sessionmaker(bind=engine)  # db_session_class 仅仅是一个类
        self.Session = db_session_class()

    def get_book_count(self):
        # conn = sqlite.connect(self.book_db)
        cursor = self.Session.query(func.count(Book.book_id)).first()
        return cursor[0]

    def get_book_id(self, start, size) -> [Book]:
        books = []
        cursor = self.Session.execute(
            "SELECT id, title, author, "
            "publisher, original_title, "
            "translator, pub_year, pages, "
            "price, currency_unit, binding, "
            "isbn, author_intro, book_intro, "
            "content, tags, picture FROM book ORDER BY id "
            "LIMIT %d OFFSET %d"%(size, start))
        for row in cursor:
            # book = {
            # "id" : str(row[0]),
            # "title" : str(row[1]),
            # "author" : str(row[2]),
            # "publisher" : str(row[3]),
            # "original_title" : str(row[4]),
            # "translator" : str(row[5]),
            # "pub_year" : str(row[6]),
            # "pages" : str(row[7]),
            # "price" : str(row[8]),
            # "currency_unit" : str(row[9]),
            # "binding" : str(row[10]),
            # "isbn": str(row[11]),
            # "author_intro" : str(row[12]),
            # "book_intro" : str(row[13]),
            # "content" : str(row[14]),
            # "tags" : str(row[15]),
            # "pictures" : str(row[16])}
            # tags = row[15]
            # picture = row[16]

            # for tag in tags.split("\n"):
            #     if tag.strip() != "":
            #         book.tags.append(tag)
            # for i in range(0, random.randint(0, 9)):
            #     if picture is not None:
            #         encode_str = base64.b64encode(picture).decode('utf-8')
            #         book.pictures.append(encode_str)
            books.append(row[0])


        return books


