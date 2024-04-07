import os
import yaml
import requests
from bs4 import BeautifulSoup
import random

def file_size_check(file_size):
    if file_size.endswith('M'):
        return float(file_size[:-1])
    elif file_size.endswith("K"):
        return float(file_size[:-1])/1024
    else:
        return 0
    
def file_download(url, out_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(out_path, 'wb') as file:
            file.write(response.content)
        return response.content.split('\n')
    else:
        print(f"{url} could not be downloaded.")
        return []

def unique_identifier_creation():
    text = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'), k=8)
    return text

def save(data, out_path):
    with open(out_path, 'w') as file:
        for line in data:
            file.write(line.replace(' 0.0', '').rstrip('.').rstrip('0')+'\n')

def data_download(base_url, year, out_path, min_size):
    url = base_url.replace("YYYY", str(year))
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        urls = soup.findall('a', href=True)
        monthly_data = []
        hourly_data = []
        for link in urls:
            file_name = link['href']
            if file_name.endswith('.csv'):
                file_info = link.text.split()
                file_size = file_size_check(file_info[-1])
                if file_size > min_size:
                    id = unique_identifier_creation()
                    data = file_download(url + file_name, os.path.join(out_path, f"{id}_{file_name}"))
                    if "hourly" in file_name:
                        hourly_data.extend(data)
                    else:
                        monthly_data.extend(data)
        save(hourly_data, os.path.join(out_path, 'hourly_data.csv'))
        save(monthly_data, os.path.join(out_path, "monthly_data.csv"))
    else:
        print(f"Could not download data for the year {year}.")

if __name__ == "__main__":
    with open("params.yaml", "r") as file:
        params = yaml.safe_load(file)['download']
    
    base_url = params['base_url']
    out_path = params['out_path']
    years = params['years']
    min_size = params['min_size']

    for year in years:
        data_download(base_url, year, out_path, min_size)
                


