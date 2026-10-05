#Task 1: User Profile Creator / მომხმარებლის პროფილის შექმნა
def create_user_profile(first_name, last_name, role="Student", is_active=True):
    profile = {
        "first_name": first_name,
        "last_name": last_name,
        "role": role,
        "is_active": is_active
    }
    return profile
user1 = create_user_profile("Nino", "Chkhapelia")
print("User 1:", user1)

user2 = create_user_profile("Giorgi", "Chkhapelia", role="Admin", is_active=False)
print("User 2:", user2)


#Task 2A: The To-Do List Trap / To-Do სიის „ხაფანგი“

def add_task(task_name, task_list=[]):
    task_list.append(task_name)
    return task_list

print(add_task("Prepare for Python exam"))
print(add_task("Optimize code"))
print(add_task("Manage BI Reports"))

#Task 2B: Refactor with None / გადაკეთება None მიდგომით
def add_task(task_name, task_list=None):
    if task_list is None:
        task_list = []
    
    task_list.append(task_name)
    return task_list

print(add_task("Prepare for Python exam"))
print(add_task("Optimize code"))
print(add_task("Manage BI Reports"))

#Task 3: Text Analyzer / ტექსტის ანალიზატორი

def analyze_text(text, min_length=3, ignore_stopwords=None):

    if ignore_stopwords is None:
        ignore_stopwords = []
    
    words = text.split()
    
    count = 0
    for word in words:
        if len(word) >= min_length and word not in ignore_stopwords:
            count += 1

    return count

sample_text = "python is a great programming language and it is fun"
stopwords = ["is", "and", "it"]

result = analyze_text(sample_text, min_length=3, ignore_stopwords=stopwords)
print("Filtered word count:", result)
