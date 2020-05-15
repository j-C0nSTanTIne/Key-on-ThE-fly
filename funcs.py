import random
import sqlite3
from os import path
import hashlib

# TESTI

menu = """
+ + + + key on ThE fly + + + +

Selezionare l'opzione desiderata, oppure digitare «exit» per terminare l'applicazione:

1. Crea una nuova istanza;

2. Seleziona una istanza;

3. Elimina una istanza;"""

enter = "\n\n>>>> "

error = "\nErrore nell'inserimento dei dati. Riprovare."

new_1 = "\nInserire il nome della nuova istanza:"

new_2 = "\n(OPZIONALE) Inserire una breve descrizione dell'istanza, oppure premere INVIO:"

new_length = "\nInserire la lunghezza della password (Valori possibili = 8 - 16 - 20 - 32 - 64 - 128):"

new_specials = """
(OPZIONALE) Elencare i caratteri speciali da non usare nella creazione della password, separandoli con lo spazio, altrimenti premere INVIO:
caratteri impiegati -> ! $ % ( ) = ? , _ -"""

special_characters = [" ", "!", "$", "%", "(", ")", "=", "?", ",", "_", "-"]

new_3 = "\nInserire la prima domanda:"

new_4 = "\nInserire la prima risposta:"

new_5 = "\nInserire la seconda domanda:"

new_6 = "\nInserire la seconda risposta:"

new_7 = "\n(OPZIONALE) Inserire la terza domanda, oppure premere INVIO:"

new_8 = "\nInserire la terza risposta:"

retrieve = "\nSelezionare l'istanza da eseguire:"

delete = "\nSelezionare l'istanza da eliminare:"

delete_check = "\nSi è sicuri di voler eliminare l'istanza? ['s' per Sì, 'n' per NO]"

delete_check_2 = "\nL'istanza verrà cancellata. Confermare un'ultima volta ['s' per Sì, 'n' per NO]"

# ++++

# CLASSI

