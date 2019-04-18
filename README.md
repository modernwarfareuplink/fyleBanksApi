# FYLE BANK API: Getting Started

A simple web application to fetch bank details based on ifsc code, and branches of a bank in a city

## View Application online

You can have a look at this application hosted on heroku [here](https://fierce-reaches-85054.herokuapp.com/)

## Running Locally

Make sure you have Python 3.6.6 [installed locally](http://install.python-guide.org). Postgresql and git should also be installed locally.

Before checking the API, please make a database named "fyledb" in postgres and import the dump data available at the [repository](https://github.com/snarayanank2/indian_banks)

Update the details of postgres db in settings.py file within gettingstarted folder

```sh
$ git clone https://github.com/modernwarfareuplink/fyleBanksApi.git
$ cd fyleBanksApi

$ pip install -r requirements.txt

$ python3 manage.py runserver
```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## API Documentation

/ifsc/<ifsc_code_here>/

/search?name=bank_name&city=city_name

/credits

A detailed documentation of the API is available at [here](https://documenter.getpostman.com/view/5036904/S1ERwxDm)

## Database dump

Database dump is available in this [repository](https://github.com/snarayanank2/indian_banks)

## Pull requests

Pull requests to this repository are welcomed!. Contact me for any queries at aruntvs227@gmail.com
