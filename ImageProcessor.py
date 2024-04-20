import os
from PyQt5.QtCore import Qt # нужна константа Qt.KeepAspectRatio для изменения размеров с сохранением пропорций
from PyQt5.QtGui import QPixmap # оптимизированная для показа на экране картинка
from PIL import Image

class imageProcessor():
    def __init__(self): #конструктор
        self.image = None 
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/" #название пути 

    def loadImage(self, filename, workdir):
        self.dir = workdir
        self.filename = filename #название имени файла, для использования в классе
        image_path = os.path.join(workdir, filename) #переменная для обьединения пути получения и имени файла
        self.image = Image.open(image_path) #переменная для класса, в которую добавляем полученное изоюражение (для PIL)

    def showImage(self, path, image):
        self.imageVisible = image
        self.imageVisible.hide()
        pixmapimage = QPixmap(path) #переменная для хранения пути, как пердмета модуля  QPixmap
        w, h = self.imageVisible.width(),self.imageVisible.height() #данные о параметрах загружаемой фотографии
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio) #сохранение отмасштабированного изображения
        self.imageVisible.setPixmap(pixmapimage) #присваивает image отмасщтабированную картинку (pixmapimage)
        self.imageVisible.show() #отображает отмасштабированную картинку  image

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path,  self.imageVisible)


    def saveImage(self):
        ''' сохраняет копию файла в подпапке '''
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
