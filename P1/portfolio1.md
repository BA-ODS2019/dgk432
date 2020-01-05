# Portfolio opgave nr. 1

Det datasæt vi har fået foræret til at løse Portfolio nr. 1 handler om Titanic færgens forlis (https://github.com/BA-ODS2019/dgk432/blob/master/data/titanic.csv). 
Opgaven går ud på at foretage nogle enkle analyser på indhold i datasættet ved brug af Python og Pandas biblioteket, bl.a. 

## Opgaven lyder som følgende:
1. Åben filen i en tekst-editor og se på indholdet.

    Hvilke data typer kan i identificere? (tekst / tal / typer af tal mv)

   Mangler der data?
2. Ved at bruge panda – api skal i importere data til en dataframe.

    Beskriv nu data-sættet med de funktioner der findes i Pandas til beskrivelse af en
dataframe ( se f.eks i https://datacarpentry.org/python-socialsci/08-Pandas/index.html )

3. Og nu er det op til jer at udtrække og beregne på data i filen som kan give os informationer om de personer der var involveret i ulykken fx hvor mange overlevede?, gennemsnitsalder og medianen alder på personerne? (Dvs deskriptiv statistik)

4. Findes der personer med samme efternavn?

5. I skal nu lave en pivot-tabel som viser hvor mange der rejste på hhv 1., 2. og 3. klasse.  

    Hvilken rejseklasse havde flest omkomne?

Løsningen på ovenstående opgave kan naturligvis ses i tilhørende python script - som kan findes via https://github.com/BA-ODS2019/dgk432/blob/master/P1/portfolio_1.py 

### Ad spm 1
Indledningsvis har jeg blot åbnet filen via min texteditor ( Visual Code Studio i mit tilfælde) og med "menneskelige intellekt og egne øjne" tjekket datasættet for indhold, herunder kolonne overskrifter mv. Datasættet består at både tekst og heltal/decimaltal, og der synes ikke at mangle nogle data i de mange rækker af data. 

### Ad spm. 2
Her skal vi ved hjælp af data analyse processer skabe os et (digitalt) overblik over indholdet og formatet af den delte *.csv fil. 
Denne sidste process foregå ved hjælp af Python, samt to relevante "add on biblioteker", kaldet Pandas og Numpy. 
Pandas er et Open Source Python bibliotek ideelt til indledende data analyse. Det gør det muligt at arbejde i Python med "spreadsheet like data for fast data loading, manipulating, aligning and merging" (https://learning.oreilly.com/library/view/pandas-for-everyone/9780134547046/).
Pandas tilføjer nye datatyper til selve Python programmet, dels *Series* og *DataFrame*. DataFrame er unikt for Pandas, og repræsenterer hele ens spreadsheet/data i en RAMME, mens Series blot fokuserer på een enkelt kolonne af denne Dataframe.
Numpy er ligeledes et Open Source bibliotek til Python, her er fokus på store, multi-dimensionelle "arrays og matrices" (tal), tilsat en pæn, stor samling af matematiske funktioner. 
Pandas og Numpy er afhængige af hinanden og begge biblioteker skal/bør importeres til ens Python installation for optimal udnyttelse. 
Datasættet er i første omgang undersøgt via en Data Carpentry lesson https://datacarpentry.org/python-socialsci/08-Pandas/index.html om basis Data Analyse vha Pandas.

### Ad spm. 3 - 4 og 5, så fremgår resultaterne af scriptet 
Men eftersom at data automatisk indlæses som en DataFrame, så kan man let via enkle statements kan danne sig et overblik over størrelsen på ens datasæt eks. >>> print(titanic.shape) giver resultatet 8 kolonner/887 rækker, og >>> print(titanic.columns) giver mig overskrifterne på de 8 kolonner, som jeg efterfølgende skal arbejde med.

# Arbejdet med data ( store og små datasæt )  

Arbejdet med store datamængder (eller små) handler om mere en blot ren kodning. Data Analyse og Data "cleaning" aspektet har vist sig at tage en stor del af den tid, man afsætter til at arbejde med data. Det er vigtig at forstå datasættet uanset størrelse. For at kunne foretage reelle "data manipulationer" kræver det at man har indsigt, overblik og kender sine data grundigt, da forkert kodning/programmering kan få fæle konsekvenser og skæve resultater, hvis ikke man bearbejder data korrekt. Derfor er god forståelse for kode samt god forståelse og indsigt i ens data vigtige parametre inden data analysen foretages. 
Desuden skal man behandle data ordentligt,  både ud fra data etiske overvejelser som anonymisering hvor det kan være krævet (interviews, surveys), men også korrekt citering/kreditering af data er vigtig, når man evt. finde åbne datasæt via Scraping eller API løsninger, men også når man finder sine datasæt fra repositories som Zenodo, Figshare eller Dryad for selv at arbejde videre med disse tilgængelige data. 
I tilfældet med Portfolio 1 *Titanic datasættet* så kan man finde dette og lignende datasæt fra Titanic mange steder via nettet - dels har sitet Kaggle link til datasættet (https://www.kaggle.com/c/titanic-gettingStarted/data) men også et slutbrugerprodukt som databasic.io anvender titanic data (https://www.databasic.io/en/wtfcsv). Vi har ikke fået en konkret kilde anvist til hvor vores datasæt er hentet fra, men det er tydeligt, at portfolio 1 *Titanic datasættet* ikke er helt det samme som ovenfor nævnte. Vores sæt har færre kolonner og rækker.

I Open Science Training Handbook, kapitel 4 ( https://open-science-training-handbook.gitbook.io/book/open-science-basics/reproducible-research-and-data-analysis ) beskrives de 5 trin af den videnskabelige metode:

* 1. Formulating a hypothesis
* 2. Designing the study
* 3. Running the study and collecting the data
* 4. Analyzing the data
* 5. Reporting the study

Open Science har fokus på åbenhed, og hver af de 5 trin skal beskrives klart vha åben dokumentation, så studiet/forskningen gøres genneskuelig og transparent. I første omgang for at imødekomme "bedrageri og videnskabelig uredelighed", men også for at kunne genbruge nyttige datasæt til ny forskning og studie. 
I gamle dage skulle metodeafsnittet i et paper beskrive, hvordan data var indsamlet og anvendt, fremadrettet skal data også beskrives udførligt ( metadata-beskrivelser til samtlige dele af forsknings-data-sæt). Metadata beskrivelserne omfatter parametre som ophav, ansvarlig, brugslicens, redistribuering, lagring, reproduktion - hvilket i dag betyder, at man kan (og skal ) beskrive sine datasæt, uanset om selve datasættet i sig selv er frit tilgængelig eller ej. 
En måde man kan gøre dette er ved anvendelse af "FAIR principperne". FAIR står for 
FINDABLE, ACCESSIBLE, INTEROPERABLE, og REUSEABLE (https://en.wikipedia.org/wiki/FAIR_data) - dvs. data skal være beskrevet ud fra nogle standarder som gør det let at gennemskue hvad det er for data, hvordan man evt. kan få adgang, hvordan det vedligeholdes osv. 

# Overvejelser her på falderebet
Kurset er jo ikke et decideret programmerings-kursus, og læringskurven var stejl. Færdigheder i basal programmeringsforståelse viste sig at være meget nødvendig for at komme i mål med opgaverne. Men i løbet af kursusforløbet har de mange øvelser vist sig nyttige. Respekten for at Data Analyse tager tid er helt klart noget som jeg tager med mig fra kurset. Og det at kunne planlægge og udføre analyseopgaver kan først for alvor omfavnes, når man har de teoretiske og håndværksmæssige begreber på plads. Dataforståelse, kode-flair og viden om hvad man må med data og hvordan spiller en lige så stor rolle - i min verden (universitetsbibliotek) kalder vi den samlede pakke for DATA LITERACY. 
Der er "indirekte" krav til Data Literacy på alle niveauer, og derfra hvor min arbejdsverden udspringer, så mærkes det tydeligt, at udviklingen hen i mod større data forstålse, ønske om support og servicetiltag i forbindelse med Data Management, Data håndtering (licenser, etik, citationer, storage, curaation) bliver stadig større. 

Det at nødvendigt at forstå flere parametre end blot adgang til data og interesse for programmering. At nå til det stadie, hvor man kan gennemskue kode, kan "formulere de rette spørgsmål til "fejlfinding, support, råb om hjælp" via eks. https://stackoverflow.com/ og nettet generelt, så er man nået langt. Men derfra kræves cases og masser af øvelse.
For at nå næste læringsniveau - at sætte teori og læring ind i den praktiske arbejdsopgave - er man nødt til at have konkrete opgaver og bare blive ved med at anvende det lærte.

Enkle scripts og programmerings-snippets udarbejdet i eksempelvis et program som Python kan lette denne data-analyse proces, gøre den mere automatisk og re-producerbar. Åbenhed om den data-analyse-metode man har anvendt medfører, at andre vil kunne genskabe lignende, måske endda nøjagtig samme resultater - til gavn for samfundet, til nytte for videnskab & studier.

Kurset har gjort, at jeg nu føler mig bedre rustet til de mange nye opgaver, som kan løses med enkle scripts og lidt programmerings-krydderi.
Det at kunne læse "et styk kode uden af flippe ud" og samtidig kunne omsætte dette til noget praktisk anvendeligt har været målet. Mine primære arbejdsopgaver handler om og har fokus på læring, formidling og videndeling. At være DATA SAVVY på et teknisk universitet er nødvendig. Og det er min overbevisning, at lidt programmeringskendskab kan lette mange opgaver i dagens forskningsbibliotek. Både overfor brugerne, men også i de mange daglige driftsopgaver, som finder sted i nutidens fag,- forsknings,- og universitetsbiblioteker. 
At kunne tænke smarte løsninger ud fra "trivielle og gentagne opgaver" vil helt klart være mit fokus fremadrettet.

