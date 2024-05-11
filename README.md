
<p align="center">
    <a>
        <img src="https://i.imgur.com/v5TxqD6.png" alt="cover"/>
    </a>
</p>
<p align="center">
    <a href="https://mit-license.org/">
        <img src="https://img.shields.io/badge/license-mit-915a9c?style=for-the-badge" alt="license">
    <a>
    <a href="https://www.python.org/downloads/release/python-3115/">
        <img src="https://img.shields.io/badge/python-v3.11.5-915a9c?style=for-the-badge" alt="version"/>
    <a>
    <a href="https://pypi.org/project/PySide6/6.4.2/">
        <img src="https://img.shields.io/badge/pyside6-v6.4.2-915a9c?style=for-the-badge" alt="version"/>
    </a>
</p>

<details>
<summary><kbd>Table of contents</kbd></summary>

- [Demo](#Demo)
- [Features](#Features) 
- [Installation](#Installation)
- [Usage](#Usage)
- [Customization](#️Customization)
- [Ecosystem](#Ecosystem)
- [Notes](#Notes)

####
<br/>
</details>

# Demo
Coming soon...

# Features

- `1` **Widget Customization**: Tailor your interface with fully customizable widgets or "display blocks" such as Graphs, Labels, Buttons, State Indicator and Countdown/up displays and save them as "DASHBOARDS".

- `2` **Dashboards**: Dashboards, stored as JSON files, enable dynamic management of display block collections. These files house properties such as data, color, placement, and other relevant parameters for the widgets. Users can create multiple dashboards based on different devices or specific tests/missions, providing organizational adaptability. The system supports dynamic visualization, allowing users to easily switch between dashboards while visualizing data or change dashboard parameters on the fly. See [Customization](#Customization) section.

- `3` **Cloud Integration**: Login with Google and use Drive for secure data backup storage and retrieval. Cloud mission/settings sync coming soon.

- `4` **Intelligent Packet Handling**: Distinguish between MSG (message) and TLM (telemetry) packets, presenting messages as notifications, retaining the ability to view previous notifications, and displaying telemetry in the widgets. Implement data discrimination based on signature headers for streamlined processing.

- `5` **Aesthetic Flexibility**: Personalize your user experience with a range of color themes to suit your preferences. Opt for a compact Small Mode for a focused view of essential information.

- `6` **Configuration Tab**: Switch dashboards, theme, packet handling properties and much more in the Configuration Tab. Widget customization and dashboard creation ? see [Customization](#Customization) section.

- `7` **Serial Terminal Integration**: A built-in Serial Terminal, providing efficient communication and data handling capabilities.

- `8` **Ecosystem**: Seamlessly create and edit missions, design custom dashboards, and analyze data with personalized reports. Our system sets a new standard for efficient CanSat mission management.

- `9` **Unrivaled in quality, uniqueness and Elegance**: this surpasses anything witnessed in a CanSat competition. Its exceptional attributes stand as a testament to innovation, and notably, it's available free of charge, setting a groundbreaking standard.

- `10` **Simplicity**: Most of the management and development actions can be done by using the "wm.py" script, see [Manager](#Manager) section.

**COMING SOON**

- **Collaborative Rooms For Data Sharing**: Connect a device to the serial interface, open a shared room, and link multiple computers. Easily view data from one computer on others, even with different dashboards.

- **Mission-Critical Features**: Implement Mission Mode, offering insights into weather alerts, launch window indications, and the next expected state. Facilitate data recording for comprehensive mission analysis.

# Ecosystem

- [Wavelabs](https://github.com/TecnoclubCansat/Cansat-Data-Analytics) - Data Analysis Interface, for Waves Recordings.

# Troubleshooting

> coming soon...

# Installation

### Windows

1. Clone the repository

```shell
git clone https://github.com/TecnoclubCansat/Cansat-Mission-Control.git
```

2. Change Directory to the cloned repository.

```shell
cd Cansat-Mission-Control
```

3. Setup Virtual Environment, name it **'.venv'**

```shell
python -m venv .venv
```

4. Activate the environment

```shell
.\.venv\Scripts\activate
```

3. Install Requirements

```shell
pip install -r requirements.txt
```

# Usage

### windows

1. Activate the environment (if not already activated, duh)

```shell
.\.venv\Scripts\activate
```

2. Call the launcher

```shell
python ./launcher.py
```

# Manager

Use the manager to access development/usage critical features

```shell
python wm.py -h
```

### Dashboard Management

```shell
python wm.py dashboard -h
```

> for more help, see [Dashboard Management](#dashboards-management)

### Format

add a header to all files and remove pycache files

```shell
python wm.py format -h
```

### Update Ui

transform the .ui files to .py, this files are in fixed directories './src/ui/design'

```shell
python wm.py updateui -h
```

### Cloud

At the moment only import credentials.

```shell
python wm.py cloud -h
```

# Customization

At the core of the project lies customization, flexibility, and adaptability for any device communicating over serial. The primary tools/systems facilitating this are the dashboards, as detailed in the [Features](#features).

## Dashboards Management

Dashboards organize and group display blocks cohesively, to modify them you will use the built in waves [manager](#Manager) (wm.py) Here is how:

### List Dashboards

List all the dashboards you currently have.

```shell
python ./wm.py dashboard list
```

### New Dashboard

This command will create a new dashboard, name it what you want, names are not permanent.

```shell
python ./wm.py dashboard new {NAME}
```

### Edit Dashboard

In next versions this will open the interface for dashboard editing, currently it will open the file in your default editor. for more information about actual editing see [Dashboard Editing](#editing-dashboards)

```shell
python ./wm.py dashboard edit {NAME}
```

### Clone Dashboard

Clone dashboards for convenience, for example if you are testing a new graph or whatever for a new sensor.

NAME_DASHBOARD_TO_CLONE: The dashboard you want to clone.

NEW_DASHBOARD_NAME: The name of dashboard that will be created with the cloned data.

```shell
python ./wm.py dashboard clone {NAME_DASHBOARD_TO_CLONE} {NEW_DASHBOARD_NAME}
```

### Delete Dashboard

Delete an existing dashboard.

```shell
python ./wm.py dashboard del {NAME}
```

### Fix Dashboards

In case you mess up something or want to reset the dashboards.

```shell
python ./wm.py dashboard fix
```

### Import/Export Dashboards

Export your current dashboards to a single manageable file, and the use import to import them.

```shell
python ./wm.py import {path}
```

```shell
python ./wm.py export
```

## Editing Dashboards

Inside of a dashboard json file, you can fine-tune all the aspects of your dashboard, i recommend to looking at the default dashboard, using the managers [edit command](#edit-dashboard) at the name "default".

Before proceeding, familiarize yourself with the term:

> **value_index_in_chain:** This refers to the index position of the value in the packet value chain. For example in the image the highlighted value is at index 0, a widget set to display data for value*index_in_chain in \_0* will always show the value at that position, in this example the widget will display/plot 0, if the _'value_index_in_chain'_ will be at _1_ it would have displayed/plotted 3 then 4 then 5.

<p align="center">
    <a>
        <img src="https://i.imgur.com/MEIJJza.png" alt="packet"/>
    </a>
</p>

> What you should put in 'value*index_in_chain' are the purple numbers, in this case the 5 is the latitude so if i wanted to display it i would set the value_index_in_chain to \_5*:

<p align="left">
    <a>
        <img src="https://i.imgur.com/079n2hJ.png" alt="packet"/>
    </a>
</p>

---

For creating a new dashboards use the command [new](#new-dashboard) of the manager, after that a json will be opened in your default editor, you will see a structure like this:

### General Information

<p align="center">
    <a>
        <img src="https://i.imgur.com/o4Lit1o.png" alt="information"/>
    </a>
</p>

1. **NAME:** Display name of the dashboard.
2. **MAX_COLS:** Determines the maximum number of columns allowed in the left panel. Setting it to 1 allows only one widget per row. For instance, if you have 2 buttons and set MAX_COLS to 1, you'll need two rows. If MAX_COLS is set to 2, both buttons can fit in a single row.
3. **PEN_WIDTH:** The thickness sor of the graph lines (pixels).
4. **DATA_POINTS:** Determines the quantity of data points in each graph. A lower value, such as 200, prioritizes better performance with less detailed data over time. Conversely, a higher value, like 600, showcases more data over time but may impact performance. Adjust based on your update time and compute power; slower updates can benefit from fewer data points for optimized performance.
5. **GPS_DATA_POINTS:** Same as _DATA_POINTS_ but for gps graphs.

6. **DISPLAY_BLOCKS:** The Good Stuff:

   Here you will be able to modify all the display blocks and the filter criteria.

   <p align="center">
       <a>
           <img src="https://i.imgur.com/ng0XUuQ.png" alt="cover"/>
       </a>
   </p>

## States

States provide a quick, visual overview of your craft's performance. The state display, the leftmost widget in the panel (which can be disabled in the settings tab), initially shows "N/A" by default. widget will change color and text based on value from the telemetry packet (configurable in settings tab).

Example of a new state.

```json
"{VALUE}": ["{DISPLAY TEXT}","{DISPLAY COLOR}"]
```

for example if the VALUE is **0** it will show that text with the color, in the following example, when the value received is **0** it will show IDLE with a blue color, and when it changes to **1** it will show GO FOR LAUNCH with a green color, the packet value index is changed in the configuration tab.

```json
"STATES":
{
    "0": ["IDLE","7ed6df"],
    "1": ["GO FOR LAUNCH","44bd32"]
}
```

### Labels

Labels are added similarly, differing only in size and position; these guidelines suggest intended use but can be adapted as needed. Feel free to utilize them in any way that best suits your preferences and requirements.

**Big labels:** These are the largest, positioned below the state and countdown widgets. They convey very important data but are limited in number.

**Primary labels:** Smaller than big labels, they appear below the big. They aim to present important data in a straightforward manner, with a moderate quantity.

**Secondary labels:** Positioned at the bottom of the left panel, these labels are intended for non-critical data, offering a less prominent display.

There are some special cases, this will be done by changing the unit to one of the following:

_"format_seconds":_ Setting this as the unit will transform the value into a time format. For instance, if the received value is 10, the label will display "00:00:10". If the value is 300, it will show "00:05:00". IT ONLY WORKS WITH SECONDS, although code modification is an option.

```json
  "unit": "format_seconds",
```

_"sensor":_ When the received value is 0, it will display "OFF". If the value is 1, it will display "ON".

```json
  "unit": "sensor",
```

_"tlm_rate":_ This unit shows the time elapsed between the last and current packets in milliseconds.

```json
  "unit": "tlm_rate",
```

if you type any other value it will display it as its unit, m, s, kg etc...

**Example of a label (same format no matter the category):**

```json
{
  "name": "Example",
  "unit": "m",
  "value_index_in_chain": 1
}
```

Example for all categories:

```json
"LABELS": {
    "big": [
       {
            "name": "Example",
            "unit": "m",
            "value_index_in_chain": 1
        }
    ],
    "primary": [
        {
            "name": "Example",
            "unit": "m/s",
            "value_index_in_chain": 2
        }
    ],
    "secondary": [
        {
            "name": "Example",
            "unit": "C",
            "value_index_in_chain": 3
        }
    ]
}
```

> **coming Soon:** Min and Max ranges, this are not filters but range indicators, if the value is between the min and max value it will show green, otherwise red.

### Buttons

Buttons serve as a means to transmit pre-written commands via serial communication. They offer customization options for names, payload data, and colors.

Example of a button:

```json
"BUTTONS": [
    {
    "name": "BUTTON 1",
    "payload": 0,
    "color": "16a085"
    },
    {
    "name": "BUTTON 2",
    "payload": "payload_example",
    "color": "27ae60"
    }
]
```

### Graphs

Well just normal graphs they provide visual representation of the data over time, and there are four types:

1. **One Axis/Curve:**

```json
{
  "title": "One Axes",
  "unit": "m",
  "axes": 1,
  "color_1": "AE2012",
  "value_index_in_chain_1": 1,
  "row": 0,
  "col": 0
}
```

2. **Two Axis/Curves:**

```json
{
  "title": "Two Axes",
  "unit": "m/s",
  "axes": 2,
  "color_1": "0A9396",
  "color_2": "EE9B00",
  "name_1": "X",
  "name_2": "Y",
  "value_index_in_chain_1": 2,
  "value_index_in_chain_2": 3,
  "row": 0,
  "col": 1
}
```

3. **Three Axis/Curves:**

```json
{
  "title": "Three Axes",
  "unit": "\u00ba",
  "axes": 3,
  "name_1": "X",
  "name_2": "Y",
  "name_3": "Z",
  "color_1": "0A9396",
  "color_2": "E9D8A6",
  "color_3": "AE2012",
  "value_index_in_chain_1": 1,
  "value_index_in_chain_2": 2,
  "value_index_in_chain_3": 3,
  "row": 1,
  "col": 0
}
```

3. **GPS:**

```json
{
  "title": "GPS",
  "unit": "m",
  "axes": "gps",
  "1_x_axis_name": "Latitude",
  "2_x_axis_name": "Longitude",
  "value_index_in_chain_1": 1,
  "value_index_in_chain_2": 2,
  "color_1": "6a994e",
  "row": 1,
  "col": 1
}
```

### Filter Criteria

The criteria which the data will be filtered with, you can provide a minimum and maximum value to it, if the value is more than the maximum it will show the maximum value, and if it is below minimum it will show the minium value

```json
"{value_index_in_chain}": [ "{MIN_ALLOWED_VALUE}" , "{MAX_ALLOWED_VALUE}" ]
```

example of more values:

```json
"FILTER_CRITERIA": {
    "0": [0.0,20.0],
    "1": [-20.0,50.0],
    "2": [120.0,2350.0],
    "3": [-1990.0,-230.0]
}
```

## Data Record/Review

> Coming soon

## Cloud Integration

> Coming soon

## Notes

> Coming soon
