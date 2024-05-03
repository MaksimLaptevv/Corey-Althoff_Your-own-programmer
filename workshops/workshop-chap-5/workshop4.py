about_me = {'Maksim':'16',
            'height':'181',
            'color':'green',
            'education':'school',
            'github':'https://github.com/MaksimLaptevv',
            'about workshop':'https://github.com/MaksimLaptevv/Corey-Althoff_Your-own-programmer'}

ans = input('enter Maksim, height, color, education, github, about workshop: ')
if ans in about_me:
    print(about_me[ans])