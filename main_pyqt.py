import subprocess, datetime
from files_manage import get_res
from botw_duplicator_tools.actorinfo_tool import get_entry_by_name, file_to_pio

def test():
    series_adv = get_res('Series_adv')
    ups = get_res('upgradeable')
    pio = file_to_pio('cache\\ActorInfo.product.sbyml')
    res = {}
    for s in series_adv:
        for i, elem in enumerate(pio['Actors'], 0):
            if not 'seriesArmorSeriesType' in elem: continue
            if s != elem['seriesArmorSeriesType']: continue
            if not elem['name'] in ups: continue
            series_adv[s] = elem['name']
            break
    for i in series_adv:
        print(f'\"{i}\" : \"{series_adv[i]}\",')

def main():
    print('Starting SIC')
    f = open('errors.log', 'a')
    f.write(f'\n___________________________________________________________\n\n')
    f.write(f'Command output for SIC on {datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")} :\n')
    #p = subprocess.Popen('python main_window.py', stdout=f, stderr=f, shell=True) #no skipping
    p = subprocess.Popen('python main_window.py', stdout=f, stderr=f, shell=True)

    print('SIC started')
    #f.close()

if __name__ == '__main__':
    #test()
    main()