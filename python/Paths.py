from datetime import datetime


class Paths:
    res_folder = "res/"
    log_folder = res_folder + "Log/"
    data_folder = res_folder + "Data/"
    default_folder = res_folder + "default/"
    json_type = ".json"
    log_type = ".log"
    txt_type = ".txt"
    log_path = log_folder + str(datetime.now()) + log_type
    default_file_path = default_folder + "Default_File" + txt_type

