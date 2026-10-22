#task_2
numbers= [3,7,2,9,4,1,8]
numbers.append(5)
numbers.remove(9)
numbers.sort(reverse=True)
numbers.insert(2, 6)
print(numbers.index(4))
print(numbers)

#task_3
my_tuple=(15, "Python", 3.14, True, 42, False)
print(my_tuple.index("Python"))
print(my_tuple.count(True))
print(my_tuple[0:4])

#task_4
score_students = {"Alice": 85, 
                  "Bob": 92,
                  "Charlie": 78, 
                  "David": 90,
                  "Eva": 95,
                  "Sardor": 88,
                  "Farruh": 80,
                  "Gulnora": 92,
                  "Husan": 87,
                  "Jasur": 91,
                  "Karim": 89,
                  "Lola": 94,
                  "Mansur": 86,
                  "Nodira": 93,
                  "Otabek": 88,}
score_students["Frank"] = 60
print(score_students)


