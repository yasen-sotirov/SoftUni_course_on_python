def forecast(*args):
    sunny_locations = []
    cloudy_locations = []
    rainy_locations = []
    output_list = []
    args = list(args)
    while len(args) > 0:
        el = args.pop()
        location = el[0]
        weather = el[1]
        if weather == "Sunny":
            sunny_locations.append(location)
        elif weather == "Cloudy":
            cloudy_locations.append(location)
        else:
            rainy_locations.append(location)

    if sunny_locations:
        sunny_locations = sorted(sunny_locations)
        for current_location in sunny_locations:
            output_list.append(f"{current_location} - Sunny")

    if cloudy_locations:
        cloudy_locations = sorted(cloudy_locations)
        for current_location in cloudy_locations:
            output_list.append(f"{current_location} - Cloudy")

    if rainy_locations:
        rainy_locations = sorted(rainy_locations)
        for current_location in rainy_locations:
            output_list.append(f"{current_location} - Rainy")

    return "\n".join(output_list)


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))




