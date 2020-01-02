## Portfolio opgave nr. 1

Det datasæt vi har fået foræret til at få løst portfolio nr. 1 handler om Titanic færgens forlis. Og vi skal foretage nogle enkle analyser på indhold i datasættet. Indledningsvis ved at kigge data igennem (den menneskelige intellekt og med egne øjne iagttaget), og derefter skal vi ved hjælp af data analyse processer skabe os et (digitalt) overblik over indholdet og formatet af den delte *.csv fil.
Denne sidste process foregå ved hjælp af Python, samt to relevante "add on biblioteker", kaldet Pandas og Numpy. 
Pandas er et Open Source Python bibliotek ideelt til indledende data analyse. Det gør det muligt at arbejde i Python med "spreadsheet like data for fast data loading, manipulating, aligning and merging"(1)
Pandas tilføjer nye datatyper til selve Python programmet, dels *Series* og *DataFrame*. DataFrame er uniktt for Pandas, og repræsenterer hele ens spreadsheet/data i en RAMME, mens Series blot er een enkelt kolonne af denne Dataframe.
Numpy er ligeledes Open Source bibliotek til Python programmering, og her er fokus på store, multi-dimensionelle "arrays og matrices", tilsat en stor samling af matematiske funktioner. 
Pandas og Numpy er afhængige af hinanden og begge biblioteker skal importeres til ens Python installation for optimal udnyttelse. 

Kurset her har bevist, at Data Analyse aspektet ofte tager størstedelen af den tid, som bør afsættes til at arbejde med data. Det er vigtig at forstå datasættet uanset størrelse. For at kunne foretage reelle "data manipulationer" kræver det at man har indsigt, overblik og kender sine data grundigt, da forkert kodning/programmering kan få fæle konsekvenser og skæve resultater, hvis ikke man bearbejder data korrekt. Derfor er god forståelse for kode samt god forståelse og indsigt i ens data vigtige parametre inden data analysen foretages. 
Desuden skal man behandle data ordentligt,  både ud fra data etiske overvejelser som anonymisering hvor det kan være krævet (interviews, surveys), men også korrekt citering/kreditering af data er vigtig, når man evt. finde åbne datasæt via Scraping eller API løsninger, men også når man finder sine datasæt fra repositories som Zenodo, Figshare eller Dryad for selv at arbejde videre med disse tilgængelige data. 
I tilfældet med Portfolio 1 *Titanic datasættet* så kan man finde dette og lignende datasæt fra Titanic mange steder via nettet - dels har sitet Kaggle link til datasættet (https://www.kaggle.com/c/titanic-gettingStarted/data) men også et slutbrugerprodukt som databasic.io anvender titanic data (https://www.databasic.io/en/wtfcsv). Vi har ikke fået en konkret kilde anvist til vores datasæt, men det er tydeligt, at portfolio 1 *Titanic datasættet* ikke er helt det samme som ovenfor nævnte.

At data og konkrete datasæt let kan forefindes via enkle og målrettede søgninger på www er resultatet af hele ideologien bag begrebet Open Science ((Fra Open Science Training Handbook https://open-science-training-handbook.gitbook.io/book/introduction). Open Science har som vigtigste formål at samarbejde, synliggøre og sørge for at data let kan gennemskues og er transparent. Umiddelbart for at imødekomme "bedrageri og videnskabelig uredelighed", men også for at kunne genbruge nyttige datasæt i egen forskning og studie. Derfor stilles der fremadrettet krav til ordentlig beskrivelse af datasæt ( metadata beskrivelser ) og man skal ligeledes tilføje parametre som brugslicens, redistribuering, storage, reproductions - hvilket i dag betyder, at man bør (og skal ) beskrive sine datasæt, uanset om de er frit tilgængelige eller ej. Disse principper som anvendes til det hedder FAIR principperne, og betyder i bund og grund, at "læseren af datasættet" skal være i stand til følgende: 
FIND, ACCESS, INTEROPERATE og REUSE data (https://en.wikipedia.org/wiki/FAIR_data) - dvs. data skal være beskrevet ud fra nogle bbør man også kunne gennemskue, udfra hvilke terme man kan anvende datasæt man finder. 

. korrekt, og endda holder en ordentlig data-struktur i sin kode, så det er let at gennemskue, hvad der foregå - selv for een selv. 
Kurset er jo ikke et decideret programmerings-kursus, men læringskurven var stejl, og behovet for basal programmeringsforståelse viste sig at være meget nødvendig, men i løbet af kursusforløbets ca. 3 måneder og processen mod målet har været så lærerig, inspirerende og utrolig nyttig. Respekten for, at Data Analyse tager tid, at der er flere parametre end blot adgang til data og interesse i data er relevant, samt naturligvis, at der skal afsættes masser af tid til at foretage data analyserne så det gøres klart og gennemskueligt, har været en fantastisk øjenåbner.

# Vejen til målet 

  arbejde som finder sted, når man indsamler, undersøger og vurderer data. Man er nødt til at danne sig et overblik over, hvilken type data man har at arbejde med  inden man foretager konklusioner ud fra "formodninger". Python (inkl. Pandas og Numpy bibliotekerne) gør det muligt at undersøge datasæt nærmere for herved at kunne uddrage og konkludere på data. Data analysen og programmeringsdelen tager derfor en betydelig del af eens tid, inden man når til mere synlige (visualiseringer) fortællinger og resultater. Vejen til overblik kræver en del Data Munging, og en stor del kendskab til valgt programmeringssprog.

Enkle scripts og programmerings-snippets udarbejdet i eksempelvis et program som Python kan lette denne data analyse process, gøre den mere automatisk og re-producerbar. Åbenhed om den data analyse metode man har anvendt medfører, at andre vil kunne genskabe lignende, måske endda nøjagtig samme resultater - til glæde for andre forskere og studerende, til gavn for samfundet, til nytte for videnskaben.. Begrebet som at være "Data Savvy" gælder for alle idag - ikke kun i forskningsmiljøer, og programmering og viden om programmering bliver et stadig stigende krav til alle, som arbejder med vidensarbejde. Der er "indirekte" krav til Data Literacy på alle niveauer, og derfra hvor min arbejdsverden udspringer, så mærkes det tydeligt, at udviklingen hen i mod større data forstålse, ønske om support og servicetiltag i forbindelse med Data Management, Data håndtering (licenser, etik, citationer, storage, curaation) bliver stadig større. 
Viden om enkle programmeringssprog som eksempelvis Python, at kunne læse "et styk kode uden af flippe ud" og samtidig kunne omsætte dette til noget praktisk anvendeligt har været målet. Jeg har klart fokus på læring, formidling og videndeling. Og programmering kan lette mange opgaver i dagens forskningsbibliotek. Både overfor brugerne, men også i de mange daglige driftsopgaver, som foregår i et stort forsknings- universitetsbibliotek. At kunne tænke smarte løsninger ud fra "trivielle og gentagne opgaver" vil helt klart være mit fokus fremadrettet.

Eftersom et program/script kan udvikles, genbruges og tilpasses, så lignende analyser/undersøgelser kan foretages over flere & lignende datasæt, så kan jeg slet ikke vente med at komme længere ind i programmerings-sprogets verden. 

**** her skal indsættes nogle af de open science, open data, science data overvejelser som kurset skal forholde sig til - etiske, licens, FAIR. 

 - og Titanic datasættet består af følgende 8 kolonner og 887 rækker 
>>> print(titanic.shape) 

# selve programmet som undersøger datasættet nærmere findes dels via Github (... stien ind her... ) og i slutningen af dette dokument 




(1): Pandas for Everyone Python Data Analysis, First edition 