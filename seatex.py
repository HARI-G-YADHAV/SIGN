import csv
import networkx as nx
import itertools

def read_nominal_roll(file_path):
    class_data = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            register_no = row['register_no']
            class_details = register_no[:8] 
            if class_details in class_data:
                class_data[class_details].append(register_no)
            else:
                class_data[class_details]=[register_no]
        return class_data


if __name__ == "__main__":
    file_path = "Sample_NominalRoll.csv"
    student_data = read_nominal_roll(file_path)
    print(student_data)
    row=int(input("Enter the row of examination class"))
    column=int(input("Enter the columns of examination class"))
    
    