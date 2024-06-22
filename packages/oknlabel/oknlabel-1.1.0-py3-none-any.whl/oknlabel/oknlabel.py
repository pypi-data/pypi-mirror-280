import sys
import csv
import os
import argparse
import importlib.metadata
from importlib.resources import files
import commentjson


# This function is to get header position from the given array
def get_index(search_input, array_in):
    idx_found = False
    return_idx = None
    for idx, val in enumerate(array_in):
        if val == search_input:
            idx_found = True
            return_idx = idx
            break

    if not idx_found:
        print(f"{search_input} can not be found!")

    return return_idx


# This function is to get built-in config location with new library (from importlib.resources import files)
def get_config_location(module_name, config_file_name):
    config_dir = files(module_name).joinpath(config_file_name)
    return str(config_dir)


# This function is print updater config information
# This is separate function because we only want to see filters info from it
def show_config(config_location):
    try:
        with open(config_location) as config_file:
            config_info = commentjson.load(config_file)
            filter_info = config_info["labels"]
            for info in filter_info:
                print(info)
    except Exception as error:
        print(f"Error:{error}")


# This function is to check the config file type is valid or not
def valid_config_name(name_to_be_checked):
    if str(name_to_be_checked).lower().endswith(".json") or str(name_to_be_checked).lower().endswith(".config"):
        return True
    else:
        return False


def read_table(input_file_dir):
    file = open(input_file_dir)
    csv_reader = csv.reader(file)
    header_array = []
    rows = []
    data_table_dict = {}
    count = 0

    for row in csv_reader:
        if count <= 0:
            header_array = row
            count += 1
        else:
            rows.append(row)

    for header in header_array:
        header_position = get_index(header, header_array)
        value_array = []
        for row in rows:
            input_value = str(row[header_position])
            value_array.append(input_value)
        data_table_dict[header] = value_array

    return data_table_dict


def get_rule_info(file_input):
    with open(file_input, 'r') as rule_config:
        rule_info_dict = commentjson.load(rule_config)
        try:
            min_okn_chain_length_value = int(rule_info_dict["min_okn_chain_length"])
            min_okn_per_window_value = int(rule_info_dict["min_okn_per_window"])
        except KeyError:
            print(f"There is no min_okn_chain_length and min_okn_per_window info in the given {file_input}.")
            return
        except TypeError:
            print(f"Invalid rule info file input : {file_input}.")
            return
    return min_okn_chain_length_value, min_okn_per_window_value


def check_signal_data(result_id_array, result_chain_id_array, return_data_name):
    result_data = []

    # Looking for result id and result chain id.
    # When they are found, they are added into result data array
    for r_id, r_c_id in zip(result_id_array, result_chain_id_array):
        if int(r_id) != -1 and int(r_c_id) != -1:
            result_data.append((int(r_c_id), int(r_id)))

    # remove duplicate number from result data array
    unique_result_data = list(dict.fromkeys(result_data))
    # print(unique_result_data)

    # taking only result id
    raw_unique_result_id_array = []
    for ri in unique_result_data:
        raw_unique_result_id_array.append(ri[0])

    # remove duplicate result id from raw unique result id array
    unique_result_id_array = list(dict.fromkeys(raw_unique_result_id_array))

    final_data_array = []

    # looping unique result id array to get all result chain id which are
    # related to their individual result id into temp array
    # after that, add result id and its related result chain id into final data array as a tuple
    for rid in unique_result_id_array:
        temp_array = []
        for data in unique_result_data:
            if rid == data[0]:
                temp_array.append(data[1])
        final_data_array.append((rid, temp_array))

    if return_data_name == "is_chained_okn":
        is_chained_okn_array = []
        chained_id_array = []
        if len(final_data_array) > 0:
            # print(f"Raw result: {final_data_array}")
            for tuple_item in final_data_array:
                chain_length = len(tuple_item[1])
                if chain_length > 1:
                    is_chained_okn_array.append((tuple_item[0], "TRUE"))              
                else:
                    is_chained_okn_array.append((tuple_item[0], "FALSE"))
                chained_id_array.append(tuple_item[0])
        return is_chained_okn_array, chained_id_array
    else:
        num_of_chained_okn_array = []
        chained_id_array = []
        if len(final_data_array) > 0:
            # print(f"Raw result: {final_data_array}")
            for tuple_item in final_data_array:
                chain_length = len(tuple_item[1])
                num_of_chained_okn_array.append((tuple_item[0], chain_length))              
                chained_id_array.append(tuple_item[0])
        return num_of_chained_okn_array, chained_id_array


