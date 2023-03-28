# Unofficial Craigslist API

## About ⚡

---

[Craigslist](https://www.craigslist.org/about/sites) is a wonderful tool for finding classified ads for just about anything. This project is intended to make interfacing with Craigslist easier - so that you can build projects faster. There is LOTS more to be done so all contributions are more than welcome.

![I met mittens [the cat] on craigslist!](https://25.media.tumblr.com/1d3e40ff0553a1c4d53e08e62b6a88bf/tumblr_mn7c88xXDY1rc88bzo1_500.gif)

## Current Endpoints 🌱

> Any POST data must be sent as JSON, with attributes wrapped in a "data" object (See example requests below).

---

### `/api/v1/craigslist/vehicles`

**POST**

Searches for vehicles matching the paramaters supplied in the JSON body. Available parameters include:

```
    'location': String,
    'hasPhoto': Bool,
    'mostRecent': Bool,
    'noDuplicates': Bool,
    'zipCode': Integer,
    'searchDistance': Integer,
    'minPrice': Integer,
    'maxPrice': Integer,
    'make': String,
    'model': String,
    'minModelYear': Integer,
    'maxModelYear': Integer,
    'minOdometer': Integer,
    'maxOdometer': Integer
```

(ex. request)

```
{
    "data" : {
        "location": "desmoines",
        "make": "lexus",
        "maxPrice": 5000,
        "hasPhoto": true
    }
}
```
(ex. response) 
```
"data": {
    "result_4": {
        "title": "2003 LEXUS ES300 GOOD RUNNING CAR",
        "link": "https://rockford.craigslist.org/cto/d/rockford-2003-lexus-es300-good-running/7604046151.html",
        "price": "$2,900"
    },
    "result_5": {
        "title": "1997 Lexus ES 300 Sedan",
        "link": "https://kansascity.craigslist.org/cto/d/kansas-city-1997-lexus-es-300-sedan/7604002076.html",
        "price": "$4,200"
},
```

---

## TODO:✍🏽

---

Lots! More endpoints, cleanup on existing ones, documentation. Please feel free to contribute!
