import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Plotter:
    def __init__(self, parent):
        self.parent = parent

    def plot_data(self, df):
        fig, ax = plt.subplots()
        df.plot(ax=ax)
        canvas = FigureCanvasTkAgg(fig, master=self.parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
