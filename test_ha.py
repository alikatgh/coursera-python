import os
import json
from employee import details
from employee import employee_name, age, title

employee_dict = {'first name': str(employee_name),
                 'age': int(age),
                 'title': str(title)}


def create_dict(name, age, title):
    return {
        'first_name': str(name),
        'age': int(age),
        'title': str(title)
    }


def write_json_to_file(json_obj, output_file):
    file_path = os.path.join(os.getcwd(), output_file)
    newfile = open(file_path, "w")
    newfile.write(json_obj)
    newfile.close()


def main():

    details()

    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))
    write_json_to_file(json_object, "employee.json")


if __name__ == "__main__":
    main()
