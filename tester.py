import os
from subprocess import call


def listing_music():
    file_names = []
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        if file.endswith(".wav"):
            name = os.path.join(cwd, file)
            file_names.append(file)

    return file_names


def main():
    music = listing_music()
    for i in range(len(music)):
        print(music[i])
        call(['python3', 'inf145347_inf145216.py', music[i]])

if __name__ == '__main__':
    main()