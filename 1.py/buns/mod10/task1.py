import requests
import json

def get_starship_info(starship_name):
    base_url = "https://swapi.dev/api/starships/"
    search_params = {"search": starship_name}
    response = requests.get(base_url, params=search_params)
    
    if response.status_code == 200:
        data = response.json()
        
        if data['count'] > 0:
            starship = data['results'][0]
            ship_info = {
                "name": starship['name'],
                "model": starship['model'],
                "starship_class": starship['starship_class'],
                "manufacturer": starship['manufacturer'],
                "cost_in_credits": starship['cost_in_credits'],
                "max_atmosphering_speed": starship['max_atmosphering_speed'],
                "crew": starship['crew'],
                "passengers": starship['passengers'],
                "films": starship['films'],
                "pilots": starship['pilots'],
                "url": starship['url']
            }
            
            return ship_info
        else:
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    starship_name = "Millennium Falcon"
    ship_info = get_starship_info(starship_name)
    
    if ship_info:
        print("Starship Information:")
        for key, value in ship_info.items():
            print(f"{key}: {value}")
        with open('starship_info.json', 'w') as json_file:
            json.dump(ship_info, json_file, indent=2)
    else:
        print(f"No information found for starship: {starship_name}")

if __name__ == "__main__":
    main()
