# Reliable-Energy-Consumption-Analysis\
## Mail to : [suriyaa2002@gmail.com](mailto:suriyaa2002@gmail.com) for access to all the design documents listed below, report and full code

![image](https://github.com/SuriyaaVijay/Reliable-Energy-Consumption-Analysis/assets/92075531/5f4957bd-6931-4ac7-8552-854dd878b896)


## Contents
1. This project aims to predict the world active power 
2. From the predicted power, it uses ChatGPT API to give power saving recommendations on our total Energy Consumption.
3. UI is built using Python flask 
4. Also a time series LSTM for forecasting monthly power consumption is present.
5. All the design documents typically used in the Software world are provided for this project

## Description:
Active and reactive energy refer to the technical details of alternative current. In general terms, the active energy is the real power consumed by the household, whereas the reactive energy is the unused power in the lines. We can see that the dataset provides the active power as well as some division of the active power by main circuit in the house, specifically the kitchen, laundry, and climate control. These are not all the circuits in the household. The remaining watt-hours can be calculated from the active energy by first converting the active energy to watt-hours then subtracting the other sub-metered active energy in watt-hours, as follows:

The remaining watt-hours can be calculated from the active energy by first converting the active energy to watt-hours then subtracting the other sub-metered active energy in watt-hours, as follows:

 ![image](https://github.com/SuriyaaVijay/Reliable-Energy-Consumption-Analysis/assets/92075531/cf0ad888-dcc1-4845-9b5a-a806a67e8911)

## Features Information:

1. DateTime : Date and Time combined in format dd/mm/yyyy hh:mm:ss
2. global_active_power : household global minute-averaged active power (in kilowatt). Active power is the power that is consumed.
3. global_reactive_power : Household global minute-averaged reactive power (in kilowatt). Reactive power is the unsed power in the lines
4. voltage : Minute-averaged voltage (in volt)
5. global_intensity : Household global minute-averaged current intensity (in ampere)
6. sub_metering_1 : Energy sub-metering No. 1 (in watt-hour of active energy). It corresponds to the kitchen, containing mainly a dishwasher, an oven and a microwave (hot plates are not electric but gas powered).
7. sub_metering_2 : Energy sub-metering No. 2 (in watt-hour of active energy). It corresponds to the laundry room, containing a washing-machine, a tumble-drier, a refrigerator and a light.
8. sub_metering_3 : Energy sub-metering No. 3 (in watt-hour of active energy). It corresponds to an electric water-heater and an air-conditioner.
Predicting the world active power using C

#### Active and reactive energy refer to the technical details of alternative current.

In general terms, the active energy is the real power consumed by the household, whereas the reactive energy is the unused power in the lines.
We can see that the dataset provides the active power as well as some division of the active power by main circuit in the house, specifically the kitchen, laundry, and climate control. These are not all the circuits in the household.

