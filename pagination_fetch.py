import requests
import json
import os
import datetime
def fetch_paginate(url: str, min_page: int = 0, max_page : int = -1, page_separation: bool = False) -> list:
    """
    Creates multiple requests to fetch a paginated API

        Args:
            url (string, required): The base-url of the page
            min_page (int, optional): The lowest page that should be fetched. Defaults to 0.
            max_page (int, optional): The highest page that should be fetched. -1 to fetch until no more results can be found. Defaults to -1.
            page_separation (bool, optional): If True, the results will be separated by page in form of an array. Defaults to False.    
        
        Returns:
            result (list): A list with data that was fetched from the url converted into a json format
    """
    result = []
    page = min_page
    while True:
        response = requests.get(f"{url}&page={page}").json()
        if len(response) == 0:
            print("All pages of API have been fetched.")
            return result
        if page_separation:
            result.append(response)
        else:
            result += response  
        if max_page != -1 and page >= max_page:
            print("Reached custom defined limit.")
            return result
        page = page + 1

def exportToJson(data:list, path: str = os.path.join(os.path.dirname(os.path.realpath(__file__)),"exports"), filename:str=f"data_{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.json") -> None:
    """
    Exports a list to a JSON-file.

        Args:
            data (list, required): Data to be exported
            path (str, optional): Path where the exported file should be written to. Defaults to the directory where the script is currently located.
            filename (str, optional): Name of the exported file. Defaults to data.json
    """
    if not os.path.exists(path):
        os.makedirs(path)
    
    jsonFile = open(os.path.join(path,filename), "w")
    jsonFile.write(json.dumps(data))
    jsonFile.close()
    print(f"Export completed. Data saved at {os.path.join(path,filename)}.")