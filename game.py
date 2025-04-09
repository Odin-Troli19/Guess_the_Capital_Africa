
import tkinter as tk
from tkinter import messagebox, ttk
import random
import time


countries = [
    # African Countries Complete Data
  {
    "name": "Nigeria", 
    "capital": "Abuja", 
    "population": "213 million", 
    "independence": "October 1, 1960", 
    "president": "Bola Ahmed Tinubu", 
    "language": "English", 
    "flag": "🇳🇬", 
    "currency": "Nigerian Naira (₦)",
    "facts": "Nigeria is the most populous country in Africa."
  },
  {
    "name": "Egypt", 
    "capital": "Cairo", 
    "population": "110 million", 
    "independence": "February 28, 1922", 
    "president": "Abdel Fattah el-Sisi", 
    "language": "Arabic", 
    "flag": "🇪🇬", 
    "currency": "Egyptian Pound (E£)",
    "facts": "The pyramids of Egypt are one of the seven wonders of the world."
  },
  {
    "name": "South Africa", 
    "capital": "Pretoria (administrative), Cape Town (legislative), Bloemfontein (judicial)", 
    "population": "60 million", 
    "independence": "May 31, 1961", 
    "president": "Cyril Ramaphosa", 
    "language": "11 official languages including English, Afrikaans, Zulu", 
    "flag": "🇿🇦", 
    "currency": "South African Rand (R)",
    "facts": "South Africa has three capital cities."
  },
  {
    "name": "Algeria", 
    "capital": "Algiers", 
    "population": "44 million", 
    "independence": "July 5, 1962", 
    "president": "Abdelmadjid Tebboune", 
    "language": "Arabic, Berber", 
    "flag": "🇩🇿", 
    "currency": "Algerian Dinar (DA)",
    "facts": "Algeria is the largest country in Africa by land area."
  },
  {
    "name": "Ethiopia", 
    "capital": "Addis Ababa", 
    "population": "118 million", 
    "independence": "Never colonized (briefly occupied by Italy 1936-1941)", 
    "president": "Sahle-Work Zewde", 
    "language": "Amharic", 
    "flag": "🇪🇹", 
    "currency": "Ethiopian Birr (Br)",
    "facts": "Ethiopia is the only African country that was never fully colonized by European powers."
  },
  {
    "name": "Morocco", 
    "capital": "Rabat", 
    "population": "37 million", 
    "independence": "March 2, 1956", 
    "president": "King Mohammed VI (monarchy)", 
    "language": "Arabic, Berber", 
    "flag": "🇲🇦", 
    "currency": "Moroccan Dirham (MAD)",
    "facts": "Morocco has the oldest continuously operating university in the world, University of Al Quaraouiyine."
  },
  {
    "name": "Kenya", 
    "capital": "Nairobi", 
    "population": "54 million", 
    "independence": "December 12, 1963", 
    "president": "William Ruto", 
    "language": "Swahili, English", 
    "flag": "🇰🇪", 
    "currency": "Kenyan Shilling (KSh)",
    "facts": "Kenya is known for its long-distance runners and safari tourism."
  },
  {
    "name": "Tanzania", 
    "capital": "Dodoma", 
    "population": "63 million", 
    "independence": "December 9, 1961", 
    "president": "Samia Suluhu Hassan", 
    "language": "Swahili, English", 
    "flag": "🇹🇿", 
    "currency": "Tanzanian Shilling (TSh)",
    "facts": "Mount Kilimanjaro, Africa's highest peak, is located in Tanzania."
  },
  {
    "name": "Sudan", 
    "capital": "Khartoum", 
    "population": "44 million", 
    "independence": "January 1, 1956", 
    "president": "Abdel Fattah al-Burhan (chairman of transitional council)", 
    "language": "Arabic, English", 
    "flag": "🇸🇩", 
    "currency": "Sudanese Pound (SDG)",
    "facts": "Sudan once had the largest number of pyramids in the world, more than Egypt."
  },
  {
    "name": "Uganda", 
    "capital": "Kampala", 
    "population": "47 million", 
    "independence": "October 9, 1962", 
    "president": "Yoweri Museveni", 
    "language": "English, Swahili", 
    "flag": "🇺🇬", 
    "currency": "Ugandan Shilling (USh)",
    "facts": "Uganda is home to Lake Victoria, the largest lake in Africa."
  },
  {
    "name": "Ghana", 
    "capital": "Accra", 
    "population": "32 million", 
    "independence": "March 6, 1957", 
    "president": "Nana Akufo-Addo", 
    "language": "English", 
    "flag": "🇬🇭", 
    "currency": "Ghanaian Cedi (₵)",
    "facts": "Ghana was the first sub-Saharan African country to gain independence from colonial rule."
  },
  {
    "name": "Angola", 
    "capital": "Luanda", 
    "population": "34 million", 
    "independence": "November 11, 1975", 
    "president": "João Lourenço", 
    "language": "Portuguese", 
    "flag": "🇦🇴", 
    "currency": "Angolan Kwanza (Kz)",
    "facts": "Angola is the seventh-largest country in Africa."
  },
  {
    "name": "Mozambique", 
    "capital": "Maputo", 
    "population": "32 million", 
    "independence": "June 25, 1975", 
    "president": "Filipe Nyusi", 
    "language": "Portuguese", 
    "flag": "🇲🇿", 
    "currency": "Mozambican Metical (MT)",
    "facts": "Mozambique's flag features an AK-47 rifle, symbolizing defense and vigilance."
  },
  {
    "name": "Ivory Coast (Côte d'Ivoire)", 
    "capital": "Yamoussoukro (official), Abidjan (de facto)", 
    "population": "27 million", 
    "independence": "August 7, 1960", 
    "president": "Alassane Ouattara", 
    "language": "French", 
    "flag": "🇨🇮", 
    "currency": "West African CFA Franc (CFA)",
    "facts": "Ivory Coast is the world's largest cocoa producer."
  },
  {
    "name": "Madagascar", 
    "capital": "Antananarivo", 
    "population": "28 million", 
    "independence": "June 26, 1960", 
    "president": "Andry Rajoelina", 
    "language": "Malagasy, French", 
    "flag": "🇲🇬", 
    "currency": "Malagasy Ariary (Ar)",
    "facts": "About 90% of Madagascar's wildlife is found nowhere else on Earth."
  },
  {
    "name": "Cameroon", 
    "capital": "Yaoundé", 
    "population": "27 million", 
    "independence": "January 1, 1960", 
    "president": "Paul Biya", 
    "language": "French, English", 
    "flag": "🇨🇲", 
    "currency": "Central African CFA Franc (FCFA)",
    "facts": "Cameroon is often called 'Africa in miniature' due to its geographical and cultural diversity."
  },
  {
    "name": "Niger", 
    "capital": "Niamey", 
    "population": "25 million", 
    "independence": "August 3, 1960", 
    "president": "Abdourahamane Tiani (military leader)", 
    "language": "French", 
    "flag": "🇳🇪", 
    "currency": "West African CFA Franc (CFA)",
    "facts": "Niger is named after the Niger River that flows through it."
  },
  {
    "name": "Mali", 
    "capital": "Bamako", 
    "population": "21 million", 
    "independence": "September 22, 1960", 
    "president": "Assimi Goïta (military leader)", 
    "language": "French", 
    "flag": "🇲🇱", 
    "currency": "West African CFA Franc (CFA)",
    "facts": "Timbuktu in Mali was once a major center for Islamic scholarship."
  },
  {
    "name": "Burkina Faso", 
    "capital": "Ouagadougou", 
    "population": "22 million", 
    "independence": "August 5, 1960", 
    "president": "Ibrahim Traoré (military leader)", 
    "language": "French", 
    "flag": "🇧🇫", 
    "currency": "West African CFA Franc (CFA)",
    "facts": "The name 'Burkina Faso' means 'Land of the honest people'."
  },
  {
    "name": "Malawi", 
    "capital": "Lilongwe", 
    "population": "20 million", 
    "independence": "July 6, 1964", 
    "president": "Lazarus Chakwera", 
    "language": "English, Chichewa", 
    "flag": "🇲🇼", 
    "currency": "Malawian Kwacha (MK)",
    "facts": "Lake Malawi contains more species of fish than any other lake in the world."
  },
  {
    "name": "Zambia", 
    "capital": "Lusaka", 
    "population": "19 million", 
    "independence": "October 24, 1964", 
    "president": "Hakainde Hichilema", 
    "language": "English", 
    "flag": "🇿🇲", 
    "currency": "Zambian Kwacha (ZK)",
    "facts": "Victoria Falls, one of the Seven Natural Wonders of the World, is located on Zambia's border with Zimbabwe."
  },
  {
    "name": "Senegal", 
    "capital": "Dakar", 
    "population": "17 million", 
    "independence": "April 4, 1960", 
    "president": "Bassirou Diomaye Faye", 
    "language": "French", 
    "flag": "🇸🇳", 
    "currency": "West African CFA Franc (CFA)",
    "facts": "Senegal's Pink Lake (Lake Retba) is one of the few pink lakes in the world."
  },
  {
    "name": "Chad", 
    "capital": "N'Djamena", 
    "population": "17 million", 
    "independence": "August 11, 1960", 
    "president": "Mahamat Déby (transitional military leader)", 
    "language": "French, Arabic", 
    "flag": "🇹🇩", 
    "currency": "Central African CFA Franc (FCFA)",
    "facts": "Chad is named after Lake Chad, which was once one of Africa's largest lakes but has shrunk dramatically."
  },
  {
    "name": "Somalia", 
    "capital": "Mogadishu", 
    "population": "16 million", 
    "independence": "July 1, 1960", 
    "president": "Hassan Sheikh Mohamud", 
    "language": "Somali, Arabic", 
    "flag": "🇸🇴", 
    "currency": "Somali Shilling (Sh.So.)",
    "facts": "Somalia has the longest coastline on mainland Africa."
  },
  {
    "name": "Zimbabwe", 
    "capital": "Harare", 
    "population": "15 million", 
    "independence": "April 18, 1980", 
    "president": "Emmerson Mnangagwa", 
    "language": "16 official languages including English, Shona, Ndebele", 
    "flag": "🇿🇼", 
    "currency": "Zimbabwean Dollar (Z$)",
    "facts": "The Great Zimbabwe ruins are the largest ancient stone structure in sub-Saharan Africa."
  },
  {
    "name": "Guinea", 
    "capital": "Conakry", 
    "population": "13 million", 
    "independence": "October 2, 1958", 
    "president": "Mamady Doumbouya (military leader)", 
    "language": "French", 
    "flag": "🇬🇳", 
    "currency": "Guinean Franc (GNF)",
    "facts": "Guinea is known as the 'water tower of West Africa' due to its many rivers."
  },
  {
    "name": "Rwanda", 
    "capital": "Kigali", 
    "population": "13 million", 
    "independence": "July 1, 1962", 
    "president": "Paul Kagame", 
    "language": "Kinyarwanda, English, French", 
    "flag": "🇷🇼", 
    "currency": "Rwandan Franc (RWF)",
    "facts": "Rwanda is known as the 'Land of a Thousand Hills' due to its mountainous terrain."
  },
  {
    "name": "Benin", 
    "capital": "Porto-Novo (official), Cotonou (de facto)", 
    "population": "13 million", 
    "independence": "August 1, 1960", 
    "president": "Patrice Talon", 
    "language": "French", 
    "flag": "🇧🇯", 
    "currency": "West African CFA Franc (CFA)",
    "facts": "Benin is considered the birthplace of vodun (voodoo)."
  },
  {
    "name": "Burundi", 
    "capital": "Gitega", 
    "population": "12 million", 
    "independence": "July 1, 1962", 
    "president": "Évariste Ndayishimiye", 
    "language": "Kirundi, French", 
    "flag": "🇧🇮", 
    "currency": "Burundian Franc (FBu)",
    "facts": "Burundi is one of the smallest countries in Africa."
  },
  {
    "name": "Tunisia", 
    "capital": "Tunis", 
    "population": "12 million", 
    "independence": "March 20, 1956", 
    "president": "Kais Saied", 
    "language": "Arabic", 
    "flag": "🇹🇳", 
    "currency": "Tunisian Dinar (DT)",
    "facts": "Tunisia is the northernmost country in Africa."
  },
  {
    "name": "South Sudan", 
    "capital": "Juba", 
    "population": "11 million", 
    "independence": "July 9, 2011", 
    "president": "Salva Kiir Mayardit", 
    "language": "English", 
    "flag": "🇸🇸", 
    "currency": "South Sudanese Pound (SSP)",
    "facts": "South Sudan is the newest internationally recognized country in Africa and the world."
  },
  {
    "name": "Togo", 
    "capital": "Lomé", 
    "population": "8.5 million", 
    "independence": "April 27, 1960", 
    "president": "Faure Gnassingbé", 
    "language": "French", 
    "flag": "🇹🇬", 
    "currency": "West African CFA Franc (CFA)",
    "facts": "Togo is one of the smallest countries in Africa."
  },
  {
    "name": "Sierra Leone", 
    "capital": "Freetown", 
    "population": "8.1 million", 
    "independence": "April 27, 1961", 
    "president": "Julius Maada Bio", 
    "language": "English", 
    "flag": "🇸🇱", 
    "currency": "Sierra Leonean Leone (Le)",
    "facts": "Freetown, Sierra Leone's capital, was founded as a home for repatriated slaves."
  },
  {
    "name": "Libya", 
    "capital": "Tripoli", 
    "population": "7 million", 
    "independence": "December 24, 1951", 
    "president": "Mohamed al-Menfi (Chairman of Presidential Council)", 
    "language": "Arabic", 
    "flag": "🇱🇾", 
    "currency": "Libyan Dinar (LD)",
    "facts": "Libya has the largest proven oil reserves in Africa."
  },
  {
    "name": "Central African Republic", 
    "capital": "Bangui", 
    "population": "5.5 million", 
    "independence": "August 13, 1960", 
    "president": "Faustin-Archange Touadéra", 
    "language": "French, Sango", 
    "flag": "🇨🇫", 
    "currency": "Central African CFA Franc (FCFA)",
    "facts": "The Central African Republic is located precisely at the center of the African continent."
  },
  {
    "name": "Republic of the Congo", 
    "capital": "Brazzaville", 
    "population": "5.8 million", 
    "independence": "August 15, 1960", 
    "president": "Denis Sassou Nguesso", 
    "language": "French", 
    "flag": "🇨🇬", 
    "currency": "Central African CFA Franc (FCFA)",
    "facts": "The Republic of the Congo is often called Congo-Brazzaville to distinguish it from the neighboring Democratic Republic of the Congo."
  },
  {
    "name": "Democratic Republic of the Congo", 
    "capital": "Kinshasa", 
    "population": "95 million", 
    "independence": "June 30, 1960", 
    "president": "Félix Tshisekedi", 
    "language": "French", 
    "flag": "🇨🇩", 
    "currency": "Congolese Franc (FC)",
    "facts": "The Democratic Republic of the Congo is the second-largest country in Africa by land area."
  },
  {
    "name": "Eritrea", 
    "capital": "Asmara", 
    "population": "3.6 million", 
    "independence": "May 24, 1993", 
    "president": "Isaias Afwerki", 
    "language": "Tigrinya, Arabic, English", 
    "flag": "🇪🇷", 
    "currency": "Eritrean Nakfa (Nfk)",
    "facts": "Eritrea's capital Asmara is known as 'Africa's Modernist City' due to its Italian colonial architecture."
  },
  {
    "name": "Mauritania", 
    "capital": "Nouakchott", 
    "population": "4.7 million", 
    "independence": "November 28, 1960", 
    "president": "Mohamed Ould Ghazouani", 
    "language": "Arabic", 
    "flag": "🇲🇷", 
    "currency": "Mauritanian Ouguiya (MRU)",
    "facts": "Mauritania was the last country in the world to abolish slavery, in 1981."
  },
  {
    "name": "Namibia", 
    "capital": "Windhoek", 
    "population": "2.6 million", 
    "independence": "March 21, 1990", 
    "president": "Nangolo Mbumba", 
    "language": "English", 
    "flag": "🇳🇦", 
    "currency": "Namibian Dollar (N$)",
    "facts": "Namibia has the oldest desert in the world, the Namib Desert."
  },
  {
    "name": "Botswana", 
    "capital": "Gaborone", 
    "population": "2.4 million", 
    "independence": "September 30, 1966", 
    "president": "Mokgweetsi Masisi", 
    "language": "English, Setswana", 
    "flag": "🇧🇼", 
    "currency": "Botswana Pula (P)",
    "facts": "Botswana is home to the world's largest elephant population."
  },
  {
    "name": "Gabon", 
    "capital": "Libreville", 
    "population": "2.3 million", 
    "independence": "August 17, 1960", 
    "president": "Brice Clotaire Oligui Nguema (transitional leader)", 
    "language": "French", 
    "flag": "🇬🇦", 
    "currency": "Central African CFA Franc (FCFA)",
    "facts": "Gabon is one of the most forested countries in the world, with over 85% forest cover."
  },
  {
    "name": "Gambia", 
    "capital": "Banjul", 
    "population": "2.5 million", 
    "independence": "February 18, 1965", 
    "president": "Adama Barrow", 
    "language": "English", 
    "flag": "🇬🇲", 
    "currency": "Gambian Dalasi (D)",
    "facts": "The Gambia is the smallest country on mainland Africa."
  },
  {
    "name": "Guinea-Bissau", 
    "capital": "Bissau", 
    "population": "2 million", 
    "independence": "September 24, 1973", 
    "president": "Umaro Sissoco Embaló", 
    "language": "Portuguese", 
    "flag": "🇬🇼", 
    "currency": "West African CFA Franc (CFA)",
    "facts": "Guinea-Bissau was once part of the Kingdom of Gabu, part of the Mali Empire."
  },
  {
    "name": "Lesotho", 
    "capital": "Maseru", 
    "population": "2.2 million", 
    "independence": "October 4, 1966", 
    "president": "King Letsie III (monarch), Sam Matekane (Prime Minister)", 
    "language": "Sesotho, English", 
    "flag": "🇱🇸", 
    "currency": "Lesotho Loti (L)",
    "facts": "Lesotho is completely surrounded by South Africa, making it an enclave country."
  },
  {
    "name": "Djibouti", 
    "capital": "Djibouti City", 
    "population": "1 million", 
    "independence": "June 27, 1977", 
    "president": "Ismaïl Omar Guelleh", 
    "language": "French, Arabic", 
    "flag": "🇩🇯", 
    "currency": "Djiboutian Franc (Fdj)",
    "facts": "Djibouti is located at the intersection of the Red Sea and the Gulf of Aden."
  },
  {
    "name": "Eswatini (formerly Swaziland)", 
    "capital": "Mbabane (administrative), Lobamba (royal and legislative)", 
    "population": "1.2 million", 
    "independence": "September 6, 1968", 
    "president": "King Mswati III (monarch)", 
    "language": "English, Swazi", 
    "flag": "🇸🇿", 
    "currency": "Swazi Lilangeni (L)",
    "facts": "Eswatini is one of the last absolute monarchies in the world."
  },
  {
    "name": "Equatorial Guinea", 
    "capital": "Malabo", 
    "population": "1.5 million", 
    "independence": "October 12, 1968", 
    "president": "Teodoro Obiang Nguema Mbasogo", 
    "language": "Spanish, French, Portuguese", 
    "flag": "🇬🇶", 
    "currency": "Central African CFA Franc (FCFA)",
    "facts": "Equatorial Guinea is the only Spanish-speaking country in Africa."
  },
  {
    "name": "Mauritius", 
    "capital": "Port Louis", 
    "population": "1.3 million", 
    "independence": "March 12, 1968", 
    "president": "Prithvirajsing Roopun", 
    "language": "English, French, Mauritian Creole", 
    "flag": "🇲🇺", 
    "currency": "Mauritian Rupee (Rs)",
    "facts": "Mauritius was the only known home of the now-extinct dodo bird."
  },
  {
    "name": "Comoros", 
    "capital": "Moroni", 
    "population": "870,000", 
    "independence": "July 6, 1975", 
    "president": "Azali Assoumani", 
    "language": "Comorian, Arabic, French", 
    "flag": "🇰🇲", 
    "currency": "Comorian Franc (CF)",
    "facts": "Comoros is an archipelago nation made up of three main islands."
  },
  {
    "name": "Cabo Verde", 
    "capital": "Praia", 
    "population": "560,000", 
    "independence": "July 5, 1975", 
    "president": "José Maria Neves", 
    "language": "Portuguese", 
    "flag": "🇨🇻", 
    "currency": "Cape Verdean Escudo (CVE)",
    "facts": "Cabo Verde is an archipelago of 10 volcanic islands in the central Atlantic Ocean."
  },
  {
    "name": "São Tomé and Príncipe", 
    "capital": "São Tomé", 
    "population": "220,000", 
    "independence": "July 12, 1975", 
    "president": "Carlos Vila Nova", 
    "language": "Portuguese", 
    "flag": "🇸🇹", 
    "currency": "São Tomé and Príncipe Dobra (Db)",
    "facts": "São Tomé and Príncipe is Africa's smallest Portuguese-speaking country."
  },
  {
    "name": "Seychelles", 
    "capital": "Victoria", 
    "population": "100,000", 
    "independence": "June 29, 1976", 
    "president": "Wavel Ramkalawan", 
    "language": "English, French, Seychellois Creole", 
    "flag": "🇸🇨", 
    "currency": "Seychellois Rupee (SR)",
    "facts": "Seychelles has the smallest population of any sovereign African country."
  },
  {
    "name": "Western Sahara", 
    "capital": "Laayoune (claimed)", 
    "population": "600,000", 
    "independence": "Disputed territory", 
    "president": "Brahim Ghali (Sahrawi Arab Democratic Republic)", 
    "language": "Arabic", 
    "flag": "🇪🇭", 
    "currency": "Moroccan Dirham (MAD)",
    "facts": "Western Sahara is a disputed territory, partially controlled by Morocco and partially by the Sahrawi Arab Democratic Republic."
  },
  {
    "name": "Liberia", 
    "capital": "Monrovia", 
    "population": "5.2 million", 
    "independence": "July 26, 1847", 
    "president": "Joseph Boakai", 
    "language": "English", 
    "flag": "🇱🇷", 
    "currency": "Liberian Dollar (L$)",
    "facts": "Liberia was founded by freed American slaves and is Africa's oldest republic."
  }
]
class CapitalGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Capital - Africa")
        self.root.geometry("600x500")  # Set a larger default size
        self.score = 0
        self.total_questions = 0
        self.max_questions = 15  # Set maximum number of questions to 15
        self.current_question = None
        self.difficulty = "easy"
        self.time_limit = 20  # Default time limit in seconds
        self.time_remaining = 0
        self.timer_running = False
        self.timer_id = None  # For storing the after() ID
        
        # Create style for ttk widgets
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 11))
        self.style.configure("TLabel", font=("Helvetica", 11))
        
        self.setup_widgets()

    def setup_widgets(self):
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(self.frame, text="African Capitals Challenge", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Name input
        name_frame = ttk.Frame(self.frame)
        name_frame.pack(pady=10)
        
        self.name_label = ttk.Label(name_frame, text="What's your name?")
        self.name_label.pack(side=tk.LEFT, padx=5)

        self.name_entry = ttk.Entry(name_frame, width=20)
        self.name_entry.pack(side=tk.LEFT, padx=5)

        # Start button
        self.start_button = ttk.Button(self.frame, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        # Score and timer display
        stats_frame = ttk.Frame(self.root)
        stats_frame.pack(fill=tk.X, padx=20, pady=5)
        
        self.score_label = ttk.Label(stats_frame, text=f"Score: 0/0 (Question 0/{self.max_questions})", font=("Helvetica", 12))
        self.score_label.pack(side=tk.LEFT)
        
        self.timer_label = ttk.Label(stats_frame, text="Time: --", font=("Helvetica", 12))
        self.timer_label.pack(side=tk.RIGHT)
        
        # Status bar at the bottom
        self.status_bar = ttk.Label(self.root, text="Ready to play", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def start_game(self):
        self.player_name = self.name_entry.get()
        if not self.player_name:
            messagebox.showwarning("Input needed", "Please enter your name.")
            return
        
        self.clear_frame()
        greeting = ttk.Label(self.frame, text=f"Hi {self.player_name}, welcome!", font=("Helvetica", 14, "bold"))
        greeting.pack(pady=10)

        # Difficulty selection
        diff_label = ttk.Label(self.frame, text="Select difficulty level:")
        diff_label.pack(pady=10)  # padding is applied to pack() not to the Label itself

        diff_frame = ttk.Frame(self.frame)
        diff_frame.pack(pady=5)
        
        easy_btn = ttk.Button(diff_frame, text="Easy (20s)", command=lambda: self.set_difficulty("easy"))
        easy_btn.pack(side=tk.LEFT, padx=5)
        
        medium_btn = ttk.Button(diff_frame, text="Medium (15s)", command=lambda: self.set_difficulty("medium"))
        medium_btn.pack(side=tk.LEFT, padx=5)
        
        hard_btn = ttk.Button(diff_frame, text="Hard (10s)", command=lambda: self.set_difficulty("hard"))
        hard_btn.pack(side=tk.LEFT, padx=5)
        
        expert_btn = ttk.Button(diff_frame, text="Expert (5s)", command=lambda: self.set_difficulty("expert"))
        expert_btn.pack(side=tk.LEFT, padx=5)

        # Reset button
        self.reset_button = ttk.Button(self.root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        if difficulty == "easy":
            self.time_limit = 20
        elif difficulty == "medium":
            self.time_limit = 15
        elif difficulty == "hard":
            self.time_limit = 10
        elif difficulty == "expert":
            self.time_limit = 5
            
        self.status_bar.config(text=f"Difficulty: {difficulty.capitalize()}, Time limit: {self.time_limit} seconds")
        self.next_question()

    def start_timer(self):
        self.timer_running = True
        self.time_remaining = self.time_limit
        self.timer_label.config(text=f"Time: {self.time_remaining}s")
        
        def update_timer():
            if not self.timer_running:
                return
                
            if self.time_remaining > 0:
                self.time_remaining -= 1
                self.timer_label.config(text=f"Time: {self.time_remaining}s")
                # Schedule the next update using after()
                self.timer_id = self.root.after(1000, update_timer)
            else:
                # Time's up
                self.time_up()
        
        # Start the timer using Tkinter's after() method
        self.timer_id = self.root.after(1000, update_timer)

    def stop_timer(self):
        self.timer_running = False
        # Cancel any pending timer events
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def time_up(self):
        if not self.timer_running:
            return
            
        self.stop_timer()
        # Show the message in the main thread
        messagebox.showinfo("Time's Up!", f"Time's up! The correct answer was {self.current_question['capital']}.")
        # Schedule the next question
        self.root.after(100, self.next_question)

    def next_question(self):
        self.stop_timer()
        self.clear_frame()
        
        # Check if we've reached the maximum number of questions
        if self.total_questions >= self.max_questions:
            self.show_game_summary()
            return
        
        self.current_question = random.choice(countries)
        self.total_questions += 1
        
        # Update the score display
        self.score_label.config(text=f"Score: {self.score}/{self.total_questions-1} (Question {self.total_questions}/{self.max_questions})")

        # Create a frame for the question
        question_frame = ttk.Frame(self.frame)
        question_frame.pack(pady=10, fill=tk.X)
        
        # Display the question with country name and flag emoji
        question_text = f"What is the capital of {self.current_question['name']} {self.current_question['flag']}?"
        ttk.Label(question_frame, text=question_text, font=("Helvetica", 12)).pack(pady=5)

        # Get options based on difficulty
        options = self.get_options_by_difficulty()
        
        # Create options frame
        options_frame = ttk.Frame(self.frame)
        options_frame.pack(pady=10, fill=tk.X)
        
        # Create a grid of buttons
        row, col = 0, 0
        for option in options:
            btn = ttk.Button(options_frame, text=option, 
                          command=lambda opt=option: self.check_answer(opt), 
                          width=20)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky=tk.W+tk.E)
            col += 1
            if col > 1:  # 2 columns
                col = 0
                row += 1
                
        # Show additional information based on difficulty
        info_frame = ttk.Frame(self.frame)
        info_frame.pack(pady=10, fill=tk.X)
        
        if self.difficulty == "easy":
            hint_text = f"Hint: The capital starts with '{self.current_question['capital'][0]}'"
            hint_label = ttk.Label(info_frame, text=hint_text, font=("Helvetica", 10, "italic"))
            hint_label.pack()
        
        # Start the timer
        self.start_timer()
        
    def show_game_summary(self):
        """Display a summary screen at the end of the game"""
        summary_frame = ttk.Frame(self.frame)
        summary_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        # Display score and congratulatory message
        accuracy = (self.score / self.max_questions) * 100
        
        title_label = ttk.Label(
            summary_frame, 
            text="Game Over!", 
            font=("Helvetica", 18, "bold")
        )
        title_label.pack(pady=10)
        
        score_label = ttk.Label(
            summary_frame,
            text=f"You got {self.score} out of {self.max_questions} answers correct!",
            font=("Helvetica", 14)
        )
        score_label.pack(pady=5)
        
        accuracy_label = ttk.Label(
            summary_frame,
            text=f"Accuracy: {accuracy:.1f}%",
            font=("Helvetica", 12)
        )
        accuracy_label.pack(pady=5)
        
        if accuracy >= 80:
            message = "Excellent! You're an African geography expert!"
        elif accuracy >= 60:
            message = "Well done! You know Africa quite well!"
        elif accuracy >= 40:
            message = "Good job! You're learning about African capitals."
        else:
            message = "Keep practicing to improve your knowledge of African capitals!"
            
        feedback_label = ttk.Label(
            summary_frame,
            text=message,
            font=("Helvetica", 12)
        )
        feedback_label.pack(pady=10)
        
        # Buttons to play again or exit
        button_frame = ttk.Frame(summary_frame)
        button_frame.pack(pady=20)
        
        play_again_btn = ttk.Button(
            button_frame, 
            text="Play Again", 
            command=self.reset_game
        )
        play_again_btn.pack(side=tk.LEFT, padx=10)
        
        exit_btn = ttk.Button(
            button_frame, 
            text="Exit Game", 
            command=lambda: self.root.destroy()
        )
        exit_btn.pack(side=tk.LEFT, padx=10)

    def get_options_by_difficulty(self):
        # The correct answer
        correct_capital = self.current_question['capital']
        
        # Create different numbers of options based on difficulty
        # Now we'll always have 4 options minimum, but can add more for harder levels
        if self.difficulty == "easy":
            num_options = 4  # Changed from 3 to 4
        elif self.difficulty == "medium":
            num_options = 4
        elif self.difficulty == "hard":
            num_options = 5
        else:  # expert
            num_options = 6
            
        # Generate options
        options = [correct_capital]
        
        # For harder difficulties, add similar-sounding capitals to make it more challenging
        all_capitals = [country['capital'] for country in countries]
        
        # Sort capitals by similarity to the correct answer
        # For simplicity, we'll just use the first letter as a rough measure of similarity
        similar_capitals = [cap for cap in all_capitals 
                           if cap != correct_capital and cap[0] == correct_capital[0]]
        
        other_capitals = [cap for cap in all_capitals 
                         if cap != correct_capital and cap not in similar_capitals]
        
        # Add similar capitals first if they exist
        while len(options) < num_options and similar_capitals:
            option = random.choice(similar_capitals)
            if option not in options:
                options.append(option)
                similar_capitals.remove(option)
                
        # Fill the rest with random capitals
        while len(options) < num_options and other_capitals:
            option = random.choice(other_capitals)
            if option not in options:
                options.append(option)
                other_capitals.remove(option)
                
        # Shuffle the options
        random.shuffle(options)
        return options

    def check_answer(self, answer):
        self.stop_timer()
        
        if answer == self.current_question['capital']:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}/{self.total_questions} (Question {self.total_questions}/{self.max_questions})")
            
            # Calculate points based on time remaining and difficulty
            time_bonus = self.time_remaining
            diff_multiplier = {"easy": 1, "medium": 1.5, "hard": 2, "expert": 3}[self.difficulty]
            points = int(10 + (time_bonus * diff_multiplier))
            
            # Show success message with detailed info
            info = self.current_question
            messagebox.showinfo(
                "Correct!",
                f"Correct! 🎉 +{points} points\n\n"
                f"Country: {info['name']} {info['flag']}\n"
                f"Capital: {info['capital']}\n"
                f"Population: {info['population']}\n"
                f"Independence: {info['independence']}\n"
                f"President: {info['president']}\n"
                f"Currency: {info['currency']}\n"
                f"Official Language: {info['language']}\n"
                f"Fact: {info['facts']}"
            )
        else:
            messagebox.showerror("Wrong!", f"Oops! The correct answer was {self.current_question['capital']}.")
        
        self.next_question()

    def reset_game(self):
        self.stop_timer()
        self.score = 0
        self.total_questions = 0
        self.score_label.config(text=f"Score: 0/0 (Question 0/{self.max_questions})")
        self.timer_label.config(text="Time: --")
        self.status_bar.config(text="Ready to play")
        
        # Clear and recreate the frame
        self.frame.destroy()
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.setup_widgets()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

# Function to handle application closing
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit the game?"):
        root.destroy()

# Start the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CapitalGame(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)  # Handle window closing
    root.mainloop()