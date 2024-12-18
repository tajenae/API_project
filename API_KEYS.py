# function to load API key - as I dont want it to be uploaded anywhere else but in the txt file.
def load_api_key(file_name):
    
    with open(file_name, 'r') as file:
        return file.read().strip()

# load the NOAA API key which i stored in the noaa_api_key.txt file which will be ignore by Github.
def load_noaa_api_key():
    return load_api_key('noaa_api_key.txt')

