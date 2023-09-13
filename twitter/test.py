from nltk.sentiment import SentimentIntensityAnalyzer
import csv
from matplotlib import pyplot as plt
import numpy as np

sia = SentimentIntensityAnalyzer()
rows = []
with open("Nupur_dataset.csv", 'r') as file:
    csvreader = csv.reader(file)
    for i in csvreader:
        rows.append(i)

pos = 0
neg = 0
neu = 0

for j in range(len(rows)):

    print(rows[j])
    text = rows[j][1]
    scores = sia.polarity_scores(text)
    pos = pos + scores['pos']
    neu = neu + scores['neu']
    neg = neg + scores['neg']
    print(scores)

Ratio = ['Positive', 'Negative', 'Neutral']
data = [pos, neg, neu]
explode = (0.1, 0.0, 0.2)
colors = ("orange", "cyan", "red")

wp = {'linewidth': 1, 'edgecolor': "green"}


def func(pct, allvalues):
    absolute = int(pct / 100. * np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data), explode=explode, labels=Ratio, shadow=True, colors=colors, startangle=90, wedgeprops=wp, textprops=dict(color="magenta"))

ax.legend(wedges, Ratio, title="Ratio", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Customizing pie chart")

plt.show()