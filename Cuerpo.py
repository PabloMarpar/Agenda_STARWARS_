# Import requirements
import os
import pandas as pd
import warnings


# Agenda
ala_x = r"""
   __                                                      
.-.__      \ .-.  ___  __
|_|  '--.-.-(   \/\;;\_\.-._______.-.
(-)___     \ \ .-\ \;;\(   \       \ \
 Y    '---._\_((Q)) \;;\\ .-\     __(_)
 I           __'-' / .--.((Q))---'    \,                                      
 A  .-'      \ .-.\   \   \ \ '--.__     '\                        /\:::::/\            /\:::::/\
 |  |____.----((Q))\   \__|--\_      \     '                      /::\:::/::\          /==\:::/::\
    ( )        '-'  \_  :  \-' '--.___\                          /::::\_/::::\   .--. /====\_/::::\
     Y                \  \  \       \(_)                        /_____/ \_____\-' .-.`-----' \_____\
     I                 \  \  \         \,                       \:::::\_/:::::/-. `-'.-----._/:::::/
     I                  \  \  \          \                       \::::/:\::::/   `--' \::::/:\::::/
     A                   \  \  \          '\                      \::/:::\::/          \::/:::\::/    
     |                    \  \__|           '                      \/:::::\/            \/:::::\/     
                           \_:.  \
                              \ \  \
                               \ \  \
                                \_\_|

"""
# Pandas esta cambiando append por concat y printea un error siempre, y concat no me funciona
# asique quito los warnings
warnings.filterwarnings('ignore')
print(ala_x)

print("Haga clic en el siguiente enlace si quiere banda sonora")
url = "https://www.youtube.com/watch?v=SwE0UYtJogw"
print(f'{url}')


class Fuerza():
    def __init__(self, poder_j, rango_j, nombre):
        self.poder_j = poder_j
        self.rango_j = rango_j
        self.nombre = nombre


class LadoOscuro():
    def __init__(self, poder_s, rango_s, nombre):
        self.poder_s = poder_s
        self.rango_s = rango_s
        self.nombre = nombre


