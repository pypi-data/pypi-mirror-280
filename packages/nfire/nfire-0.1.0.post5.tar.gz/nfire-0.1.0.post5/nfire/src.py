import pandas as pd
import requests
import json
from time import sleep

from typing import List, Tuple, Optional


class Nfire:
    def __init__(
        self, map_keys: List[str], sources: List[str], verbose: bool = False
    ) -> None:
        self.__map_keys = map_keys
        self.__url = "https://firms.modaps.eosdis.nasa.gov/api/area/csv/{MAP_KEY}/{SOURCE}/{R}/{DAYS_RANGE}/{DATE}"
        self.__sources = sources

        self.__current_map_key_idx = None

        self.__assign_map_key()

        self.verbose = verbose

    def __assign_map_key(self) -> None:

        if self.__current_map_key_idx is None:
            self.__current_map_key_idx = 0
        elif self.__current_map_key_idx == len(self.__map_keys) - 1:
            self.__current_map_key_idx = 0
        elif self.__current_map_key_idx < len(self.__map_keys) - 1:
            self.__current_map_key_idx += 1

    def __check_limit(self):
        _url = "https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY={MAP_KEY}"
        url = _url.format(MAP_KEY=self.__map_keys[self.__current_map_key_idx])  # type: ignore
        response = requests.get(url)
        data = json.loads(response.text)
        if data["current_transactions"] > 900:
            if self.verbose:
                print(f"Map key {self.__current_map_key_idx} has reached the limit")
            self.__assign_map_key()
            self.__check_limit()

        if self.verbose:
            rem = 1000 - data["current_transactions"]
            print(f"Map key {self.__current_map_key_idx} has {rem} transactions left")

    def __split_date_range(
        self, start_date: str, end_date: str
    ) -> Tuple[List[str], Optional[List[str]]]:
        start_date = pd.to_datetime(start_date)  # type: ignore
        end_date = pd.to_datetime(end_date)  # type: ignore
        date_range = pd.date_range(start_date, end_date, freq="D")
        # how many days in the range
        days_range = len(date_range)
        # if the range is more than 10 days, split the range into two ranges 10 days + the remaining days
        if days_range > 10:
            # get the first 10 days
            first_10_days = date_range[:10]
            first_10_days = [d.strftime("%Y-%m-%d") for d in first_10_days]
            # get the remaining days
            remaining_days = date_range[10:]
            remaining_days = [d.strftime("%Y-%m-%d") for d in remaining_days]
            return first_10_days, remaining_days
        else:
            date_range = [d.strftime("%Y-%m-%d") for d in date_range]
            return date_range, None

    def __query_data(self, R: str, days_range: int, date: str) -> List[pd.DataFrame]:
        data = []
        for source in self.__sources:

            sleep(10)

            url = self.__url.format(
                MAP_KEY=self.__map_keys[self.__current_map_key_idx],  # type: ignore
                SOURCE=source,
                R=R,
                DAYS_RANGE=days_range,
                DATE=date,
            )

            self.__check_limit()

            df = pd.read_csv(url)

            assert df.columns[0] == "latitude", "A map key has reached the limit"

            if not df.empty:
                data.append(df)

        return data

    def get_fire_dates(self, geofence, start_date, end_date) -> List:
        min_lat = min([point[1] for point in geofence])
        max_lat = max([point[1] for point in geofence])

        min_lon = min([point[0] for point in geofence])
        max_lon = max([point[0] for point in geofence])

        R = f"{min_lon},{min_lat},{max_lon},{max_lat}"

        data = []

        first_10_days, remaining_days = self.__split_date_range(start_date, end_date)

        # get data for the first 10 days
        data.extend(self.__query_data(R, len(first_10_days), first_10_days[0]))

        if remaining_days:
            # if len of remaining days is more than 10, split the range again
            if len(remaining_days) > 10:
                first_10_days, remaining_days = self.__split_date_range(
                    remaining_days[0], remaining_days[-1]
                )
                while remaining_days:
                    data.extend(
                        self.__query_data(R, len(first_10_days), first_10_days[0])
                    )
                    first_10_days, remaining_days = self.__split_date_range(
                        remaining_days[0], remaining_days[-1]
                    )
            else:
                data.extend(
                    self.__query_data(R, len(remaining_days), remaining_days[0])
                )

        """ df = pd.concat(data).drop_duplicates().reset_index(drop=True)

        return list(df.acq_date.values) """

        if data:
            df = pd.concat(data).drop_duplicates().reset_index(drop=True)
            return list(df.acq_date.values)

        return []
