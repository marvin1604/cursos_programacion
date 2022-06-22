DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #using hight functions
    all_python_devs= [worker["name"] for worker in DATA if worker["language"] == "python"]
    #using list comprenhension
    language1= list(filter(lambda worker: worker["language"] == "python", DATA ))
    language1= list(map(lambda worker: worker["name"], language1))

    #using hight functions
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    #using list comprenhension
    organization1= list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    organization1= list(map(lambda worker: worker["name"], organization1))


    #using list comprenhension
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    #keep only the name with map fuction
    adults = list(map(lambda worker: worker["name"], adults))
    #using hight functions
    all_adults_workers= [worker["name"] for worker in DATA if worker["age"] > 18]



    #create new valor old_people
    old_people= list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))


    # for worker in all_python_devs:
    #     print("python: ", worker)
        
    # for worker in all_platzi_workers:
    #     print("platzi: ", worker)

    # for worker in adults:
    #     print(">18: ", worker)

    for worker in language1:
        print("python: ", worker)

    for worker in organization1:
        print("platzi: ", worker)

    for worker in all_adults_workers:
        print("adults: ", worker)



if __name__ == "__main__":
    run()