while True:
    age = input("Type your ages: ")
    if 0 <= age:
        age = age
        break
    else:
        age = input("Type your ages: ")

while True:
  gpa = input("Type your GPA: ")
  if 0 <= gpa:
    gpa = gpa.round(1)
  else:
    gpa = input("Type your GPA: ") 