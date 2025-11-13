
# region Circuit

PAYLOAD_CIRCUIT = {
    "name" : "Testname",
    "city" : "Testcity",
    "country" : "Testcountry",
    "first_grand_prix_year" : 2000,
    "length_km" : 5.0,
    "number_of_laps" : 50,
    "fastest_lap_time" : 90.5
}

PAYLOAD_CIRCUIT_UPDATE = {
    "name" : "Updatedname",
    "city" : "Updatedcity",
    "country" : "Updatedcountry",
    "first_grand_prix_year" : 1999,
    "length_km" : 4.5,
    "number_of_laps" : 55,
    "fastest_lap_time" : 88.3
}
# endregion

# region Team
PAYLOAD_TEAM = {
    "name" : "Testname",
    "country" : "Testcountry",
    "address" : "Testaddress",
    "team_principal" : "Testteamprincipal",
    "founded_year" : 2000,
    "total_points": 54,
    "total_wins": 7,
    "championships_won": 1,
    "is_actual_champion": False,
    "logo_url": "logo.png"
}

PAYLOAD_TEAM_UPDATE = {
    "name" : "Updatename",
    "country" : "Updatecountry",
    "address" : "Updateaddress",
    "team_principal" : "Updateteamprincipal",
    "founded_year" : 2010,
    "total_points": 145,
    "total_wins": 34,
    "championships_won": 4,
    "is_actual_champion": True,
    "logo_url": "update.png"
}
# endregion

# region Driver
PAYLOAD_DRIVER = {
    "driver_ref" : "TES",
    "first_name" : "Testfirstname",
    "last_name" : "Testlastname",
    "nationality" : "Testnationality",
    "birth_date" : "1980-05-23",
    "is_actual_champion" : True,
    "is_using_number_one" : True,
    "car_number" : 3,
    "team_id" : 1,
    "total_points" : 234,
    "total_wins" : 3,
    "total_podiums" : 7,
    "number_championship_won" : 1,
    "image" : "image.png"
}

PAYLOAD_DRIVER_UPDATE = {
    "driver_ref" : "UPD",
    "first_name" : "Updatefirstname",
    "last_name" : "Updatelastname",
    "nationality" : "Updatenationality",
    "birth_date" : "1997-12-05",
    "is_actual_champion" : False,
    "is_using_number_one" : False,
    "car_number" : 45,
    "team_id" : 3,
    "total_points" : 87,
    "total_wins" : 0,
    "total_podiums" : 1,
    "number_championship_won" : 0,
    "image" : "update.png"
}