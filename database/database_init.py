# coding=utf8
# import sqlite3
from Database import Database
from Subject import Subject

db = Database()
db.create_table()

subject_1 = Subject('ZPI', 'Zarządzanie projektami informatycznymi', 'Celem przedmiotu jest zapoznanie studentów z metodykami kierowania dużych projektów informatycznych. Omawiane są tradycyjne oraz zwinne podejścia do zarządzania projektami. W szczególności rozpatrywane są zagadnienia związane z organizacją zespołów projektowych, procesem zarządzania wymaganiami, metodami szacowania pracochłonności i planowania oraz zarządzaniem zespołem wykonawców.',4.0)
subject_2 = Subject('WDEC', 'Wspomaganie decyzji','Celem wykładu jest wprowadzenie studentów w tematykę komputerowych systemów wspomagania decyzji. Wykład rozpoczyna się od przedstawienia podstaw teoretycznych wspomagania decyzji. Następnie omawiana jest rola systemów komputerowych we wspomaganiu procesów decyzyjnych oraz elementy składowe takich systemów. W trakcie kolejnych wykładów przedstawiane są najbardziej reprezentatywne techniki wykorzystywane we wspomaganiu decyzji. Omawiane są zagadnienia budowy modeli rzeczowych sytuacji decyzyjnej, budowy modeli preferencji oraz metody reprezentacji niepewności. Dużo uwagi poświęca się zagadnieniom właściwej organizacji danych, pod kątem wspomagania decyzji, a w szczególności tematyce hurtowni danych oraz narzędziom OLAP (On-Line Analytical Processing). Wykład jest wzbogacony prezentacją przykładowych systemów wspomagania decyzji.' , 5.0)
subject_3 = Subject('SCZR', 'Systemy czasu rzeczywistego','Celem przedmiotu jest przedstawienie specyfiki systemów komputerowych w zastosowaniach do sterowania i pomiarów. Przedstawienie metodyki projektowania oprogramowania dla systemów wbudowanych z uwzględnieniem zagadnień bezpieczeństwa i niezawodności systemu. Wykład obejmuje także systemy operacyjne czasu rzeczywistego, sieci przemysłowe i przykładowe aplikacje systemów czasu rzeczywistego. Ćwiczenia laboratoryjne pozwalają studentom nabyć praktyczną umiejętność projektowania i uruchamiania oprogramowania dla systemów wbudowanych z uwzględnieniem aplikacji czasu rzeczywistego.' , 4.0)
subject_4 = Subject('PSZT', 'Podstawy sztucznej inteligencji','Wykład stanowi wyczerpującą prezentację zasad automatycznego wnioskowania oraz konstrukcji systemów wnioskujących w oparciu o logikę. Jednocześnie, wykład stanowi wprowadzenie do różnych gałęzi tzw. miękkiej sztucznej inteligencji (czy inteligencji obliczeniowej), takich jak algorytmy ewolucyjne, uczenie maszynowe i sieci neuronowe.' , 4.0)
subject_5 = Subject('IOP', 'Inżynieria oprogramowania','Celem przedmiotu jest wprowadzenie słuchaczy w podstawowe zagadnienia inżynierii oprogramowania, obejmujące organizację cyklu wytwarzania aplikacji, metodykę projektowania i weryfikacji programów oraz zarządzania projektem programistycznym. Związane z wykładem laboratorium pozwala studentom nabyć praktyczną umiejętność obiektowego modelowania i projektowania programów oraz posługiwania się systemem wspomagającym.' , 4.0)
subject_6 = Subject('GKOM', 'Grafika komputerowa','Celem wykładu jest zapoznanie słuchaczy z zagadnieniami i algorytmami stosowanymi w grafice komputerowej. Wykład pokazuje kluczowe pojęcia i algorytmy grafiki komputerowej. Na wstępie omówione są typowe architektury potoku przetwarzania i generowania obrau oraz pojęcia grafiki wektorowej i rastrowej z uwzględnieniem zagadnień dotyczących stosowanych modeli barw. W dalszej części wykład dotyczy zagadnień grafiki 3D. Omawiane są metody i algorytmy dotyczące modelowania i wizualizacji scen trójwymiarowych, generowania grafiki wysokiej jakości oraz animacji komputerowej.' , 4.0)
subject_7 = Subject('PROD', 'Protokół dyplomatyczny','Celem zajęć jest przekazanie wiedzy dotyczącej protokołu dyplomatycznego i norm zachowania przyjętych w stosunkach oficjalnych i międzynarodowych. Zajęcia prowadzone są w formie wykładu aktywnego (konwersatorium), uzupełniane analizą przypadków i aktów prawnych, prezentacjami, oraz dyskusjami umożliwiającymi uczestnikom zajęć podzielenie się swoimi spostrzeżeniami i obserwacjami na temat stosowania obecnie protokołu dyplomatycznego i etykiety w kontaktach międzynarodowych, urzędowych i gospodarczych.' , 2.0)
db.insert_subject(subject_1)
db.insert_subject(subject_2)
db.insert_subject(subject_3)
db.insert_subject(subject_4)
db.insert_subject(subject_5)
db.insert_subject(subject_6)
db.insert_subject(subject_7)
subjects = db.get_subjects_by_code("W%")
print(subjects)
print("Selected: " + str(db.get_number_of_subjects_by_code("P%")) + " subjects")

print("All: " + str(db.get_number_of_subjects()))
# # print(subjects)