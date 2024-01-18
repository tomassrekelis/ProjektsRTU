# ProjektsRTU
#Projekta uzdevums:
Programmas mērķis ir atvieglot slidu nomas dzīvi, kurā strādāju, jo bieži tiek saņemti zvani uz ofisu, kur tiek uzdoti jautājumi par to vai ir pieejams konkrētais izmērs, kad nomas darbinieki ir pārāk aizņemti ar klientiem, lai atbildētu uz telefonu. Lietotājam ofisā ir jāievada Dzimums (Sieviete vai Vīrietis), pēc tam programma prasa ievadīt slidu izmēru, kuru klients vēlas un datumu. Līdz ar to programma izvada cik daudz slidas ir pieejamas konkrētajā datumā uz esošo brīdi ņemot vērā dzimumu un izmēru. Programmai nepieciešams Excel fails, kurā nomas darbinieki vienmēr ievada datus par cilvēku, kas nomā slidas, lai veiktu uzskaiti.
#Python bibliotēkas un to skaidrojums:
Pandas bibliotēka tiek izmantota datu apstrādei un analīzei, lai varētu apstrādāt un analizēt datus no Excel faila.
Datetime bibliotēka tiek izmantota datuma formāta pārbaudei un apstrādei.
OS bibliotēka tiek izmantota, lai iegūtu informāciju par failu ceļu un nolādētu datiem nepieciešamo Excel failu. Bibliotēka palīdz noteikt precīzu atrašanās vietu neņemot vērā, kur tiek izpildīts skripts. 
kopskaits_viriesu_slidas un kopskaits_sieviesu_slidas . Šīs funkcijas atgriež attiecīgajam dzimumam slidu skaitu atkarībā no izmēra.
available_and_taken_skates . Šī funkcija aprēķina pieejamo un jau iznomāto slidu skaitu atkarībā no dzimuma, slidu izmēra un datuma.
gender_input, size_input, date_input . Šīs funkcijas iegūst datus par attiecīgi dzimumu, izmēriem un datumiem.
#Programmatūras izmantošanas metodes:
data = pd.read_excel(file_path) šī koda rinda nolasa Excel failu, kurā glabājas informācija par iznomātajām slidām konkrētā datumā janvārī, atkarībā no lietotāja ievadītajiem datiem.
kopskaits_viriesu_slidas un kopskaits_sieviesu_slidas . Šīs funkcijas atgriež attiecīgajam dzimumam slidu skaitu atkarībā no izmēra.
available_and_taken_skates . Šī funkcija aprēķina pieejamo un jau iznomāto slidu skaitu atkarībā no dzimuma, slidu izmēra un datuma.
gender_input, size_input, date_input . Šīs funkcijas iegūst datus par attiecīgi dzimumu, izmēriem un datumiem.
gender_input = input("Ievadiet dzimumu (Vīrietis or Sieviete): ")
size_input = int(input("Ievadiet slidu izmēru: "))
date_input = input("Ievadiet datumu (format: DD.MM.YYYY.): ")    Šīs funkcijas liek lietotājam ievadīt attiecīgi dzimumu, slidu izmēru un datumu.
datetime.strptime(date_input, "%d.%m.%Y.")    Šī funkcija pārbauda ievadīto datumu, pārliecinātos, ka tas atbilst pareizajam datuma formātam, citādāk izvadās kļūda.
filtered_data = data[(data['Dzimums'] == gender) & (data['Kājas izmērs'] == size) & (data['Nomas datums'] == date)]    Šī funkcija filtrē tos datus, kas atbilst noteiktajam dzimumam, izmēram un datuma nosacījumiem.
