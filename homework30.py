# Գրել MyShows class, որը․
#    - __init__ ում կստանա 
#      -- սերիալի անունը (պետք է լինի տեքստ), 
#      -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ), 
#      -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
#      -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
#      -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
#      -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
#    - բոլոր ատրիբուտները կլինեն private,
#    - կունենա getter բոլոր ատրիբուտների համար,
#    - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
#    - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
#    - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
#    - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան

class MyShows:
    def __init__(self, series_name: str, platform: str, first_episode_year: int, 
                 serial_number: int = 1, series_mark: int = None, actors: list = []):
        self.__series_name = series_name
        self.__platform = platform
        self.__first_episode_year = first_episode_year
        self.__serial_number = serial_number
        self.__series_mark = series_mark
        self.__actors = actors

    @property
    def series_name(self):
        return self.__series_name

    @property
    def platform(self):
        return self.__platform

    @property
    def first_episode_year(self):
        return self.__first_episode_year

    @property
    def serial_number(self):
        return self.__serial_number

    @serial_number.setter
    def serial_number(self, serial_number: int):
        self.__serial_number = serial_number

    @property
    def series_mark(self):
        return self.__series_mark

    @series_mark.setter
    def series_mark(self, series_mark: int):
        if series_mark is None or (series_mark >= 1 and series_mark <= 10):
            self.__series_mark = series_mark
        else:
            print("Invalid user mark")

    @series_mark.deleter
    def series_mark(self):
        del self.__series_mark

    def update_actors(self, update: True, actor_name: str):
        if update == True:
            self.__actors.append(actor_name)
        ....................??????????

    def get_series_info(self):
        return {
            self.__series_name,
            self.__platform,
            self.__first_episode_year,
            self.__serial_number,
            self.__series_mark,
            self.__actors
        }




my_show = MyShows("SerialiAnun", "Netflix", 2024, actors=["Derasan1", "Derasan2"])

print(my_show.series_name)   
print(my_show.platform)
print(my_show.first_episode_year)
print(my_show.serial_number)
my_show.serial_number = 15
my_show.series_mark = 10
