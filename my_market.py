import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.myauto.ge/ka/s/00/0/45/1211/00/00/00/00/gaz-24?stype=0&marka=45&model=1211&currency_id=3&det_search=0&ord=7&last_model=1211&keyword='
r = requests.get(url)
content = r.text
soup = BeautifulSoup(content, 'html.parser')
content = soup.find('div', {'class': 'content'})
section = content.find('div', {'class': 'main-wrapper v2'})
details = section.find('div', {'class': 'detail-container'})
container_main = details.find('div', {'class': 'container-main'})
all_cars = container_main.find('div', {'class': 'search-lists-container'})
for gaz in all_cars:
    gaz24 = all_cars.find('div', {'class': 'current-item add53495316 car-short-info'})
    inner = gaz24.find('div', {'class': 'current-item-inner'})
    info = inner.find('div', {'class': 'car-info-wrapper'})
    car_name = info.find('div', {'class': 'car-name-left'})
    car_year = info.find('div', {'class': 'car-name-right'})
    car_year1 = car_year.find('p', {'class': 'car-levy car-year'})
    car_body = info.find('div', {'class': 'car-body-wrapper'})
    figure_list = car_body.find('div', {'class': 'search-list-figure'})
    gaz_details = car_body.find('div', {'class': 'car-list-detail'})
    motor = gaz_details.find('div', {'class': 'car-detail-in cr-engine'})
    cr_road = gaz_details.find('div', {'class': 'car-detail-in cr-road'})
    wheel = gaz_details.find('div', {'class': 'car-detail-in cr-wheel'})
    gas = gaz_details.find('div', {'class': 'car-detail-in cr-1s cr-gas'})

    motor_size = motor.text
    road = cr_road.text
    wheel_t = wheel.text
    name = car_name.text
    year = car_year1.text
    print(name, year, motor_size, road, wheel_t)

for gaz in all_cars:
    gaz24 = all_cars.find('div', {'class': 'current-item add53315140 car-short-info'})
    inner = gaz24.find('div', {'class': 'current-item-inner'})
    info = inner.find('div', {'class': 'car-info-wrapper'})
    car_name = info.find('div', {'class': 'car-name-left'})
    car_year = info.find('div', {'class': 'car-name-right'})
    car_year1 = car_year.find('p', {'class': 'car-levy car-year'})
    car_body = info.find('div', {'class': 'car-body-wrapper'})
    figure_list = car_body.find('div', {'class': 'search-list-figure'})
    gaz_details = car_body.find('div', {'class': 'car-list-detail'})
    motor = gaz_details.find('div', {'class': 'car-detail-in cr-engine'})
    cr_road = gaz_details.find('div', {'class': 'car-detail-in cr-road'})
    wheel = gaz_details.find('div', {'class': 'car-detail-in cr-wheel'})
    gas = gaz_details.find('div', {'class': 'car-detail-in cr-1s cr-gas'})

    motor_size = motor.text
    road = cr_road.text
    wheel_t = wheel.text
    name = car_name.text
    year = car_year1.text
    print(name, year, motor_size, road, wheel_t)

for gaz in all_cars:
    gaz24 = all_cars.find('div', {'class': 'current-item add51565566 car-short-info'})
    inner = gaz24.find('div', {'class': 'current-item-inner'})
    info = inner.find('div', {'class': 'car-info-wrapper'})
    car_name = info.find('div', {'class': 'car-name-left'})
    car_year = info.find('div', {'class': 'car-name-right'})
    car_year1 = car_year.find('p', {'class': 'car-levy car-year'})
    car_body = info.find('div', {'class': 'car-body-wrapper'})
    figure_list = car_body.find('div', {'class': 'search-list-figure'})
    gaz_details = car_body.find('div', {'class': 'car-list-detail'})
    motor = gaz_details.find('div', {'class': 'car-detail-in cr-engine'})
    cr_road = gaz_details.find('div', {'class': 'car-detail-in cr-road'})
    wheel = gaz_details.find('div', {'class': 'car-detail-in cr-wheel'})
    gas = gaz_details.find('div', {'class': 'car-detail-in cr-1s cr-gas'})

    motor_size = motor.text
    road = cr_road.text
    wheel_t = wheel.text
    name = car_name.text
    year = car_year1.text
    print(name, year, motor_size, road, wheel_t)

for gaz in all_cars:
    gaz24 = all_cars.find('div', {'class': 'current-item add53126005 car-short-info'})
    inner = gaz24.find('div', {'class': 'current-item-inner'})
    info = inner.find('div', {'class': 'car-info-wrapper'})
    car_name = info.find('div', {'class': 'car-name-left'})
    car_year = info.find('div', {'class': 'car-name-right'})
    car_year1 = car_year.find('p', {'class': 'car-levy car-year'})
    car_body = info.find('div', {'class': 'car-body-wrapper'})
    figure_list = car_body.find('div', {'class': 'search-list-figure'})
    gaz_details = car_body.find('div', {'class': 'car-list-detail'})
    motor = gaz_details.find('div', {'class': 'car-detail-in cr-engine'})
    cr_road = gaz_details.find('div', {'class': 'car-detail-in cr-road'})
    wheel = gaz_details.find('div', {'class': 'car-detail-in cr-wheel'})
    gas = gaz_details.find('div', {'class': 'car-detail-in cr-1s cr-gas'})

    motor_size = motor.text
    road = cr_road.text
    wheel_t = wheel.text
    name = car_name.text
    year = car_year1.text
    print(name, year, motor_size, road, wheel_t)

