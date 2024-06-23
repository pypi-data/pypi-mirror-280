import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def live_line_chart(data, title="Live Line Chart", xlabel="X Axis", ylabel="Y Axis", color='blue'):
    fig, ax = plt.subplots()
    line, = ax.plot(data, color=color)
    
    def update(frame):
        new_data = data[-1] + np.random.randn()  # Simulating new data point
        data.append(new_data)
        line.set_ydata(data)
        ax.set_xlim(0, len(data) - 1)
        ax.relim()
        ax.autoscale_view()
        return line,

    ani = animation.FuncAnimation(fig, update, frames=range(100), blit=True, interval=200)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    return ani

def live_bar_chart(data, title="Live Bar Chart", xlabel="Category", ylabel="Value", color='blue'):
    fig, ax = plt.subplots()
    bars = ax.bar(data.keys(), data.values(), color=color)

    def update(frame):
        new_data = {k: v + np.random.randn() for k, v in data.items()}  # Simulating new data point
        for bar, new_height in zip(bars, new_data.values()):
            bar.set_height(new_height)
        ax.relim()
        ax.autoscale_view()
        return bars

    ani = animation.FuncAnimation(fig, update, frames=range(100), blit=True, interval=200)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    return ani
