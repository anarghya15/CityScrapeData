# -*- coding: utf-8 -*-
import re
import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('wordnet', '/usr/share/nltk_data')
nltk.download('stopwords')

text = "Jodhpur (Hindi: .mw-parser-output .IPA-label-small{font-size:85%}.mw-parser-output .references .IPA-label-small,.mw-parser-output .infobox .IPA-label-small,.mw-parser-output .navbox .IPA-label-small{font-size:100%}IPA: listenⓘ) is the second-largest city of the north-western Indian state of Rajasthan after its capital Jaipur. As of 2011, the city has a population of 1.03 million. It serves as the administrative headquarters of the Jodhpur district and Jodhpur division. It is historic capital of the Kingdom of Marwar, founded in 1459 by Rao Jodha, a Rajput chief of the Rathore clan. On 11 Aug, 1947 four days prior to the Indian independence, Maharaja Hanwant Singh, the last ruler of Jodhpur state signed the Instrument of Accession and merged his state in Union of India. On March 30, 1949, it became part of the newly formed state of Rajasthan, which was created after merging the states of the erstwhile Rajputana Agency. Jodhpur is a famous tourist spot with a palace, fort, and temples, set in the stark landscape of the Thar Desert. It's also known as the Blue City due to the dominant color scheme of its buildings in old town. The old city circles the Mehrangarh Fort and is bounded by a wall with several gates. Jodhpur lies near the geographic centre of the Rajasthan state, which makes it a convenient base for travel in a region much frequented by tourists. The name \"Jodhpur\" is derived from its founder, Rao Jodha, who established the city in 1459. \"Jodh\" represents Rao Jodha, and \"pur\" means city or town in Sanskrit, making it the \"City of Jodha.\" Jodhpur city was founded in 1459 by Rao Jodha Rathore. Jodha succeeded in conquering the surrounding territory from the Delhi Sultanate and thus founded a kingdom that came to be known as Marwar. As Jodha hailed from the nearby town of Mandore, that town initially served as the capital of this state; however, Jodhpur soon took over that role, even during the lifetime of Jodha. The city was located on the strategic road linking Delhi to Gujarat. This enabled it to profit from a flourishing trade in opium, copper, silk, sandalwood, dates, and other tradeable goods. After the death of Rao Chandrasen Rathore in 1581, the kingdom was annexed by the Mughal Emperor Akbar, Marwar thus became a Mughal vassal, owing fealty to them while enjoying internal autonomy. Jodhpur and its people benefited from this exposure to the wider world as new styles of art and architecture made their appearance and opportunities opened up for local tradesmen to make their mark across northern India. Aurangzeb briefly sequestrated the state (circa 1679) after the death of Maharaja Jaswant Singh, but his son Maharaja Ajit Singh was restored to the throne by Durgadas Rathore at the death of Aurangzeb in 1707 ending the 30 year long Rathore rebellion. The Mughal empire declined gradually after 1707, but the Jodhpur court was beset by intrigue; rather than benefiting from circumstances, Marwar descended into strife and invited the intervention of the Marathas, who soon supplanted the Mughals as overlords of the region. In 1755 Jai Appa Scindia attacked Nagaur after looting several places of Rajasthan. Jai Appa halted his army near samas pond of Tausar which was 3.5 km from Nagaur fort. He surrounded Nagaur fort and cut off food and water supply. Maharaja Vijay Singh called Darbar and asked for volunteer to kill Scindia. Gaji Khan Khokhar (Chawata Kallan) and Kan Singh (Dotalai) were volunteered and took responsibility of killing Jaiappa Scindia. Both changed their outfit as traders and opened shop near Jaiappa's army. They observed their activities for two month. On 25 Jul 1755 on Friday at 11 am, when found opportunity attacked Jaiappa with daggers and killed him (Painting situated in Mandore museum). While fighting both the loyal Soldier of Jodhpur got killed. From then on a common proverb still people say \"Khokhar bada khuraki kha gaya appa jaisa daaki\" (Khokhar are great gluttons, eaten demon like appa). Even after killing of Jai Appa Sindhia Maratha army continued fighting for a few months near Nagaur but they lost hope after Jai Appa's death.Dissipated the wealth of the state, which sought the help of the British and entered into a subsidiary alliance with them. A major revolt occurred in 1857 by some Rathore nobles of Pali led by Thakur Kushal Singh of Auwa, but the rebels were defeated by the British Army under Colonel Holmes and peace was restored. During the British Raj, the state of Jodhpur had the largest land area in the Rajputana. The land area of the state was 93,424 km2 (36,071 sq mi) its population in 1901 was 44,73,759. It enjoyed an estimated revenue of £3,529,000. Its merchants, the Marwaris, flourished and came to occupy a position of dominance in trade across India. In 1947, when India became independent, the state merged into the union, and Jodhpur became the second-largest city of Rajasthan. At the time of division, the ruler of Jodhpur, Hanwant Singh, did not want to join India, but finally, due to the effective persuasion of Vallabhbhai Patel at the time, the state of Jodhpur was included in the Indian Republic. Later after the State Reorganisation Act, 1956 came into effect, it was included within the state of Rajasthan. As per provisional reports of Census India, Jodhpur had a population of 1,033,918 in 2011, consisting of approximately 52.62% males and approximately 47.38% females. The average literacy rate is 80.56 percent, approximately 88.42 percent for males and 73.93 percent for females. Approximately 12.24 percent of the population is under six years of age. Jodhpur city is governed by a Municipal Corporation which comes under Jodhpur Urban Agglomeration. The Jodhpur Urban/Metropolitan area includes Jodhpur, Kuri Bhagtasani, Mandore Industrial Area, Nandri, Pal Village and Sangariya. Its urban/metropolitan population is 1,137,815 of which 599,332 are males and 538,483 are females. With the inclusion of 395 villages in Jodhpur city in the month of February 2021 by JoDA, the new population count for the city is 2,330,000 and is expected to grow by 33.04% over the next decade. In the year 2031 population of Jodhpur city is expected to be more than 3.1 million. The population of Jodhpur city after expansion of city borders is 2,330,000. Jodhpur has a hot arid climate (Köppen BWh), just short of a hot semi-arid climate (Köppen BSh), due to its very high potential evapotranspiration. Although the average rainfall is around 362 mm (14.3 in), which falls mostly from June to September, it fluctuates greatly. In the famine year of 1899, Jodhpur received only 24 mm (0.94 in), but in the flood year of 1917, it received as much as 1,178 mm (46.4 in). Jojari river, a tributary of Luni River, flows from Banad to Salawas in Jodhpur Urban Area. A Riverfront project is approved and is in Planning for this river for 35 km length coming inside Jodhpur Urban Area which is under Nammi Ganga Project of Ministry of Jal Shakti from January 2021, earlier this project was under Jodhpur Development Authority. Pin Code of Jodhpur is 342001 which comes under Jodhpur postal division (Jodhpur Region). Temperatures are extreme from March to October, except when the monsoonal rain produces thick clouds to lower it slightly. In April, May, and June, high temperatures routinely exceed 40 °C. During the monsoon season, average temperatures decrease slightly, but the city's generally low humidity rises, which adds to the perception of the heat.The highest temperature recorded in Jodhpur was on 20 May 2016, when it rose to 48.8 °C (119.8 °F). Jodhpur contributes $4 billion (approx) to Rajasthan's economy through different Industries. It is also considered the center of India's $200 million handicraft industry. The city is also a major tourist destination, claiming some of the top heritage hotels in India. Jodhpur also has the largest standardized test training industry in western Rajasthan, with top coaching institutes for the IIT-JEE, NEET-UG and NEET-PG, and Civil Service Exams. Hindustan Petroleum Corporation Limited (HPCL) and the government of Rajasthan have been working since 2018 on a joint project to construct a refinery in Pachpadra, Barmer district with a capacity of nine MMTPA (million metric tonnes per annum). The refinery is expected to come online in January 2024, and was described by Union Petroleum Minister Hardeep Singh Puri as \"...the 'Jewel of the Desert', bringing jobs, opportunities and joy to the people of Rajasthan...\". Pachpadra lies just 60 kilometres from the industrial area of Boranada in Jodhpur. Around 120 by-products produced by the refinery are expected to provide major opportunities for new industries to be set up in and around Jodhpur. India's most ambitious industrial development project, the over US$100 billion Delhi-Mumbai Industrial Corridor Project is also expected to impact the industrial scenario in Jodhpur in a big way. Marwar Junction, which is located about 100 kilometres from the city, will be one of the nine freight loading points along the DMIC route. Inaddition, both the Jodhpur and Pali districts fall under the region that is planned to be developed as a manufacturing hub for the DMIC. The present Member of Parliament from Jodhpur is Gajendra Singh Shekhawat of the BJP. Jodhpur is a significant city of western Rajasthan and lies about 250 km from the border with Pakistan. This location makes it a key base for the Indian Army, Indian Air Force (IAF), and Border Security Force. Jodhpur's South Western Air Command is one of Asia's largest and one of the most critical and strategically located airbases of the IAF (The Jodhpur Airport played the crucial role during the Indo-Pakistani wars of 1965 and 1971) deployed fighter jets and advanced light helicopters. There are 5 squadrons of Indian Air force which known as 32 wing. Jodhpur has culturally been known by the name of Jodhana by the locals. The city is famous for its food and its popularity can be judged by the fact that one can find sweet shops named \"Jodhpur Sweets\" in many cities throughout India. Being at the onshore of Thar Desert, life has been influenced by ways of select nomadic tribes (so-called \"gypsy\" groups – Banjara in Hindi – have settled in some parts of the city). Jodhpur has distinct cultural identity through its food and is famous for its Mirchi Bada, Rabdi Ghewar and Mawa Kachori. Jodhpur's most notable attractions are Mehrangarh Fort which overlooks upon the city, the blue bylanes of the old city are also an attraction, Umaid Bhawan Palace, Jaswant Thada, and the Ghanta Ghar, or Clock Tower. Tourists are also within proximity to Mandore Garden, Kaylana Lake and Garden, Balsamand Lake, Machia Biological Park, Rao Jodha Desert Rock Park, Ratanada Ganesh Temple, Toorji Ka Jhalra, Sardar Samand Lake and Palace, Masooria Hills, Veer Durgadas Smarak (monument, park, and museum), Surpura Dam and Bhim Bhadak Cave. Other attractions of people are at markets of food, antique items, traditional clothes and traditional shoes (also called Jodhpuri Mojari) held in Jodhpur. Mahamandira, a temple consecrated to Sri Jalandharnath, is known for its murals showing ascetics in yoga poses and murals bearing inscriptional records of the dignitaries visiting the shrine which includes Charanas, nobles, and the Rajas. The city is famous for its charming locations and is often featured in various films, advertisements, music videos, and soaps. The historic buildings and landscapes of the city were featured in a number of movies, including The Dark Knight Rises directed by Christopher Nolan; Baadshaho starring Ajay Devgn and Emraan Hashmi, The Darjeeling Limited starring Owen Wilson, Adrien Brody, and Jason Schwartzman; The Fall directed by Tarsem Singh; Hum Saath-Saath Hain directed by Sooraj Barjatya; Veer directed by Anil Sharma; Shuddh Desi Romance directed by Maneesh Sharma; I directed by S. Shankar, Kung Fu Yoga starring Jackie Chan, Sonu Sood, and Disha Patani; Loafer starring Varun Tej and Disha Patani; Supreme starring Sai Dharam Tej and Rashi Khanna; and Airlift featuring Akshay Kumar and Nimrat Kaur. Many foreign-language films and series have also been shot in Jodhpur, such as Buddies in India, which was produced in Mandarin and was launched in China in 2017 featuring some Indian actors, and even the songs were in Hindi. A number of dishes from Indian cuisine originated in Jodhpur. The city savours a number of food items, but the specialties of the city are Pyaaj Kachori, Mirchi Bada and Mawa Kachori.Dal-Baati-Churma, Makhaniya Lassi, Ker Sangri are also some famous foods in Jodhpur. Educational facilities include: Major research institutes and organizations have been established in the city for promoting research: Rajasthan High Court is the High Court of the state of Rajasthan. It was established on 21 June 1949 under the Rajasthan High Court Ordinance, 1949. The High Court of Rajasthan was founded in 1949 in Jodhpur and was inaugurated by the Rajpramukh, Maharaja Sawai Man Singh on 29 August 1949. The first Chief Justice was Kamala Kant Verma and the current Chief Justice of the Rajasthan High Court is the Honorable Justice Manindra Mohan Shrivastava. A bench was formed at Jaipur which was dissolved in 1958 and was again formed on 31 January 1977. Currently, there are forty sanctioned judges. Till 2020, the city was administered by a single municipal body, Jodhpur Nagar Nigam with a mayor. In 2019, the Rajasthan government  decided to form two municipal corporation in Jaipur, Jodhpur and Kota for better administration. For administrative purposes, the city is divided into wards, from which the members of the corporation council are elected for five years. The municipal corporation has elected members known as councilors, or parshad in Hindi, representing their respective wards (geographical units of the city). The ward members are elected by direct voting by electorate for a period of 5 years. In addition to these directly elected members, the corporation has four ex-officio members (one member of parliament, three members of legislative assembly, namely Sardarpura, Soorsagar, City), and three nominated members. Currently, the city has two civic bodies – Jodhpur North and Jodhpur South each headed by a mayor. Each municipal corporation has 80 wards, making a total of 160 wards in the city. The Jodhpur Development Authority (JDA) executes and supervises plans and schemes for the development of the urban region. The city has well-established rail, road, and air networks connecting it to other major cities of the country. For experiencing the true magnificence and royal opulence of Rajasthan, luxury trains Palace on Wheels, Royal Rajasthan on Wheels, and Maharaja Express are run jointly by Rajasthan Tourism Development Corporation and Indian Railways. Jodhpur is one of the destinations of both of the trains. In 2012-13 Railway Budget,A plan for building a High Speed Rail Corridor between Delhi-Jodhpur via Jaipur and Ajmer of 591 km was introduced which later in 2020 was included in HSR by Indian Railways and Government of India and now is in Pre-Feasibility phase. In 2013, a plan to start metro train service in Jodhpur was proposed by then Rajasthan Government to decongest the city traffic. However, this proposal is still pending with the state government for its approval.But in 2021, Jodhpur Development Authority and Municipal Corporations made a Future Mobility Plan where a 35-km Metro Line is proposed from IIT Jodhpur to Jaisalmer Bypass after Year 2030. With another proposed 11 more BRTS Corridors in Jodhpur between 2021–2030 to provide public transport to the increasing population before starting Metro. Suburban stations around Jodhpur: Jodhpur Airport is one of the prominent airports of Rajasthan. It is primarily a military airbase with a civilian enclosure to allow for civilian air traffic. Due to Jodhpur\'s strategic location, this airport is regarded as one of the most important ones for the Indian Air Force. At present,  direct flights from Ahmedabad, Belgaum, Bengaluru, Chennai, Delhi, Hyderabad, Indore, Kolkata and Mumbai to the city are operated by Air India Indigo, SpiceJet, Vistara and Star Air. The bill and basic formalities for the long-awaited expansion of the airport were cleared by all the concerned authorities in June 2016, clearing the way for the expansion of the airport in two phases beginning February 2016. After the expansion, morning and evening flights are expected from the city to more cities than presently available, in addition to more airlines coming to and from the city. Jodhpur is connected by road to all major cities in Rajasthan and neighboring states, such as Delhi, Ahmedabad, Surat, Ujjain, and Agra. Apart from deluxe and express bus services to cities within the state, Rajasthan Roadways provides Volvo and Mercedes Benz bus service to Delhi, Ahmedabad, Jaipur, Udaipur, and Jaisalmer. In 2016, Bus Rapid Transit System Jodhpur was launched in the city with low-floor and semi-low-floor buses plying on 6 major routes.Jodhpur is connected to the National Highway network with three national highways and to the Rajasthan State Highway network with 10 state highways.Jodhpur Ring Road is under construction encircling Jodhpur to reduce vehicular traffic. National highways passing through Jodhpur include: State highways passing through Jodhpur are: Paota Bus Stand is a most important bus stand for all the government and private buses for Jodhpur route which is operated by RSRTC. This Bus stand serves to various rural and urban areas. This is a biggest Bus stand in Jodhpur. Jodhpur has two outdoor stadiums and one indoor stadium complex. Barkatullah Khan Stadium has hosted two cricket one day internationals matches. Maharaja Umaid Singh Stadium and Gaushala Maidan Sports Complex are also among other sports facilities.The city has a well developed polo ground where tournaments are held occasionally. Jodhpur has these FM stations: Tehsils of Jodhpur:"

text = text.lower()  # Lowercase
pattern = r'\((?!(mw-parser-output|English|Bengali pronunciation|Kannada pronunciation|IPA|Gujarati|Hindi))[^)]+\)'
text = re.sub(pattern, '', text)
text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
# Remove stop words
stop_words = set(stopwords.words('english'))
words = text.split()

# Lemmatize and remove stop words
filtered_words = [word for word in words if word not in stop_words]
text = ' '.join(filtered_words)

print('Final text: ', text)