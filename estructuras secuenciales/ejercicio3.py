segundos=int(input("ingrese segundos"))
dia = segundos // 86400

horas = (segundos % 86400)//3600

minutos = ((segundos % 86400)%3600)// 60

segundo = ((segundos % 86400)%3600)% 60

print(segundos, "segundos equivalen a", dia, "días,", horas, "horas,", minutos, "minutos y", segundo, "segundos.")



