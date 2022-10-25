import json
import itertools

with open("data\\all_data.json", "r", encoding="utf-8") as file:
        all_data = json.load(file)

# for personal_number in dict(itertools.islice(all_data["шифр"]["87100"]["Табельный"].items(),1)):

# Пробегаемся по табельным

for personal_number in all_data["шифр"]["87100"]["Табельный"]:

    # каждому табельному создаем словарь
    personal_number_for_him_dict = {}

    # пробегаемся у этого табельного по пропущенным сменам
    for data in all_data["шифр"]["87100"]["Табельный"][personal_number]["Пропущенные смены"]:
        #Проверяем если в причине пропущеной смены цифра(значит, человек брал часы), пропускаем этот день
        if all_data["шифр"]["87100"]["Табельный"][personal_number]["Причина пропуска смен"][str(data)] in range(0,8):
            continue
        # проверяем совпадает ли день на замещение с выходным, пропускаем этот день
        if all_data["шифр"]["87100"]["Рабочий календарь"][str(data)]=="-":
            continue

        # создаем список людей которые могут замещать в пропущенную смену
        personal_number_for_him_in_data = []

        #пробегаем по всем табельным и проверяем кто не отсутствовал в указанную дату
        for item in all_data["шифр"]["87100"]["Табельный"]:
            # исключаем из списка табельный проверяемого
            if item == personal_number:
                continue
            # print(f'{item}---{all_data["шифр"]["87100"]["Табельный"][item]["Пропущенные смены"]}')
            if data not in all_data["шифр"]["87100"]["Табельный"][item]["Пропущенные смены"]:
                #добавлеям в список табельные которые могут замещать на конкретную дату
                personal_number_for_him_in_data.append(item)
            
            #заполняем словарь по датам
            personal_number_for_him_dict[data]=personal_number_for_him_in_data
    # добавляем словарь каждому табельному
    all_data["шифр"]["87100"]["Табельный"][personal_number]["Замещающие"]=personal_number_for_him_dict

with open("data\\all_data2.json", "w", encoding="utf-8") as file:
            json.dump(all_data,file, ensure_ascii=False, indent=4)
    

            
