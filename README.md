# Progetto Biblioteca
## Gestione libri, autori e editori

Applicazione web per la gestione dei libri sviluppata in Django e su ambiente Docker.

### Ambiente di sviluppo
- Utilizzato *** Docker *** per l'ambiente di sviluppo, con variabili d'ambiente per l'accesso al database e per il servizio di redis per la parte di database.
- Anche se sembrerebbe eccessivo utilizzare Redis per la gestione della cache, è stato scelto per la sua semplicità di utilizzo e per la sua velocità di risposta, anche in previsione di un uso intensivo futuro delle API di ricerca.


### Stack tecnologico
- Base di dati: ***PostgreSQL***, ***Redis***
- Backend: ***Django***, ***Django Rest Framework*** (evntualmente per la gestione delle API), ***Docker***
- Frontend: ***HTML***, ***CSS***, ***Javascript***, ***Bootstrap***, ***DataTables***
- Gestione dei campi telefono: https://django-phonenumber-field.readthedocs.io/
---

#### Struttura del progetto
- **gestione**: Applicazione Django per la gestione dei libri, autori e editori
- **Biblioteca**: Progetto Django per la gestione dei libri, autori e editori

Struttura dati:

- Ogni libro ha:
    - almeno un Autore
    - un Titolo
    - un Editore 
    - un anno di Edizione (opzionale)
  
- L'autore ha:
  - Nome
  - Cognome

- L' Editore ha:
  - Ragione sociale
  - indirizzo (opzionale)
  - numero di telefono (opzionale)



Funzionalità aggiuntive:
- Aggiungere anagrafica libri con relativi Autori ed Editori
- Importare l'anagrafica dal json allegato
- View per visualizzare elenco libri ordinati per anno (una semplice tabella)
- Api rest per aggiungere un libro
- Api rest per ottenere l'elenco dei libri

### OPERAZIONI
### Operazioni preliminari
Creazione untete per accesso al sistema di gestione:  admin / accesso1234

```
python manage.py createsuperuser --username admin --email admin@localhost
```

