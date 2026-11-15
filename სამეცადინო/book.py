
class Book:
    def __init__(self, title, author, year):   #init ით იწყება კონსტურქტორი, რა ატრიბუტერი უნდა ქონდეს მაგას განსაზღვრას კლასი იგივ ბლუ პრინთ ჩონჩხი
        if not title.strip():
            raise ValueError("სათაური ცარიელი არ უნდა იყოს.")

        if not author.strip():
            raise ValueError("ავტორი ცარიელი არ უნდა იყოს.")

        if not isinstance(year, int) or not 1 <= year <= 2026:   #ინსტანსე ფუქნვის ამოწმებს წელი არის თუარა ინთეჯერის ტიპის 
            raise ValueError("გამოცემის წელი არასწორია.")  #ველიუერორს მე თვითონ ვარტყმევინებ თუ ეს ქეისი გაეძრო

        self.__title = title.strip()  #ამ ატრიბუტს აზძლევს მნიშვნეკობას  სტრიფს  ნიშნავს 
        self.__author = author.strip() 
        self.__year = year
       # self.fexi = 5  ეს გარედან გადაეცემა 

    @property  #დეკორატორი რას აკეთებს დეკორატორი და აქ  რა რა საჭირო რა დედისტყვნაში მჭირდება (ცვლი)
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    def display_info(self):
        print(f"სათაური: {self.title}")
        print(f"ავტორი: {self.author}")
        print(f"გამოცემის წელი: {self.year}")
