import matplotlib
import numpy
from matplotlib.backends.backend_wxagg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import wx
import pandas as pd
import io

def plot(df):
    features = ['Mean', 'Median', 'Mode', 'Kurtosis', 'Skewness', 'Standard Deviation',
       'Variance', 'Standard Error', 'Max', 'Min', 'Sum', 'Range',
       '2nd Quartile', 'RMS', 'Shape Factor', 'Impulse Factor',
       'K Factor']
        
    conditions = df.Condition.unique() 
    fig, ax = plt.subplots(5,4)
    fig.set_size_inches(30,30)
    for i in range(17):
        feat = features[i]
        for j in conditions:
            C = df[df['Condition'] == j]
            ax[i%5, int((i - i%5)/5)].scatter(C[feat].index, C[feat])
            ax[i%5, int((i - i%5)/5)].title.set_text(feat)
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)


EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'

class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        if data is None:
            data = pd.DataFrame()
        self.data = data

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data.columns) + 1

    def GetValue(self, row, col):
        if col == 0:
            return self.data.index[row]
        return self.data.iloc[row, col - 1]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col - 1] = value

    def GetColLabelValue(self, col):
        if col == 0:
            if self.data.index.name is None:
                return 'Index'
            else:
                return self.data.index.name
        return str(self.data.columns[col - 1])

    def GetTypeName(self, row, col):
        return wx.grid.GRID_VALUE_STRING

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr


class p1(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, (100,100), wx.TAB_TRAVERSAL)

        self.figure = matplotlib.figure.Figure()
        self.axes = self.figure.add_subplot(111)
        t = numpy.arange(0.0,10,1.0)
        s = [0,1,0,1,0,2,1,2,1,0]
        self.y_max = 10
        self.axes.plot(t,s)
        self.canvas = FigureCanvas(self.figure)