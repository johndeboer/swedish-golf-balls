# data_scripts

The scripts used to scrape and format the data for Swedish Golf Balls

## How To Run

Start with the `*-scrape.py` scripts, these will use requests to the IKEA and Topgolf websites to grab the list of US stores and addresses, dumping them into text files.

Next up, `*-parse-geocode.py` scripts will parse the text files, use the Open Street Map Nominatim API to attempt geocoding the addresses, and write to .json files.

Run the `*-correct.py` scripts to find addresses that failed to geocode. The script will prompt for latitude and longitude values for the missed addresses, which you can find manually and enter.

Lastly, `nearest-partner.py` will use GeoPy to calculate the distance between stores and update the .json files with nearest corresponding store attributes.

The produced .json files are copied to the Vue project's public directory so that they can be queried by the app at runtime.
