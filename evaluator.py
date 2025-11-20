def ask_question(quesobj):
    print("\n" + quesobj["question"])

    options = quesobj["options"]
    for i, opt in enumerate(options):
        print(f"{chr(65+i)}) {opt}")

    while True:
        user_ans = input("Your answer: ").strip().upper()

        if not user_ans.isalpha() or len(user_ans) != 1:
            print("Invalid input, please enter A, B, C, or D.")
            continue 

        chosen = ord(user_ans) - 65

        if chosen < 0 or chosen >= len(options):
            print("Invalid input, please choose A, B, C, or D.")
            continue 

        break 

    correct = quesobj["answer"]

    if chosen == correct:
        return True
    
    else:
        return False
