# import typing
from typing import List, Dict, str



class CV():
    def __init__(self, name: str, last_name: str, phone: int, addres: str) -> None:
        self.name = "Andrei"
        self.last_name = "Gavrilov"
        self.phene = 46222695
        self.addres = "Oslo 0756, Ekraveien 39c"

    def skills(self):
        git = 'GIT'
        sql = 'SQL'
        flask = 'Flask'
        return f"ALL TOOSLS for Python and little more\n{git}\n{sql}\n{flask}"

    def education(self):
        python: str = "August 2023 - skillbox" 
        sport_medical: str = "September 2005 - Juni 2011\
        Russia, Kaliningrad Master's in physical education and sports. \
        Major in medical science Theory and methodology for physical culture and sports. \
        I chose the direction of medicine rehabilitation and health\
        "

    def languge(self):
        Norwegian_nynorsk: List =[
            Written: Beginner,
            Oral: Adwancer
            ]

        English: List = [
            In writing: Good,
            Oral: Very good
            ]
        
        Russian: List = [
            Written: First language (mother tongue),
            Oral: First language (mother tongue)
            ]

    def project(self):
        parser: Dict ={
            'parser_vg':"https://github.com/tr211/diplom"
        } 
