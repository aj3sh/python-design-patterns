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
        self.__current_index = 0
        self.__songs = songs
        super().__init__()

    @property
    def length(self):
        if not hasattr(self, '__song_length'):
            self.__song_length = len(self.__songs)
        return self.__song_length

    def add_song(self, song: Song):
        self.__songs.append(song)

    def next(self):
        self.__current_index += 1
        return self.__songs[self.__current_index - 1]

    def has_next(self):
        return self.__current_index < self.length

class Album:
    def __init__(self, songs):
        self.__songs = songs
        super().__init__()

    def get_songs(self) -> SongList:
        return SongList(self.__songs)

def print_songs(songs: Iterator):
    while songs.has_next():
        song = songs.next()
        print(song)

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