def get_sparse_boolean_by_rows(row_index, w_size, id_array, num_chained_okn_array, rules_input):
    start_index = row_index
    end_index = start_index + w_size
    end_index = len(id_array) if end_index >= len(id_array) else end_index
    id_array_cropped = id_array[start_index:end_index]
    num_chained_okn_array_cropped = num_chained_okn_array[start_index:end_index]

    temp_array = []
    current_id = 0
    for id, num_chained in zip(id_array_cropped, num_chained_okn_array_cropped):
        id = int(float(id))
        if id >= 0 and id != current_id:
            current_id = id
            temp_array.append((id, num_chained))

    # print(temp_array)
    
    min_okn_chain_length = int(rules_input["min_okn_chain_length"])
    min_okn_per_window = int(rules_input["min_okn_per_window"])

    # Checking if there is chained okn or not
    for t_item in temp_array:
        if t_item[1] >= min_okn_chain_length:
            return True
    
    unchained_count = len(temp_array)
    if unchained_count >= min_okn_per_window:
        return True
    else:
        return False


def get_sparse_boolean_by_time(row_index, w_size, id_array, num_chained_okn_array, time_array, rules_input):
    start_time = time_array[row_index]
    end_time_index = row_index + 1
    search_time = float(start_time) + w_size
    for ind, value in enumerate(time_array):
        time_value = float(value)
        if time_value >= search_time:
            end_time_index = ind
            break
        else:
            if ind >= len(time_array):
                end_time_index = len(time_array)
                break
    
    id_array_cropped = id_array[row_index:end_time_index]
    num_chained_okn_array_cropped = num_chained_okn_array[row_index:end_time_index]

    temp_array = []
    current_id = 0
    for id, num_chained in zip(id_array_cropped, num_chained_okn_array_cropped):
        id = int(float(id))
        if id >= 0 and id != current_id:
            current_id = id
            temp_array.append((id, num_chained))

    # print(temp_array)
    
    min_okn_chain_length = int(rules_input["min_okn_chain_length"])
    min_okn_per_window = int(rules_input["min_okn_per_window"])

    # Checking if there is chained okn or not
    for t_item in temp_array:
        if t_item[1] >= min_okn_chain_length:
            return True
    
    unchained_count = len(temp_array)
    if unchained_count >= min_okn_per_window:
        return True
    else:
        return False


