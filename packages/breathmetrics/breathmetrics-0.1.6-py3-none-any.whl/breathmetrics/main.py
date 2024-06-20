"""
Module: Breathmetrics

This module defines the Breathmetrics class for analyzing breathing data, calculating metrics, and generating results.

Dependencies:
- numpy as np
- pandas as pd
- openpyxl
- breathmetrics_function.createBreathmetricsData.create_breathmterics_data
- breathmetrics_function.getInhaleExhaleonsets.onsets_detection
- breathmetrics_function.getBreathingRate.breathing_rate
- breathmetrics_function.getTidalVolume.get_tidal_volume

"""

import numpy as np
import pandas as pd

from utils.multiplot import multiplot
from breathmetrics_function.createBreathmetricsData import create_breathmterics_data
from breathmetrics_function.getBreathingRate import breathing_rate
from breathmetrics_function.getInhaleExhaleonsets import onsets_detection
from breathmetrics_function.getTidalVolume import get_tidal_volume


class Breathmetrics:
    """
    A class for analyzing breathing data, calculating metrics, and generating results.

    This class allows you to perform an analysis of breathing data, calculate metrics such as breathing rate,
    interbreath interval, tidal volume rate, and minute ventilation, and generate results and summaries.

    Attributes:
        yhat (list): A list of breathing data values.
        xaxis (list): A list of time values corresponding to the breathing data.
        sample_rate (float): The sample rate of the breathing data.
        x (list): A list of indices for splitting the data into segments.
        index (int): An index for excel sheet pages number.
        df (pandas.DataFrame): A DataFrame to store analysis results.

    Methods:
        __init__(self, path: str, minutes: int, minute_split: int) -> None:
            Initialize the Breathmetrics analysis and process data.

        __str__(self) -> str:
            Return a string representation of the Breathmetrics analysis summary.
    """

    def __init__(self, data: str, minutes: int, minute_split: int) -> None:
        """
        Initialize the Breathmetrics.

        Args:
            path (str): The path to the breathing data file.
            minutes (int): Total duration of data in minutes.
            minute_split (int): Split duration in minutes for analysis.

        This constructor initializes the Breathmetrics analysis, processes the data, and calculates metrics.

        """

        self.sensor_temp1 = data["Sensor1_Temp"].tolist()
        self.sensor_temp2 = data["Sensor2_Temp"].tolist()
        # self.sensor_pressure1 = data['Sensor1_Pressure'].tolist()
        # self.sensor_pressure2 = data['Sensor2_Pressure'].tolist()
        # self.sensor_humidity1 = data['Sensor1_Humidity'].tolist()
        # self.sensor_humidity2 = data['Sensor2_Humidity'].tolist()
        self.raw_temp_1, self.temp_1, self.default_xaxis, self.sample_rate = (
            create_breathmterics_data(self.sensor_temp1, minutes)
        )
        self.raw_temp_2, self.temp_2, _, _ = create_breathmterics_data(
            self.sensor_temp2, minutes
        )
        # self.raw_pressure_1, self.pressure_1, _, _ = create_breathmterics_data(self.sensor_pressure1, minutes)
        # self.raw_pressure_2, self.pressure_2, _, _ = create_breathmterics_data(self.sensor_pressure2, minutes)
        # self.raw_humidity_1, self.humidity_1, _, _ = create_breathmterics_data(self.sensor_humidity1, minutes)
        # self.raw_humidity_2, self.humidity_2, _, _ = create_breathmterics_data(self.sensor_humidity2, minutes)
        # multiplot('Raw Data',
        #           self.default_xaxis, self.raw_temp_1, self.raw_temp_2,
        #           self.raw_pressure_1, self.raw_pressure_2,
        #           self.raw_humidity_1, self.raw_humidity_2)
        # multiplot('Processed Data',
        #           self.default_xaxis, self.temp_1, self.temp_2,
        #           self.pressure_1, self.pressure_2,
        #           self.humidity_1, self.humidity_2)
        self.x = [
            int(x)
            for x in np.linspace(0, len(self.temp_1), (minutes // minute_split) + 1)
        ]
        self.index = 0
        self.df = pd.DataFrame()
        self.results = []
        for i in range(len(self.x) - 1):
            # print('\n=======================================================')
            start = str(minute_split * i)
            end = str(minute_split * (i + 1))
            # print("Duration = " + start + "min to " + end + "min")
            self.temp_1_sliced = self.temp_1[(self.x[i] + 1) : self.x[i + 1]]
            self.temp_2_sliced = self.temp_2[(self.x[i] + 1) : self.x[i + 1]]
            self.x_sliced = []
            self.index += 1
            for j in range(len(self.temp_1_sliced)):
                self.x_sliced.append(j / self.sample_rate)
            self.temp_1_inhaleonsets, self.temp_1_exhaleonsets = onsets_detection(
                start,
                end,
                "Sensor-1",
                self.temp_1_sliced,
                self.x_sliced,
                self.sample_rate,
            )
            self.temp_2_inhaleonsets, self.temp_2_exhaleonsets = onsets_detection(
                start,
                end,
                "Sensor-2",
                self.temp_2_sliced,
                self.x_sliced,
                self.sample_rate,
            )
            (
                self.temp_1_breathing_rate,
                self.temp_1_inhale_interbreath_interval,
                self.temp_1_exhale_interbreath_interval,
                self.temp_1_interbreath_interval,
            ) = breathing_rate(
                self.temp_1_inhaleonsets, self.temp_1_exhaleonsets, self.sample_rate
            )
            (
                self.temp_2_breathing_rate,
                self.temp_2_inhale_interbreath_interval,
                self.temp_2_exhale_interbreath_interval,
                self.temp_2_interbreath_interval,
            ) = breathing_rate(
                self.temp_2_inhaleonsets, self.temp_2_exhaleonsets, self.sample_rate
            )
            self.temp_1_volume = get_tidal_volume(
                self.temp_1_sliced,
                self.temp_1_exhaleonsets,
                self.sample_rate,
                self.temp_1_interbreath_interval,
                self.index,
            )
            self.temp_2_volume = get_tidal_volume(
                self.temp_2_sliced,
                self.temp_2_exhaleonsets,
                self.sample_rate,
                self.temp_2_interbreath_interval,
                self.index,
            )
            self.temp_1_minute_ventilation = round(
                self.temp_1_breathing_rate * self.temp_1_volume, 2
            )
            self.temp_2_minute_ventilation = round(
                self.temp_2_breathing_rate * self.temp_2_volume, 2
            )
            data = [
                f"{minute_split*i} min to {minute_split*(i+1)} min",
                self.temp_1_breathing_rate,
                self.temp_2_breathing_rate,
                self.temp_1_inhale_interbreath_interval,
                self.temp_2_inhale_interbreath_interval,
                self.temp_1_exhale_interbreath_interval,
                self.temp_2_exhale_interbreath_interval,
                self.temp_1_interbreath_interval,
                self.temp_2_interbreath_interval,
                self.temp_1_volume,
                self.temp_2_volume,
                self.temp_1_minute_ventilation,
                self.temp_2_minute_ventilation,
            ]
            self.df = pd.concat([self.df, pd.DataFrame(data).T])
            temp_1_result = {
                "Duration": f"{start} - {end} mins",
                "YData": self.temp_1_sliced,
                "XData": self.x_sliced,
                "InhaleOnsets": self.temp_1_inhaleonsets,
                "ExhaleOnsets": self.temp_1_exhaleonsets,
                "BreathingRate": self.temp_1_breathing_rate,
                "InterbreathInterval": self.temp_1_interbreath_interval,
                "InhaleInterbreathInterval": self.temp_1_inhale_interbreath_interval,
                "ExhaleInterbreathInterval": self.temp_1_exhale_interbreath_interval,
                "TidalVolume": self.temp_1_volume,
                "MinuteVentilation": self.temp_1_minute_ventilation,
            }
            self.results.append(temp_1_result)
            temp_2_result = {
                "Duration": f"{start} - {end} mins",
                "YData": self.temp_2_sliced,
                "XData": self.x_sliced,
                "InhaleOnsets": self.temp_2_inhaleonsets,
                "ExhaleOnsets": self.temp_2_exhaleonsets,
                "BreathingRate": self.temp_2_breathing_rate,
                "InterbreathInterval": self.temp_2_interbreath_interval,
                "InhaleInterbreathInterval": self.temp_2_inhale_interbreath_interval,
                "ExhaleInterbreathInterval": self.temp_2_exhale_interbreath_interval,
                "TidalVolume": self.temp_2_volume,
                "MinuteVentilation": self.temp_2_minute_ventilation,
            }
            self.results.append(temp_2_result)
            # print("Sensors                     : Sensor 1 | Sensor 2")
            # print(
            #     f"Breathing Rate              : {self.temp_1_breathing_rate}   | {self.temp_2_breathing_rate} breaths/min"
            # )
            # print(
            #     f"Inhale Interbreath Interval : {self.temp_1_inhale_interbreath_interval}    | {self.temp_2_inhale_interbreath_interval} sec"
            # )
            # print(
            #     f"Exhale Interbreath Interval : {self.temp_1_exhale_interbreath_interval}    | {self.temp_2_exhale_interbreath_interval} sec"
            # )
            # print(
            #     f"Interbreath Interval        : {self.temp_1_interbreath_interval}    | {self.temp_2_interbreath_interval} sec"
            # )
            # print(
            #     f"Tidal Volume Rate           : {self.temp_1_volume}   | {self.temp_2_volume} mL/breath"
            # )
            # print(
            #     f"Minute Ventilation          : {self.temp_1_minute_ventilation}  | {self.temp_2_minute_ventilation} mL/min"
            # )
            # print("\n=======================================================")
        self.temp_1_inhaleonsets, self.temp_1_exhaleonsets = onsets_detection(
            0,
            minute_split * (i + 1),
            "Sensor 1",
            self.temp_1,
            self.default_xaxis,
            self.sample_rate,
        )
        self.temp_2_inhaleonsets, self.temp_2_exhaleonsets = onsets_detection(
            0,
            minute_split * (i + 1),
            "Sensor 2",
            self.temp_2,
            self.default_xaxis,
            self.sample_rate,
        )
        (
            self.temp_1_breathing_rate,
            self.temp_1_inhale_interbreath_interval,
            self.temp_1_exhale_interbreath_interval,
            self.temp_1_interbreath_interval,
        ) = breathing_rate(
            self.temp_1_inhaleonsets, self.temp_1_exhaleonsets, self.sample_rate
        )
        (
            self.temp_2_breathing_rate,
            self.temp_2_inhale_interbreath_interval,
            self.temp_2_exhale_interbreath_interval,
            self.temp_2_interbreath_interval,
        ) = breathing_rate(
            self.temp_2_inhaleonsets, self.temp_2_exhaleonsets, self.sample_rate
        )
        self.temp_1_volume = get_tidal_volume(
            self.temp_1,
            self.temp_1_exhaleonsets,
            self.sample_rate,
            self.temp_1_interbreath_interval,
            len(self.temp_1),
        )
        self.temp_2_volume = get_tidal_volume(
            self.temp_2,
            self.temp_2_exhaleonsets,
            self.sample_rate,
            self.temp_2_interbreath_interval,
            len(self.temp_2),
        )
        self.temp_1_minute_ventilation = round(
            self.temp_1_breathing_rate * self.temp_1_volume, 2
        )
        self.temp_2_minute_ventilation = round(
            self.temp_2_breathing_rate * self.temp_2_volume, 2
        )
        temp_1_result = {
            "Duration": f"0 - {minute_split * (i + 1)} mins",
            "YData": self.temp_1,
            "XData": self.default_xaxis,
            "InhaleOnsets": self.temp_1_inhaleonsets,
            "ExhaleOnsets": self.temp_1_exhaleonsets,
            "BreathingRate": self.temp_1_breathing_rate,
            "InterbreathInterval": self.temp_1_interbreath_interval,
            "InhaleInterbreathInterval": self.temp_1_inhale_interbreath_interval,
            "ExhaleInterbreathInterval": self.temp_1_exhale_interbreath_interval,
            "TidalVolume": self.temp_1_volume,
            "MinuteVentilation": self.temp_1_minute_ventilation,
        }
        self.results.append(temp_1_result)
        temp_2_result = {
            "Duration": f"0 - {minute_split * (i + 1)} mins",
            "YData": self.temp_2,
            "XData": self.default_xaxis,
            "InhaleOnsets": self.temp_2_inhaleonsets,
            "ExhaleOnsets": self.temp_2_exhaleonsets,
            "BreathingRate": self.temp_2_breathing_rate,
            "InterbreathInterval": self.temp_2_interbreath_interval,
            "InhaleInterbreathInterval": self.temp_2_inhale_interbreath_interval,
            "ExhaleInterbreathInterval": self.temp_2_exhale_interbreath_interval,
            "TidalVolume": self.temp_2_volume,
            "MinuteVentilation": self.temp_2_minute_ventilation,
        }
        self.results.append(temp_2_result)
        data = [
            f"0 min to {minute_split*(i+1)} min",
            self.temp_1_breathing_rate,
            self.temp_2_breathing_rate,
            self.temp_1_inhale_interbreath_interval,
            self.temp_2_inhale_interbreath_interval,
            self.temp_1_exhale_interbreath_interval,
            self.temp_2_exhale_interbreath_interval,
            self.temp_1_interbreath_interval,
            self.temp_2_interbreath_interval,
            self.temp_1_volume,
            self.temp_2_volume,
            self.temp_1_minute_ventilation,
            self.temp_2_minute_ventilation,
        ]
        self.df = pd.concat([self.df, pd.DataFrame(data).T])
        self.df.columns = [
            "Duration",
            "Breathing Rate 1",
            "Breathing Rate 2",
            "Inhale Interbreath Interval 1",
            "Inhale Interbreath Interval 2",
            "Exhale Interbreath Interval 1",
            "Exhale Interbreath Interval 2",
            "Interbreath Interval 1",
            "Interbreath Interval 2",
            "Tidal Volume Rate 1",
            "Tidal Volume Rate 2",
            "Minute Ventilation 1",
            "Minute Ventilation 2",
        ]
        self.df.to_csv("Results.csv", index=False)

    def __str__(self) -> str:
        """
        Return a string representation of the Breathmetrics analysis summary.

        Returns:
            str: A string containing the summary of the analysis.

        This method returns a summary of the analysis, including breathing rate, interbreath interval,
        tidal volume rate, and minute ventilation.

        """
        return f"""
=======================================================
Summary of Complete Data without segmentation
Sensors                     : Sensor 1 | Sensor 2
Breathing Rate              : {self.temp_1_breathing_rate}   | {self.temp_2_breathing_rate} breaths/min
Inhale Interbreath Interval : {self.temp_1_inhale_interbreath_interval}    | {self.temp_2_inhale_interbreath_interval} sec
Exhale Interbreath Interval : {self.temp_1_exhale_interbreath_interval}    | {self.temp_2_exhale_interbreath_interval} sec
Interbreath Interval        : {self.temp_1_interbreath_interval}    | {self.temp_2_interbreath_interval} sec
Tidal Volume Rate           : {self.temp_1_volume}   | {self.temp_2_volume} mL/breath
Minute Ventilation          : {self.temp_1_minute_ventilation}  | {self.temp_2_minute_ventilation} mL/min
\n=======================================================
\n=======================================================
"""

    def show_results(self):
        return self.results


# if __name__ == "__main__":
#     data = pd.read_csv("./Sample.csv")
#     breathing_instance = Breathmetrics(data, 15, 2)
#     results = breathing_instance.show_results()
#     print(results)
# print(breathing_instance)
