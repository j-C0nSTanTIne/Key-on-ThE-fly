from funcs import *
import sys

# APPLICAZIONE

while(True):
    choice = input(menu + enter)
    if choice.lower() == "exit":
        sys.exit(0)
    elif choice.lower() != "1" and choice.lower() != "2" and choice.lower() != "3" and choice.lower() != "exit":
        print(error)
        continue
    elif choice.lower() == "1":
        name_instance = input(new_1 + enter)
        if name_instance == "":
            print(error)
            continue
        else:
            description_instance = input(new_2 + enter)
            length = input(new_length + enter)
            if length != "8" and length != "16" and length != "20" and length != "32" and length != "64" and length != "128":
                print(error)
                continue
            else:
                special_excluded = input(new_specials + enter)
                temp = True
                if special_excluded != "": 
                    for char in special_excluded:
                        if char not in special_characters:
                            temp = False
                if temp:
                    first_question = input(new_3 + enter)
                    if first_question == "":
                        print(error)
                        continue
                    else:
                        first_answer = input(new_4 + enter)
                        if first_answer == "":
                            print(error)
                            continue
                        else:
                            second_question = input(new_5 + enter)
                            if second_question == "":
                                print(error)
                                continue
                            else:
                                second_answer = input(new_6 + enter)
                                if second_question == "":
                                    print(error)
                                    continue
                                else:
                                    third_question = input(new_7 + enter)
                                    if third_question != "":
                                        third_answer = input(new_8 + enter)
                                        if third_answer == "":
                                            print(error)
                                            continue
                                        else:
                                            instance = New_Instance(name_instance.upper(), description_instance, length, special_excluded, first_question.lower(), first_answer.lower(), 
                                            second_question.lower(), second_answer.lower(), third_question.lower(), third_answer.lower())
                                            instance.generate("creation")
                                    else:
                                        instance = New_Instance(name_instance.upper(), description_instance, length, special_excluded, first_question.lower(), first_answer.lower(), 
                                        second_question.lower(), second_answer.lower(), "", "")
                                        instance.generate("creation")
                else:
                    print(error)
                    continue
    elif choice.lower() == "2":
        instance = Instance()
        show = instance.database_names()
        if show:
            request = input(retrieve + enter)
            if int(request) not in instance.instances_dict.keys():
                print(error)
                continue
            else:
                result = instance.retrieve(request)
                check_one = input("\nPRIMA DOMANDA: [ " + result[4] + " ]" + enter)
                if check_one == "":
                    print(error)
                    continue
                else:
                    check_two = input("\nSECONDA DOMANDA: [ " + result[5] + " ]" + enter)
                    if check_two == "":
                        print(error)
                        continue
                    else:
                        if result[6] != "":
                            check_three = input("\nTERZA DOMANDA: [ " + result[6] + " ]" + enter)
                            if check_three == "":
                                print(error)
                                continue
                            else:
                                answer = New_Instance(result[0], result[1], result[2], result[3], result[4], check_one.lower(), result[5], check_two.lower(), result[6], check_three.lower())
                                answer.generate("give_answer")
                        else:
                            answer = New_Instance(result[0], result[1], result[2], result[3], result[4], check_one.lower(), result[5], check_two.lower(), result[6], "")
                            answer.generate("give_answer")
        else:
            continue
    elif choice.lower() == "3":
        instance = Instance()
        show = instance.database_names()
        if show:
            request = input(delete + enter)
            if int(request) not in instance.instances_dict.keys():
                print(error)
                continue
            else:
                result = instance.retrieve(request)
                check_one = input("\n" + delete_check + enter)
                if check_one.lower() == "s":
                    check_two = input("\n" + delete_check_2 + enter)
                    if check_two.lower() == "s":
                        instance.delete_db(request)
                else:
                    continue
        else:
            continue
    else:
        print(error)
        continue
        
# ++++