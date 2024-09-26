



import random
import pandas as pd
from datetime import datetime, timedelta
import time
from faker import Faker

fake = Faker('ru_RU')

iso_format = "{Year}-{Month}-{Day}T{Hour}:{Minute}+{Offset}"

year_range = ["2020", "2021", "2022", "2023"]
month_range = ["01","02","03","04","05","06","07","08","09","10","11","12"]
day_range = [str(i).zfill(2) for i in range(1,29)]
hour_range = [str(i).zfill(2) for i in range(8,21)]
min_range = [str(i).zfill(2) for i in range(0,60)]
offset = ["03:00"]

def gen_snils():
    snils = str(random.randint(100, 999)) + '-' + str(random.randint(100, 999)) + '-' + str(random.randint(100, 999)) + ' ' + str(random.randint(10, 99))
    return snils

def gen_passport(country):
    if country == 0:
        passport = 'Ru' + ' ' + str(random.randint(10, 99)) + ' ' + str(random.randint(10, 99)) + ' ' + str(random.randint(100000, 999999))
    elif country == 1:
        passport = "Kz" + ' ' + str(random.randint(0, 9)) + ' ' + str(random.randint(0, 9)) + ' ' + str(random.randint(100000000, 999999999))
    else:
        passport = "Bel" + ' ' + str(random.randint(10, 99)) + ' ' + str(random.randint(100, 999)) + ' ' + str(random.randint(10000, 99999))
    return passport

def gen_name(gender):
    if gender == 'male':
        return fake.name_male()
    else:
        return fake.name_female()

def gen_time():
    argz = {"Year": random.choice(year_range),
            "Month": random.choice(month_range),
            "Day" : random.choice(day_range),
            "Hour": random.choice(hour_range),
            "Minute": random.choice(min_range),
            "Offset": random.choice(offset)
            }
    return iso_format.format(**argz)

def gen_payment_system(payment_system, bank):
    if payment_system == 0:
        system_bank = "Mastercard"
        if bank == 0:
            number_card = "4222" + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999))  # SBER
        elif bank == 1:
            number_card = "2322" + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999))  # VTP
        elif bank == 2:
            number_card = "2232" + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999))  # T-Bank
        else:
            number_card = "2222" + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999))  # Alpha
    elif payment_system == 1:
        system_bank = "Mir"
        if bank == 0:
            number_card = "1114" + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999))  # SBER
        elif bank == 1:
            number_card = "1113" + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999))  # VTP
        elif bank == 2:
            number_card = "1112" + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999))  # T-Bank



        else:
            number_card = "1111" + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999))  # Alpha
    else:
        system_bank = "Visa"
        if bank == 0:
            number_card = "3333" + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999))  # SBER
        elif bank == 1:
            number_card = "3232" + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999))  # VTP
        elif bank == 2:
            number_card = "2323" + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999))  # T-Bank
        else:
            number_card = "3223" + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999)) + ' ' + str(random.randint(1000, 9999))  # Alpha
    return f"{system_bank} {number_card}"

def gen_dataset(Mastercard, Visa, Mir, SBER, TBank, Vtb, Alpha, size):
    df = pd.DataFrame({'ФИО':[], 'Паспортные данные':[], 'СНИЛС':[], 'Симптомы':[], 'Выбор врача':[], 
                       'Дата посещения врача':[], 'Анализы':[], 'Дата получения анализов':[], 
                       'Стоимость анализов':[], 'Карта оплаты':[]})
    used_snils = []
    used_passports = []
    gender = random.choice(['male', 'female'])
    for i in range(size):
        bank = random.choices(['Сбербанк', 'Тинькофф', 'ВТБ', 'Альфа'], weights = [SBER, TBank, Vtb, Alpha])[0]
        pay_system = random.choices(['Мир', 'MasterCard', 'Visa'], weights = [Mir, Mastercard, Visa])[0]
        analyze_cost = random.randint(5000, 20000)
        snils = gen_snils()
        passport = gen_passport(random.randint(0,2))
        
        used_symp =[]
        used_ans =[]

        while snils in used_snils:
            snils = gen_snils()
        used_snils.append(snils)
        
        while passport in used_passports:
            passport = gen_passport(random.randint(0,2))
        used_passports.append(passport)
        
    
        num_1 = random.randint(0, len(analyzes) - 1)
        num_2 = random.randint(0,len(symptoms)-1)
        num_3 = random.randint(0,len(doctors)-1)
        symps = str(symptoms[num_2])
        ans = str(analyzes[num_1])
        num_symp =[]
        num_ans =[]

        for j in range(random.randint(0, 49)):
            n_symptoms = random.randint(0, len(symptoms) - 1)
            symps += ", " + str(symptoms[n_symptoms]) 
            num_symp.append(n_symptoms)
            n_analyzes = random.randint(0, len(analyzes) - 1)
            ans += ", " + str(analyzes[n_analyzes])
            num_ans.append(n_analyzes)
        time = gen_time() 

        time_new = (datetime.fromisoformat(time) + timedelta(hours=random.choices([24,48,72])[0])).isoformat()

        df.loc[len(df.index)] = [gen_name(gender), passport, snils, symps, doctors[num_3].replace("n",""),
                                   time, ans, time_new, analyze_cost, gen_payment_system(pay_system, bank)]

    df.to_excel('out.xlsx', index=False)
with open("doctors.txt") as file:
    doctors = [row.strip() for row in file]
with open("analyzes.txt") as file:
    analyzes = [row.strip() for row in file]
with open("symptoms.txt") as file:
    symptoms = [row.strip() for row in file]
gen_dataset(Mastercard=0.2, Visa=0.3, Mir=0.5, SBER=0.4, TBank=0.2, Vtb=0.3, Alpha=0.1, size=100)
