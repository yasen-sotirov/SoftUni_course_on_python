from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__init_photos(pages)

    def __init_photos(self, pages):
        result = []
        for _ in range(pages):
            result.append([])
        return result           # или return [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for idx, current_page in enumerate(self.photos):
            if len(current_page) < PhotoAlbum.PHOTOS_PER_PAGE:
                current_page.append(label)
                return f"{label} photo added successfully on page {idx +  1} slot {len(current_page)}"
        return "No more free slots"

    def display(self):
        separator = '-' * 11
        result = separator + '\n'
        for page in self.photos:
            result += ' '.join(['[]' for _ in page]) + '\n'
            result += separator + '\n'
        return result.strip()


photo_album_1 = PhotoAlbum.from_photos_count(9)
print(photo_album_1.add_photo('my 1 game'))
print(photo_album_1.add_photo('my 2 game'))
print(photo_album_1.add_photo('my 3 game'))
print(photo_album_1.add_photo('my 4 game'))
print(photo_album_1.add_photo('my 5 game'))
print(photo_album_1.display())


