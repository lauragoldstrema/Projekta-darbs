# Projekts


### Projekta uzdevums

Projekta uzdevums ir noskaidrot aktuālo gaisa temperatūru kādā konkrētā pilsētā, ko ievada lietotājs. Tiek izmantota Selenium bibliotēka, lai no mājaslapas [AccuWeather](https://www.accuweather.com/) iegūtu datus par šī brīža temperaturu un tepmeratūru pēc sajūtām, tad šī informācija tiek izvadīta konsolē.

Sākotnēji projektā tiek inicializētas visas nepieciešamās bibliotēkas, tālāk tiek pieprasīts lietotājam ievadīt pilsētas nosaukumu, tad tiek atvērts interneta pārluks Chrome un norādītā mājaslapa, no kuras tiek iegūti dati. Tālāk tiek apstiprināta piekrišana personas datu izmantošanai, pēc tam tiek ievadīta lietotāja norādītā pilsēta meklētāja, pēc datu ielādes tiek izgūta gaisa temperatūra un izvadīta lietotājam.


### Izmantotās bibliotēkas


1. Selenium - Selenium ir bibliotēka, kas paredzēta dažādu tīmekļa vietņu automatizēšanai, šajā projektā tā tiek izmantota, lai atvērtu nepieciešamo mājaslapu, piekristu personas datu izmantošanai, ievadītu meklēšanas logā lietotāja ievadīto pilsētu un iegūtu aktuālo temperatūru.

2. WebDriver - WebDriver tiek izmantots, lai automatizētu interneta pārlūka darbibu, šajā projektā tas tiek izmantots, lai automatizētu Google Chrome. 'webdriver.Chrome()' inicializē ChromeDriver.

3. Time - Time bibliotēka tiek izmantota ar laiku saistītām darbībām. Projektā tiek izmantota funkcija sleep, lai apstādinātu koda izpildi uz noteiktu skaitu sekunžu, lai mājaslapa varētu ielādēties.

4. By (from selenium.webdriver.common.by) - Tiek izmantots, lai atrastu HTML objektus, kas satur nepieciešamo informāciju vai uz kuriem ir nepieciešams uzspiest, vai kuros nepieciešams ievadīt informāciju.

5. WebElement (from selenium.webdriver.remote.webelement) - Tiek izmantots, lai veiktu nepieciešamās darbības ar iepriekš atrastajiem HTML objektiem - uzpiestu uz tiem, ievadītu tekstu vai izgūtu nepieciešamo informāciju.


### Programmatūras izmantošanas metodes

Lai izmantotu šo programmu, ir nepieciešams uzinstalēt Python3 versiju, kā arī Selenium bibliotēku ar pip install selenium, kā arī atjaunot izmantotā interneta pārlūka versiju uz jaunāko.
