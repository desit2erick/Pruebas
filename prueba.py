from bs4 import BeautifulSoup
import requests, csv, time

pagina = requests.get('https://ecat.spectrapremium.com/?language=en')
soup = BeautifulSoup(pagina.content, 'html.parser')

# Headers Spectra Premium
headers = {'x-requested-with': 'XMLHttpRequest'}

with open( 'data_spectra_premium.csv', 'w', encoding='UTF8' ) as f:
    # Obtención de años
    writer = csv.writer(f)
    dataYears =  soup.find_all('select', attrs={'id': 'menu_vertical_vehicles_ymm_year'})
    for data in dataYears:
        options = data.findAll('option')
        for year in options:
            anio = year.string
            if anio != 'Select':
                dataJS1 = requests.get( f'https://ecat.spectrapremium.com/vehicles/makes.json?year={anio}', headers=headers ).json()
                for option1 in dataJS1:
                    marca = option1['code']
                    dataJS2 = requests.get( f'https://ecat.spectrapremium.com/vehicles/models.json?year={anio}&make={marca}', headers=headers ).json()
                    for option2 in dataJS2:
                        modelo = option2['code']
                        dataJS3 = requests.get( f'https://ecat.spectrapremium.com/vehicles/submodels.json?year={anio}&make={marca}&model={modelo}', headers=headers ).json()
                        for option3 in dataJS3:
                            submodelo = option3['code']
                            row = [ anio, marca, modelo, submodelo ]
                            writer.writerow(row)
            time.sleep(10)