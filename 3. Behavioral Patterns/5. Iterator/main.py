import abc


class Iterator(metaclass=abc.ABCMeta):
    def next(self):
        raise NotImplementedError('next method is not implemented.')

    def has_next(self):
        raise NotImplementedError('has_next method is not implemented.')


class Song:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class SongList(Iterator):
    def __init__(self, songs=[]):
        self.__songs = songs
        super().__init__()

    def add_song(self, song: Song):
        pass

    def next(self):
        pass

    def has_next(self):
        pass

class Album:
    def __init__(self, songs):
        self.__songs = []
        super().__init__()

    def get_songs(self) -> SongList:
        pass

def print_songs(songs: Iterator):
    pass

def main():
    songs = SongList(songs=[
        'Song 1',
        'Song 2',
        'Song 3',
    ])

    album = Album(songs=[
        'Album Song 1',
        'Album Song 2',
        'Album Song 3',
    ])

    print_songs(songs)
    print_songs(album.get_songs())
    

if __name__ == '__main__':
    main()