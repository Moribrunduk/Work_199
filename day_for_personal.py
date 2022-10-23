import json
import itertools

with open("data\\all_data.json", "r", encoding="utf-8") as file:
        all_data = json.load(file)

for personal_number in dict(itertools.islice(all_data["шифр"]["87100"]["Табельный"].items(),1)):
    personal_number_for_him_dict = {}
    print(personal_number)
    for data in all_data["шифр"]["87100"]["Табельный"][personal_number]["Пропущенные смены"][0:3]:
        print(data)
        personal_number_for_him_in_data = []
        for item in all_data["шифр"]["87100"]["Табельный"]:
            if item == personal_number:
                continue
            print(f'{item}---{all_data["шифр"]["87100"]["Табельный"][item]["Пропущенные смены"]}')
            if data not in all_data["шифр"]["87100"]["Табельный"][item]["Пропущенные смены"]:
                personal_number_for_him_in_data.append(item)
        print(personal_number_for_him_in_data)
    personal_number_for_him_dict[data]=personal_number_for_him_in_data
print(personal_number_for_him_dict)
    

            
