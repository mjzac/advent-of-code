from utils import get_input

declarations = get_input(6)


unique_questions = set()
common_questions = set()
p1_result = 0
p2_result = 0
first_entry = True
for ans in declarations:
    if ans == "":
        p1_result += len(unique_questions)
        unique_questions.clear()
        p2_result += len(common_questions)
        common_questions.clear()
        first_entry = True
    else:
        unique_questions.update((set(list(ans))))
        if first_entry:
            common_questions = set(list(ans))
            first_entry = False
        else:
            common_questions = common_questions.intersection(set(list(ans)))

if (len(unique_questions)) > 0:
    p1_result += len(unique_questions)
    unique_questions.clear()
if (len(common_questions)) > 0:
    p2_result += len(common_questions)
    common_questions.clear()
print(p1_result)

print(p2_result)