def dispatch_label_function(label_info_input, data_dictionary, rules):
    function_name = label_info_input["function"]
    if function_name == "is_any_true":
        first_data_name = label_info_input["input"][0]
        second_data_name = label_info_input["input"][1]
        first_data_array = data_dictionary[first_data_name]
        second_data_array = data_dictionary[second_data_name]
        out_data_name = label_info_input["output"]
        out_data_array = []
        for first, second in zip(first_data_array, second_data_array):
            if str(first).lower() == "true" or str(second).lower() == "true":
                out_data_array.append("TRUE")
            else:
                out_data_array.append("FALSE")
        data_dictionary[out_data_name] = out_data_array
    elif function_name == "is_any_false":
        first_data_name = label_info_input["input"][0]
        second_data_name = label_info_input["input"][1]
        first_data_array = data_dictionary[first_data_name]
        second_data_array = data_dictionary[second_data_name]
        out_data_name = label_info_input["output"]
        out_data_array = []
        for first, second in zip(first_data_array, second_data_array):
            if str(first).lower() == "false" or str(second).lower() == "false":
                out_data_array.append("TRUE")
            else:
                out_data_array.append("FALSE")
        data_dictionary[out_data_name] = out_data_array
    elif function_name == "is_both_true":
        first_data_name = label_info_input["input"][0]
        second_data_name = label_info_input["input"][1]
        first_data_array = data_dictionary[first_data_name]
        second_data_array = data_dictionary[second_data_name]
        out_data_name = label_info_input["output"]
        out_data_array = []
        for first, second in zip(first_data_array, second_data_array):
            if str(first).lower() == "true" and str(second).lower() == "true":
                out_data_array.append("TRUE")
            else:
                out_data_array.append("FALSE")
        data_dictionary[out_data_name] = out_data_array
    elif function_name == "is_both_false":
        first_data_name = label_info_input["input"][0]
        second_data_name = label_info_input["input"][1]
        first_data_array = data_dictionary[first_data_name]
        second_data_array = data_dictionary[second_data_name]
        out_data_name = label_info_input["output"]
        out_data_array = []
        for first, second in zip(first_data_array, second_data_array):
            if str(first).lower() == "false" and str(second).lower() == "false":
                out_data_array.append("TRUE")
            else:
                out_data_array.append("FALSE")
        data_dictionary[out_data_name] = out_data_array
    elif function_name == "is_chained_okn":
        first_data_name = label_info_input["input"][0]
        second_data_name = label_info_input["input"][1]
        first_data_array = data_dictionary[first_data_name]
        second_data_array = data_dictionary[second_data_name]
        result_id_array = [int(value) for value in first_data_array]
        result_chain_id_array = [int(value) for value in second_data_array]
        is_chained_array, id_array = check_signal_data(result_id_array, result_chain_id_array, function_name)
        
        out_data_array = []
        for chain_id in result_chain_id_array:
            if chain_id in id_array:
                for t_item in is_chained_array:
                    t_chain_id = t_item[0]
                    if chain_id == t_chain_id:
                        out_data_array.append(t_item[1])
                        break
            else:
                out_data_array.append("FALSE")
        out_data_name = label_info_input["output"]
        data_dictionary[out_data_name] = out_data_array
    elif function_name == "num_of_chained_okn":
        first_data_name = label_info_input["input"][0]
        second_data_name = label_info_input["input"][1]
        first_data_array = data_dictionary[first_data_name]
        second_data_array = data_dictionary[second_data_name]
        result_id_array = [int(value) for value in first_data_array]
        result_chain_id_array = [int(value) for value in second_data_array]
        num_chained_array, id_array = check_signal_data(result_id_array, result_chain_id_array, function_name)
        
        out_data_array = []
        for chain_id in result_chain_id_array:
            if chain_id in id_array:
                for t_item in num_chained_array:
                    t_chain_id = t_item[0]
                    if chain_id == t_chain_id:
                        out_data_array.append(t_item[1])
                        break
            else:
                out_data_array.append(0)
        out_data_name = label_info_input["output"]
        data_dictionary[out_data_name] = out_data_array
    elif function_name == "is_sparse_okn":
        window_type = label_info_input["window_type"]
        if window_type == "rows":
            first_data_name = label_info_input["input"][0]
            second_data_name = label_info_input["input"][1]
            first_data_array = data_dictionary[first_data_name]
            second_data_array = data_dictionary[second_data_name]
            window_size = label_info_input["window_size"]
            out_data_array = []
            for index in range(len(first_data_array)):
                sparse_boolean = get_sparse_boolean_by_rows(index, window_size, first_data_array, second_data_array, rules)
                out_data_array.append(sparse_boolean)
            out_data_name = label_info_input["output"]
            data_dictionary[out_data_name] = out_data_array
        elif window_type == "time":            
            first_data_name = label_info_input["input"][0]
            second_data_name = label_info_input["input"][1]
            time_data_name = label_info_input["input"][2]  
            first_data_array = data_dictionary[first_data_name]
            second_data_array = data_dictionary[second_data_name]
            time_data_array = data_dictionary[time_data_name]
            window_size = label_info_input["window_size"]
            out_data_array = []
            for index in range(len(first_data_array)):
                sparse_boolean = get_sparse_boolean_by_time(index, window_size, first_data_array, second_data_array, time_data_array, rules)
                out_data_array.append(sparse_boolean)
            out_data_name = label_info_input["output"]
            data_dictionary[out_data_name] = out_data_array
        else:
            print(f"Unknown window type in \"is_sparse_okn\" function: {window_type}")
    else:
        print(f"Unknown function: {function_name}")
    return data_dictionary


