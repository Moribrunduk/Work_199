import configparser

# from ctypes import alignment
import json

profession_code = 87100



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

        # print("\n".join(f'{item[0]}-{item[1]} отсутствовал по причине {item[2]}' for item in reason_list_x))
    except IndexError:
         print("[INFO] - человек отработал весь месяц")
    return reason_list_x

def user_rework():
    # config['DEFAULT']['path'] = '/var/shared/'    # update
    # config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create
    # with open('FILE.INI', 'w') as configfile:    # save
    # config.write(configfile)

    config = configparser.ConfigParser()
    config.read('temp.ini')
    # print(config['General']['for_summ'])    # -> "/path/name/"
    list_of_user_input = config['General']['for_summ']
    list_of_user_input = eval(eval(list_of_user_input))
    # print (list_of_user_input)

    # задаем начальный день, когда первый раз идет замещение
    data_x = list(list_of_user_input.keys())[0][1]
    # Приравниваем конечный день, к начальному, чтобы изменять в дальнейшем
    data_z = data_x
    # первый заамещающий, чтобы потом изменять
    personal = list(list_of_user_input.values())[0]
    # создаем лист замещения
    remoove_day_list = [()]
    item_namber = 0
    # print(data_x)
    personal_number = '406'
    #создаем словарь для того чтобы добавить в него "-" в дни, когда небыло замещений(новый, чтобы попорядку)
    list_of_user_input_selected_number = {}
    # создаем цикл в который добавляем дни где небыло замещения
    for day in range(1,32):
        # если ключа (табельный, день) нет в словаре
        if (personal_number,str(day)) not in list_of_user_input:
            # добавляем такой ключ со значением "-"
            list_of_user_input_selected_number[personal_number,str(day)] = "-"
        else:
            # если такой ключ есть добавляем его в новый словарь
            list_of_user_input_selected_number[personal_number,str(day)] = list_of_user_input[personal_number,str(day)]

    # Пробегаемся по этому словарю, чтобы вычислить периоды замещения
    for key,value in list_of_user_input_selected_number.items():
           
            # if key[0] == personal_number:
                # print(f' {key[1]}-----{value}')
            # если значение ключа равно предыдущему значению(значение personal первое выбрано в самом начале)
            if value == personal:
                # то меняем дату окончания замещения
                data_z = key[1]
                # перезаписываем пару(ключ)=значение
                remoove_day_list[item_namber] = (data_x,data_z,value)
    
            if value != personal:
                # если в итерации поменялся табельный замещающего
                # перезаписываем этот табельный
                personal = value
                # устанавливаем первый день замещения
                data_x = key[1]
                # устанавливаем последний день замещения
                data_z = key[1]
                # прибавляем к количеству элементов номер 1
                item_namber+=1
                # добавляем в лист новый элемент
                remoove_day_list.append("")
                # заполняем этот элемент
                remoove_day_list[item_namber] = (data_x,data_z,value)
    
    for item in remoove_day_list:
        if item[2] == "-":
            remoove_day_list.remove(item)

    # print(remoove_day_list)
    return remoove_day_list

def main():
    reasons = reason_block()
    rework = user_rework()

    print(reasons)
    print(rework)
    final_list = [()]
    count = 0
    for reason in reasons:
        #обьявляем начальный день
        item_x = reason[0]
        #обьявляем конечный день
        item_z = item_x
        #обьявляем первый табельный
        number = rework[0][2]

        for item in rework:
            if number == item[2]:
                if int(reason[0])<=int(item[0])<=int(item[1])<=int(reason[1]):
                    # print(f"{item} входит в {reason}")
                    item_z = item[1]
                    
            else:
                final_list[count] = ("406",item_x,item_z,number)
                number = item[2]
                item_x = item[0]
                item_z = item_x
                final_list.append((""))
                count =+1
                final_list[count] = ("406",item_x,item_z,number)
                if int(reason[0])<=int(item[0])<=int(item[1])<=int(reason[1]):
                    # print(f"{item} входит в {reason}")
                    item_z = item[1]
                    
            print(f"[info] - {item_x,item_z}")
    print(final_list)
                
                
            
            

    

if __name__ == '__main__':
    # reason_block()
    # user_rework()
    main()




