import matplotlib.pyplot as plt
import matplotlib.animation as animation

def live_line_chart(data, title="Live Line Chart", xlabel="X Axis", ylabel="Y Axis", color='blue'):
    fig, ax = plt.subplots()
    line, = ax.plot(data, color=color)

    def update(new_data):
        line.set_ydata(new_data)
        ax.relim()
        ax.autoscale_view()
        plt.draw()

    ani = animation.FuncAnimation(fig, update, frames=[data], repeat=False)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    return ani

def live_bar_chart(data, title="Live Bar Chart", xlabel="Category", ylabel="Value", color='blue'):
    fig, ax = plt.subplots()
    bars = ax.bar(data.keys(), data.values(), color=color)

    def update(new_data):
        for bar, new_height in zip(bars, new_data.values()):
            bar.set_height(new_height)
        ax.relim()
        ax.autoscale_view()
        plt.draw()

    ani = animation.FuncAnimation(fig, update, frames=[data], repeat=False)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    return ani
