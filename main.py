import json
import urllib.request

api = 'https://play.kahoot.it/rest/kahoots/'
usrinput = input("Quiz ID >")
link = api + usrinput

try:
    with urllib.request.urlopen(link) as url:
        data = json.load(url)
        # print(data['questions'][0]['choices'])
        quizlength = len(data['questions'])
        answers = {}

        def IsAQuestion(dat):
            try:
                eval(dat)
                return True
            except KeyError:
                return False

        question = 0
        for x in range(quizlength):
            if IsAQuestion("data['questions'][question]['choices']"):
                try:
                    # answers[f"Question {question + 1}"][1] = data['questions'][question]['choices'][questioninquestion]
                    if data['questions'][question]['type'] == "quiz":
                        if data['questions'][question]['choices'][0]['correct']:
                            answers[f"Question {question + 1}"] = 'Red'
                        elif data['questions'][question]['choices'][1]['correct']:
                            answers[f"Question {question + 1}"] = 'Blue'
                        elif data['questions'][question]['choices'][2]['correct']:
                            answers[f"Question {question + 1}"] = 'Yellow'
                        elif data['questions'][question]['choices'][3]['correct']:
                            answers[f"Question {question + 1}"] = 'Green'
                    elif data['questions'][question]['type'] == "jumble":
                        length = len(data['questions'][question]['choices'])
                        for y in range(length):
                            if answers.get(f"Question {question + 1}") is None:
                                answers[f"Question {question + 1}"] = ""
                            answers[f"Question {question + 1}"] += str(data['questions'][question]['choices'][y]['answer']).upper()

                    elif data['questions'][question]['type'] == "survey":
                        answers[f"Question {question + 1}"] = "This is a survey, there are no answers"

                    elif data['questions'][question]['type'] == "content":
                        answers[f"Question {question + 1}"] = "This is just content, there are no answers"

                    elif data['questions'][question]['type'] == "multiple_select_quiz":
                        for z in range(len(data['questions'][question]['choices'])):
                            if data['questions'][question]['choices'][0]['correct']:
                                if answers.get(f"Question {question + 1}") is None:
                                    answers[f"Question {question + 1}"] = ""

                                if answers[f"Question {question + 1}"] == "":
                                    answers[f"Question {question + 1}"] += "Blue"
                                else:
                                    answers[f"Question {question + 1}"] += ", " + "Blue"

                            if data['questions'][question]['choices'][1]['correct']:
                                if answers.get(f"Question {question + 1}") is None:
                                    answers[f"Question {question + 1}"] = ""

                                if answers[f"Question {question + 1}"] == "":
                                    answers[f"Question {question + 1}"] += "Red"
                                else:
                                    answers[f"Question {question + 1}"] += ", " + "Red"

                            if data['questions'][question]['choices'][2]['correct']:
                                if answers.get(f"Question {question + 1}") is None:
                                    answers[f"Question {question + 1}"] = ""

                                if answers[f"Question {question + 1}"] == "":
                                    answers[f"Question {question + 1}"] += "Yellow"
                                else:
                                    answers[f"Question {question + 1}"] += ", " + "Yellow"

                            if data['questions'][question]['choices'][3]['correct']:
                                if answers.get(f"Question {question + 1}") is None:
                                    answers[f"Question {question + 1}"] = ""

                                if answers[f"Question {question + 1}"] == "":
                                    answers[f"Question {question + 1}"] += "Green"
                                else:
                                    answers[f"Question {question + 1}"] += ", " + "Green"

                        string2 = ', '.join(set(answers[f"Question {question + 1}"].split(', ')))
                        answers[f"Question {question + 1}"] = string2
                    else:
                        answers[f"Question {question + 1}"] = 'This is not a question'

                    question += 1

                except Exception as err:
                    print(err)
            else:
                answers[f"Question {question + 1}"] = 'This is not a question'
                question += 1

    for key, value in answers.items():
        print(key, ':', value + "\n")
except Exception as err:
    print("There was an error! It could be because the quiz id is incorrect.\n")
    print(err)

input("\nEnter to exit...")
