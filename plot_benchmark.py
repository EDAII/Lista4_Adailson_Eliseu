import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
from os import listdir
from os.path import isfile, join

def get_dataset(dataset_file_name):
    df = pd.read_csv(dataset_file_name, skipinitialspace=True)
    return df

def sort_by_columns(dataframe, columns):
    df = dataframe.sort_values(by=columns)
    return df

def plot_benchmark(dataframes, *args):
    ax = None
    if dataframes:
        pass
    elif args:
        dataframes = [x for x in args]

    for dataframe in dataframes:
        if not ax:
            ax = dataframe.plot(kind='line', x='dataset_size', y='time_in_ms', title="Sort benchmark")
            ax.set_ylabel('Time (ms)')
            ax.set_xlabel('Number of elements to sort')
        else:
            dataframe.plot(kind='line', x='dataset_size', y='time_in_ms', ax=ax)
    return ax

if __name__ == '__main__':
    files = []
    if len(sys.argv) > 1:
        if sys.argv[1] == '__all__':
            mypath = "."
            extension = ".csv"
            files = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and extension in f)]
        else:
            for y in sys.argv[1:]:
                files.append(str(y))
    else:
        files.append('benchmark_recursive_merge_sort.csv')
    file_dfs = []
    legends_dfs = []
    df_medians = []
    legends_dfs_medians = []
    for file in files:
        df_median = []
        df = get_dataset(file)
        df = sort_by_columns(df, ['dataset_size','time_in_ms'])

        dataset_file_name = "_".join("".join(file.split('performance_report/')[:]).split('_sort')[0].split('_')[1:] +['sort'])
        median_of = "{}_median".format(dataset_file_name)

        for i in range(df.dataset_size.unique().size):
            df_median.append([median_of, df.dataset_size.unique()[i], np.median(df[df.dataset_size == df.dataset_size.unique()[i]].iloc[:,2].values), True])

        file_dfs.append(df)

        df_median = pd.DataFrame(df_median, columns=["strategy", "dataset_size", "time_in_ms", "is_random"])
        df_median = sort_by_columns(df_median, ['dataset_size','time_in_ms'])
        df_medians.append(df_median)

        legends_dfs.append(dataset_file_name)
        legends_dfs_medians.append(median_of)

    dfs = file_dfs

    data_figure = plot_benchmark(dataframes=dfs)
    data_figure.legend(legends_dfs)
    data_medians_figure = plot_benchmark(dataframes=df_medians)
    data_medians_figure.legend(legends_dfs_medians)
    plt.show()
