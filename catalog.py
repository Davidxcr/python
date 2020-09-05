fhand = open('cd_catalog.xml', 'r').readline()

print()
print("{0:35}{1:20}{2:15}{3:15}{4:10}{5:15}".format("Title", "Artist", "Country", "Company", "Price", "Year"))
print()

i = 0
total_price = 0
count = 0

for cd in fhand:
    title = fhand[i][0]
    if title != None:
        pass
    else:
        title = "N/A"
    
    artist = fhand[i][1]
    if artist != None:
        pass
    else:
        artist = "N/A"

    country = fhand[i][2]
    if country != None:
        pass
    else:
        country = "N/A"
    
    company = fhand[i][3]
    if company != None:
        pass
    else:
        company = "N/A"
    
    price = fhand[i][4]
    if price != None:
        pass
    else:
        price = "N/A"
    
    year = fhand[i][5]
    if year != None:
        pass
    else:
        year = "N/A"
    
    i += 1

    print("{title: 35}{artist: 20}{country: 15}{company: 15}{price: 10}{year: 5}".format(
    title=title, artist=artist, country=country, company=company, price=price, year=year))

    total_price += float(price)
    count += 1

    print()
    average_price = round(total_price) + float(price)
    count += 1
    print("{count} items - $(average_price} average price".format(
        count = count, average_price = average_price))