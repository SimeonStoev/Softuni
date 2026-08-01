from products.chair import Chair
from products.hobby_horse import HobbyHorse
from stores.furniture_store import FurnitureStore

furniture_store = FurnitureStore("test", "LA3")
chair1 = Chair("some_chair", 100)
chair2 = Chair("some_chair", 200)
chair3 = Chair("some_chair1", 50)
hobby_horse = HobbyHorse("hobby_horse", 100)
furniture_store.products.append(chair1)
furniture_store.products.append(chair2)
furniture_store.products.append(chair3)
furniture_store.products.append(hobby_horse)
print(furniture_store.store_stats())
