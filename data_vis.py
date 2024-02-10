import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#cd WB\ data\ science

df = pd.read_csv("venv/CSV_files/All artists_top_tracks.csv", index_col=0)
df.info()