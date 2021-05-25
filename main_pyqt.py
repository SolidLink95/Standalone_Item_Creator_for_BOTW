import subprocess, datetime

def main():
    f = open('errors.log', 'a')
    f.write(f'\n___________________________________________________________\n\n')
    f.write(f'Command output for SIC on {datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")} :\n')
    #p = subprocess.Popen('python main_window.py', stdout=f, stderr=f, shell=True) #no skipping
    p = subprocess.Popen('python main_window.py', stdout=f, stderr=f, shell=True)
    print('Exiting SIC')
    f.close()

if __name__ == '__main__':
    main()