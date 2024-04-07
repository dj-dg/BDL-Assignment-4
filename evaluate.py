import pandas as pd
import yaml
from sklearn.metrics import r2_score

def r2_score_calculate(monthly_aggregated_gt_file, computed_monthly_aggregate_file, output_file):
    monthly_aggregated_gt = pd.read_csv(monthly_aggregated_gt_file)
    computed_monthly_aggregate = pd.read_csv(computed_monthly_aggregate_file)
    r2_scores = {}
    for field in monthly_aggregated_gt.columns:
        r2_scores[field] = r2_score(monthly_aggregated_gt[field], computed_monthly_aggregate[field])
    with open(output_file, 'w') as file:
        for key, value in r2_scores.items():
            file.write(f"{key}: {value}\n")

if __name__ == "__main__":
    with open("params.yaml", 'r') as file:
        params = yaml.safe_load(file)
    
    monthly_aggregated_gt_file = params['monthly_aggregated_gt']
    computed_monthly_aggregate_file = params['computed_monthly_aggregate_file']
    output_file = params['output_file']

    r2_score_value = r2_score_calculate(monthly_aggregated_gt_file,computed_monthly_aggregate_file,output_file)
    
    if r2_score_value >= 0.9:
        print("Dataset is consistent")
    
    else:
        print("Dataset is not consistent")