for gaz in all_cars:
    gaz24 = all_cars.find('div', {'class': 'current-item add53104361 car-short-info'})
    inner = gaz24.find('div', {'class': 'current-item-inner'})
    info = inner.find('div', {'class': 'car-info-wrapper'})
    car_name = info.find('div', {'class': 'car-name-left'})
    car_year = info.find('div', {'class': 'car-name-right'})
    car_year1 = car_year.find('p', {'class': 'car-levy car-year'})
    car_body = info.find('div', {'class': 'car-body-wrapper'})
    figure_list = car_body.find('div', {'class': 'search-list-figure'})
    gaz_details = car_body.find('div', {'class': 'car-list-detail'})
    motor = gaz_details.find('div', {'class': 'car-detail-in cr-engine'})
    cr_road = gaz_details.find('div', {'class': 'car-detail-in cr-road'})
    wheel = gaz_details.find('div', {'class': 'car-detail-in cr-wheel'})
    gas = gaz_details.find('div', {'class': 'car-detail-in cr-1s cr-gas'})

    motor_size = motor.text
    road = cr_road.text
    wheel_t = wheel.text
    name = car_name.text
    year = car_year1.text
    print(name, year, motor_size, road, wheel_t)

for gaz in all_cars:
    gaz24 = all_cars.find('div', {'class': 'current-item add52922693 car-short-info'})
    inner = gaz24.find('div', {'class': 'current-item-inner'})
    info = inner.find('div', {'class': 'car-info-wrapper'})
    car_name = info.find('div', {'class': 'car-name-left'})
    car_year = info.find('div', {'class': 'car-name-right'})
    car_year1 = car_year.find('p', {'class': 'car-levy car-year'})
    car_body = info.find('div', {'class': 'car-body-wrapper'})
    figure_list = car_body.find('div', {'class': 'search-list-figure'})
    gaz_details = car_body.find('div', {'class': 'car-list-detail'})
    motor = gaz_details.find('div', {'class': 'car-detail-in cr-engine'})
    cr_road = gaz_details.find('div', {'class': 'car-detail-in cr-road'})
    wheel = gaz_details.find('div', {'class': 'car-detail-in cr-wheel'})
    gas = gaz_details.find('div', {'class': 'car-detail-in cr-1s cr-gas'})

    motor_size = motor.text
    road = cr_road.text
    wheel_t = wheel.text
    name = car_name.text
    year = car_year1.text
    print(name, year, motor_size, road, wheel_t)

for gaz in all_cars:
    gaz24 = all_cars.find('div', {'class': 'current-item add51557286 car-short-info'})
    inner = gaz24.find('div', {'class': 'current-item-inner'})
    info = inner.find('div', {'class': 'car-info-wrapper'})
    car_name = info.find('div', {'class': 'car-name-left'})
    car_year = info.find('div', {'class': 'car-name-right'})
    car_year1 = car_year.find('p', {'class': 'car-levy car-year'})
    car_body = info.find('div', {'class': 'car-body-wrapper'})
    figure_list = car_body.find('div', {'class': 'search-list-figure'})
    gaz_details = car_body.find('div', {'class': 'car-list-detail'})
    motor = gaz_details.find('div', {'class': 'car-detail-in cr-engine'})
    cr_road = gaz_details.find('div', {'class': 'car-detail-in cr-road'})
    wheel = gaz_details.find('div', {'class': 'car-detail-in cr-wheel'})
    gas = gaz_details.find('div', {'class': 'car-detail-in cr-1s cr-gas'})

    motor_size = motor.text
    road = cr_road.text
    wheel_t = wheel.text
    name = car_name.text
    year = car_year1.text
    print(name, year, motor_size, road, wheel_t)

for gaz in all_cars:
    gaz24 = all_cars.find('div', {'class': 'current-item add52372234 car-short-info'})
    inner = gaz24.find('div', {'class': 'current-item-inner'})
    info = inner.find('div', {'class': 'car-info-wrapper'})
    car_name = info.find('div', {'class': 'car-name-left'})
    car_year = info.find('div', {'class': 'car-name-right'})
    car_year1 = car_year.find('p', {'class': 'car-levy car-year'})
    car_body = info.find('div', {'class': 'car-body-wrapper'})
    figure_list = car_body.find('div', {'class': 'search-list-figure'})
    gaz_details = car_body.find('div', {'class': 'car-list-detail'})
    motor = gaz_details.find('div', {'class': 'car-detail-in cr-engine'})
    cr_road = gaz_details.find('div', {'class': 'car-detail-in cr-road'})
    wheel = gaz_details.find('div', {'class': 'car-detail-in cr-wheel'})
    gas = gaz_details.find('div', {'class': 'car-detail-in cr-1s cr-gas'})

    motor_size = motor.text
    road = cr_road.text
    wheel_t = wheel.text
    name = car_name.text
    year = car_year1.text
    print(name, year, motor_size, road, wheel_t)

def main():
    motor_size, road, wheel_t, name, year

    data = {}
    data = {
        "ძრავის მოცულობა": motor_size,
        "გარბენი": road,
        "საწვავის ტიპი": wheel_t,
        "სახელი": name,
        "წელი": year
    }
    print(json.dumps(data))
