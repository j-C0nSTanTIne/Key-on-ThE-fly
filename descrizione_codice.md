# SPIEGAZIONE GENERALE DEL CODICE

* Il codice python fa inserire all'utente un minimo di due domande, un massimo di tre, con le relative risposte (convertite in minuscolo). Solamente le domande verranno poi salvate nel database sqlite3;
* Per ciascuna risposta il codice trova l'hash SHA512, creando una stringa alfanumerica di 128 caratteri. Le lettere [A B C D E F] di ciascun hash vengono convertite nei numeri [ 10 11 12 13 14 15], in modo da avere una stringa solamente numerica;
* I numeri dell'hash della prima risposta vengono convertiti in lettere minuscole e numeri [a-z0-9] grazie ad un dizionario {1 : "a", 2 : "b"...};
* I numeri dell'hash della seconda risposta vengono convertiti sia in caratteri speciali [ ! $ % ( ) = ?" , _ - ] sia in lettere maiuscole [A-Z];
    * Se l'utente ha dichiarato che nella generazione della password devono essere esclusi alcuni carattei speciali, questi vengono esclusi dal dizionario in modo da non essere utilizzati;
* Se la terza risposta (opzionale) è stata fornita, anche i numeri del suo hash vengono convertiti in lettere minuscole e numeri [a-z0-9] come per la prima risposta;
* A questo punto, se sono state fornite tre risposte, avremo dunque quattro stringhe: due stringhe di caratteri alfanumerici, una di caratteri speciali ed una di caratteri maiuscoli;
* L'Utente ha indicato la lunghezza desiderata della password (8 - 16 - 20 - 32 - 64 - 128). Questa lunghezza viene utilizzata per determinare quanti caratteri dovranno essere selezionati dalle stringhe in precedenza ottenute.  
Se ho due risposte, metà della password sarà composta dai caratteri alfanumerici generati dalla prima risposta, e poi 1/4 dai caratteri speciali generati dalla seconda risposta ed 1/4 dai caratteri maiuscoli sempre generati dalla seconda risposta.  
Se ho tre risposte, 1/4 della password sarà composta dai caratteri alfanumerici generati dalla prima risposta, 1/4 dai caratteri speciali generati dalla seconda risposta, 1/4 dai caratteri maiuscoli sempre generati dalla seconda risposta, ed infine 1/4 dai caratteri alfanumerici generati dalla terza risposta;     
* Da ciascuna stringa vengono quindi selezionati, tramite un ciclo *for*, i primi **N** caratteri (N è dato dalle lunghezze stabilite prima) e salvati in una lista. La lista sarà quindi composta di caratteri minuscoli, maiuscoli, numeri e caratteri speciali;
ESEMPIO:
    - lunghezza password = 8
    - due risposte fornite
    - lunghezza primo segmento = 4
    - lunghezza secondo segmento = 2
    - lunghezza terzo segmento = 2
    - `lista = [prima_stringa[primo segmento], seconda_stringa[secondo segmento], terza_stringa[terzo segmento]]`
* Per l'assemblaggio della password, viene determinata la lunghezza complessiva delle risposte fornite, data dalla somma della lunghezza delle due/tre risposte inserite (ad esempio le risposte "tre", "mia madre" e "42" avranno lunghezza complessiva di 13).  
Il numero ottenuto viene utilizzato per la funzione `random.seed()`, in modo che se le risposte saranno sempre le stesse, il seed sarà sempre lo stesso;
* La funzione `random.shuffle()` viene usata sugli elementi della lista, mescolandone quindi l'ordine. Come si è detto, se le risposte saranno sempre le stesse, il seed sarà sempre lo stesso e dunque il risultato dello "shuffle" sarà sempre lo stesso;
* Gli elementi della lista vengono concatenati con `.join()` creando la password finale;
* L'Utente salva le domande create nel database sqlite3, dando un titolo all'istanza (ad esempio "password google") ed una descrizione opzionale;
* Quando l'utente ha bisogno della password, il codice enumera il database e restituisce all'utente le istanze disponibili;
* Quando l'utente seleziona una istanza, il codice gli restituisce le relative domande ed in base alle risposte fornite riesegue il codice sopra descritto. Se le risposte saranno le stesse, la password finale sarà la stessa, altrimenti sarà diversa;
* Il database viene creato al primo utilizzo del codice, qualora il programma non lo trovi nell'attuale directory.

## ESEMPIO PRATICO

