import json

def extract_and_convert_into_list(target_file):
    my_file = open(target_file, "r")
    data = my_file.read()
    data = data[1:-2]
    data_into_list = data.replace('\n', ' ').split("},")
    return data_into_list

def modify_list(data_into_list):
    modified_list = []
    for data in data_into_list:
        individual_data = data+"}"
        individual_data_as_json = json.loads(individual_data)
        modified_list.append(individual_data_as_json)
    return modified_list

def create_new_data(modified_list):
    f = open("Modified.json", "a")
    for data in modified_list:
        # print(x)
        f.write('"'+str(data["pixel_id"])+'"'+': [')
        f.write('{"date":"'+str(data["date"])+'",'+'"conversions": '+str(data["conversions"])+'},')
        f.write('{"date":"'+str(data["date"])+'",'+'"conversions": '+str(data["conversions"])+'}],')
    f.close()

def main(target_file):
    data_into_list = extract_and_convert_into_list(target_file)
    modified_list = modify_list(data_into_list)
    create_new_data(modified_list)

main("sample.txt")