def main():
    parser = argparse.ArgumentParser(prog='oknlabel',
                                     description='oknlabel package.')
    oknlabel_version = importlib.metadata.version('oknlabel')
    parser.add_argument('--version', action='version', version=oknlabel_version),
    parser.add_argument("-i", dest="input_file", required=True, default=sys.stdin,
                        metavar="input signal csv file")
    parser.add_argument("-r", dest="rule_info", required=False, default=None,
                        metavar="rule info")
    parser.add_argument("-c", dest="label_config", required=False, default=None,
                        metavar="okn label config")
    parser.add_argument("-o", dest="output_file", required=False, default=None,
                        metavar="output csv file")

    args = parser.parse_args()
    input_file = args.input_file
    rule_info = args.rule_info
    label_config = args.label_config
    output_file = args.output_file

    if os.path.isfile(input_file):
        file_name = os.path.basename(input_file)
        if not str(file_name).endswith(".csv"):
            print("Input file must be csv file.")
            return
    else:
        print(f"Invalid input file input : {input_file}")
        return

    if rule_info is None:
        rule_info_location = get_config_location("oknlabel", "okn_detection_rule.json")
        # print(rule_info_location)
        min_okn_chain_length, min_okn_per_window = get_rule_info(rule_info_location)
        # print(min_okn_chain_length)
        # print(min_okn_per_window)
    else:
        if os.path.isfile(rule_info):
            # print(rule_info)
            if valid_config_name(rule_info):
                try:
                    min_okn_chain_length, min_okn_per_window = get_rule_info(rule_info)
                except TypeError:
                    print(f"Invalid rule info file input : {rule_info}.")
                    return
                # print(min_okn_chain_length)
                # print(min_okn_per_window)
            else:
                print("Rule info file must be json or config file type.")
                return
        else:
            if "," in str(rule_info) and ":" in str(rule_info): 
                rule_info_string = str(rule_info).replace("{", "").replace("}", "").replace("\'", "").replace("\"", "")
                min_okn_chain_length_str, min_okn_per_window_str = rule_info_string.split(",")
                rule_info_dict = {}
                key1, value1 = min_okn_chain_length_str.split(":")
                rule_info_dict[key1] = value1
                key2, value2 = min_okn_per_window_str.split(":")
                rule_info_dict[key2] = value2
                try:
                    min_okn_chain_length = int(rule_info_dict["min_okn_chain_length"])
                    min_okn_per_window = int(rule_info_dict["min_okn_per_window"])
                except KeyError:
                    print(f"There is no min_okn_chain_length and min_okn_per_window info in the given string : {rule_info}.")
                    return
                # print(min_okn_chain_length)
                # print(min_okn_per_window)
    rule_info_dict = {}
    rule_info_dict["min_okn_chain_length"] = min_okn_chain_length
    rule_info_dict["min_okn_per_window"] = min_okn_per_window

    if label_config is None:
        label_config_location = get_config_location("oknlabel", "oknlabel_config.json")
    else:
        if os.path.isfile(label_config):
            label_config_location = label_config
        else:
            print(f"Invalid label config input : {label_config}.")
            return
    
    try:
        with open(label_config_location, 'r') as label_info:
            label_info_loaded = commentjson.load(label_info)
    except Exception as error:
        print(error)
        return
    
    label_info_array = label_info_loaded["labels"]
    
    if output_file is None:
        input_file_name = os.path.basename(input_file)
        output_file = str(input_file).replace(input_file_name, "signal.updated.csv")
    else:
        if not str(output_file).lower().endswith(".csv"):
            print("Outupt file must be csv file.")
            return
    
    print("--------------------------------------------------------------------------------------")
    print(f"Input file : {input_file}")
    print(f"Output file : {output_file}")
    print(f"Rule info : min_okn_chain_length: {min_okn_chain_length}, min_okn_per_window: {min_okn_per_window}")
    print("Label Info :")
    for label in label_info_array:
        print(label)
    
    data_dict = read_table(input_file)

    for label in label_info_array:
        if label["Enabled"]:
            data_dict = dispatch_label_function(label, data_dict, rule_info_dict)
    
    out_header_array = []
    for key in data_dict:
        out_header_array.append(key)

    print("Start writing the output csv!")
    with open(output_file, mode='w', newline="") as destination_file:
        csv_writer = csv.DictWriter(destination_file, fieldnames=out_header_array)
        csv_writer.writeheader()

        row_count = len(data_dict[out_header_array[0]])

        for i in range(row_count):
            temp_dict = {}
            for header in out_header_array:
                temp_dict[header] = data_dict[header][i]
            csv_writer.writerow(temp_dict)
    print(f"Output csv is saved in the {output_file}.")
    print("--------------------------------------------------------------------------------------")

