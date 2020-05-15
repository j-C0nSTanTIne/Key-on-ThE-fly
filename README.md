# Key on ThE fly
Software in python per generare in modo sicuro password complesse in base alle risposte fornite a determinate domande, senza che le risposte e le password generate vengano salvate. 

# Descrizione

Si sa che una password, per essere buona, dovrebbe:
* essere lunga
* non contenere parole di senso compiuto
* contenere anche numeri, caratteri maiuscoli e speciali.  

Un *primo* metodo sarebbe quello di affidarsi alla propria memoria, ma risulterebbe praticamente impossibile ottenere una password con le superiori caratteristiche.  
Un *secondo* metodo sarebbe quello di affidarsi ad un software che genera password complesse per noi. Tuttavia, queste password vengono poi salvate, e dunque possono essere rubate. Generalmente questi software salvano le password generate in appositi archivi cifrati, che per essere aperti necessitano di una "master" password da ricordare, tornando dunque al punto di partenza.  
Un *terzo* metodo sarebbe allora quello di avere un software che genera ogni volta **LA STESSA PASSWORD COMPLESSA** se l'Utente fornisce **LE STESSE RISPOSTE** a determinate domande **da lui pre-impostate**. Ciò che tenta di fare il programma qui presentato e scritto in *python*.

La generazione avviene "al volo", nel senso che il software non salva alcuna password, che quindi non può essere rubata. Nè vengono salvate le risposte.
Il software si limita a fare delle domande all'Utente, ed in base alle risposte fornite genera sempre e comunque una password. Se le risposte fornite sono corrette, la password sarà quella originaria, altrimenti no.
Con tale software l'Utente crea due/tre domande da fare, e solamente queste domande vengono salvate nel database dell'applicazione.
L'applicazione, poi, estrarrà le domande dal database, le sottoporrà all'Utente, ed in base alle risposte fornite genererà una password complessa.  

La forza di questo programma dipende dunque esclusivamente dalla capacità dell'Utente di creare domande per le quali lui e lui soltanto può conoscere le risposte, le quali dovranno essere sempre identiche per generare la stessa password.
La bontà di questo meccanismo è evidente: ognuno di noi sa qualcosa che nessun'altro sa, che non abbiamo mai pubblicizzato sui social network, che non abbiamo mai rivelato ad anima viva. Oppure riferimenti, citazioni, gusti, eventi del passato, sogni etc... che solamente noi possiamo dedurre/sapere/ricavare in base alle domande presentate.  
Ad esempio: se come domanda imposto *«la mia squadra di calcio preferita»* e la mia pagina facebook è piena di riferimenti alla juventus (che è poi la risposta da me impostata), ovviamente il meccanismo diventa debolissimo.
Già il meccanismo migliorerebbe se impostassi la domanda *«la mia squadra di calcio preferita»* e la risposta *«nessuna»*, creando quindi una risposta inaspettata.
Ma se invece imposto domande su cose che solamente io posso conoscere, oppure su prove/quiz/indovinelli che solamente io saprei risolvere conoscendo i necessari riferimenti, oppure formulate in una lingua ma che richiedono una risposta in una lingua diversa, oppure ancora formulate in modo estramemente oscuro ma per me chiaro, o che fanno riferimento ad eventi del mio passato e così via, allora un attaccante non potrà indovinare le risposte e generare la password corretta.

## Getting Started

Il codice è ricompreso in due file *.py*, «**Key on ThE fly.py**» (il quale gestisce l'interfaccia da riga di comando che interagisce con l'Utente) e «**funcs.py**» che contiene le classi e le funzioni utilizzate (e importate) dal primo.  
Scaricandoli nella medesima directory ed avendo python 3.x installato sul pc, si può eseguire il software con:  
`python "Key on ThE fly.py"`  

Altrimenti, viene fornito anche l'eseguibile già creato utilizzando *pyinstaller*, «**Key on ThE fly.exe**», che basta scaricare ed eseguire.

## Prerequisiti

Python 3.x installato se viene eseguito il codice, altrimenti per l'eseguibile non occorre nulla.  
Le librerie generali utilizzate dal codice sono *sys, random, sqlite3, os.path, hashlib*

## Utilizzo

Per vedere quali operazioni "tecniche" esegue il codice, si rimanda al diverso file «*descrizione_codice.md*» nel quale sono spiegate più tecnicamente le diverse fasi.  

Per quanto riguarda invece l'utilizzo generale del programma:
* Tre sono le possibili operazioni: creare una istanza, selezionare una istanza, eliminare una istanza
* Per "istanza" si intende la situazione in cui occorre la password, ad esempio "gmail", "hotmail", "sito aziendale" etc...
* Prima occorre creare una o più istanze (il database dell'applicazione verrà creato al primo utilizzo)
    * Nella creazione dell'istanza dovrà darsi un nome significativo all'istanza (ad esempio "hotmail") e si potrà inserire una breve descrizione della stessa
    * Si dovrà selezionare la lunghezza della password desiderata fra quelle indicate, minimo 8 - massimo 128. Si consiglia di sceglierla il più lunga possibile
    * Si potranno indicare eventuali caratteri speciali - fra quelli indicati - da non utilizzare nella password, perchè ad esempio vietati dallo specifico sito per il quale occorre la password
    * Quindi andranno fornite le domande e le risposte. Il numero minimo e necessario di domande è due, la terza è opzionale, anche se si consiglia di implementarla
    * Nel fornire le risposte non ha importanza il carattere maiuscolo, perchè poi dal programma verranno sempre convertite tutte in minuscolo
    * Prestare la massima attenzione nelle risposte fornite, che dovranno sempre essere le stesse per generare la stessa password. Un carattere diverso causerà una password diversa. Ad esempio: entrambe le risposte «BRUCE SPRINGSTEEN» e «bruce springsteen» vanno bene, perchè il programma converità comunque le risposte in minuscolo ottenendo il medesimo risultato. Invece le risposte «bruce springsteen» e «springsteen bruce» sono diverse e genereranno password diverse
    * Al termine dell'inserimento il software chiederà se creare l'istanza. In caso di risposta positiva, le domande inserite verranno salvate nel database
* Creata una istanza, la si potrà selezionare all'occorrenza
    * Selezionata una istanza, il software estrarrà le domande dal database presentandole all'Utente, che dovrà rispondere per generare la password
    * Se le risposte fornite saranno identiche a quelle originariamente inserite dall'Utente, la password generata sarà la stessa
* Sarà possibile anche eliminare dal database una o più istanze precedentemente create

### Versione grafica

L'attuale codice è una beta, certamente migliorabile.  
Inoltre è in via di realizzazione la versione grafica utilizzando *tkinter*.

### Licenza

Sinceramente mi secca studiare le varie licenze disponibili.  
In generale, se qualcuno è interessato può liberamente esportare, modificare ed usare il codice per qualsiasi fine, con l'unico limite di citarne la paternità.

### Autore

*Dario Brocato*
