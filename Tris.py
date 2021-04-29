##
# IL CLASSICO GIOCO DEL TRIS
#      0     1     2
#   +-----+-----+-----+
# 0 |  0  |  3  |  6  |
#   +-----+-----+-----+
# 1 |  1  |  4  |  7  |
#   +-----+-----+-----+
# 2 |  2  |  5  |  8  |
#   +-----+-----+-----+
#
from colorama import *
from random import randint
import sys

##
# INIZIALIZZA LA LIBRERIA COLORAMA.
# VERRANNO UTILIZZATE SOPRATUTTO
# LE FUNZIONI SEGUENTI PRECEDUTE
# DA PRINT(....) :
# Fore.LIGHTRED_EX  -> COLORE DEL TESTO
# Back.LIGHTYELLOW_EX -> COLORE DELLO SFONDO
# Cursor.POS(5, 17) -> POSIZIONE DEL CURSORE
# Style.RESET_ALL) -> RESET ALLE CONDIZIONI INIZIALI
init()

gioca = ''  # Azzero la variabile che conterrà la coordinata da giocare
SPACE = ' '  # COSTANTE PER LO SPAZIO

##
#   IMPOSTAZIONI PER LA
#   MATRICE BI-DIMENSIONALE
#   CHE CONTERRA'LA PARTITA
#   PER ACCEDERE AD OGNI SINGOLA
#   POSIZIONE PER INSERIRE LE POSIZIONI
#   SI USA LA SEGUENTE NOTAZIONE :
#   scacchiera[1][2] = 'x'
#   INSERISCE IL CARATTERE X NELLA
#   POSIZIONE (riga=1;colonna=2)
#
scacchiera = []
riga1 = ['', '', '']
riga2 = ['', '', '']
riga3 = ['', '', '']

#   creo la matrice 3x3
scacchiera.append(riga1)
scacchiera.append(riga2)
scacchiera.append(riga3)

#   lista celle vuote
freeCell = []
#   mossa random computer
mossa_random_pc: int


def initialize_screen() :
    # CANCELLA LO SCHERMO E MUOVE IL CURSORE SU (0,0). E' come [system("cls")]
    print('\33[2J')
    # STAMPO IL TITOLO
    print(Fore.LIGHTGREEN_EX + Cursor.POS(5, 1) + " IL GIOCO DEL TRIS \n" + Fore.WHITE)
    # STAMPA LA GRIGLIA VUOTA SULLA CONSOLE
    griglia()


def riga_vuota(nome) :
    divisore = '|'
    spazio = ' '
    # 'nome' sono i numeri all'inizio riga
    print(spazio, Fore.LIGHTRED_EX + nome + Fore.WHITE, end=' ')
    for t in range(3) :
        print(divisore, end=' ')
        for i in range(4) :
            print(spazio, end='')
    print(divisore)


def separatore() :
    croce = '+'
    tratto = '-'
    spazio = ' '
    print(spazio * 4, end='')
    for t in range(3) :
        print(croce, end='')
        for i in range(5) :
            print(tratto, end='')
    print(croce)


def griglia() :
    titoli = "   0     1     2   "
    spazio = " "
    # Stampa 3 spazi iniziali + i numeri 0,1,2 in ROSSO
    # poi ripristina la scrittura in BIANCO
    print(Fore.LIGHTRED_EX + spazio * 3, titoli, Fore.WHITE)
    separatore()
    riga_vuota('0')  # prima riga
    separatore()
    riga_vuota('1')  # seconda riga
    separatore()
    riga_vuota('2')  # terza riga
    separatore()


# La funzione "play()" restituisce le coordinate
# x(colonna) e y(riga) in cui verrà stampato il
# carattere "x" oppure "o" a seconda del giocatore
def play(game) :
    r = 0
    c = 0
    if game[0] == '0' :
        if (game[1]) == '0' :
            c = 8
            r = 5
        if (game[1]) == '1' :
            c = 14
            r = 5
        if (game[1]) == '2' :
            c = 20
            r = 5
    if (game[0]) == '1' :
        if (game[1]) == '0' :
            c = 8
            r = 7
        if (game[1]) == '1' :
            c = 14
            r = 7
        if (game[1]) == '2' :
            c = 20
            r = 7
    if (game[0]) == '2' :
        if (game[1]) == '0' :
            c = 8
            r = 9
        if (game[1]) == '1' :
            c = 14
            r = 9
        if (game[1]) == '2' :
            c = 20
            r = 9
    return c, r


