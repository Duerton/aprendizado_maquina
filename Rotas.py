import pandas as pd
import datetime as dt
import calendar
from datetime import timedelta


def main(file):
    init_date = file['DataIni'].to_numpy()
    init_hour = file['HoraIni'].to_numpy()
    finish_date = file['DataFim'].to_numpy()
    finish_hour = file['HoraFim'].to_numpy()
    duracao = file['DuraçãoViagem'].to_numpy()
    converted_init_date = convert_date(init_date)
    converted_init_hour = convert_hour(init_hour)
    converted_finish_date = convert_date(finish_date)
    converted_finish_hour = convert_hour(finish_hour)
    converted_duracao = convert_hour(duracao)
    new_init_hour = []
    new_finish_hour = []
    new_duracao = []
    timestamp = []
    week_day = []
    classificatory_duration = []
    count = -1
    for item in converted_init_date:
        count = count + 1
        new_init_time = converted_init_hour[count].time()
        temp = dt.datetime.combine(item.date(), new_init_time)
        week_day.append(calendar.day_name[item.weekday()])
        timestamp.append(round(temp.timestamp()))
        new_init_hour.append(new_init_time)
        new_finish_time = converted_finish_hour[count].time()
        new_finish_hour.append(new_finish_time)
        temp_duracao = converted_duracao[count].time()

        t1 = dt.datetime.strptime('00:23:00', "%H:%M:%S")
        t2 = dt.datetime.strptime('00:59:00', "%H:%M:%S")
        if converted_duracao[count].time() < t1.time():
            classificatory_duration.append('Abaixo do esperado')
        elif converted_duracao[count].time() > t2.time():
            classificatory_duration.append('Acima do esperado')
        else:
            classificatory_duration.append('Esperado')
        new_duracao.append(temp_duracao)

    file['timestamp'] = timestamp
    file['Data_inicio'] = converted_init_date
    file['Hora_inicio'] = new_init_hour
    file['Data_fim'] = converted_finish_date
    file['Hora_fim'] = new_finish_hour
    file['Dia_semana'] = week_day
    file['DuracaoViagem'] = new_duracao
    file['Classificação'] = classificatory_duration

    return file


def convert_date(date_in):
    date_format = '%Y-%m-%d'
    return list(map(lambda x: dt.datetime.strptime(x.split(' ')[0], date_format), date_in))


def convert_hour(hour_in):
    hour_format = '%H:%M:%S'
    return list(map(lambda x: dt.datetime.strptime(x.split(' ')[1], hour_format), hour_in))


file1 = pd.read_csv('~/Documents/Estudos/sample/Jan2019.csv')
file2 = pd.read_csv('~/Documents/Estudos/sample/Fev2019.csv')
file3 = pd.read_csv('~/Documents/Estudos/sample/Mar2019.csv')
file4 = pd.read_csv('~/Documents/Estudos/sample/Abr2019.csv')
file5 = pd.read_csv('~/Documents/Estudos/sample/Mai2019.csv')
file6 = pd.read_csv('~/Documents/Estudos/sample/Jun2019.csv')
file7 = pd.read_csv('~/Documents/Estudos/sample/Jul2019.csv')
file8 = pd.read_csv('~/Documents/Estudos/sample/Ago2019.csv')
file9 = pd.read_csv('~/Documents/Estudos/sample/Set2019.csv')
file10 = pd.read_csv('~/Documents/Estudos/sample/Out2019.csv')
file11 = pd.read_csv('~/Documents/Estudos/sample/Nov2019.csv')
file12 = pd.read_csv('~/Documents/Estudos/sample/Dez2019.csv')
#
new_file1 = main(file1)
new_file2 = main(file2)
new_file3 = main(file3)
new_file4 = main(file4)
new_file5 = main(file5)
new_file6 = main(file6)
new_file7 = main(file7)
new_file8 = main(file8)
new_file9 = main(file9)
new_file10 = main(file10)
new_file11 = main(file11)
new_file12 = main(file12)

frames = [new_file1, new_file2, new_file3, new_file4, new_file5, new_file6, new_file7, new_file8, new_file9,
          new_file10, new_file11, new_file12]
rotas = pd.concat(frames)
rotas[(rotas.KmPerc == 16.308) & (rotas.DuracaoViagem >= dt.datetime.strptime('00:10:00', "%H:%M:%S").time())]\
    .to_csv('~/Documents/Estudos/Rota100-v2.csv')

