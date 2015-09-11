from graphics_field_item_class import *

class AnimalGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    """This class provides a pixmap item with a preset image for the animal"""
    #constructor
    def __init__(self, graphics_list):
        super().__init__(graphics_list)

        self.crop = None

    def update_status(self):
        if self.animal._status == "Baby":
            self.setPixmap(QPixmap(self.available_graphics[0]).scaledToWidth(25, 1))
        elif self.animal._status == "Young":
            self.setPixmap(QPixmap(self.available_graphics[1]).scaledToWidth(25, 1))
        elif self.animal_status == "Mature":
            self.setPixmap(QPixmap(self.available_graphics[2]).scaledToWidth(25, 1))
        elif self.animal_status == "Adult":
            self.setPixmap(QPixmap(self.available_graphics[3]).scaledToWidth(25, 1))
        elif self.animal._status == "Old":
            self.setPixmap(QPixmap(self.available_graphics[4]).scaledToWidth(25, 1))
            
