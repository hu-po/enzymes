"""Combine the predictions from the best models."""
import pandas as pd

# read in the csv files using pandas
best_runs = [    
    pd.read_csv('pred_run_esm1v_t33_650M_UR90S_5_64_0.0009884843919684074.csv'),
    pd.read_csv('pred_run_esm1v_t33_650M_UR90S_1_128_0.0014695742681208302.csv'),
    pd.read_csv('pred_run_esm1v_t33_650M_UR90S_5_128_0.0005322629125219.csv'),
]

# First, we will concatenate the three dataframes into a single dataframe
df_combined = pd.concat(best_runs)

# Next, we will group the rows by "seq_id" and compute the average of the "tm" column
df_averaged = df_combined.groupby("seq_id")["tm"].mean().reset_index()

# Round the values in the "tm" column to the nearest decimal place
df_averaged["tm"] = df_averaged["tm"].round(1)

# write the resulting dataframe to a csv file
df_averaged = df_averaged[['seq_id', 'tm']]
df_averaged.to_csv('submission.csv', index=False)

# Read the "sample_submission.csv" and "submission.csv" files into pandas dataframes
df1 = pd.read_csv("sample_submission.csv")
df2 = pd.read_csv("submission.csv")

# Check if the "seq_id" columns in the two dataframes are equal
if (df1["seq_id"] == df2["seq_id"]).all():
    print("The 'seq_id' columns are equal!")
else:
    print("The 'seq_id' columns are not equal.")