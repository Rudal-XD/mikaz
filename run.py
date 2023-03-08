import os,sys,json,time
import threading
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col

def update():
  os.system('git pull')
def clear():
  os.system('clear')
def banner():
	print('''
      	\x1b[1;93m_______           ______   _______  _                 ______  
       (  ____ )|\     /|(  __  \ (  ___  )( \      |\     /|(  __  \ 
       | (    )|| )   ( || (  \  )| (   ) || (      ( \   / )| (  \  )
       | (____)|| |   | || |   ) || (___) || | _____ \ (_) / | |   ) |
       \x1b[1;92m|     __)| |   | || |   | ||  ___  || |(_____) ) _ (  | |   | |
       | (\ (   | |   | || |   ) || (   ) || |       / ( ) \ | |   ) |
       | ) \ \__| (___) || (__/  )| )   ( || (____/\( /   \ )| (__/  )
       |/   \__/(_______)(______/ |/     \|(_______/|/     \|(______/ 
       ''')
 
class login:
    update()
    clear()
    banner()
    sol='[1] MY SOCIAL MEDIA\n[2] Line 1\n[3] Line 2\n[4] Line 3\n[5] Line 4\n[6] EXIT'
    soi=nel(sol,style='green')
    cetak(nel(soi,style='cyan',title='PILIHAN MENU'))
    coi = input('\x1b[1;92m[?] pilih : ')
    if coi in ['1','01']:
        os.system('xdg-open https://linktr.ee/mikaz_')
    elif coi in['2','02']:
        from Data import lin1
    elif coi in['3','03']:
        from Data import lin2
    elif coi in['4','04']:
        from Data import lin3
    elif coi in['5','05']:
        from Data import lin4
    elif coi in ['6','06']:
        exit()
        
if __name__=='__main__':
    login()