# En mi diseño todas las funciones están en la agenda y es el menu quien hereda de agenda
class agenda(Fuerza, LadoOscuro):
    def __init__(self):
        # Creo un dataframe para fuerza y ladoOscuro
        self.df_fuerza = pd.DataFrame(columns=['Poder', 'Rango', 'Nombre'])
        self.df_lado_oscuro = pd.DataFrame(columns=['Poder', 'Rango', 'Nombre'])
        # Con añadir podemos meter hasta 50 jedis y 50 siths

    def anadir_jedi(self):
        if len(self.df_fuerza) >= 50:
            print('No se pueden agregar más jedis.')
            return
        # Creo bucles para en cada caso, hacer el tratamiento de errores adecuado.
        while True:
            try:
                poder_j = int(input('Introduce el poder del jedi: '))
                break
            except ValueError:
                print('El poder del jedi está medido numéricamente, intentalo de nuevo.')
        while True:
            rango_j = input('Introduce el rango del jedi: padawan, caballero, maestro, gran maestro ').lower()
            if rango_j.isdigit():
                print('El rango del jedi no debe ser un número. Inténtalo de nuevo.')
            elif rango_j not in ['padawan', 'caballero jedi', 'caballero', 'maestro', 'maestro jedi',
                                 'gran maestro']:  # Itero sobre una lista con los tipos de rangos para asegurarme que no se introduce uno erroneo
                print('No es un rango válido, ingrese el rango de su jedi de nuevo.')
            else:
                break
        while True:
            nombre = input('Introduce el nombre del jedi: ').lower()
            if nombre.isdigit():
                print('El nombre no puede ser un número. Inténtelo de nuevo. ')
            elif nombre.lower() in self.df_fuerza['Nombre'].tolist() or nombre in self.df_lado_oscuro[
                'Nombre'].tolist():  # Busca en los dataframes si hay algún nombre igual que el recibido
                print('Ya hay un jedi o sith con ese nombre. Inténtelo de nuevo. ')
            else:
                break
        # Meto los datos recopilados en el dataframe de fuerza
        jedi = Fuerza(poder_j=poder_j, rango_j=rango_j, nombre=nombre)
        self.df_fuerza = self.df_fuerza.append({'Poder': jedi.poder_j, 'Rango': jedi.rango_j, 'Nombre': jedi.nombre},
                                               ignore_index=True)
        print('Su jedi se ha añadido a la agenda')

    def anadir_sith(self):
        if len(self.df_lado_oscuro) >= 50:
            print('No se pueden agregar más sith.')
            return
        while True:
            try:
                poder_s = int(input('Introduce el poder del sith: '))
                break
            except ValueError:
                print('El poder de un sith esta medido numéricamente, intentalo de nuevo.')
        while True:
            print('Los rangos Sith válidos son : aprendiz, lord, darth, ari')
            rango_s = input('Introduce el rango del sith: ').lower()
            if rango_s.isdigit():
                print('El rango de un sith no puede ser un número, intentalo de nuevo.')
            elif rango_s not in ['aprendiz sith', 'aprendiz', 'lord', 'lord sith', 'darth', 'darth sith', 'sith\'ari']:
                print('No es un rango válido, ingrese el rango de su sith de nuevo')
            else:
                break
        while True:
            nombre = input('Introduce el nombre del sith: ').lower()
            if nombre.isdigit():
                print('El nombre de un sith no puede ser un número, intentelo de nuevo.')
                # Busco en ambos dataframes para saber si el nombre introducido se ha puesto anteriormente o no
            elif nombre.lower() in self.df_fuerza['Nombre'].tolist() or nombre in self.df_lado_oscuro[
                'Nombre'].tolist():
                print('Ya hay un jedi o sith con ese nombre. Inténtelo de nuevo. ')
            else:
                break
        sith = LadoOscuro(rango_s=rango_s, poder_s=poder_s, nombre=nombre)
        self.df_lado_oscuro = self.df_lado_oscuro.append(
            {'Poder': sith.poder_s, 'Rango': sith.rango_s, 'Nombre': sith.nombre}, ignore_index=True)
        print('Su sith se ha añadido a la agenda')

        # Aqui podremos modificar los jedi y los sith, lo buscamos por nombre en el dataframe
        # y despues escogemos que es lo que queremos cambiar y actualizamos el dataframe con los nuevos datos

    def mod_jedi(self, jedi):
        nombre_jedi = input('Introduce el nombre del jedi que quieres modificar: ')
        jedi_filtrado = self.df_fuerza[self.df_fuerza['Nombre'] == nombre_jedi]
        if len(jedi_filtrado) == 0:
            print('El jedi no se encuentra en la agenda')
            return
        op = int(input('Que quieres modificar? 1-->nombre 2-->poder 3-->rango    '))
        if op == 1:
            while True:
                nuevo_nombre = input('Introduce el nuevo nombre: ')
                if nuevo_nombre.isdigit():  # Nos aseguramos que el nombre esta bien introducido
                    print('El nombre no puede tener números, inetentelo de nuevo:')
                else:
                    self.df_fuerza.loc[self.df_fuerza['Nombre'] == nombre_jedi, 'Nombre'] = nuevo_nombre
                    print('El nombre del jedi ha sido modificado')
                    break
        elif op == 2:
            while True:
                try:
                    nuevo_poder = int(input('Introduce el nuevo poder del jedi: '))
                    self.df_fuerza.loc[self.df_fuerza['Nombre'] == nombre_jedi, 'Poder'] = nuevo_poder
                    print('El poder del jedi ha sido modificado')
                    break
                except ValueError:
                    print('El poder debe de ser númerico.')
        elif op == 3:
            while True:
                nuevo_rango = input(' Introduce el nuevo rango :').lower()
                if nuevo_rango.isdigit():
                    print('El rango no puede ser un número, intentelo de nuevo.')
                    # Me aseguro que el rango introducido es correcto iterando en la lista de rangos el nuevo_rango
                elif nuevo_rango not in ['padawan', 'caballero jedi', 'caballero', 'maestro', 'maestro jedi',
                                         'gran maestro']:
                    print('No es un rango válido, ingrese el rango de su jedi de nuevo.')
                else:
                    self.df_fuerza.loc[self.df_fuerza['Nombre'] == nombre_jedi, 'Rango'] = nuevo_rango
                    print('El rango ha sido modificado')
                    break
        elif op > 3:
            print('Debe estar entre 1 y 3, empiece de nuevo.')

    def mod_sith(self, sith):
        nombre_sith = input('Introduce el nombre del sith que quieres modificar: ')
        sith_filtrado = self.df_lado_oscuro[self.df_lado_oscuro['Nombre'] == nombre_sith]
        if len(sith_filtrado) == 0:
            print('El sith no se encuentra en la agenda')
            return
        op = int(input('Que quieres modificar?  1-->nombre 2-->poder 3-->rango  '))
        if op == 1:
            while True:
                nuevo_nombre = input('Introduce el nuevo nombre: ')
                if nuevo_nombre.isdigit():
                    print('El nombre no puede tener valores númericos, intentelo de nuevo.')
                else:
                    self.df_lado_oscuro.loc[self.df_lado_oscuro['Nombre'] == nombre_sith, 'Nombre'] = nuevo_nombre
                    print('El nombre del sith ha sido modificado')
                    break
        elif op == 2:
            while True:
                try:
                    nuevo_poder = int(input('Introduce el nuevo poder del sith: '))
                    self.df_lado_oscuro.loc[self.df_lado_oscuro['Nombre'] == nombre_sith, 'Poder'] = nuevo_poder
                    print('El poder del sith ha sido modificado')
                    break
                except ValueError:
                    print('El poder debe de ser un número, intentelo de nuevo.')
        elif op == 3:
            while True:
                nuevo_rango = input('Introduce el nuevo rango: ').lower()
                if nuevo_rango.isdigit():
                    print('El rango de un sith no puede tener dígitos')
                elif nuevo_rango not in ['aprendiz sith', 'aprendiz', 'lord', 'lord sith', 'darth', 'darth sith',
                                         'sith\'ari']:
                    print('El rango no es válido, intentelo de nuevo.')
                else:
                    self.df_lado_oscuro.loc[self.df_lado_oscuro['Nombre'] == nombre_sith, 'Rango'] = nuevo_rango
                    print('El rango del sith ha sido modificado')
                    break
        elif op > 3:
            print('Debes pulsar un numero entre el 1 y el 3, empiece de nuevo.')

        # Aquí buscamos por nombre al jedi, buscamos en el dataframe y si se encuentra printea sus datos

    def consult_jedi(self, jedi):
        while True:
            jedd = input('Introduce el nombre del jedi que quieres buscar: ')
            if jedd.isdigit():
                print('Los jedi no tienen números en su nombre, no estarás buscando a un soldado imperial?')
            else:
                break
        jedi_filtrado = self.df_fuerza[self.df_fuerza['Nombre'] == jedd]
        if len(jedi_filtrado) > 0:
            print('El jedi se encuentra en la agenda')
            print(jedi_filtrado)
        else:
            print('El jedi no se encuentra en la agenda')

    def consult_sith(self, sith):
        while True:
            sithh = input('Introduce el nombre del sith que quieres buscar: ')
            if sithh.isdigit():
                print('El nombre de un sith no puede tener números, intetelo de nuevo.')
            else:
                sith_filtrado = self.df_lado_oscuro[self.df_lado_oscuro['Nombre'] == sithh]
                if len(sith_filtrado) > 0:
                    print('El sith se encuentra en la agenda')
                    print(sith_filtrado)
                    break
                else:
                    print('El sith no se encuentra en la agenda')
                    break

        # En este caso tambien buscamos por nombre al jedi y si se encuentra lo quitamos del dataframe

    def eliminar_jedi(self):
        while True:
            jed_e = input('Introduce el nombre del jedi que quieres eliminar: ')
            if jed_e.isdigit():
                print('El nombre de un jedi no puede tener números, intentelo de nuevo.')
            else:
                jedi_filtrado = self.df_fuerza[self.df_fuerza['Nombre'] == jed_e]  # Encontramos al jedi en el dataframe
                if len(jedi_filtrado) > 0:
                    self.df_fuerza.drop(self.df_fuerza[self.df_fuerza['Nombre'] == jed_e].index,
                                        inplace=True)  # Lo eliminamos
                    print('El jedi ha sido eliminado')
                    break
                else:
                    print('El jedi no se encuentra en la agenda')
                    break

    def eliminar_sith(self):
        while True:
            sith_e = input('Introduce el nombre del sith que quieres eliminar: ')
            if sith_e.isdigit():
                print('El nombre no puede tener números')
            else:
                sith_filtrado = self.df_lado_oscuro[self.df_lado_oscuro['Nombre'] == sith_e]
                if len(sith_filtrado) > 0:
                    self.df_lado_oscuro.drop(self.df_lado_oscuro[self.df_lado_oscuro['Nombre'] == sith_e].index,
                                             inplace=True)
                    print('El sith ha sido eliminado')
                    break
                else:
                    print('El sith no se encuentra en la agenda')
                    break

        # En esta función podemos buscar por nombre,rango,poder o colsultar todos los jedis o siths

    def buscar_jedi(self, jedi):
        p = int(input('Quiere buscar(1) o sonsultar la lista entera(2)   '))
        if p == 2:
            print(self.df_fuerza.to_string(index=False))
        if p == 1:
            jj = int(input('1--> Busqueda por nombre 2--> Busqueda por rango 3--> Busqueda por poder    '))
            consulta = input('Introduce el valor de búsqueda: ')
            if jj == 1:
                filtro = self.df_fuerza[self.df_fuerza['Nombre'] == consulta]
            elif jj == 2:
                filtro = self.df_fuerza[self.df_fuerza['Rango'] == consulta]
            elif jj == 3:
                filtro = self.df_fuerza[self.df_fuerza['Poder'] == consulta]
            else:
                print('Opción no válida')
                return
            if len(filtro) == 0:
                print('Jedi no encontrado.')
            else:
                print(filtro)

    def buscar_sith(self, sith):
        s = int(input('Quiere buscar(1) o sonsultar la lista entera(2)   '))
        if s == 2:
            print(self.df_lado_oscuro.to_string(index=False))
        elif s == 1:
            ss = int(input('1--> Busqueda por nombre 2--> Busqueda por rango 3--> Busqueda por poder: '))
            consult = input('Introduce el valor de búsqueda: ')
            if ss == 1:
                filtro = self.df_lado_oscuro[self.df_lado_oscuro['Nombre'] == consult]
            elif ss == 2:
                filtro = self.df_lado_oscuro[self.df_lado_oscuro['Rango'] == consult]
            elif ss == 3:
                filtro = self.df_lado_oscuro[self.df_lado_oscuro['Poder'] == consult]
            else:
                print('Opción no válida')
                return
            if len(filtro) == 0:
                print('Sith no encontrado.')
            else:
                print(filtro)


