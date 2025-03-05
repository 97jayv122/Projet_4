# Projet_4

## Overview

Projet_4 is a Python-based application designed to manage tournaments, players, and generate various reports.
The application follows an MVC (Model-View-Controller) structure, ensuring a clear separation between data management, user interface, and business logic.

## Features

- **Player Management:** Add, display, modify, and remove players.
- **Tournament Management:** Create and manage tournaments, assign players, and start rounds.
- **Reporting:** Generate reports for tournaments and players, including detailed match results and tournament information.
- **User Interface:** Interactive menus and table displays for easy navigation.


## Setup

1. **Clone the repository:**

   bash
   `git clone https://github.com/97jayv122/Projet_4.git`

   `cd Projet_4`

2. **Create a Virtual Environment:**

`python -m venv env`

3. **Activate the Virtual Environment:**
   
On Windows:
    
`env\Scripts\activate`

On macOS/Linux:

`source env/bin/activate`

4. **Install Dependencies:**

`pip install -r requirements.txt`

5. **Running the Application**
To start the application, run:

`python main.py`

Follow the on-screen menus to navigate between player management, tournament management, and reporting.

6. **Generate the Report:**

Run the following command from the project root:

bash
`flake8 --format=html --htmldir=flake8_report`

This command runs flake8 checks on your code and outputs an HTML report into the flake8_report directory.
Open the index.html file inside that folder with your browser to view the report.

## Authors

97jayv122
