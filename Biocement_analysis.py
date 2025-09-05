import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("biocement_tests.csv")
summary = df.groupby(['mix_id','curing_days'])['compressive_strength_MPa'].agg(['mean','count','std']).reset_index()
summary.to_csv("biocement_summary_bymix_curings.csv", index=False)

plt.figure(figsize=(8,5))
sns.lineplot(data=df, x='curing_days', y='compressive_strength_MPa', hue='mix_id', marker='o')
plt.title("Compressive Strength vs Curing Days")
plt.savefig("strength_vs_curing.png", dpi=200)
plt.close()

plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='mix_id', y='compressive_strength_MPa')
plt.title("Strength distribution by Mix")
plt.savefig("strength_by_mix.png", dpi=200)
plt.close()

print("Saved plots and summary CSV")