##
# creo un dizionario che conterrà l'elenco
# degli avvisi da emettere in caso di errori
#
def gestione_errori(code) :
    # GESTISCO GLI ERRORI CON UN DIZIONARIO
    errori = {0 : "      Cella già occupata      ",
              1 : "    Inserire 2 cifre [12]     ",
              2 : "   Inserire cifre numeriche   ",
              3 : "Superato valore max coordinata"}
    # estrazione stringa errore corrispondente
    # al codice passato
    str_errore = errori[code]
    print(Fore.LIGHTRED_EX +
          Back.LIGHTYELLOW_EX +
          Cursor.POS(5, 17) +
          str_errore +  # RILEVA IL CODICE DI ERRORE
          Style.RESET_ALL)


##
#   Questa funzione viene chiamata
#   quando il giocatore effettua la
#   sua mossa. Vengono applicate le
#   regole del gioco.
#   Restituisce TRUE per gioco valido
#   e FALSE per gioco non valido
#
def ctrl_move_player(mossa: str) :
    if mossa.isdigit() :  # SE SI INTRODUCONO LETTERE INVECE DI NUMERI ESCO DAL CICLO CON RISPOSTA=FALSE
        if len(mossa) != 2 :  # SE 'MOSSA' E' COMPOSTA DA MENO O PIU DI 2 CHAR ESCO DAL CICLO CON RISPOSTA=FALSE
            risposta = False
            gestione_errori(1)
        elif int(mossa[0]) > 2 or int(
                mossa[1]) > 2 :  # SE LE CIFRE INSERITE NELLA 'MOSSA' SONO INFERIORI A 2 ESCO DAL CICLO CON RISPOSTA=FALSE
            risposta = False
            gestione_errori(3)
        elif (scacchiera[int(mossa[0])][int(mossa[1])] == 'x') or (scacchiera[int(mossa[0])][int(mossa[1])] == 'o') :
            risposta = False
            gestione_errori(0)
        elif scacchiera[int(mossa[0])][int(mossa[1])] == '' :
            risposta = True
            print(Cursor.POS(5, 17) + SPACE * 30)  # ELIMINO IL MESSAGGIO DI ERRORE PRESENTE SULLA LINEA
        else :
            risposta = True
    else :
        risposta = False
        if mossa != 'q' and mossa != 'Q' :  # 'Q' e 'q' sono le uniche lettere concesse.Non viene sollevato errore
            gestione_errori(2)
    return risposta


##
#   Effettua la mossa inserendo il segnaposto (placeholder)
#   x - per il giocatore
#   o - per il computer
#   In ingresso oltre al segnaposto (x-o) nella griglia
#   inserire anche la stringa contenente la giocata , ad es "11"
#   e la sua conversione nelle relative coordinate
#   dello schermo cioè Colonna-14 (posx) Riga-7 (posy)
#
def make_move(mossa, posx, posy, placeholder) :
    # Aggiorno la matrice 3x3 che contiene le mosse fatte
    scacchiera[int(mossa[0])][int(mossa[1])] = placeholder
    # Cancella con alcuni SPAZI,la riga della console, dove sono
    # state inserite precedentemente le coordinate
    print(Cursor.POS(25, 15) + SPACE * 30)
    # Inserisco la posizione scelta con una 'x' GIALLO CHIARO
    print(Fore.LIGHTYELLOW_EX + Cursor.POS(posx, posy) + placeholder + Fore.WHITE)


def mossa_giocatore(giocata) :
    x, y = play(giocata)
    make_move(giocata, x, y, 'x')
    # Pulisco la lista delle celle libere
    freeCell.clear()
    aggiorna_celle_vuote(scacchiera)


def mossa_computer() :
    ##
    # Estrae dalla lista delle mosse possibili una mossa random
    # La funzione 'randint' è presente nel modulo 'random'
    # Uso : randint(0,5) restituisce un intero compreso tra
    #       zero e 5 inclusi.
    # Il numero random restituito è compreso tra 0 e la lunghezza
    # massima della lista.
    # Questo numero sarà usato dal pc per giocare
    # mossa_casuale_pc = freeCell[randint(0, len(freeCell))]
    mossa_casuale_pc = freeCell[randint(0, len(freeCell))]
    x, y = play(str(mossa_casuale_pc))
    make_move(str(mossa_casuale_pc), x, y, 'o')
    # Pulisco la lista delle celle libere
    freeCell.clear()
    aggiorna_celle_vuote(scacchiera)


