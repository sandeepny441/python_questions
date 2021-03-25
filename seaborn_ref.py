import seaborn as sns 
import pandas as pd 

print(100)

fig,ax = plt.subplots()
sns.scatterplot(data=df, hue='category', x='attempts', y='success')
plt.legend(loc=2)
plt.savefig('scatter.png')
plt.show()

tips = sns.load_dataset("tips")
tips.head()
sns.scatterplot(data=tips, x="total_bill", y="tip")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="time")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size", palette="deep")
tip_rate = tips.eval("tip / total_bill").rename("tip_rate")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue=tip_rate)
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size", size="size")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size", size="size",
                sizes=(20, 200), legend="full")
markers = {"Lunch": "s", "Dinner": "X"}
sns.scatterplot(data=tips, x="total_bill", y="tip", style="time", markers=markers)
sns.scatterplot(data=tips, x="total_bill", y="tip", s=100, color=".2", marker="+")

index = pd.date_range("1 1 2000", periods=100, freq="m", name="date")
data = np.random.randn(100, 4).cumsum(axis=0)
wide_df = pd.DataFrame(data, index, ["a", "b", "c", "d"])
sns.scatterplot(data=wide_df)

sns.relplot(
    data=tips, x="total_bill", y="tip",
    col="time", hue="day", style="day",
    kind="scatter"
)
