echo "Generating \"myOpenWeatherKey.py\" file..."

echo "# This returns my OpenWeather API key in string format
# Should replace {MY_API_KEY} with my own API key

def myKey():
    return \"{MY_API_KEY}\"
    #       ^^^^^^^^^^^^  replace
" > myOpenWeatherKey.py

echo "
============================== DONE =============================
Please open the file and replace {MY_API_KEY} with your API key.
================================================================="
