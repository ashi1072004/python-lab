import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import concurrent.futures
import json

url = "https://www.ehorses.com/Homepage/HorsesResults"
base_url = "https://www.ehorses.com"
header = {
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'referer': 'https://www.ehorses.com/caballoria?page=horses&type=0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}
keys = ["headline", "horse-id", "img-list", "price", "more-details", "description", "further-info", "agent", "agent-type", "location", "latitude", "longitude"]
main_list = []

def get_data(link, div):
    res = requests.get(link, headers={'accept-language': 'en-US,en;q=0.9'})
    print(res.status_code)
    soup2 = BeautifulSoup(res.content, "lxml")
    vals = []
    data = soup2.find("div", {'id': 'details'})
    vals.append(data.find("h1", class_="headline").text) #headline
    vals.append(div.get("id")) #horse_id
    img_list = [pic.get('href') for pic in data.find("div", {'id': 'media'}).find_all("a", class_="picItem")]
    vals.append(img_list) #imgs
    vals.append(div.find("div", class_="priceTag").text.strip()) #price
    rows = data.find("div", class_="moreDetails").find_all("div", class_="row")
    chr_dict = {}
    for row in rows: #more_details
        key = row.find("label").text.replace(" ", "-")
        if row.find("label").text == "more disciplines":
            val = [a.text for a in row.find("span").find_all("a")]
        elif row.find("label").text == "Further Characteristics":
            val = [text for text in row.find("span").findAll(string=True) if not text == "\ue0a2"]
        else:
            val = row.find("span").text
        chr_dict.update({key : val})
    vals.append(chr_dict)
    desc = data.find("div", {'id': 'description'})
    vals.append(desc.find("div", class_="desc_en").text.strip()) #description
    vals.append(data.find("div", class_='description').text.lstrip("Further information\r\n\r\n\t\t\t\t\t").strip()) #further_info
    contact = data.find("div", class_='infos').findAll(string=True)
    vals.append(contact[2]) #agent
    vals.append(contact[3]) #agent-type
    vals.append(contact[5]) #location
    geolocator = Nominatim(user_agent="Chrome/125.0.0.0")
    loc = geolocator.geocode(contact[5], namedetails=True)
    vals.append(loc.latitude) #latitude
    vals.append(loc.longitude) #longitude
    main_list.append({keys[i]:vals[i] for i in range(len(keys))})

seite = 1
while True:
    payload = f"Owner.Id=1455892&horseFilter.ProfilID=1455892&HorsesPerPage=10&seite={seite}"
    r = requests.request("POST", url, headers=header, data=payload)
    print(r.status_code)
    soup = BeautifulSoup(r.content, "html.parser")
    main_divs = soup.find_all("div", class_="ownHorses")
    main_links = [base_url+div.find("a").get("href") for div in main_divs]
    # print(main_links)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_data, main_links, main_divs)
    if (soup.find("div", {'id': 'results_moreBtn'})):
        seite = seite + 1
        pass
    else:
        break

# print(main_list)
with open('ehorses.json', 'w', encoding="utf-8") as f:     
    json.dump({"horse": main_list}, f, ensure_ascii=False, indent=4)