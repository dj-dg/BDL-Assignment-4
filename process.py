import yaml
import pandas as pd

def calculate_average(input, output):
    df = pd.read_csv(input)
    df["DATE"] = pd.to_datetime(df["DATE"])
    df.set_index('DATE', inplace=True)
    monthly_average = df.resample("M").mean()
    monthly_average.to_csv(output)

if __name__ == "__main__":
    with open("params.yaml", 'r') as file:
        params = yaml.safe_load(file)
    
    input = params['monthly_data']
    output = params['output_file']

    calculate_average(input,output)