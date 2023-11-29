'''Мы пишем приложение для удобного прослушивания музыки. У Вани есть список из
девяти песен группы Depeche Mode. Каждая песня состоит из названия и 
продолжительности с точностью до долей минут.Из этого списка Ваня хочет выбрать
N песен и закинуть их в особый плейлист с другими треками. При этом ему важно, 
сколько времени в сумме эти N песен будут звучать. Напишите программу, которая
запрашивает у пользователя количество песен из списка и затем названия этих 
есен, а на экран выводит общее время их звучания.'''

violator_songs = [
['World in My Eyes', 4.86],
['Sweetest Perfection', 4.43],
['Personal Jesus', 4.56],
['Halo', 4.9],
['Waiting for the Night', 6.07],
['Enjoy the Silence', 4.20],
['Policy of Truth', 4.76],
['Blue Dress', 4.29],
['Clean', 5.83]
]

playlist_time = 0
songs_number = int(input('Сколько песен выбрать? '))

for song in range(songs_number):
    song_name = input(f'Название {song + 1}-й песни: ')
    for title in violator_songs:
        if title[0] == song_name:
            playlist_time += title[1]
        
print(f'\nОбщее время звучания песен: {round(playlist_time, 2)}')