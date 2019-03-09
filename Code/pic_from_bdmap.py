import requests
import os
import xlrd
from PIL import Image


file = './Data/xy.xls'
# ak = 'ZHx52zV2G7k04Aw5L96yVmYVrdslaDHx'
ak = '7pYSUEk3LWVkzN7R9otSbi95VydZFvk2'

class Acqusition:
    def __init__(self, file, ak):
        pass

    def get_pic(self, file, ak):
        # 从xlf中location及id
        # 获取百度街景地图
        wb = xlrd.open_workbook(filename=file)
        sheet1 = wb.sheet_by_name('xy')

        for i in range(1, sheet1.nrows):
            lat = str(sheet1.cell_value(i, 2))
            lng = str(sheet1.cell_value(i, 3))
            fid = str(sheet1.cell_value(i, 0))

            location = lat + ',' + lng
            print(fid.zfill(6), location)
            url = "http://api.map.baidu.com/panorama/v2?ak=" + ak + "&width=1024&height=512&location=" + location + "&fov=180" + '&coordtype=wgs84ll'
            r = requests.get(url)

            root = './street//'
            if not os.path.exists(root):
                os.makedirs(root)

            m = fid.zfill(6) + ' ' + location + '.jpg'
            name = root + m
            with open(name, 'wb') as f:
                f.write(r.content)

class Check_again:
    def __init__(self):
        self.image_path = './street/'
        self.filenames = self.read_img()

    def is_valid_image(self, filename):
        valid = True
        try:
            Image.open(filename).load()
        except OSError:
            valid = False
        return valid

    def read_img(self):
        l=[]
        for image_name in os.listdir(self.image_path):
            if image_name.endswith(".jpg") & (self.is_valid_image(self.image_path+image_name) is not True):
                print(self.image_path+image_name)
                l.append(image_name)
        return l

    def get_pic(self):
        l = self.filenames
        for i in range(len(l)):
            # ak = 'ZHx52zV2G7k04Aw5L96yVmYVrdslaDHx'
            ak = '7pYSUEk3LWVkzN7R9otSbi95VydZFvk2'
            location = l[i][7:].split('.jpg')[0]
            fid = l[i][:6]
            print(fid.zfill(6), location)
            url = "http://api.map.baidu.com/panorama/v2?ak=" + ak + "&width=1024&height=512&location=" + location + "&fov=180" + '&coordtype=wgs84ll'
            r = requests.get(url)

            root = './street//'
            if not os.path.exists(root):
                os.makedirs(root)
            m = fid.zfill(6) + ' ' + location + '.jpg'
            name = root + m
            with open(name, 'wb') as f:
                f.write(r.content)

if __name__ == 'main':
    c = Acqusition()
    c.get_pic(file, ak)

    c_2 = Check_again()
    c.get_pic()


