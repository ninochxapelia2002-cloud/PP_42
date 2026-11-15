import csv

# TASK 1: Quotes

def save_quote():
    author = input("შეიყვანეთ მწერლის სახელი: ")
    quote = input("შეიყვანეთ ციტატა: ")
    with open("quotes.txt", "w", encoding="utf-8") as file:
        file.write(f"მწერალი: {author}\nციტატა: {quote}\n")
    print("ციტატა წარმატებით ჩაიწერა quotes.txt ფაილში.")

def read_quote():
    try:
        with open("quotes.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print("\n--- quotes.txt შიგთავსი ---")
            print(content)
    except FileNotFoundError:
        print("ფაილი quotes.txt ჯერ არ არსებობს.")

# TASK 2: Titanic Survivors

def filter_titanic_survivors():
    try:
        survivors = []
        with open("titanic.csv", "r", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames 
            for row in reader:
                if row.get("survived") == "1" or row.get("Survived") == "1":
                    survivors.append(row)
        if fieldnames and survivors:
            with open("survived.csv", "w", newline="", encoding="utf-8") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(survivors)
            print("გადარჩენილი მგზავრები წარმატებით ჩაიწერა survived.csv ფაილში.")
        else:
            print("მონაცემები ვერ მოიძებნა ან ფაილი ცარიელია.")
            
    except FileNotFoundError:
        print("ფაილი titanic.csv ვერ მოიძებნა დირექტორიაში.")

# TASK 3: Companies Filter

def filter_companies():
    try:
        filtered_data = []
        with open("ssl_companies.csv", "r", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                try:
                    emp_count_str = row.get("Number of employee") or row.get("Number of employees") or "0"
                    emp_count = int(emp_count_str)
                    if emp_count > 1000:
                        filtered_data.append({
                            "Name": row.get("Name"),
                            "Industry": row.get("Industry"),
                            "Number of employee": emp_count
                        })
                except ValueError:
                    continue      
        fieldnames = ["Name", "Industry", "Number of employee"]
        with open("sorted_companies.csv", "w", newline="", encoding="utf-8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_data)
        print("კომპანიების გაფილტრული სია წარმატებით ჩაიწერა sorted_companies.csv ფაილში.")
        
    except FileNotFoundError:
        print("ფაილი ssl_companies.csv ვერ მოიძებნა დირექტორიაში.")

if __name__ == "__main__":
    # Task 1 ტესტი:
    # save_quote()
    # read_quote()
    
    # Task 2 ტესტი:
    # filter_titanic_survivors()
    
    # Task 3 ტესტი:
    # filter_companies()
    pass