class New_Instance:
    def __init__(self, instance_title, instance_description, instance_length, instance_excluded, question_one, answer_one, question_two, answer_two, question_three, answer_three):
        self.instance_title = instance_title
        self.instance_description = instance_description
        self.instance_length = int(instance_length)
        self.instance_excluded = instance_excluded
        self.question_one = question_one
        self.answer_one = answer_one
        self.question_two = question_two
        self.answer_two = answer_two
        self.question_three = question_three
        self.answer_three = answer_three
        
        self.reconversion_matrix = {
                                        1 : "a",
                                        2 : "b",
                                        3 : "c",
                                        4 : "d",
                                        5 : "e",
                                        6 : "f",
                                        7 : "g",
                                        8 : "h",
                                        9 : "i",
                                        10 : "j",
                                        11 : "k",
                                        12 : "l",
                                        13 : "m",
                                        14 : "n",
                                        15 : "o",
                                        16 : "p",
                                        17 : "q",
                                        18 : "r",
                                        19 : "s",
                                        20 : "t",
                                        21 : "u",
                                        22 : "v",
                                        23 : "w",
                                        24 : "x",
                                        25 : "y",
                                        26 : "z",
                                        27 : "1",
                                        28 : "2",
                                        29 : "3",
                                        30 : "4",
                                        31 : "5",
                                        32 : "6",
                                        33 : "7",
                                        34 : "8",
                                        35 : "9",
                                        36 : "0"
        }
        
        self.reconversion_matrix_2 = {
                                        1 : "!",
                                        2 : "$",
                                        3 : "%",
                                        4 : "(",
                                        5 : ")",
                                        6 : "=",
                                        7 : "?",
                                        8 : ",",
                                        9 : "_",
                                        10 : "-"
        }
        
        self.reconversion_matrix_3 = {
                                        1 : "A",
                                        2 : "B",
                                        3 : "C",
                                        4 : "D",
                                        5 : "E",
                                        6 : "F",
                                        7 : "G",
                                        8 : "H",
                                        9 : "I",
                                        10 : "J",
                                        11 : "K",
                                        12 : "L",
                                        13 : "M",
                                        14 : "N",
                                        15 : "O",
                                        16 : "P",
                                        17 : "Q",
                                        18 : "R",
                                        19 : "S",
                                        20 : "T",
                                        21 : "U",
                                        22 : "V",
                                        23 : "W",
                                        24 : "X",
                                        25 : "Y",
                                        26 : "Z"
        }
    
    def generate(self, task):
        self.task = task
        
        print("\n[ + + + + ]")
        print("[ + ] Trovo l'hash sha512 delle risposte fornite...")
        magic_instance_one = self.get_magic(self.answer_one)
        print("magic 1 -> " + str(magic_instance_one))
        magic_instance_two = self.get_magic(self.answer_two)
        print("magic 2 -> " + str(magic_instance_two))
        if self.question_three != "":
            magic_instance_three = self.get_magic(self.answer_three)
            print("magic 3 -> " + str(magic_instance_three))
        
        print("[ + ] Converto i numeri trovati in lettere, numeri e caratteri speciali...")
        phrase_instance_one = self.from_magic_to_phrase("one", magic_instance_one)
        print("phrase 1 -> " + str(phrase_instance_one))
        phrase_instance_two_special = self.from_magic_to_phrase("two_special", magic_instance_two)
        print("phrase 2 (caratteri speciali) -> " + str(phrase_instance_two_special))
        phrase_instance_two_upper = self.from_magic_to_phrase("two_upper", magic_instance_two)
        print("phrase 2.1 (caratteri maiuscoli) -> " + str(phrase_instance_two_upper))
        if self.question_three != "":
            phrase_instance_three = self.from_magic_to_phrase("three", magic_instance_three)
            print("phrase 3 -> " + str(phrase_instance_three))
        else:
            phrase_instance_three = ""
        
        print("[ + ] Assemblo la password...")
        self.password = self.assemble(phrase_instance_one, phrase_instance_two_special, phrase_instance_two_upper, phrase_instance_three)
        print("password -> " + str(self.password))
        print("[ + + + + ]")
        
        if self.task == "creation":
            self.print_recap_and_save()
        elif self.task == "give_answer":
            self.print_answer()
        
    def get_magic(self, answer):
        temp = []
        hash = hashlib.sha512(answer.encode()).hexdigest()
        for char in hash:
            if char == "a":
                temp.append("10")
            elif char == "b":
                temp.append("11")
            elif char == "c":
                temp.append("12")
            elif char == "d":
                temp.append("13")
            elif char == "e":
                temp.append("14")
            elif char == "f":
                temp.append("15")
            else:
                temp.append(char)
        
        return "".join(temp)
    
    def from_magic_to_phrase(self, type_of_conversion, magic_to_convert):
        temp = magic_to_convert
        if len(str(temp)) % 2 != 0:
            while(len(str(temp)) % 2 != 0):
                temp = int(str(temp) + "0")
        magic = str(temp)
        phrase = ""
        
        if type_of_conversion == "one":
            for index, char in enumerate(magic):
                if index % 2 == 0:
                    if magic[index] != "0":
                        if int(magic[index] + magic[index + 1]) > 36:
                            temp = int(magic[index] + magic[index + 1])
                            while(temp > 36):
                                temp = int(temp / 2)
                            phrase += self.reconversion_matrix[temp]
                        else:
                            phrase += self.reconversion_matrix[int(magic[index] + magic[index + 1])] 
                    else:
                        if magic[index + 1] != "0":
                            phrase += self.reconversion_matrix[int(magic[index + 1])]
                        else:
                            pass
        elif type_of_conversion == "two_special":
            dict_length = len(self.reconversion_matrix_2)
            
            if self.instance_excluded != "":
                excluded = []
                for char in self.instance_excluded:
                    if char not in excluded:
                        excluded.append(char)
                
                new_dict = {}
                i = 1
                for key,value in self.reconversion_matrix_2.items():
                    if value not in excluded:
                        new_dict[i] = value
                        i += 1
                
                self.reconversion_matrix_2 = new_dict
                dict_length = len(self.reconversion_matrix_2)
            
            for index, char in enumerate(magic):
                if index % 2 == 0:
                    if magic[index] != "0":
                        if int(magic[index] + magic[index + 1]) > dict_length:
                            temp = int(magic[index] + magic[index + 1])
                            while(temp > dict_length):
                                temp = int(temp / 2)
                            phrase += self.reconversion_matrix_2[temp]
                        else:
                            phrase += self.reconversion_matrix_2[int(magic[index] + magic[index + 1])] 
                    else:
                        if magic[index + 1] != "0" and int(magic[index + 1]) <= dict_length:
                            phrase += self.reconversion_matrix_2[int(magic[index + 1])]
                        else:
                            pass
        elif type_of_conversion == "two_upper":
            for index, char in enumerate(magic):
                if index % 2 == 0:
                    if magic[index] != "0":
                        if int(magic[index] + magic[index + 1]) > 26:
                            temp = int(magic[index] + magic[index + 1])
                            while(temp > 26):
                                temp = int(temp / 2)
                            phrase += self.reconversion_matrix_3[temp]
                        else:
                            phrase += self.reconversion_matrix_3[int(magic[index] + magic[index + 1])] 
                    else:
                        if magic[index + 1] != "0":
                            phrase += self.reconversion_matrix_3[int(magic[index + 1])]
                        else:
                            pass
        elif type_of_conversion == "three":
            for index, char in enumerate(magic):
                if index % 2 == 0:
                    if magic[index] != "0":
                        if int(magic[index] + magic[index + 1]) > 36:
                            temp = int(magic[index] + magic[index + 1])
                            while(temp > 36):
                                temp = int(temp / 2)
                            phrase += self.reconversion_matrix[temp]
                        else:
                            phrase += self.reconversion_matrix[int(magic[index] + magic[index + 1])] 
                    else:
                        if magic[index + 1] != "0":
                            phrase += self.reconversion_matrix[int(magic[index + 1])]
                        else:
                            pass
        
        return phrase
        
    def assemble(self, segment_one, segment_two, segment_three, segment_four):
        if segment_four == "":
            first_part_length = int(self.instance_length / 2)
            second_part_length = int(first_part_length / 2)
            third_part_length = int(second_part_length)
            print("lunghezza password -> " + str(self.instance_length))
            print("suddivisione della sua lunghezza nelle componenti -> " + str(first_part_length) + " - " + str(second_part_length) + " - " + str(third_part_length))
        else:
            first_part_length = int(self.instance_length / 4)
            second_part_length = int(self.instance_length / 4)
            third_part_length = int(self.instance_length / 4)
            fourth_part_length = int(self.instance_length / 4)
            print("lunghezza password -> " + str(self.instance_length))
            print("suddivisione della sua lunghezza nelle componenti -> " + str(first_part_length) + " - " + str(second_part_length) + " - " + str(third_part_length) + " - " + str(fourth_part_length))
        pre_result = []
        result = ""
        
        for counter in range(first_part_length):
            pre_result.append(segment_one[counter])
        for counter in range(second_part_length):
            pre_result.append(segment_two[counter])
        for counter in range(third_part_length):
            pre_result.append(segment_three[counter])
        if segment_four != "":
            for counter in range(fourth_part_length):
                pre_result.append(segment_four[counter])
        print("pre-password -> " + str(pre_result))
        
        if segment_four == "":
            random.seed(len(self.answer_one) + len(self.answer_two))
            print("lunghezza complessiva delle risposte, per derivarne il seed -> " + str(len(self.answer_one) + len(self.answer_two)))
        else:
            random.seed(len(self.answer_one) + len(self.answer_two) + len(self.answer_three))   
            print("lunghezza complessiva delle risposte, per derivarne il seed -> " + str(len(self.answer_one) + len(self.answer_two) + len(self.answer_three)))
        random.shuffle(pre_result)    
        result = "".join(pre_result)
        
        return result
        
    def print_recap_and_save(self):
        recap = """
        +++ RIEPILOGO +++
        
        ISTANZA: {}
        
        DESCRIZIONE: {}
        
        LUNGHEZZA PASSWORD: {}
        
        CARATTERI SPECIALI ESCLUSI: {}
        
        1) PRIMA DOMANDA: [ {} ]
        
        1.2) PRIMA RISPOSTA: [ {} ]
        
        2) SECONDA DOMANDA: [ {} ]
        
        2.2) SECONDA RISPOSTA: [ {} ]
        
        3) TERZA DOMANDA: [ {} ]
        
        3.3) TERZA RISPOSTA: [ {} ]
        
        PA$$WORD GENERATA: [ {} ]
        
        +++ END +++
        
        SI CONFERMA LA CREAZIONE DELL'ISTANZA? ['s' per Sì, 'n' per NO]""".format(self.instance_title, self.instance_description, str(self.instance_length), self.instance_excluded,  
                                                                                  self.question_one, self.answer_one, self.question_two, self.answer_two, self.question_three, self.answer_three, 
                                                                                  self.password)
        
        while(True):
            recap_choice = input(recap + enter)
            if recap_choice.lower() != "s" and recap_choice.lower() != "n":
                print(error)
                continue
            elif recap_choice.lower() == "n":
                print("\nCREAZIONE ANNULLATA!\n++++++++++++++++++++++++++++++++")
                break
            elif recap_choice.lower() == "s":
                self.insert_db()
                break
                
    def print_answer(self):
        recap = """
        +++ RIEPILOGO +++
        
        ISTANZA: {}
        
        DESCRIZIONE: {}
        
        LUNGHEZZA PASSWORD: {}
        
        CARATTERI SPECIALI ESCLUSI: {}
        
        1) PRIMA DOMANDA: [ {} ]
        
        1.2) PRIMA RISPOSTA: [ {} ]
        
        2) SECONDA DOMANDA: [ {} ]
        
        2.2) SECONDA RISPOSTA: [ {} ]
        
        3) TERZA DOMANDA: [ {} ]
        
        3.3) TERZA RISPOSTA: [ {} ]
        
        PA$$WORD GENERATA: [ {} ]
        
        +++ END +++""".format(self.instance_title, self.instance_description, str(self.instance_length), self.instance_excluded, self.question_one, self.answer_one, self.question_two, 
                                                                                  self.answer_two, self.question_three, self.answer_three, self.password)
        
        input(recap)
        
    def create_db(self):
        conn = sqlite3.connect('d@TaBA$E.db')
        c = conn.cursor()
        c.execute("CREATE TABLE instances(name text, description text, password_length text, excluded_characters text, first_question text, second_question text, third_question text)")
        conn.commit()
        conn.close()
    
    def insert_db(self):
        print("\nSalvataggio in corso...")
        if not path.exists("d@TaBA$E.db"):
            self.create_db()
        conn = sqlite3.connect('d@TaBA$E.db')
        c = conn.cursor()
        t = (self.instance_title, self.instance_description, str(self.instance_length), self.instance_excluded, self.question_one, self.question_two, self.question_three,)
        c.execute('INSERT INTO instances VALUES (?,?,?,?,?,?,?)', t)
        conn.commit()
        conn.close()
        print("\nSalvataggio effettuato.\n++++++++++++++++++++++++++++++++")
        
