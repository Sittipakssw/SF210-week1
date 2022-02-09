while True:
    age = input("Type your age: ")
    if 0 <= age:
        age = age
        break
    else:
        age = input("Type your age: ")

while True:
  gpa = input("Type your GPA: ")
  if 0 <= gpa:
    gpa = gpa.round(1)
  else:
    gpa = input("Type your GPA: ")