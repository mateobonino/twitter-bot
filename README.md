# Tweet data collector (DEVELOPING)



Bot coded in Python 3.10.5 usin Twitter API and Tweepy library.

This is a simple bot that collects tweets data such as body text, when it was created, the author and the tweet ID.

## Instructions

- Clone this repo
```
> git clone https://github.com/mateobonino/twitter-bot
```

- Create a Twitter Developer account, create a new app and save your API Key and API secret key.

- Put your keys in the file 'creds.py'

- Run the python script and pass the arguments for the search in this order

### Example:
```
> python3 app.py < keyword for the search >

>python3 app.py @elonmusk
```
You can search for keywords, mentions, etc.

## Output:

The result of your search will be saved into different JSON files, each one having the Tweet ID as filename.
```
{
    "tweet_date": "2022-11-30 19:53:28+00:00",
    "tweet_id": 1598042548706369536,
    "tweet_body": "@elonmusk  any update on @thedesertdaddy or @forestmommy   ??",
    "author_username": "@FMUniverse84",
    "author_name": "Santa's lil Forest Mommy",
    "author_id": 1573453575442792458
}
```

```
{
    "tweet_date": "2022-11-30 19:53:28+00:00",
    "tweet_id": 1598042549260005379,
    "tweet_body": "@carlos_veccio2 @LawrenceForbe16 @bennyjohnson @elonmusk Not",
    "author_username": "@judy_miron",
    "author_name": "Judy Miron",
    "author_id": 1176943679992422400
}
```

Created by: Mateo Bonino - <mbonino1810@gmail.com>