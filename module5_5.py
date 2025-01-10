
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.age = int(age)
        self.password = hash(str(password))
    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode = False, time_now = 0):
        self.title = str(title)
        self.duration = int(duration)
        self.adult_mode = bool(adult_mode)
        self.time_now = int(time_now)

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):# анализ экземпляров в списке перебором.
        # Другого способа не придумал.
        flag = 0 # маркер обнаружения nickname в экземпляре списка.
        for j in self.users:
            if nickname in j.nickname:
                flag = 1
                print(f'Пользователь {nickname} уже существует')
                break
        if flag == 0:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            # print(f'{nickname}, Поздравляем с успешной регистрацией.')

    def log_in(self, nickname, password):
        flag1 = 0  # маркер обнаружения nickname в экземпляре списка.
        for j in self.users:
            if nickname in j.nickname:
                flag1 = 1
                if hash(str(password)) == j.password:
                    print(f'{nickname}, добро пожаловать')
                    self.current_user = nickname
                    break
                else:
                    print('Неверный пароль')
        if flag1 == 0:
            print("Пользователь не существует")

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for k in args:
            if type(k) is Video:
                flag2 = 0  # маркер обнаружения title в экземпляре списка.
                for j in self.videos:
                    if k.title in j.title:
                        # print(f'Видео с названием "{k.title}" уже загружено')
                        flag2 = 1
                        break
                if flag2 == 0:
                    self.videos.append(k)
                    # print(f'"{k.title}" успешно загружено.')

    def get_videos(self, text):
        low_text = (str(text)).lower()
        list = []
        for j in self.videos:
            if low_text in j.title.lower():
                list.append(j.title)
        return list

    def watch_video(self, search):
        if self.current_user:
            for i in self.videos:
                if i.title.__contains__(search):
                    if self.current_user.age > 17:
                        for k in range(i.duration):
                            i.time_now = k + 1
                            sleep(1)
                            print(i.time_now)# Секунды выводятся вертикально, надеюсь это не ошибка.
                        i.time_now = 0
                        print('Конец просмотра')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")



ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)



# Добавление видео

ur.add(v1, v2)



# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))



# Проверка на вход пользователя и возрастное ограничение

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

