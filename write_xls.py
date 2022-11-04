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

def write_excel():
    # # рабочая часть файла
    data = eval(config['General']['for_summ'])
    print(data)
    work_smens  = tabels["4"]["отработанные смены"]
    print(work_smens)
    

def reason_block():
    reasons = tabels["447"]["Причина пропуска смен"]
    data_list = []
    all_list = []
    for key,value in reasons.items():
        data_list.append((key,value))
    # print(data_list)
    try:
        #задаем первую причину отсутсвия
        reason = data_list[0][1]
        #задаем с какой даты отсутствовал
        data_x = data_list[0][0]
        #задаем по какую дату отсутствовал(для наачала это один и тотже день)
        data_z = data_x
        # так выглядит список(первый день отсутсвиия, последний, причина)
        all_info = (data_x,data_z,reason)
        #номер в списке отсутствия
        item_number = 0
        # создаем список отсутсвия
        reason_list = [()]
        
        for item in data_list:
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
        print(reason_list)

        print("\n".join(f'{item[0]}-{item[1]} отсутствовал по причине {item[2]}' for item in reason_list))
    except IndexError:
        print("[INFO] - человек отработал весь месяц")


        

        
        


    
    
    


if __name__ == '__main__':
    # write_excel()
    reason_block()




