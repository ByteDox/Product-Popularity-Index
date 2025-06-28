"""
Title: Product Popularity Index (PPI)
Date: 19/03/25
"""
from tkinter import *

W1 = 0.0005
W2 = 0.06
W3 = 0.0004

# First Calculations
def calculate_ppi(sales_volume, prod_rating, num_review):
    return (sales_volume * W1) +  (prod_rating * W2) + (num_review * W3)

def classify_ppi(ppi):
    if ppi <= 0.3:
        return 'low'
    elif ppi >= 0.3 and ppi <= 0.5:
        return 'moderate'
    elif ppi >= 0.5 and ppi <= 0.8:
        return 'medium'
    elif ppi >= 0.8:
        return 'top seller'
    return ppi

class ProductPopularity(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Product Popularity Index')
        self.grid()

        # Variables
        self.sales_volume = DoubleVar()
        self.prod_rating = DoubleVar()
        self.num_review = DoubleVar()
        self.ppi = StringVar()
        self.prod_popularity = StringVar()


        # Layout

        # Sales Volume -- Label, Entry and Grid
        sales_label = Label(self, text = 'Sales Volume: ')
        sales_label.grid(row = 0, column = 0, sticky = W)
        sales_entry = Entry(self, textvariable = self.sales_volume)
        sales_entry.grid(row = 0, column = 1, sticky = W)


        # Product Rating -- Label, Entry and Grid
        prod_label = Label(self, text = 'Product Rating: ')
        prod_label.grid(row = 1, column = 0, sticky = W)
        prod_entry = Entry(self, textvariable = self.prod_rating)
        prod_entry.grid(row = 1, column = 1, sticky = W)

        # Number of Reviews -- Label, Entry and Grid
        num_label = Label(self, text = 'Number of Reviews: ')
        num_label.grid(row = 2, column = 0, sticky = W)
        num_entry = Entry(self, textvariable = self.num_review)
        num_entry.grid(row = 2, column = 1, sticky = W)

        # results -- Label and Grid
        ppi_label = Label(self, textvariable = self.ppi)
        ppi_label.grid(row = 5, column = 0, sticky = W)

        prod_pop_label = Label(self, textvariable = self.prod_popularity)
        prod_pop_label.grid(row = 6, column = 0, sticky = W)

        # Buttons -- Display and Clear
        display_btn = Button(self, text = 'Display', command = self.calculate)
        display_btn.grid(row = 3, column = 0, sticky = W)

        clear_btn = Button(self, text = 'Clear', command = self.clear)
        clear_btn.grid(row = 3, column = 1, sticky = W)

    # Final Calculations
    def calculate(self):
        sales = self.sales_volume.get()
        rating = self.prod_rating.get()
        review = self.num_review.get()

        display = calculate_ppi(sales, rating, review)
        self.ppi.set(f'PPI: {display:.3f}')

        classify = classify_ppi(display)
        self.prod_popularity.set(f'Product Popularity: {classify}')

    def clear(self):
        self.sales_volume.set(0.0)
        self.prod_rating.set(0.0)
        self.num_review.set(0.0)
        self.ppi.set("")
        self.prod_popularity.set("")



if __name__ == "__main__":
    ProductPopularity().mainloop()