##
#   Aggiorna la lista contenente le
#   celle vuote su cui poter muovere
#
def aggiorna_celle_vuote(tabel) :
    idx = 0
    for rr in range(3) :
        for cc in range(3) :
            # CONTROLLO LA PRESENZA DI CELLE VUOTE
            # SE NE TROVO UNA SALVO LA SUA COORDINATA
            if tabel[rr][cc] == '' :
                freeCell.append(str(rr) + str(cc))
                idx = idx + 1
    print(Cursor.POS(5, 17) + SPACE * 60)
    print(Cursor.POS(5, 17), freeCell)
    if len(freeCell) == 0 :
        uscita_gioco()
        sys.exit()  # vuole import sys


##
#   CONTROLLO SE SULLE LINEE O LE DIAGONALI C'E UN TRIS
#   EFFETTUATO DAL GIOCATORE UMANO
#
def ctrl_tris_linea(lin: int, placeholder: str) :
    flag = 0
    for col in range(3) :
        if scacchiera[lin][col] == placeholder :
            flag += 1
    return flag


def ctrl_tris_colonna(col: int, placeholder: str) :
    flag = 0
    for lin in range(3) :
        if scacchiera[lin][col] == placeholder :
            flag += 1
    return flag


def ctrl_tris_diag1(placeholder) :
    flag = 0
    for x in range(3) :
        if scacchiera[x][x] == placeholder :
            flag += 1
    return flag


def ctrl_tris_diag2(placeholder) :
    flag = 0
    if scacchiera[0][2] == placeholder : flag += 1
    if scacchiera[1][1] == placeholder : flag += 1
    if scacchiera[2][0] == placeholder : flag += 1
    return flag


def uscita_gioco() :
    # Premendo "q" oppure "Q" si esce dal ciclo e resetto le eventuali opzioni IMPOSTATE al testo
    print(Fore.LIGHTRED_EX +
          Back.LIGHTYELLOW_EX +
          Cursor.POS(5, 17) +
          "       Il gioco è terminato       " +
          Style.RESET_ALL)


# Inizializzo lo schermo
initialize_screen()

##
# CICLO PRINCIPALE DEL MENU'
# SI ESCE QUANDO SI INSERISCE 'q' OPPURE 'Q'
#
while gioca != 'q' and gioca != 'Q' :
    # Cancella le coordinate inserite nel ciclo precedente utilizzando 30 SPAZI
    print(Cursor.POS(25, 15) + SPACE * 30)
    print(Cursor.POS(2, 12) + "['q' oppure 'Q' PER USCIRE]")
    print(Cursor.POS(1, 14) + '------------------------------')
    gioca = input('Fai la tua mossa [R][C] ')

    if ctrl_move_player(gioca) :  # se non supera il controllo esce dall'IF e il ciclo WHILE ricomincia
        mossa_giocatore(gioca)  # mossa del giocatore umano
        mossa_computer()         # mossa del computer
        ##
        # CONTROLLO SE NELLE RIGHE OPPURE NELLE
        # COLONNE C'E UN TRIS
        #
        for ctrl in range(3) :
            if ctrl_tris_linea(ctrl, 'x') == 3 :
                print(Fore.LIGHTRED_EX + Back.LIGHTYELLOW_EX + Cursor.POS(5,17) + "       HUMAN WINS!!       " + Style.RESET_ALL)
                sys.exit()  # vuole import sys
            if ctrl_tris_colonna(ctrl, 'x') == 3 :
                print(Fore.LIGHTRED_EX + Back.LIGHTYELLOW_EX + Cursor.POS(5,17) + "       HUMAN WINS!!       " + Style.RESET_ALL)
                sys.exit()  # vuole import sys
        ##
        # CONTROLLO SE NELLE DIAGONALI C'E UN TRIS
        #
        if ctrl_tris_diag1('x') == 3 :
            print(Fore.LIGHTRED_EX + Back.LIGHTYELLOW_EX + Cursor.POS(5,17) + "       HUMAN WINS!!       " + Style.RESET_ALL)
            sys.exit()  # vuole import sys

        if ctrl_tris_diag2('x') == 3 :
            print(Fore.LIGHTRED_EX + Back.LIGHTYELLOW_EX + Cursor.POS(5,17) + "       HUMAN WINS!!       " + Style.RESET_ALL)
            sys.exit()  # vuole import sys

uscita_gioco()
