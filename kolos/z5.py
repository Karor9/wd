tekst = """ tekst w teorii literatury – wypowiedź stanowiąca zamkniętą całość z punktu widzenia treści, często utrwalona graficznie.
tekst w tekstologii – utrwalony (najczęściej w postaci pisemnej) ciąg znaków językowych, przyjmowany jako niezmienny i niemogący podlegać przemianom w procesie komunikacji językowej.
tekst w semiotyce – każdy wytwór kultury (tekst kultury) stanowiący całość uporządkowaną według określonych reguł, np. dzieło sztuki, ubiór, zachowanie realizujące jakiś utrwalony wzorzec kulturowy.
tekst w językoznawstwie strukturalistycznym – przedmiot konkretny służący do przekazywania informacji na bazie rozumianego abstrakcyjnie języka; także fizyczny wytwór sytuacji komunikacyjnej.
tekst w muzyce – słowa utworu muzycznego, np. piosenki lub arii.
tekst spójny – koherentna (np. pod względem semantycznym lub formalnym) struktura języka naturalnego. """
slowo= str(input('podaj tekst do wyszukania: '))

print(tekst.count(slowo))