# Menu, este hereda las funciones de agenda
class principal(agenda):
    def __init__(self):
        super().__init__()
        self.agenda = agenda

    def menu(self):
        while True:
            print('          ***  Bienvenido a su agenda galáctica  *** ')
            print('            Pulsa 1 para añadir un sith/jedi ')
            print('            Pulse 2 modificar un sith/jedi')
            print('            Pulse 3 consultar datos sith/jedi')
            print('            Pulse 4 eliminar un sith/jedi')
            print('            Pulse 5 buscar por Nombre/rango/lvl de poder o mostrar todos los sith/jedi')
            print('            Pulse 6 para salir de la agenda')
            ch = input('      Ingrese un número del 1 al 6: ')
            # Queremos que solo se puedan meter números, hacemos el tratamiento de errores adecuado.
            if ch.isalpha():
                print('Solo deben ser números')
            else:
                if int(ch) > 6:
                    print('Numero no válido')
                    print('Intentelo de nuevo')
                if int(ch) == 1:
                    while True:
                        im = input('     1--> Jedi    2--> Sith  ')
                        if im.isdigit():  # Nos aseguramos que im es un numero
                            if int(im) == 1:
                                agenda.anadir_jedi()
                                break
                            elif int(im) == 2:
                                agenda.anadir_sith()
                                break
                            else:
                                print('Debes poner 1 o 2')
                                break
                        else:
                            print('Error, debe ser númerico')
                            print('Intentelo de nuevo')
                elif int(ch) == 2:
                    while True:
                        im2 = input('     1--> Jedi    2--> Sith  ')
                        if im2.isdigit():
                            if int(im2) == 1:
                                agenda.mod_jedi(None)
                                break
                            elif int(im2) == 2:
                                agenda.mod_sith(None)
                                break
                            else:
                                print('El número debe ser 1 o 2')
                                break
                        else:
                            print('Error, debe ser un número')
                            print('Intentelo de nuevo')
                elif int(ch) == 3:
                    while True:
                        im3 = input('     1--> Jedi    2--> Sith  ')
                        if im3.isdigit():
                            if int(im3) == 1:
                                agenda.consult_jedi(None)
                                break
                            elif int(im3) == 2:
                                agenda.consult_sith(None)
                                break
                            else:
                                print('El número debe ser 1 o 2')
                        else:
                            print('Error, debe ser númerico')
                            print('Intentelo de nuevo')
                elif int(ch) == 4:
                    while True:
                        im4 = input('    1--> Jedi    2--> Sith  ')
                        if im4.isdigit():
                            if int(im4) == 1:
                                agenda.eliminar_jedi()
                                break
                            elif int(im4) == 2:
                                agenda.eliminar_sith()
                                break
                            else:
                                print('El número debe ser 1 o 2')
                        else:
                            print('Error, debe ser númerico')
                            print('Intentelo de nuevo')
                elif int(ch) == 5:
                    while True:
                        im5 = input('     1--> Jedi    2--> Sith  ')
                        if im5.isdigit():
                            if int(im5) == 1:
                                agenda.buscar_jedi(None)
                                break
                            elif int(im5) == 2:
                                agenda.buscar_sith(None)
                                break
                            else:
                                print('El número debe ser 1 o 2')
                                break
                        else:
                            print('Error, debe ser númerico')
                            print('Intentelo de nuevo')
                elif int(ch) == 6:
                    print("Gracias por usar la Agenda Galáctica, que la Fuerza esté contigo.")
                    print('               ™ República Galáctica')
                    break


agenda = agenda()

# Iniciamos el programa
principal.menu()

