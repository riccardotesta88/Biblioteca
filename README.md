# Progetto Biblioteca
## Gestione libri, autori e editori

Applicazione web per la gestione dei libri sviluppata in Django e su ambiente Docker.

### Ambiente di sviluppo
Utilizzato *** Docker *** per l'ambiente di sviluppo, con variabili d'ambiente per l'accesso al database e per il servizio di redis per la parte di database.
Anche se sembrerebbe eccessivo utilizzare Redis per la gestione della cache, è stato scelto per la sua semplicità di utilizzo e per la sua velocità di risposta, anche in previsione di un uso intensivo futuro delle API di ricerca.

### Struttura del progetto

- **gestione**: Applicazione Django per la gestione dei libri, autori e editori
- **Biblioteca**: Progetto Django per la gestione dei libri, autori e editori


### Stack tecnologico
Base di dati: ***PostgreSQL***, ***Redis***
Backend: ***Django***, ***Django Rest Framework***, ***Docker***
Frontend: ***HTML***, ***CSS***, ***Javascript***, ***Bootstrap***

