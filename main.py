'''
Author: zhangchao
Date: 2022-05-25 23:10:50
LastEditors: zhangchao
LastEditTime: 2022-05-26 18:18:45
Description: file content
'''


import wx
import time
from send2trash import send2trash

# pip3 config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple
# pip3 install wxPytho
# pip3 install send2trash



class MyPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.fileDrop = FileDrop(self)
        self.SetDropTarget(self.fileDrop)
        # 隐藏顶部菜单


        
        try:
            image_file = '0.png'
            # 图片居中
            self.bitmap = wx.StaticBitmap(self, -1, wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap(), (0, 0))
          
            to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            to_bmp_image = to_bmp_image.ConvertToImage()
            # to_bmp_image SetToolTip
           

            # 设置图片为150 自适应
            to_bmp_image = to_bmp_image.Scale(130,130)
           

            to_bmp_image = to_bmp_image.ConvertToBitmap()
            

        
            self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (130, 0))
           
        
            parent.SetTitle("猫猫回收站")
        except IOError:
            print ('Image file %s not found' % image_file)
      
    def ChangeBackgroundPicture(self, image_file = '1.png'):
        # print(image_file)
        to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        to_bmp_image = to_bmp_image.ConvertToImage()
        # 设置图片为150 自适应
        to_bmp_image = to_bmp_image.Scale(130, 130)
        to_bmp_image = to_bmp_image.ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (130, 0))
        self.Refresh()
        self.Update()
        time.sleep(0.02)
       
class FileDrop(wx.FileDropTarget):
    def __init__(self,win):
        wx.FileDropTarget.__init__(self)
        self.win = win
    def OnDropFiles(self,x,y,filenames):
       
       
        print(x,y,filenames)  
        
        for filename in filenames:
            self.win.ChangeBackgroundPicture()
            print(filename)
            # 回收站
            send2trash(filename)
            self.win.ChangeBackgroundPicture('0.png')
      
        return True
       
        
  
if __name__ == '__main__':
   
   
    app = wx.App()
    frame = wx.Frame(None, -1, '猫猫回收站',size = (280, 150))  
  
    frame.SetIcon(wx.Icon('icon.ico', wx.BITMAP_TYPE_ICO))
    # 禁止窗口缩放
    frame.Maximize(False)
    frame.SetMaxSize((280, 150))
    frame.SetMinSize((280, 150))
   
    my_panel = MyPanel(frame, -1) 
    frame.Show()
    app.MainLoop()
   