"""
If there are any maps you want to be added just send an email and a picture of the map

There is probably a better method of storing the nodes and positions but this is how i chose to do it.

"""

class Board():
    
    def __init__(self):
        self.maps = ['Europe', 'America', 'England', 'India', 'Switxerland', 'Nordic', 'Africa', 'Netherland', 'World', 'GreatLakes', 'Marklin', 'Italy']
        
    def getMaps(self):
        return self.maps
    
    def getMap(self, mapName):
        
        # this will be changed as more maps are implemented
        if mapName != 'Europe':
            exit('Map not implemented')
        
        europe_nodes = {'Edinburgh': {'London': 4}, 
                        'London': {'Edinburgh': 4, 'Dieppe': 2, 'Amsterdam': 2}, 
                        'Dieppe': {'London': 2, 'Brest': 2, 'Paris': 1, 'Bruxelles': 2}, 
                        'Brest': {'Dieppe': 2, 'Pamplona': 4, 'Paris': 3}, 
                        'Pamplona': {'Brest': 4, 'Madrid': 3, 'Barcelona': 2, 'Marseille': 4, 'Paris': 4}, 
                        'Paris': {'Brest': 3, 'Dieppe': 1, 'Pamplona': 4, 'Marseille': 4, 'Bruxelles': 2, 'Zurich': 3, 'Frankfurt': 3}, 
                        'Bruxelles': {'Dieppe': 2, 'Amsterdam': 1, 'Paris': 2, 'Frankfurt': 2}, 
                        'Amsterdam': {'London': 2, 'Bruxelles': 1, 'Essen': 3, 'Frankfurt': 2}, 
                        'Madrid': {'Pamplona': 3, 'Lisboa': 3, 'Cadiz': 3, 'Barcelona': 2}, 
                        'Lisboa': {'Madrid': 3, 'Cadiz': 2}, 'Cadiz': {'Lisboa': 2, 'Madrid': 3}, 
                        'Barcelona': {'Madrid': 2, 'Pamplona': 2, 'Marseille': 4}, 
                        'Marseille': {'Barcelona': 4, 'Pamplona': 4, 'Paris': 4, 'Zurich': 2, 'Roma': 4}, 
                        'Zurich': {'Paris': 3, 'Marseille': 2, 'Munchen': 2, 'Venezia': 2}, 
                        'Frankfurt': {'Paris': 3, 'Amsterdam': 2, 'Bruxelles': 2, 'Munchen': 2, 'Essen': 2, 'Berlin': 3}, 
                        'Essen': {'Amsterdam': 3, 'Kobenhavn': 3, 'Berlin': 2, 'Frankfurt': 2}, 
                        'Munchen': {'Frankfurt': 2, 'Zurich': 2, 'Venezia': 2, 'Wien': 3}, 
                        'Venezia': {'Zurich': 2, 'Roma': 2, 'Munchen': 2, 'Zagrab': 2}, 
                        'Roma': {'Marseille': 4, 'Venezia': 2, 'Palermo': 4, 'Brindisi': 2}, 
                        'Palermo': {'Roma': 4, 'Brindisi': 3, 'Smyrna': 6}, 
                        'Brindisi': {'Roma': 2, 'Palermo': 3, 'Athina': 4}, 
                        'Kobenhavn': {'Essen': 3, 'Stockholm': 3}, 
                        'Berlin': {'Essen': 2, 'Frankfurt': 3, 'Danzig': 4, 'Warzawa': 4, 'Wien': 3}, 
                        'Stockholm': {'Kobenhavn': 3, 'Petrograd': 8}, 
                        'Petrograd': {'Stockholm': 8, 'Riga': 4, 'Wilno': 4, 'Moskva': 4}, 
                        'Danzig': {'Berlin': 4, 'Riga': 3, 'Warzawa': 2}, 
                        'Warzawa': {'Berlin': 4, 'Wien': 4, 'Danzig': 2, 'Wilno': 3, 'Kyiv': 4}, 
                        'Wien': {'Berlin': 3, 'Munchen': 3, 'Zagrab': 2, 'Warzawa': 4, 'Budapest': 1}, 
                        'Zagrab': {'Venezia': 2, 'Wien': 2, 'Budapest': 2, 'Sarajevo': 3}, 
                        'Budapest': {'Wien': 1, 'Zagrab': 2, 'Sarajevo': 3, 'Bucuresti': 4, 'Kyiv': 6}, 
                        'Riga': {'Danzig': 3, 'Petrograd': 4, 'Wilno': 4}, 
                        'Wilno': {'Riga': 4, 'Warzawa': 3, 'Petrograd': 4, 'Smolensk': 3, 'Kyiv': 2}, 
                        'Moskva': {'Petrograd': 4, 'Smolensk': 2, 'Kharkov': 4}, 
                        'Smolensk': {'Wilno': 3, 'Moskva': 2, 'Kyiv': 3}, 
                        'Kyiv': {'Wilno': 2, 'Budapest': 6, 'Warzawa': 4, 'Smolensk': 3, 'Bucuresti': 4, 'Kharkov': 4}, 
                        'Smyrna': {'Palermo': 6, 'Athina': 2, 'Constantinople': 2, 'Angora': 3}, 
                        'Athina': {'Brindisi': 4, 'Sarajevo': 4, 'Sofia': 3, 'Smyrna': 2}, 
                        'Sarajevo': {'Zagrab': 3, 'Athina': 4, 'Budapest': 3, 'Sofia': 2}, 
                        'Sofia': {'Sarajevo': 2, 'Athina': 3, 'Bucuresti': 2, 'Constantinople': 3}, 
                        'Bucuresti': {'Budapest': 4, 'Sofia': 2, 'Kyiv': 4, 'Constantinople': 3, 'Sevastapol': 4}, 
                        'Constantinople': {'Sofia': 3, 'Bucuresti': 3, 'Smyrna': 2, 'Sevastapol': 4, 'Angora': 2}, 
                        'Sevastapol': {'Bucuresti': 4, 'Constantinople': 4, 'Rostov': 4, 'Sochi': 2, 'Erzurum': 4}, 
                        'Kharkov': {'Kyiv': 4, 'Moskva': 4, 'Rostov': 2}, 
                        'Rostov': {'Kharkov': 2, 'Sevastapol': 4, 'Sochi': 2}, 
                        'Sochi': {'Sevastapol': 2, 'Rostov': 2, 'Erzurum': 3}, 
                        'Erzurum': {'Sochi': 3, 'Sevastapol': 4, 'Angora': 3}, 
                        'Angora': {'Erzurum': 3, 'Constantinople': 2, 'Smyrna': 3}}
        
        europe_pos = {'Edinburgh': (3, 13), 'London': (4, 10), 'Dieppe': (4, 8), 'Brest': (2, 8), 'Pamplona': (4, 4), 'Paris': (5, 7), 'Bruxelles': (6, 9), 'Amsterdam': (6, 10), 'Madrid': (2, 3), 'Lisboa': (1, 2), 'Cadiz': (2, 1), 'Barcelona': (4, 2), 'Marseille': (7, 4), 'Zurich': (7, 6), 'Frankfurt': (7, 8), 'Essen': (8, 9), 'Munchen': (9, 7), 'Venezia': (9, 5), 'Roma': (9, 3), 'Palermo': (10, 1), 'Brindisi': (11, 3), 'Kobenhavn': (9, 11), 'Berlin': (10, 9), 'Stockholm': (11, 13), 'Petrograd': (17, 12), 'Danzig': (12, 10), 'Warzawa': (13, 9), 'Wien': (11, 7), 'Zagrab': (11, 5), 'Budapest': (12, 6), 'Riga': (14, 12), 'Wilno': (15, 10), 'Moskva': (19, 10), 'Smolensk': (17, 9), 'Kyiv': (16, 8), 'Smyrna': (15, 1), 'Athina': (13, 2), 'Sarajevo': (12, 4), 'Sofia': (14, 4), 'Bucuresti': (15, 5), 'Constantinople': (16, 3), 'Sevastapol': (17, 5), 'Kharkov': (18, 7), 'Rostov': (19, 6), 'Sochi': (19, 4), 'Erzurum': (19, 2), 'Angora': (17, 2)}

        america_nodes = {'Vancouver': {'Calgary': 3, 'Seattle': 1}, 
                         'Calgary': {'Vancouver': 3, 'Seattle': 4, 'Helena': 4, 'Winnipeg': 6}, 
                         'Seattle': {'Vancouver': 1, 'Portland': 1, 'Calgary': 4, 'Helena': 6}, 
                         'Portland': {'Seattle': 1, 'SanFrancisco': 5, 'SaltLakeCity': 6}, 
                         'SanFrancisco': {'Portland': 5, 'LosAngeles': 3, 'SaltLakeCity': 5}, 
                         'LosAngeles': {'SanFrancisco': 3, 'LasVegas': 2, 'ElPaso': 6, 'Phoenix': 3}, 
                         'LasVegas': {'LosAngeles': 2, 'SaltLakeCity': 3}, 
                         'SaltLakeCity': {'Portland': 6, 'SanFrancisco': 5, 'Helena': 3, 'LasVegas': 3, 'Denver': 3}, 
                         'Helena': {'Seattle': 6, 'Calgary': 4, 'Winnipeg': 4, 'SaltLakeCity': 3, 'Denver': 4, 'Duluth': 6}, 
                         'Winnipeg': {'Calgary': 6, 'Helena': 4, 'Duluth': 4, 'SaultStMarie': 6}, 
                         'ElPaso': {'LosAngeles': 6, 'Phoenix': 3, 'Dallas': 4, 'Houston': 6, 'OklahomaCity': 5, 'SantaFe': 2}, 
                         'Phoenix': {'LosAngeles': 3, 'SantaFe': 3, 'Denver': 5, 'ElPaso': 3}, 
                         'SantaFe': {'Phoenix': 3, 'Denver': 2, 'ElPaso': 2, 'OklahomaCity': 3}, 
                         'Denver': {'Phoenix': 5, 'SaltLakeCity': 3, 'Helena': 4, 'SantaFe': 2, 'OklahomaCity': 4, 'Omaha': 4, 'KansasCity': 4}, 
                         'Dallas': {'ElPaso': 4, 'Houston': 1, 'OklahomaCity': 2, 'LittleRock': 2}, 
                         'Houston': {'ElPaso': 6, 'Dallas': 1, 'NewOrleans': 2}, 
                         'OklahomaCity': {'SantaFe': 3, 'Denver': 4, 'ElPaso': 5, 'KansasCity': 2, 'Dallas': 2, 'LittleRock': 2}, 
                         'Omaha': {'Denver': 4, 'Duluth': 2, 'KansasCity': 1, 'Chicago': 4}, 
                         'KansasCity': {'Denver': 4, 'Omaha': 1, 'OklahomaCity': 2, 'SaintLouis': 2}, 
                         'Duluth': {'Helena': 6, 'Winnipeg': 4, 'Omaha': 2, 'Chicago': 3, 'Toronto': 6, 'SaultStMarie': 3}, 
                         'LittleRock': {'OklahomaCity': 2, 'Dallas': 2, 'SaintLouis': 2, 'NewOrleans': 3, 'Nashville': 3}, 
                         'SaintLouis': {'KansasCity': 2, 'Chicago': 2, 'LittleRock': 2, 'Nashville': 2, 'Pittsburgh': 5}, 
                         'Chicago': {'Omaha': 4, 'Duluth': 3, 'SaintLouis': 2, 'Pittsburgh': 3, 'Toronto': 4}, 
                         'NewOrleans': {'Houston': 2, 'LittleRock': 3, 'Atlanta': 4, 'Miami': 6}, 
                         'Nashville': {'LittleRock': 3, 'SaintLouis': 2, 'Pittsburgh': 4, 'Atlanta': 1, 'Raleigh': 3}, 
                         'Pittsburgh': {'SaintLouis': 5, 'Nashville': 4, 'Chicago': 3, 'Raleigh': 2, 'Washington': 2, 'NewYork': 2, 'Toronto': 2}, 
                         'Toronto': {'Chicago': 4, 'Duluth': 6, 'Pittsburgh': 2, 'SaultStMarie': 2, 'Montreal': 3}, 
                         'SaultStMarie': {'Duluth': 3, 'Winnipeg': 6, 'Toronto': 2, 'Montreal': 5}, 
                         'Atlanta': {'NewOrleans': 4, 'Nashville': 1, 'Miami': 5, 'Charleston': 2, 'Raleigh': 2}, 
                         'Raleigh': {'Nashville': 3, 'Charleston': 2, 'Atlanta': 2, 'Washington': 2, 'Pittsburgh': 2}, 
                         'Miami': {'NewOrleans': 6, 'Atlanta': 5, 'Charleston': 4}, 'Charleston': {'Miami': 4, 'Atlanta': 2, 'Raleigh': 2}, 
                         'Washington': {'Raleigh': 2, 'Pittsburgh': 2, 'NewYork': 2}, 
                         'NewYork': {'Washington': 2, 'Pittsburgh': 2, 'Montreal': 3, 'Boston': 2}, 
                         'Montreal': {'SaultStMarie': 5, 'Toronto': 3, 'NewYork': 3, 'Boston': 2}, 
                         'Boston': {'Montreal': 2, 'NewYork': 2}}
        america_pos ={} 
                  
        england_nodes ={}
        england_pos ={}
                  
        india_nodes ={}
        india_pos ={}
                  
        switxerland_nodes ={}
        switxerland_pos ={}
                  
        nordic_nodes ={}
        nordic_pos ={}
                  
        africa_nodes ={}
        africa_pos ={} 
                  
        netherland_nodes ={}
        netherland_pos ={}
        
        world_nodes ={}
        world_pos ={}
                  
        greatLakes_nodes ={}
        greatLakes_pos ={}
                  
        marklin_nodes ={}
        marklin_pos ={}
                  
        italy_nodes ={}
        italy_pos ={}

        boards = [[europe_nodes, europe_pos], 
                  [america_nodes, america_pos], 
                  [england_nodes, england_pos], 
                  [india_nodes, india_pos], 
                  [switxerland_nodes, switxerland_pos], 
                  [nordic_nodes, nordic_pos], 
                  [africa_nodes, africa_pos], 
                  [netherland_nodes, netherland_pos], 
                  [world_nodes, world_pos], 
                  [greatLakes_nodes, greatLakes_pos],
                  [marklin_nodes, marklin_pos], 
                  [italy_nodes, italy_pos]]
        
        nodes, pos = boards[self.maps.index(mapName)]
        return nodes, pos