class Instance(New_Instance):
    def __init__(self):
        self.instances_dict = {}
        
    def database_names(self):
        #self.instances_dict = {}
        print("\nEnumerazione database...")
        if not path.exists("d@TaBA$E.db"):
            print("\nNessun database trovato nell'attuale directory.\n++++++++++++++++++++++++++++++++")
            return False
        else:
            conn = sqlite3.connect('d@TaBA$E.db')
            c = conn.cursor()
            c.execute("SELECT name,description FROM instances")
            returned = c.fetchall()
            if len(returned) != 0:
                print("\nISTANZE DISPONIBILI:")
                for index, name in enumerate(returned):
                    self.instances_dict[index + 1] = name[0]
                    print()
                    if name[1] != "":
                        print(str(index + 1) + ". " + name[0] + "\n\t" + name[1])
                    else:
                        print(str(index + 1) + ". " + name[0])
                return True
            else:
                print("\nNESSUNA ISTANZA DISPONIBILE.\n++++++++++++++++++++++++++++++++")
                return False
            
            conn.commit()
            conn.close()
            
    def retrieve(self, instance_number):
        print("\nEstrazione dal database...")
        self.instance_requested = self.instances_dict[int(instance_number)]
        if not path.exists("d@TaBA$E.db"):
            print("\nNessun database trovato nell'attuale directory.\n++++++++++++++++++++++++++++++++")
        else:
            conn = sqlite3.connect('d@TaBA$E.db')
            c = conn.cursor()
            t = (self.instance_requested,)
            c.execute('SELECT * FROM instances WHERE name=?', t)
            returned = c.fetchone()
            conn.commit()
            conn.close()
            
            presentation = """
            ISTANZA: [ {} ]
            
            DESCRIZIONE: [ {} ]
            
            LUNGHEZZA PA$$WORD: [ {} ]\n\n++++++++++++++++++++++++++++++++""".format(returned[0], returned[1], returned[2])
            print(presentation)
            
            return returned
    
    def delete_db(self, instance_number):
        print("\nEliminazione in corso...")
        self.instance_requested = self.instances_dict[int(instance_number)]
        if not path.exists("d@TaBA$E.db"):
            print("\nNessun database trovato nell'attuale directory.\n++++++++++++++++++++++++++++++++")
        else:
            conn = sqlite3.connect('d@TaBA$E.db')
            c = conn.cursor()
            t = (self.instance_requested,)
            c.execute('DELETE FROM instances WHERE name=?', t)
            conn.commit()
            conn.close()
            print("\nIstanza eliminata.\n++++++++++++++++++++++++++++++++")
            
# ++++