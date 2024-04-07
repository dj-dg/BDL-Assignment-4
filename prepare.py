import yaml
import pandas as pd

def prep_hourly_data(input, output, fields):
    df = pd.read_csv(input)
    hourly_average = df[fields]
    hourly_average.to_csv(output, index=False)

def prep_monthly_data(input, output, fields):
    df = pd.read_csv(input)
    monthly_average = df[fields]
    monthly_average.to_csv(output, index=False)

def prep_ground_truth(input, output, fields):
    df = pd.read_csv(input)
    ground_truth = df[fields]
    ground_truth.to_csv(output, index=False)

if __name__ == "__main__":
    with open("params.yaml", 'r') as file:
        params = yaml.safe_load(file)
    
    input_hourly = params['hourly_data']
    input_monthly = params['monthly_data']
    input_ground_truth = params['hourly_data']

    output_hourly = params['hourly_average']
    output_monthly = params['monthly_average']
    output_ground_truth = params['ground_truth']

    hourly_fields = params['hourly_average_fields']
    monthly_fields = params['monthly_average_fields']
    ground_truth_fields = params['ground_truth_fields']

    prep_ground_truth(input_ground_truth, output_ground_truth, ground_truth_fields)
    prep_hourly_data(input_hourly, output_hourly, hourly_fields)
    prep_monthly_data(input_monthly, output_monthly, monthly_fields)
