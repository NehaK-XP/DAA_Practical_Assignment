import matplotlib.pyplot as plt
import os

def plot_results(results, input_type, title):
    x = list(range(50, 2001, 50))   # input sizes 50 to 2000
    
    for sort_name in results:
        y = results[sort_name][input_type]
        plt.plot(x, y, label=sort_name)
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    os.makedirs('graphs', exist_ok=True)
    plt.savefig(f'graphs/{input_type}.png')
    plt.show()

def plot_comparisons(results, input_type, title):
    x = list(range(50, 2001, 50))
    for sort_name in results:
        y = results[sort_name][input_type + '_comparisons']
        if y and y[0] is not None:
            plt.plot(x, y, label=sort_name)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Number of Comparisons')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    os.makedirs('graphs', exist_ok=True)
    plt.savefig(f'graphs/{input_type}_comparisons.png')
    plt.show()