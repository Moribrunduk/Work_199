import configparser
# from ctypes import alignment
import json

config = configparser.ConfigParser()
config.read('temp.ini')
# print(config['General']['for_summ'])     # -> "/path/name/"

profession_code = 87100

# config['DEFAULT']['path'] = '/var/shared/'    # update
# config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create
# with open('FILE.INI', 'w') as configfile:    # save
#     config.write(configfile)

# Напишитеexcel
with open("data\\all_data2.json", "r", encoding="utf-8") as file:
        all_data = json.load(file)

# разработано для работы по одному шифру

tabels = all_data["шифр"]["87100"]["Табельный"]

def reason_block():
    reasons = tabels["406"]["отработанные смены"]
    # удаляем 15 элемент из списка(специфика из таблицы, т.к 15 элемент это элемент между 15 числом календаря и 16)
    reasons.pop(15)
    data_list = []
    all_list = []
    for day,reason in enumerate(reasons,1):
        data_list.append((day,reason))
    try:
        for number in range(0,len(data_list)):
            if data_list[number][1] in range(0,25):
                # print(f"{number+1}----{data_list[number][1]}")
                continue
            elif data_list[number][1] == "":
                # print(f"{number+1}----({data_list[number][1]})")
                continue
            elif data_list[number][1] == "-":
                # print(f"{number+1}----({data_list[number][1]})")
                continue
            else:
                #задаем первую причину отсутсвия
                reason = data_list[number][1]
                #задаем с какой даты отсутствовал
                data_x = data_list[number][0]
                #задаем по какую дату отсутствовал(для наачала это один и тотже день)
                data_z = data_x
                # print(f"{number+1}----({data_list[number][1]})")
                break
        # print((data_x,data_z,reason))
        # так выглядит список(первый день отсутсвиия, последний, причина)
        all_info = (data_x,data_z,reason)
        #номер в списке отсутствия
        item_number = 0
        # создаем список отсутсвия
        reason_list = [()]
        
        for item in data_list[data_x:]:
            #если предыдущая причина отсутсвия совпадает с нынешней
            if item[1] == reason:
                # заменяем последнюю дату отсутствия
                data_z = item[0]
                # заполняем список по новому заменяя только дату отсутсвия
                all_info = (data_x,data_z,reason)
                # Заменяем этим списком элемент под номером ITEM_NUMBER в списке отсутствия
                reason_list[item_number]=all_info
            elif item[1] != reason:
                #Если причина отстутсвия поменялась
                #добавляем в список отсутсвия старый словарь
                reason_list.append("")
                reason_list[item_number]=all_info
                # меняем все значения
                item_number+=1
                data_x = item[0]
                data_z = data_x
                reason = item[1]
                all_info = (data_x,data_z,reason)
                # print(all_info)
        
        # если в списке оказывается ""(такое случается если причина отсутсвия одна или их нет)
        if "" in reason_list:
            reason_list.remove("")
        
        # т.к в резудьтате предыдущей итерации в список попадают числа и "" и "-"
        # очищаем от них список
        
        reason_list_x = []
        for item in reason_list:
                if item[2] in range(0,25):
                    continue
                elif item[2] == "":
                    continue
                elif item[2] == "-":
                    continue
                else:
                    if item[0]<16:
                        reason_list_x.append((item))
                    else:
                        reason_list

        print("\n".join(f'{item[0]}-{item[1]} отсутствовал по причине {item[2]}' for item in reason_list_x))
    except IndexError:
         print("[INFO] - человек отработал весь месяц")

if __name__ == '__main__':
    # reason_block_reason()
    reason_block()