* PRIMA DOMANDA: **Il mio numero magico?**
* PRIMA RISPOSTA: **56**
* SECONDA DOMANDA: **La ragazza di cui sono stato sempre innamorato segretamente**
* SECONDA RISPOSTA: **annalisa**
* TERZA DOMANDA: **print("completa il codice**
* TERZA RISPOSTA: **")**

[ + + + + ]  

[ + ] ***Trovo l'hash sha512 delle risposte fornite...***  

**magic 1:**  
`7041430688911432078141110650131431289311586514149131514578915101511181513481082414811051215147115192151415128156131114714297118151211481372596130311112113721014131111131410747137`  

**magic 2:**  
`4131315390111559101111131513248136231428149101255138139351511869112711131413514121514141112312613131410109101514276297896014411241112241901326121381028114581241394511901513631038128`  

**magic 3:**  
`1454128821790381283111511403811312611213211108241256138151111112098101591365182414121132131312131211252316410411131112661133191013116788011120133132155772648109510115461051112`  

[ + ] ***Converto i numeri trovati in lettere, numeri e caratteri speciali...***  

**phrase 1:**  
`9tufvvn6gttkfymn52wk36nnv5yvsvyaykty8thxntjyuywkywonolt2mkn9uxktyuntryxmckkum0jnmkkmnjr9r`  

**phrase 2 (caratteri speciali):**  
`-??=))??-))=?==-_)???)!==_=)==_,)=)=?==--=--))=???-!_-??=?=)??-=-))-)====-$-??=-_)))?=?-_=-`  

**phrase 2.1 (caratteri maiuscoli):**  
`TOOZVKONJKKMOMXTRWNNNVAYYSMWYYRQKMKMNMYTUYTTKWLOOOTAIJONMOXVONTLTKVTVMZLMTBTNNLTSVKVOMOJSLT`  

**phrase 3:**  
`n1lvusct25kynctml4lmukhxl2mtykklita3m6rxnlk6mmlmlkywptdkmkl7k7sjmk7vaktm56o206tiyaowjykt`  

[ + ] ***Assemblo la password...***  

*lunghezza password -> 128*  

*suddivisione della sua lunghezza nelle componenti -> 32 - 32 - 32 - 32*  

**pre-password:**  
`['9', 't', 'u', 'f', 'v', 'v', 'n', '6', 'g', 't', 't', 'k', 'f', 'y', 'm', 'n', '5', '2', 'w', 'k', '3', '6', 'n', 'n', 'v', '5', 'y', 'v', 's', 'v', 'y', 'a', '-', '?', '?', '=', ')', ')', '?', '?', '-', ')', ')', '=', '?', '=', '=', '-', '_', ')', '?', '?', '?', ')', '!', '=', '=', '_', '=', ')', '=', '=', '_', ',', 'T', 'O', 'O', 'Z', 'V', 'K', 'O', 'N', 'J', 'K', 'K', 'M', 'O', 'M', 'X', 'T', 'R', 'W', 'N', 'N', 'N', 'V', 'A', 'Y', 'Y', 'S', 'M', 'W', 'Y', 'Y', 'R', 'Q', 'n', '1', 'l', 'v', 'u', 's', 'c', 't', '2', '5', 'k', 'y', 'n', 'c', 't', 'm', 'l', '4', 'l', 'm', 'u', 'k', 'h', 'x', 'l', '2', 'm', 't', 'y', 'k', 'k', 'l']`  

*lunghezza complessiva delle risposte, per derivarne il seed -> 12*  

***password:***  
`y_2vuctv=ynylMQmcKykgaOOXA,4?1)_)R??lv?xNV)-=5JnWWkYvmnn5)?fv=)f)k=)MtT6Mnsn-K2mml!SsRkluk?YuYOt5K6y=3h=lTk9NvOtY=tN==-t_w?VZN?2`  

[ + + + + ]  
 
+++ ***RIEPILOGO*** +++

        ISTANZA: TEST

        DESCRIZIONE: esempio pratico di funzionamento

        LUNGHEZZA PASSWORD: 128

        CARATTERI SPECIALI ESCLUSI:

        1) PRIMA DOMANDA: [ il mio numero magico? ]

        1.2) PRIMA RISPOSTA: [ 56 ]

        2) SECONDA DOMANDA: [ la ragazza di cui sono stato sempre innamorato segretamente ]

        2.2) SECONDA RISPOSTA: [ annalisa ]

        3) TERZA DOMANDA: [ print("completa il codice ]

        3.3) TERZA RISPOSTA: [ ") ]

        PA$$WORD GENERATA: [ y_2vuctv=ynylMQmcKykgaOOXA,4?1)_)R??lv?xNV)-=5JnWWkYvmnn5)?fv=)f)k=)MtT6Mnsn-K2mml!SsRkluk?YuYOt5K6y=3h=lTk9NvOtY=tN==-t_w?VZN?2 ]

        +++ END +++
