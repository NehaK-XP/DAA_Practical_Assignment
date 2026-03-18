import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os


X = list(range(50, 2001, 50))

QUICKSORT_NAMES = ['quickSortFirst', 'quickSortMedian', 'quickSortRandom']

ALL_SORTS = ['heapSort', 'mergeSort', 'radixSort',
             'bubbleSort', 'insertionSort', 'selectionSort',
             'quickSortMedian']   # only best quicksort version

COLORS = {
    'heapSort':        '#1f77b4',
    'mergeSort':       '#ff7f0e',
    'radixSort':       '#2ca02c',
    'bubbleSort':      '#d62728',
    'insertionSort':   '#9467bd',
    'selectionSort':   '#8c564b',
    'quickSortFirst':  '#e377c2',
    'quickSortMedian': '#17becf',
    'quickSortRandom': '#bcbd22',
}

MARKERS = {
    'heapSort':        'o',
    'mergeSort':       's',
    'radixSort':       '^',
    'bubbleSort':      'D',
    'insertionSort':   'v',
    'selectionSort':   'P',
    'quickSortFirst':  'X',
    'quickSortMedian': '*',
    'quickSortRandom': 'h',
}


def _base_plot(title, ylabel):
    fig, ax = plt.subplots(figsize=(13, 7))
    fig.patch.set_facecolor('#f9f9f9')
    ax.set_facecolor('#f9f9f9')
    ax.set_title(title, fontsize=17, fontweight='bold', pad=18)
    ax.set_xlabel('Input Size (n)', fontsize=13, labelpad=10)
    ax.set_ylabel(ylabel, fontsize=13, labelpad=10)
    ax.grid(True, linestyle='--', linewidth=0.6, alpha=0.7, color='#cccccc')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return fig, ax

def _plot_lines(ax, results, names, input_type):
    for name in names:
        if name not in results:
            continue
        y = results[name][input_type]
        ax.plot(X, y,
                label=name,
                color=COLORS.get(name, '#333333'),
                marker=MARKERS.get(name, 'o'),
                markevery=5,          # only show marker every 5 points
                linewidth=2,
                markersize=6)

def _finish(fig, ax, filepath):
    ax.legend(fontsize=11, framealpha=0.9, loc='upper left',
              edgecolor='#cccccc', fancybox=True)
    plt.tight_layout()
    os.makedirs('graphs', exist_ok=True)
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved: {filepath}")



def plot_quicksort(results, input_type, title, filename):
    """ compare all three QuickSort versions """
    fig, ax = _base_plot(title, 'Time (seconds)')
    _plot_lines(ax, results, QUICKSORT_NAMES, input_type)
    _finish(fig, ax, f'graphs/{filename}.png')

def plot_all_sorts(results, input_type, title, filename):
    """ all 7 sorts using best QuickSort only """
    fig, ax = _base_plot(title, 'Time (seconds)')
    _plot_lines(ax, results, ALL_SORTS, input_type)
    _finish(fig, ax, f'graphs/{filename}.png')

def plot_comparisons(results, names, input_type, title, filename):
    """ comparison counts """
    fig, ax = _base_plot(title, 'Number of Comparisons')
    for name in names:
        if name not in results:
            continue
        y = results[name][input_type + '_comparisons']
        if y and y[0] is not None:
            ax.plot(X, y,
                    label=name,
                    color=COLORS.get(name, '#333333'),
                    marker=MARKERS.get(name, 'o'),
                    markevery=5,
                    linewidth=2,
                    markersize=6)
    _finish(fig, ax, f'graphs/{filename}.png')

def plot_all(results):
    # QuickSort versions
    plot_quicksort(results, 'ascending',  'QuickSort Variants — Best Case',    'qs_best')
    plot_quicksort(results, 'descending', 'QuickSort Variants — Worst Case',   'qs_worst')
    plot_quicksort(results, 'random',     'QuickSort Variants — Average Case', 'qs_average')

    # All 7 sorts
    plot_all_sorts(results, 'ascending',  'All Sorts — Best Case',    'all_best')
    plot_all_sorts(results, 'descending', 'All Sorts — Worst Case',   'all_worst')
    plot_all_sorts(results, 'random',     'All Sorts — Average Case', 'all_average')

    # Comparisons
    plot_comparisons(results, QUICKSORT_NAMES, 'ascending',  'QuickSort Comparisons — Best Case',    'qs_comp_best')
    plot_comparisons(results, QUICKSORT_NAMES, 'descending', 'QuickSort Comparisons — Worst Case',   'qs_comp_worst')
    plot_comparisons(results, QUICKSORT_NAMES, 'random',     'QuickSort Comparisons — Average Case', 'qs_comp_average')

    plot_comparisons(results, ALL_SORTS, 'ascending',  'All Sorts Comparisons — Best Case',    'all_comp_best')
    plot_comparisons(results, ALL_SORTS, 'descending', 'All Sorts Comparisons — Worst Case',   'all_comp_worst')
    plot_comparisons(results, ALL_SORTS, 'random',     'All Sorts Comparisons — Average Case', 'all_comp_average')