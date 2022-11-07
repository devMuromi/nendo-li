import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nendo_li.settings")
import django

django.setup()

import requests


from nendoroid.serializers import NendoroidSerializer
from nendoroid.models import Nendoroid, Series


DB_URL = "https://raw.githubusercontent.com/KhoraLee/NendoroidDB/main/"
API_URL = "https://api.github.com/repos/KhoraLee/NendoroidDB/contents/"
TOKEN = "token "


def get(url):
    # headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    headers = {
        "Content-Type": "application/json",
        "charset": "UTF-8",
        "Accept": "*/*",
        "Authorization": TOKEN,
    }
    try:
        response = requests.get(url, headers=headers)
        return response.json()
    except Exception as e:
        print(e)
        return


def get_list_path_list():
    URL = API_URL + "Nendoroid/"
    list_list = get(URL)

    return_list = []
    for list in list_list:
        return_list.append(list.get("path"))
    return return_list


def get_nendoroid_path_list():
    nendoroid_list_path_list = get_list_path_list()
    nendoroid_list_path_list.remove("Nendoroid/Set")  # 시리즈 폴더 제거

    return_list = []
    for nendoroid_list_path in nendoroid_list_path_list:
        URL = API_URL + nendoroid_list_path + "/"
        nendoroid_list = get(URL)
        for nendoroid in nendoroid_list:
            return_list.append(nendoroid.get("path"))
    return return_list


def get_series_path_list():
    series_list_path = "Nendoroid/Set"

    return_list = []
    URL = API_URL + series_list_path + "/"
    series_list = get(URL)
    for series in series_list:
        return_list.append(series.get("path"))
    return return_list


def get_nendoroid():
    nendoroid_path_list = get_nendoroid_path_list()

    for nendoroid_path in nendoroid_path_list:
        URL = DB_URL + nendoroid_path
        initial_nendoroid_data = get(URL)
        validated_nendoroid_data = dict()
        print(initial_nendoroid_data["num"], "넨도로이드 처리중")
        try:
            validated_nendoroid_data["number"] = initial_nendoroid_data["num"]
            if "name" in initial_nendoroid_data:
                validated_nendoroid_data["name_ko"] = (
                    initial_nendoroid_data["name"]["ko"]
                    if "ko" in initial_nendoroid_data["name"]
                    else ""
                )
                validated_nendoroid_data["name_en"] = (
                    initial_nendoroid_data["name"]["en"]
                    if "en" in initial_nendoroid_data["name"]
                    else ""
                )
                validated_nendoroid_data["name_ja"] = (
                    initial_nendoroid_data["name"]["ja"]
                    if "ja" in initial_nendoroid_data["name"]
                    else ""
                )
            validated_nendoroid_data["release_date"] = (
                initial_nendoroid_data["release_date"]
                if "release_date" in initial_nendoroid_data
                else None
            )
            validated_nendoroid_data["image_link"] = (
                initial_nendoroid_data["image"]
                if "image" in initial_nendoroid_data
                else ""
            )
            if "gender" in initial_nendoroid_data:
                if (
                    initial_nendoroid_data["gender"] == "M"
                    or initial_nendoroid_data["gender"] == "F"
                ):
                    validated_nendoroid_data["gender"] = initial_nendoroid_data[
                        "gender"
                    ]
                else:
                    validated_nendoroid_data["gender"] = "O"
            else:
                validated_nendoroid_data["gender"] = ""
            # 시리즈 추가하기

            serializer = NendoroidSerializer(data=validated_nendoroid_data)
            if serializer.is_valid():
                serializer.save()
                print(initial_nendoroid_data["num"], "넨도로이드 valid")
            else:
                print(serializer.errors)

        except Exception as e:
            print(e)


def get_series():
    # only gets name_ko
    series_path_list = get_series_path_list()

    for series_path in series_path_list:
        URL = DB_URL + series_path
        series_data = get(URL)
        print(series_data["num"], "시리즈 처리중")
        try:
            series = Series(name_ko=series_data["setName"])
            series.save()
        except Exception as e:
            print(e)

    # series_path = series_path_list[0]
    # URL = DB_URL + series_path
    # series_data = get(URL)


get_nendoroid()
