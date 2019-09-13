import os


def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__)) #trouve le nom du dossier ../../
    path_to_file = os.path.join(directory, "data", data_file) #le path

    with open(path_to_file, 'r') as file: #ouvre le fichier
        preview = file.readline()

    print("File found, here is a preview: \n\n {}",format(preview))

def main():
    launch_analysis('SyceronBrut.xml')





#lance le programme
if __name__ == "__main__":
    print("Analysis started...")
    main()
    print("Analysis complete.")