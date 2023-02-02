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
        
        
        # открываем фал и берем оттуда путь с которым сейчас работает пользователь
        self.SETINGS  = configparser.ConfigParser()
        self.SETINGS.read('data\\SETTINGS.ini', encoding="utf-8")
        self.SETINGS_current_path = self.SETINGS['Settings'][f'current_directory_{self.profession_number}']
        self.SETINGS_JSON_PATH = self.SETINGS["Settings"][f"current_directory_{self.profession_number}"]
       

        # открываем файл в котором записаны значения которые вводил пользователь
        self.SETINGS_current_path_user_input = self.SETINGS['Settings'][f'path_with_input_{self.profession_number}']
        
        if not os.path.isfile(f'{self.SETINGS_current_path_user_input}'):
            config = configparser.ConfigParser()
            config.add_section("General")
            config.add_section("For_summ")
            config["General"]["input_user"] = '"{(, ): ('', (, , ))}"'
            config["General"]["for_summ"] = '"{(0, 0): 0}"'
            
            with open(self.SETINGS_current_path_user_input, "w") as config_file:
                config.write(config_file)

            
        else:
            self.TEMP = configparser.ConfigParser()
            self.TEMP.read(f'{self.SETINGS_current_path_user_input}')
            
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
            self.missed_working_days = list(self.tabels[tabel_for_function]["Причина пропуска смен"].keys())
            self.reasons = list(self.tabels[tabel_for_function]["Причина пропуска смен"].values())
            # убираем лишнее из причины отсутствия()
            self.new_missed_working_days = []
            self.new_reasons = []
            # задае общее число эдементов с отсчетом с 0
            count = 0
            for i,item in enumerate(self.reasons):
                if str(item) in self.SETINGS["Days"]["days_keys"]:
                    self.new_reasons.append(item)
                elif str(item)[1:3] in ("МН","мн","МВ","мв","МД","мд","м","М"):
                    self.new_reasons.append("ИО")
                elif int(str(item)[0]) not in range(0,8):
                    self.new_reasons.append(int(str(item)[0]))  
                else:
                    self.missed_working_days.pop(count+i)
                    count-=1
                   
            self.reasons = self.new_reasons
            

############################################
            

            if self.reasons == []:
                reason_list_x = []
                return reason_list_x
            else:
                # print(self.reasons)
                ferst_day = self.missed_working_days[0]
                last_day = ferst_day
                count = 0
                reason_list_x = [()]
                main_reason = self.reasons[0]
                for i,reason in enumerate(self.reasons):
                    try:
                        if main_reason == reason:
                                last_day = self.missed_working_days[i]
                                reason_list_x[count]=(ferst_day,last_day,reason)

                        else:
                            ferst_day = self.missed_working_days[i]
                            last_day = ferst_day
                            reason_list_x.append("")
                            main_reason=reason
                            count+=1
                            reason_list_x[count]=(ferst_day,last_day,reason)
                    except: Exception
                
            print(reason_list_x)
            print(self.missed_working_days)
            not_missed_days = []
            try:
                for days in range(1,int(self.missed_working_days[-1])+1):
                        if str(days) not in self.missed_working_days:
                            not_missed_days.append(days)
                print(not_missed_days)
                

                if not_missed_days == []:
                    return reason_list_x
                else:
                    print("kjhjh")
                
                count = len(reason_list_x)
                new_reason_list_x = [()]
                new_count=0
                for i,reason in enumerate(reason_list_x):
                    for days in not_missed_days:
                        if int(days) in range(int(reason[0]),int(reason[1])+1):
                            new_reason_list_x[new_count]=(int(reason[0]),days,reason[2])
                            # new_reason.append(int(reason[0],days,reason[2]))
                            new_reason_list_x.append("")
                            new_count+=1
                            # print(new_reason_list_x)
                            break
                        else:
                            new_reason_list_x[new_count] = reason
                    new_count+=1
                    new_reason_list_x.append("")

                    for days in not_missed_days:
                        if int(days) in range(int(reason[0]),int(reason[1])+1):
                            new_reason_list_x[new_count]=(days+1,int(reason[1]),reason[2])
            
                while "" in new_reason_list_x:
                    new_reason_list_x.remove("")
                print(new_reason_list_x)
            except: IndexError
            
            return new_reason_list_x
                
    def UserRework(self,tabel_for_function):
        """
        функция которая возвращает список (день начала замещения, последний день замещения, табельный замещающего)

        """
        full_list_of_user_input = self.TEMP['General']['for_summ']
        # словарь представлен как {(табельный,число,количество часов,день): замещающий табельный}
        full_list_of_user_input = eval(full_list_of_user_input)
        

        # преобразуем в словарь
        # {(табельный,число): замещающий табельный}
        list_of_user_input = {}
        for key, value in full_list_of_user_input.items():
            list_of_user_input[key[0:2]]=value

        # задаем начальный день, когда первый раз идет замещение
        data_x = int(list(list_of_user_input.keys())[0][1])
        # print(data_x)
        
        
        # Приравниваем конечный день, к начальному, чтобы изменять в дальнейшем
        data_z = int(data_x)
        # print(data_z)
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
                # print((personal_number,str(day)))
                # print(list_of_user_input)
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
        # print(reasons)
        #список содержащий(первй день замещения, последний день замещения, табельный замещающего)
        rework = self.UserRework(tabel_for_function)
        print(rework)
        # print(rework)
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
                            print(f"[INFO]{item} входит в {reason}")
                            # изменяем крайний день замещения
                            Day_x = int(item[0])
                            Day_z = int(item[1])
                            # заменяем этот элемент в списке на печать
                            print(tabel_for_function,reason[2],Day_x,Day_z,tabel_number)
                            
                            print(count)
                            final_list[count]=(tabel_for_function,reason[2],Day_x,Day_z,tabel_number)
                            print(final_list)
                    # если табельный поменялся
                    else:
                        if int(reason[0])<=int(item[0])<=int(item[1])<=int(reason[1]):
                            print(f"{item} входит в {reason}")
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
                final_list.append("")
            # удаляем из списка пустой элемент("откуда взялся хз")  
        while "" in final_list:              
            final_list.remove((""))
        print(final_list)
        

        self.substitutes['DEFAULT'][f'{self.profession_number},{tabel_for_function}'] = str(final_list)
        with open(f'{self.SETINGS_current_path.split(".")[0]}.ini', 'w', encoding="utf-8") as configfile: 
            self.substitutes.write(configfile)   

    def MAIN_FINCTION(self):

        for tabel in self.tabels:
                self.WriteInFile(tabel_for_function=str(tabel))
                self.ReasonBlock(tabel_for_function=str(tabel))
        # tabel =  818
        # # self.ReasonBlock(tabel_for_function=str(tabel))
        # # self.UserRework(tabel_for_function=str(tabel))
        # self.WriteInFile(tabel_for_function=str(tabel))
                
if __name__ == '__main__':
        CF = CREATE_FILE("87200")
        CF.Main()
