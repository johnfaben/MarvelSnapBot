import csv 
from replit import db
import json
import requests
cards_url = 'https://marvelsnap.pro/snap/do.php?cmd=getcards'

def get_card_dict_from_json(cards_url):
  r = requests.get(cards_url)
  card_data = json.loads(r.text)
  card_dict = dict()
  for key in card_data.keys():
    card_dict[key] = dict()
    card_dict[key]['searchnames'] = [card_data[key]['name'].lower().replace(' ','').replace('-','')]
    card_dict[key] ['Name'] = card_data[key]['name']
    card_dict[key]['Cost'] = card_data[key]['cost']
    card_dict[key]['Power'] = card_data[key]['power']
    card_dict[key]['Card Ability'] = card_data[key]['description'].replace('<b>','**').replace('</b>','**').replace('<i>','*').replace('</i>','*')
    if card_data[key]['abilities'] == '["No Ability"]':
      card_dict[key]['Card Ability'] = 'No Ability'
  return card_dict


def get_card_dict(csvFilePath):
  csvReader = csv.DictReader(open(csvFilePath, 'rU'), delimiter=',',quotechar='"')
  card_dict = {}
  for row in csvReader:
    card_dict[row['Card']] = dict()
    card_dict[row['Card']]['Cost'] = row['Cost']
    card_dict[row['Card']]['Power'] = row['Power']
    card_dict[row['Card']]['Card Ability'] = row['Card Ability']
  return card_dict
  
def card_to_string(card,card_dict):
  cost = card_dict[card]['Cost']
  power = card_dict[card]['Power']
  card_ability = card_dict[card]['Card Ability']
  return '**\[' + card + '\]**  **Cost:** ' + cost + '  **Power:** ' + power + '  \n**Ability:**  ' + card_ability

def card_to_string_json(key,card_dict):
  name = card_dict[key]['Name']
  cost = card_dict[key]['Cost']
  power = card_dict[key]['Power']
  card_ability = card_dict[key]['Card Ability']
  return '**\[' + name + '\]**  **Cost:** ' + cost + '  **Power:** ' + power + '  \n**Ability:**  ' + card_ability
  