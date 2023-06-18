import requests
import urllib.parse
from dash import html

class WebsiteCarbonEmissionAPI:
   
    def __init__(self, website_url):
        self.website_url = website_url
        self.api_root_url = "https://api.websitecarbon.com/site?url="
        self.green_flag = None                      # Whether the site is using environmentally sustainable hosting.
        self.adjusted_kilobytes_transferred = None  # The approximate number of bytes transferred by the page load, adjusted to take first time vs returning visitor percentage into account.
        self.cleaner_than_percent = "--"            # A numeric value between 0 and 1 representing the percentage of tested resources this is cleaner than.
        self.energy_transferred = "--"              # The approximate amount of energy transferred on each page load in KWg.
        self.co2_transferred_grams = "--"           # The approximate amount of CO2 transferred on each page load in grams.
        self.co2_transferred_litres = "--"          # The approximate amount of CO2 transferred on each page load in liters.


    def get_carbon_emission_data(self):
        final_url = self.api_root_url + self.string_to_url_paramater(self.website_url)
        # print(requests.get(final_url).json())
        result = requests.get(final_url).json()
        result_dict = dict(result)
        # print("=====================================")
        # print(result_dict)

        if len(result_dict) == 0:
            return html.Div()
        else:
            self.green_flag = result_dict['green']
            self.adjusted_kilobytes_transferred = round(result_dict['statistics']['adjustedBytes']/1024, 0)
            self.cleaner_than_percent = result_dict['cleanerThan']*100
            self.energy_transferred = result_dict['statistics']['energy']
            self.co2_transferred_grams = round(result_dict['statistics']['co2']['grid']['grams'],2)
            self.co2_transferred_litres = round(result_dict['statistics']['co2']['grid']['litres'], 2)
            return html.Div()

    def string_to_url_paramater(self, string):
        return urllib.parse.quote_plus(string)

    def get_green_flag(self):
        return self.green_flag
    
    def get_adjusted_kilobytes_transferred(self):
        return self.adjusted_kilobytes_transferred
    
    def get_cleaner_than_percent(self):
        return self.cleaner_than_percent
    
    def get_energy_transferred(self):
        return self.energy_transferred
    
    def get_co2_transferred_grams(self):
        return self.co2_transferred_grams
    
    def get_co2_transferred_litres(self):
        return self.co2_transferred_litres
