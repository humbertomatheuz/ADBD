import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
from data_handler import DataHandler
from plotter import Plotter

class SpreadsheetApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Spreadsheet Viewer and Plotter")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        self.spreadsheet_frame = ttk.Frame(self.notebook)
        self.plot_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.spreadsheet_frame, text="Spreadsheet")
        self.notebook.add(self.plot_frame, text="Plot")

        self.data_handler = DataHandler()
        self.plotter = Plotter(self.plot_frame)

        self.create_widgets()

    def create_widgets(self):
        self.upload_button = ttk.Button(self.spreadsheet_frame, text="Upload Spreadsheet", command=self.upload_file)
        self.upload_button.pack(pady=10)

        self.treeview = ttk.Treeview(self.spreadsheet_frame)
        self.treeview.pack(fill='both', expand=True)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            df = self.data_handler.load_data(file_path)
            self.display_data(df)
            self.plotter.plot_data(df)

    def display_data(self, df):
        self.treeview.delete(*self.treeview.get_children())
        self.treeview["column"] = list(df.columns)
        self.treeview["show"] = "headings"
        for column in self.treeview["columns"]:
            self.treeview.heading(column, text=column)
        for row in df.itertuples(index=False):
            self.treeview.insert("", "end", values=row)
