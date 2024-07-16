import unittest

import time_series_visualizer as tsv

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.line_plot = tsv.draw_line_plot()
        self.bar_plot = tsv.draw_bar_plot()
        self.box_plot = tsv.draw_box_plot()

    def test_line_plot(self):
        self.assertEqual(self.line_plot.axes[0].get_title(), "Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    def test_bar_plot(self):
        self.assertEqual(self.bar_plot.axes[0].get_title(), "Monthly Average Page Views per Year")

    def test_box_plot(self):
        self.assertEqual(self.box_plot.axes[0].get_title(), "Year-wise Box Plot (Trend)")
        self.assertEqual(self.box_plot.axes[1].get_title(), "Month-wise Box Plot (Seasonality)")

if __name__ == "__main__":
    unittest.main()
