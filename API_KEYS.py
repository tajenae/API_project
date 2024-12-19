# function to load API key - as I dont want it to be uploaded anywhere else but in my code.
def load_api_key(file_name):
    
    with open(file_name, 'r') as file:
        return file.read().strip()

# load the NOAA API key which I stored in the noaa_api_key.txt file. this file was added to my .gitignore file.
def load_noaa_api_key():
    return load_api_key('noaa_api_key.txt')

