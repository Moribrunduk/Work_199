import configparser

# from ctypes import alignment
import json

profession_code = 87100


config = configparser.ConfigParser()
config.read('temp.ini')
# config['DEFAULT']['path'] = '/var/shared/'    # update
    # config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create
    # with open('FILE.INI', 'w') as configfile:    # save
    # config.write(configfile)

# Напишитеexcel
with open("data\\all_data2.json", "r", encoding="utf-8") as file:
        all_data = json.load(file)

# разработано для работы по одному шифру

tabels = all_data["шифр"]["87100"]["Табельный"]

def reason_block(tabel_for_function):
    # проверяем если нет смен отсутствия, сразу создаем список на выход
    if tabels[tabel_for_function]["Пропущенные смены"] == []:
        reason_list_x = []
    else:
        reasons = tabels[tabel_for_function]["отработанные смены"]
        # удаляем 15 элемент из списка(специфика из таблицы, т.к 15 элемент это элемент между 15 числом календаря и 16)
        reasons.pop(15)
        data_list = []
        for day,reason in enumerate(reasons,1):
            data_list.append((day,reason))
        try:
            for tabel_number in range(0,len(data_list)):
                if data_list[tabel_number][1] in range(0,25):
                    # print(f"{tabel_number+1}----{data_list[tabel_number][1]}")
                    continue
                elif data_list[tabel_number][1] == "":
                    # print(f"{tabel_number+1}----({data_list[tabel_number][1]})")
                    continue
                elif data_list[tabel_number][1] == "-":
                    # print(f"{tabel_number+1}----({data_list[tabel_number][1]})")
                    continue
                else:
                    #задаем первую причину отсутсвия
                    reason = data_list[tabel_number][1]
                    #задаем с какой даты отсутствовал
                    data_x = data_list[tabel_number][0]
                    #задаем по какую дату отсутствовал(для наачала это один и тотже день)
                    data_z = data_x
                    # print(f"{tabel_number+1}----({data_list[tabel_number][1]})")
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

def user_rework(tabel_for_function):
    """
    функция которая возвращает список (день начала замещения, последний день замещения, табельный замещающего)

    """
    list_of_user_input = config['General']['for_summ']
    list_of_user_input = eval(eval(list_of_user_input))
    # print (list_of_user_input)

    # задаем начальный день, когда первый раз идет замещение
    data_x = list(list_of_user_input.keys())[0][1]
    # Приравниваем конечный день, к начальному, чтобы изменять в дальнейшем
    data_z = data_x
    
    # personal = list(list_of_user_input.values())[0]
    # print(list(list_of_user_input.keys()))
    # print(personal)
    # создаем лист замещения
    remoove_day_list = [()]
    item_namber = 0
    # print(data_x)
    personal_number = tabel_for_function
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


    # первый заамещающий, чтобы потом изменять
    personal = list(list_of_user_input_selected_number.items())[0][1]

    # Пробегаемся по этому словарю, чтобы вычислить периоды замещения
    for key,value in list_of_user_input_selected_number.items():
            
            # if key[0] == personal_number:
            #     print(f' {key[1]}-----{value}')
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
    return remoove_day_list

def write_in_file(tabel_for_function):
    #список содержаший (первый день отсутсвия, последнйи,причина отсутствия)
    reasons = reason_block(tabel_for_function)
    print(reasons)
    #список содержащий(первй день замещения, последний день замещения, табельный замещающего)
    rework = user_rework(tabel_for_function)
    print(rework)
    if reasons ==[]:
        final_list=[]
    elif rework ==[]:
        final_list = []
    else:
        # создаем список, для печать в таблицу
        final_list = [()]
        # создаем переменную, количество значений в списке для печати
        count = 0
        for reason in reasons:
            #обьявляем начальный день
            Day_x = reason[0]
            #обьявляем конечный день
            Day_z = int(Day_x)
            #обьявляем первый табельный
            tabel_number = int(rework[0][2])

            # пробегаемся по элементам списка пропущенных смен
            for item in rework:
                # проверяем изменился ли табельный
                if tabel_number == item[2]:
                    # проверяем входят ли дни когда этот табельный замещает, в причину замещения
                    if int(reason[0])<=int(item[0])<=int(item[1])<=int(reason[1]):
                        # изменяем крайний день замещения
                        Day_z = int(item[1])
                        # заменяем этот элемент в списке на печать
                        final_list[count]=(tabel_for_function,reason[2],Day_x,Day_z,tabel_number)
                # если табельный поменялся
                else:
                    if int(reason[0])<=int(item[0])<=int(item[1])<=int(reason[1]):
                        # print(f"{item} входит в {reason}")
                        # увеличивем количество элементов в списке
                        count+=1
                        # меняем первый день замещения
                        Day_x = int(item[0])
                        # меняем второй день замещегия
                        Day_z = int(item[1])
                        # меняем табельный
                        tabel_number = int(item[2])
                        # добавляем в список пустое значение
                        final_list.append((""))
                        # заполняем это значение списком
                        final_list[count] = (tabel_for_function,reason[2],Day_x,Day_z,tabel_number)
        # удаляем из списка пустой элемент("откуда взялся хз")                
        final_list.remove(())
    print(final_list)
    substitutes= configparser.ConfigParser()
    substitutes.read("list of substitutes.ini")
    substitutes.set('DEFAULT',f'{tabel_for_function}',str(final_list))
    with open('data\datalist of substitutes.ini', 'a', encoding="utf-8") as configfile: 
        substitutes.write(configfile)   


def test():
    # # 438,447,448,453,464,473,479,480,487,491,503,509,513,516,517,530,531,535,544,548,563,566,601,602,608
    # tabel = "438"
    for tabel in tabels:
    # tabel = 448
        try:
            reason_block(tabel_for_function=str(tabel))
        except:
            print(f"ошибка в блоке 1[reason_block]----{tabel}")
            
        try:
            user_rework(tabel_for_function=str(tabel))
        except:
            print(f"ошибка в блоке 2[user rework]----{tabel}")
        try:
            write_in_file(tabel_for_function=str(tabel))
        except:
            print(f"ошибка в блоке 3[write in file]----{tabel}")
def MAIN_FINCTION():
    # for tabel in tabels:
        # reason_block(tabel_for_function="406")
        # user_rework(tabel_for_function="406")
        # write_in_file(tabel_for_function="406")
    pass     
            
if __name__ == '__main__':
    # MAIN_FINCTION()
    test()




