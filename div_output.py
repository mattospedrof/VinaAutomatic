import os


def read_pdbqt(number_model, name_archive_pdbqt, name_desired_file):
    with open(name_archive_pdbqt, 'r') as origin_pdbqt:
        content_in_origin = origin_pdbqt.read()
        number_model = model_number_desired

        init_model = content_in_origin.find(f"MODEL {number_model}")
        if init_model == -1:
            print(f"The model entered '{number_model}' was not found.")
            return

        next_model = content_in_origin.find("MODEL ", init_model + 1)

        if next_model == -1:
            end_model = len(content_in_origin)
        else:
            end_model = next_model

        excerpt_model = content_in_origin[init_model:end_model].strip()

        with open(name_desired_file, 'w') as desired_file:
            desired_file.write(excerpt_model)

        print(
            f"\nThe model excerpt {number_model} was written in the file {name_desired_file} \n"
            "Thank you for your support\n"
            "For any question, visit the github:\n"
            "https://github.com/Frannkz10/Automatic-Autodock-Vina"
        )


origin_pdbqt = input("Enter the file name pdbqt with the '.pdbqt': ")

if not os.path.exists(origin_pdbqt):
    print(f"The file '{origin_pdbqt}' does not exist.")
else:
    model_number_desired = input(
        "Enter the model number you want to extract: ")
    model_number_desired = int(model_number_desired)
    desired_file = f"{os.path.splitext(origin_pdbqt)[0]}_{model_number_desired}.pdbqt"
    read_pdbqt(model_number_desired, origin_pdbqt, desired_file)