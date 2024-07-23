import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


async def create_visualization(df: pd.DataFrame):
    os_counts = df['os'].value_counts().reset_index()
    os_counts.columns = ['os', 'count']

    os_counts['os'] = os_counts['os'].apply(lambda x: x[:30])

    sns.barplot(x="os", y="count", data=os_counts)
    plt.title("Number of Entries for Each OS")
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.5)
    plt.xlabel("OS", labelpad=50)
    plt.ylabel("Number of Entries")

    # Save the plot as a PNG file
    plt.savefig('/app/output/visualization.png')
    plt.close()