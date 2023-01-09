import configparser
import os

class CREATE_SETTINGS_DEFAULT():
    def main(self):
        if os.path.exists("data") == False:
            os.mkdir("data")
        if os.path.exists("data\\SETTINGS.ini") == False:
            self.create_file_SETTINGS()

    def create_file_SETTINGS(self):
        
        settings = configparser.ConfigParser()
        settings["Settings"] = {}
        settings["Settings"]["Path_87100"] = ""
        settings["Settings"]["current_directory_87100"] = ""
        settings["Settings"]["Path_87200"] = ""
        settings["Settings"]["current_directory_87200"] = ""
        settings["Settings"]["Path_08300"] = ""
        settings["Settings"]["current_directory_08300"] = ""
        settings["87100"] = {"cv_three_tarif":1,
                                "cv_four_tarif":0,
                                "cv_five_tarif":0,
                                "cv_six_tarif":0,
                                "procent_text":0}
        settings["87200"] = {"cv_three_tarif":0,
                                "cv_four_tarif":0,
                                "cv_five_tarif":0,
                                "cv_six_tarif":0,
                                "procent_text":0}
        settings["08300"] = {"cv_three_tarif":0,
                                "cv_four_tarif":0,
                                "cv_five_tarif":0,
                                "cv_six_tarif":0,
                                "procent_text":0}
        settings["Days"] = {}                        
        settings["Days"]["days_keys"]=str(['"ИО" - ', '"О" - ', '"Э" - ', '"Р" - ', '"А" - ', '"Ж" - ', '"Д" - ', '"М" - ', '"Б" - ', '"К" - '])
        settings["Days"]["days_values"]=str(['И.о.мастера', 'Отпуск очередной', 'Отпуск учебный', 'Отпуск по беремености', 'Отпуск за свой счет', 'Пенсионный день/уход за детьми', 'Донорский день', 'Медкомиссия', 'Больничный', 'Командировка'])

        with open("data\SETTINGS.ini", "w", encoding="utf-8") as configfile:
            settings.write(configfile)


if __name__ == "__main__":
    CS = CREATE_SETTINGS_DEFAULT()
    CS.main()

