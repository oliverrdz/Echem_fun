import matplotlib.pyplot as plt

def format_plot():
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid()
    plt.tight_layout()

def plot(x, y, xlab, ylab, fig=1, mark='-'):
    plt.figure(fig)
    plt.plot(x, y, mark)
    plt.xlabel(xlab, fontsize=18)
    plt.ylabel(ylab, fontsize=18)
    format_plot()
    plt.show()

def plot2(x1, y1, lab1, mark1, x2, y2, lab2, mark2, xlab, ylab, fig=1):
    plt.figure(fig)
    plt.plot(x1, y1, mark1, label=lab1)
    plt.plot(x2, y2, mark2, label=lab2)
    plt.xlabel(xlab, fontsize=18)
    plt.ylabel(ylab, fontsize=18)
    plt.legend()
    format_plot()
    plt.show()

def plot3(x1, y1, x2, y2, x3, y3, xlab, ylab, lab1, lab2, lab3, fig=1, mark1='-', mark2='--', mark3='-'):
    plt.figure(fig)
    plt.plot(x1, y1, mark1, label=lab1)
    plt.plot(x2, y2, mark2, label=lab2)
    plt.plot(x3, y3, mark3, label=lab3)
    plt.xlabel(xlab, fontsize=18)
    plt.ylabel(ylab, fontsize=18)
    plt.legend()
    format_plot()
    plt.show()
