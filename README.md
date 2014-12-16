scrapey
=======
wow maps

This will let you get the trip info between point a and point b using google maps. It will give you mileage and time with traffic.

## Using Scrapey

To get the server running:
```shell
git clone https://github.com/evanscottgray/scrapey
cd scrapey
pip install -r requirements.txt
python scrapey.py
```
Background the process or open a new terminal and then run something like this:
```shell
curl "localhost:5000/?source=1%20Infinite%20Loop%2C%20Cupertino%2C%20CA%2095014&destination=1600%20Amphitheatre%20Parkway%2C%20Mountain%20View%2C%20CA%2094043" | python -m json.tool
```
That will give you trip info for a trip between the Apple and Google campuses in a format like this:
```json
{
    "destination": "1600 Amphitheatre Parkway, Mountain View, CA 94043",
    "source": "1 Infinite Loop, Cupertino, CA 95014",
    "trip_info": {
        "miles": 9.1,
        "minutes": 13.0
    }
}
```

Yay fun!

## Quickstart Docker

If you have docker and want to just get going, simply do this:
```shell
docker run -dP --name=scrapey evanscottgray/scrapey
```
That will spawn a container named scrapey in the background.

Getting exposed port info is simple:
```
docker port scrapey
```
