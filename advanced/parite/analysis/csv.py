import os
import logging as lg                #lib pour gestion de logs

lg.basicConfig(level=lg.DEBUG)      #initie un niveau de log

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__)) #trouve le nom du dossier ../../
    path_to_file = os.path.join(directory, "data", data_file) #le path

    try:
        with open(path_to_file, 'r') as file: #ouvre le fichier en read
            preview = file.readline()
            lg.debug("File found, here is a preview: \n\n {}".format(preview))

    except FileNotFoundError as ex:     #marque l'error404 en tant que variable ex
        lg.critical("error : {}".format(e))

def main():
    launch_analysis('current_mps.csv')





#lance le programme
if __name__ == "__main__":
    print("Analysis started...")
    main()
    print("Analysis complete.")