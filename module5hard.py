import time

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return f'{self.nickname}'


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now  # секунда остановки
        self.adult_mode = adult_mode  # огрничение по возрасту

    def __str__(self):
        return f'Видео: {self.title}, продолжительность: {self.duration} сек. '


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        self.reg = 0

    def log_in(self, login, password):
        for i in range(len(self.users)):
            if login == self.users[i].nickname:
                if password == self.users[i].password:
                    self.current_user = self.users[i]
                    return self.current_user

    def register(self, nickname, password, age):
        for i in range(len(self.users)):
            if nickname == self.users[i].nickname:
                print (f'Пользователь {nickname} уже существует')
                self.log_in(nickname, password)
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for j in range(len(video)):
            for i in range(len(self.videos)):
                if video[j].title == self.videos[i].title:
                    break
            else:
                self.videos.append(video[j])

    def get_videos(self, word):
        a = []
        for i in range(len(self.videos)):
            if word.lower() in self.videos[i].title.lower():
                a.append(self.videos[i].title)
        return a

    def watch_video(self, film):
        if self.current_user != None and self.current_user.age > 17:
            for i in range(len(self.videos)):
                if film == str(self.videos[i].title):
                    j = 1
                    while j <= int(self.videos[i].duration):
                        print(j)
                        time.sleep(1)
                        j += 1
                    print('Конец видео')
        else:
            if self.current_user == None:
                print('Ввойдите в аккаунт, чтобы смотреть видео')
            else:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10) #, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


