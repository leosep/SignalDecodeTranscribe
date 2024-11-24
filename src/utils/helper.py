# Example helper function to plot a signal
import matplotlib.pyplot as plt

def plot_signal(signal, title="Signal"):
    plt.plot(signal[:1000])  # Plot first 1000 samples
    plt.title(title)
    plt.show()
