import matplotlib.pyplot as plt

def format_plot(xlab, ylab, show):
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel(xlab, fontsize=18)
    plt.ylabel(ylab, fontsize=18)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    if show:
        plt.show()

def plot(x, y, lab, xlab, ylab, fig=1, mark=0, show=False):
    ny = len(y)
    for i in range(ny):
        if mark:
            plt.plot(x, y[i], mark[i], label=lab[i])
        else:
            plt.plot(x, y[i], label=lab[i])
    format_plot(xlab, ylab, show)
