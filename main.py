import json
"""Quiz posiada 5 pytan"""
points = 0

def show_question(question):
    global points
    print(question["Pytanie"])
    print("-"*10)
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("-"*10)
    
    answer = input("Wybierz odpowiedz: ")

    if answer == question["Odpowiedz poprawna"]:
        points += 1
        print("To dobra odpowiedz masz juz kolejny punkt:", points)
    else:
        print("To niepoprawna odpowiedz, poprawna odpowiedz to:" + question["Odpowiedz poprawna"])

with open("question.json") as json_question:
    questions = json.load(json_question)

    print(questions)

    for i in range(0, len(questions)):
        show_question(questions[i])

print("Koniec Quizu, twoje punkty to: ", points)