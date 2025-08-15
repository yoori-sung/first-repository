import os

class Book:
    """책 정보를 담는 클래스"""
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"제목: {self.title}, 저자: {self.author}, ISBN: {self.isbn}"

class BookManager:
    """도서 관리 기능을 제공하는 클래스"""
    def __init__(self, filename="books.csv"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """파일에서 도서 목록을 불러옵니다."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        title, author, isbn = line.strip().split(',')
                        self.books.append(Book(title, author, isbn))
                    except ValueError:
                        print(f"경고: 잘못된 형식의 데이터가 발견되었습니다: {line.strip()}")
        print(f"총 {len(self.books)}권의 책을 불러왔습니다.")

    def save_books(self):
        """도서 목록을 파일에 저장합니다."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            for book in self.books:
                f.write(f"{book.title},{book.author},{book.isbn}\n")
        print(f"총 {len(self.books)}권의 책을 저장했습니다.")

    def add_book(self):
        """새로운 책을 추가합니다."""
        title = input("제목: ")
        author = input("저자: ")
        isbn = input("ISBN: ")

        if any(book.isbn == isbn for book in self.books):
            print("이미 존재하는 ISBN입니다.")
            return

        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print("책이 성공적으로 추가되었습니다.")
        self.save_books()

    def search_book(self):
        """제목, 저자, 또는 ISBN으로 책을 검색합니다."""
        keyword = input("검색할 키워드 (제목, 저자, ISBN): ").lower()
        found_books = [book for book in self.books if keyword in book.title.lower() or
                                                      keyword in book.author.lower() or
                                                      keyword in book.isbn.lower()]

        if found_books:
            print("\n--- 검색 결과 ---")
            for book in found_books:
                print(book)
        else:
            print("검색 결과가 없습니다.")

    def delete_book(self):
        """ISBN으로 책을 삭제합니다."""
        isbn_to_delete = input("삭제할 책의 ISBN을 입력하세요: ")
        initial_count = len(self.books)
        self.books = [book for book in self.books if book.isbn != isbn_to_delete]

        if len(self.books) < initial_count:
            print(f"ISBN {isbn_to_delete}에 해당하는 책이 삭제되었습니다.")
            self.save_books()
        else:
            print("해당 ISBN을 가진 책을 찾을 수 없습니다.")

    def list_all_books(self):
        """모든 책 목록을 출력합니다."""
        if not self.books:
            print("등록된 책이 없습니다.")
            return

        print("\n--- 전체 도서 목록 ---")
        for book in self.books:
            print(book)
        print("--------------------")

def main_menu():
    """메인 메뉴를 출력하고 사용자의 입력을 받습니다."""
    print("\n--- 도서 관리 시스템 ---")
    print("1. 책 추가")
    print("2. 책 검색")
    print("3. 책 삭제")
    print("4. 전체 목록 보기")
    print("5. 종료")
    return input("메뉴를 선택하세요: ")

def main():
    """프로그램의 메인 함수"""
    manager = BookManager()
    while True:
        choice = main_menu()
        if choice == '1':
            manager.add_book()
        elif choice == '2':
            manager.search_book()
        elif choice == '3':
            manager.delete_book()
        elif choice == '4':
            manager.list_all_books()
        elif choice == '5':
            print("프로그램을 종료합니다. 안녕히 계세요!")
            break
        else:
            print("잘못된 메뉴 선택입니다. 다시 시도해 주세요.")

if __name__ == "__main__":
    main()