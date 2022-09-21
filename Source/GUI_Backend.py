
import wx
import pandas as pd
import os 
import matplotlib.pyplot as plt
import GUI_Frontend
import Display_Utils
import io


class BackFrame(GUI_Frontend.FirstFrame):
    def __init__(self,parent): 
        GUI_Frontend.FirstFrame.__init__(self,parent)
        self.df = None
        self.Conditions = self.df.Condition.unique()
        F_list = self.df.columns
        self.Features = F_list[:len(F_list)-1] 
        
        self.MinMax = None
        self.Superlo = None
        self.Superhi = None
        self.ndf = None
       
        


    def FilePick(self, event):
        dlg = wx.FileDialog(self, message="Choose file",\
                        wildcard = "", style=wx.FD_OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            TrainFile = dlg.GetDirectory()+'\\'+dlg.GetFilename()
            TrainFile = TrainFile.replace(os.sep, '/')
            self.TrainImporter(TrainFile)

        dlg.Destroy()
    
    def TrainImporter(self, filename):
        self.df = pd.read_csv(filename, index_col= 0)
        self.Conditions = self.df.Condition.unique()
        F_list = self.df.columns
        self.Features = F_list[:len(F_list)-1] 
    
    def DisplayDF(self, event):
        table = Display_Utils.DataTable(self.df)
        self.DataGrid.SetTable(table, takeOwnership=True)
        self.DataGrid.AutoSizeColumns()

    def FilterMake(self, event):
        Meanlist = []
        for i in self.Conditions:
            tdf = self.df[self.df['Condition'] == i]
            Meanlist.append(tdf[self.Features].mean())
        meandf = pd.DataFrame(Meanlist)

        stdlist = []
        for i in self.Conditions:
            tdf = self.df[self.df['Condition'] == i]
            stdlist.append(tdf[self.Features].std())
        stdf = pd.DataFrame(stdlist)

        span = float(self.Span.GetValue())

        lo_frame = meandf - span*stdf
        self.Superlo = lo_frame.min()

        hi_frame = meandf + span*stdf 
        self.Superhi = hi_frame.max()
        
        self.MinMax = pd.DataFrame([self.Superlo, self.Superhi])

        
        self.ndf = self.df[self.df[self.Features] >= self.MinMax.iloc[0]]

        self.ndf = self.ndf[self.ndf[self.Features] <= self.MinMax.iloc[1]]
        self.ndf.Condition = self.df.Condition
        self.ndf = self.ndf.dropna()
        
    def FilterShow(self, event):
        table = Display_Utils.DataTable(self.ndf)
        self.DataGrid.SetTable(table, takeOwnership=True)
        self.DataGrid.AutoSizeColumns()

    def Plotter(self, df):
        DPI = self.GetDPI()[0] 
        fig, ax = plt.subplots(6,3)
        
        fig.set_size_inches(self.Plot.Size[0]/DPI, self.Plot.Size[1]/DPI)
        # f_list = list(self.Features)
        # f_list.remove('Count')


        for i in range(17):
            #feat = f_list[i]
            feat = self.Features[i]
           
            for j in self.Conditions:
                C = df[df['Condition'] == j]
                # lene = range(len(C[feat].index))
                # print(C[feat])
                ax[i%6, int((i - i%6)/6)].scatter(C[feat].index, C[feat])
                ax[i%6, int((i - i%6)/6)].title.set_text(feat)
        fig.tight_layout()
        buf = io.BytesIO()
        fig.savefig(buf,format='jpg', dpi = DPI)
        buf.seek(0)

        self.Image = wx.Image(buf, wx.BITMAP_TYPE_ANY, index = -1)
        self.Image = wx.StaticBitmap(self.Plot, wx.ID_ANY, wx.Bitmap(self.Image))
        
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.Image,1,wx.ALIGN_CENTRE)
        self.SetSizer(self.sizer)

    def OGPlotShow(self, event):
        self.Plotter(self.df)

    def FilterPlotShow(self, event):
        self.Plotter(self.ndf)




app = wx.App(redirect= False)
frame = BackFrame(None)
frame.Show()
frame.Maximize()
app.MainLoop()
