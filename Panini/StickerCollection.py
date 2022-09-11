from Panini import Pack

class StickerCollection:

    def __init__(self, size, stickers_requestable, pack_size, already_owned):
        self.__size = size
        self.collection = [0] * (size-already_owned) + [1] * already_owned
        self.stickers = already_owned
        self.__threshold = size - stickers_requestable
        self.__pack_size = pack_size

    def packs_till_complete(self):
        packs = 0
        while self.stickers < self.__threshold:
            self.add_pack()
            packs += 1
        return packs

    def add_pack(self):
        new_pack = Pack.Pack(self.__pack_size, self.__size)
        for i in new_pack.contents():
            self.collection[i] += 1
            if self.collection[i] == 1:
                self.stickers += 1

class SpecificSticker:

    def __init__(self, size, pack_size):
        self.__size = size
        self.collection = [0] * size
        self.stickers = 0
        self.__sticker = 10
        self.__pack_size = pack_size
        self.found=False

    def packs_till_complete(self):
        packs = 0
        while not self.collection[self.__sticker]:
            self.add_pack()
            packs += 1
        return packs

    def add_pack(self):
        new_pack = Pack.Pack(self.__pack_size, self.__size)
        for i in new_pack.contents():
            self.collection[i] += 1
            if self.collection[i] == 1:
                self.stickers += 1
