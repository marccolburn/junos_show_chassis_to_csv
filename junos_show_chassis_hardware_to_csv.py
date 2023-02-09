#!/usr/bin/env python
import json
import csv
import os


def output_to_json(json_raw_data):
    """Function to read show chassis output and return json in python usable objects"""
    json_data = json.loads(json_raw_data)
    return json_data

def dump_json_to_csv(json_data):
    """Take JSON data and dump part descriptions with serial number in a csv"""
    chassis_modules = json_data["chassis-inventory"][0]["chassis"][0]["chassis-module"]
    with open('hardware_parts.csv', mode='a') as hardware_file:
        hardware_writer = csv.writer(hardware_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        hardware_writer.writerow(
            [
                json_data["chassis-inventory"][0]["chassis"][0]["name"][0]["data"], 
                json_data["chassis-inventory"][0]["chassis"][0]["description"][0]["data"], 
                json_data["chassis-inventory"][0]["chassis"][0]["serial-number"][0]["data"]
            ]
        )
        for module in chassis_modules:
            if 'serial-number' in module:
                hardware_writer.writerow(
                    [
                        module['name'][0]['data'],
                        module['description'][0]['data'],
                        module['serial-number'][0]['data']
                    ]
                )
            if 'chassis-sub-module' in module:
                for sub_module in module['chassis-sub-module']:
                    if 'serial-number' in sub_module and 'description' in sub_module:
                        hardware_writer.writerow(
                            [
                                sub_module['name'][0]['data'],
                                sub_module['description'][0]['data'],
                                sub_module['serial-number'][0]['data']
                            ]
                        )
                    elif 'serial-number' in sub_module:
                        hardware_writer.writerow(
                            [
                                sub_module['name'][0]['data'],
                                "No Description",
                                sub_module['serial-number'][0]['data']
                            ]
                        )
                    if 'chassis-sub-sub-module' in sub_module:
                        for sub_sub_module in sub_module['chassis-sub-sub-module']:
                            if 'serial-number' in sub_sub_module and 'description' in sub_sub_module:
                                hardware_writer.writerow(
                                    [
                                        sub_sub_module['name'][0]['data'],
                                        sub_sub_module['description'][0]['data'],
                                        sub_sub_module['serial-number'][0]['data']
                                    ]
                                )
                            elif 'serial-number' in sub_sub_module:
                                hardware_writer.writerow(
                                    [
                                        sub_sub_module['name'][0]['data'],
                                        "No Description",
                                        sub_sub_module['serial-number'][0]['data']
                                    ]
                                )
                        
        


if __name__ == "__main__":
    list_of_raw_files = []
    source_dir = "./chassis_hardware_outputs/"
    for file in os.listdir(source_dir):
        if file.endswith(".json"):
            list_of_raw_files.append(file)
    for file in list_of_raw_files:
        full_file_path = "{0}/{1}".format(source_dir,file)
        with open(full_file_path, "r") as data_file:
            read_data = data_file.read()
            json_data = output_to_json(read_data)
        dump_json_to_csv(json_data)
