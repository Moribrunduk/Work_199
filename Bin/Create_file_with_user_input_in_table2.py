import configparser
import json
import os


class CREATE_FILE():
    def __init__(self, profession_number):
        self.profession_number = profession_number
        super(CREATE_FILE, self).__init__()
        # self.Main()


    def Main(self):
        self.LoadPathInformation()
        self.MAIN_FINCTION()


    def LoadPathInformation(self):
        # открываем файл в котором записаны значения которые вводил пользователь
        if os.path.isfile('temp.ini'):
            self.TEMP = configparser.ConfigParser()
            self.TEMP.read('temp.ini')
        else:
            config = configparser.ConfigParser()
            config.add_section("General")
            config["General"]["input_user"] = '"{(, ): ('', (, , ))}"'
            config["General"]["for_summ"] = '"{(0, 0): 0}"'
            # config.set("General", "input_user", "'{('',''): ('',('','',''))}'")
            # config.set("General", "for_summ", "'{('',''): ''}'")
            with open('temp.ini', "w") as config_file:
                config.write(config_file)

        # открываем фал и берем оттуда путь с которым сейчас работает пользователь
        self.SETINGS  = configparser.ConfigParser()
        self.SETINGS.read('data\\SETTINGS.ini', encoding="utf-8")
        self.SETINGS_current_path = self.SETINGS['Settings'][f'current_directory_{self.profession_number}']
        # файл для записи
        self.substitutes = configparser.ConfigParser()
        self.substitutes.read('datalist of substitutes')

        with open(f'{self.SETINGS_current_path}', "r", encoding="utf-8") as file:
            self.all_data = json.load(file)

        self.tabels = self.all_data["шифр"][str(self.profession_number)]["Табельный"]
        

    def ReasonBlock(self,tabel_for_function):
        # проверяем если нет смен отсутствия, сразу создаем список на выход
        if self.tabels[tabel_for_function]["Пропущенные смены"] == []:
            reason_list_x = []
            
        else:
            reasons = self.tabels[tabel_for_function]["отработанные смены"]
            print(tabel_for_function)
            print(reasons)
            # удаляем 15 элемент из списка(специфика из таблицы, т.к 15 элемент это элемент между 15 числом календаря и 16)
            reasons.pop(15)
            data_list = []
            all_info =()
            for day,reason in enumerate(reasons,1):
                data_list.append((day,reason))
            try:
                for tabel_number in range(0,len(data_list)):
                    if data_list[tabel_number][1] ==7 :
                        print(f"{tabel_number+1}----{data_list[tabel_number][1]}")
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
                        print(reason)
                        #задаем с какой даты отсутствовал
                        data_x = data_list[tabel_number][0]
                        print(data_x)
                        #задаем по какую дату отсутствовал(для наачала это один и тотже день)
                        data_z = data_x
                        print(f"{tabel_number+1}----({data_list[tabel_number][1]})")
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
                            reason_list_x.append((item))
            except IndexError:
                print("[INFO] - человек отработал весь месяц")
        print(reason_list_x)
        return reason_list_x

    def UserRework(self,tabel_for_function):
        """
        функция которая возвращает список (день начала замещения, последний день замещения, табельный замещающего)

        """
        list_of_user_input = self.TEMP['General']['for_summ']
        list_of_user_input = eval(eval(list_of_user_input))
        # print (list_of_user_input)

        # задаем начальный день, когда первый раз идет замещение
        data_x = list(list_of_user_input.keys())[0][1]
        # Приравниваем конечный день, к начальному, чтобы изменять в дальнейшем
        data_z = data_x
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

    def WriteInFile(self,tabel_for_function):
        #список содержаший (первый день отсутсвия, последнйи,причина отсутствия)
        reasons = self.ReasonBlock(tabel_for_function)
        print(reasons)
        #список содержащий(первй день замещения, последний день замещения, табельный замещающего)
        rework = self.UserRework(tabel_for_function)
        print(rework)
        if reasons ==[]:
            final_list=[]
        elif rework ==[]:
            final_list = []
        else:
            # создаем список, для печать в таблицу
            final_list = []
            # создаем переменную, количество значений в списке для печати
            count = 0
            reason_count = 0
            for reason in reasons:
                count+=reason_count
                final_list.append("")
                print(reason)
                #обьявляем начальный день
                Day_x = reason[0]
                #обьявляем конечный день
                Day_z = int(Day_x)
                #обьявляем первый табельный
                tabel_number = int(rework[0][2])
                # пробегаемся по элементам списка пропущенных смен
                for item in rework:
                    # проверяем изменился ли табельный
                    if tabel_number == int(item[2]):
                        # проверяем входят ли дни когда этот табельный замещает, в причину замещения
                        if int(reason[0])<=int(item[0])<=int(item[1])<=int(reason[1]):
                            # изменяем крайний день замещения
                            Day_z = int(item[1])
                            # заменяем этот элемент в списке на печать
                            final_list[count]=(tabel_for_function,reason[2],Day_x,Day_z,tabel_number)
                            print(final_list)
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
                reason_count+=1
            # удаляем из списка пустой элемент("откуда взялся хз")  
            while "" in final_list:              
                final_list.remove((""))
        print(final_list)
        

        self.substitutes['DEFAULT'][f'{self.profession_number},{tabel_for_function}'] = str(final_list)
        with open(f'{self.SETINGS_current_path.split(".")[0]}.ini', 'w', encoding="utf-8") as configfile: 
            self.substitutes.write(configfile)   


        
    # def MAIN_FINCTION(self):

    #     for tabel in self.tabels:
    #         try:
    #             self.WriteInFile(tabel_for_function=str(tabel))
    #         except:
    #             print(f"ошибка в блоке 3[write in file]----{tabel}")  

    def MAIN_FINCTION(self):

        for tabel in self.tabels:
                self.WriteInFile(tabel_for_function=str(tabel))
            

                
if __name__ == '__main__':
        CF = CREATE_FILE(87100)
        CF.Main()
