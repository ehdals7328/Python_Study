# 이 함수는 enumerate 기능을 확인하는 코드임
class PlayList():
    def __init__(self):
        self.songs = ['song1', 'song2', 'song3']

    def add_song(self, title):
        if title in self.songs:
            return False
        else:
            self.songs.append(title)
            return True

    def show_song(self):
        if not self.songs:
            print("플레이리스트가 비어있습니다")
            return
        for idx, song in enumerate(self.songs, start=1):
            print(f"{idx}.{song}")