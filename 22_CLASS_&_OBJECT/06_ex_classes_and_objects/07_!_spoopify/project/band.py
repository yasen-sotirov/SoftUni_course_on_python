from project.album import Album
from project.song import Song


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):      # албума ми го подават на конзолата и го взимам от класа
        if album in self.albums:
            return f"Band {self.name} already has {album} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for el in self.albums:
            if el.name == album_name:
                if el.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album)
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}"
        for el in self.albums:
            result += '\n' + el.details()
        return result


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())


# def add_album(self, album: Album):  # албума ми го подават на конзолата и го взимам от класа
#     if album in self.albums:
#         return f"Band {self.name} already has {album} in their library."
#
#     self.albums.append(album)
#     return f"Band {self.name} has added their newest album {album.album_name}."
#
#
# def remove_album(self, album_name):
#     for el in self.albums:
#         if el.album_name == album_name:
#             if el.published:
#                 return "Album has been published. It cannot be removed."
#             self.albums.remove(album)
#     return f"Album {album_name} is not found."
#
#
# def details(self):
#     result = f"Band {self.name}\n"
#     for el in self.albums:
#         result += el.details()
#     return result




