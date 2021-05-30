## Guide for a regolith GUI

#### Overview
- This GUI is written with the help of PySimpleGUI (a wrapper for Tk inter) 
- The GUI uses the `SCHEMAS` class objects in `schemas.py` module for building the user interface. 
- A schema object should contain (recommendation comment : couple to schema.org standards):
    - description
    - type 
    - anyof_type (if no 'type')
    - required (opt. for 'dict')
    - schema (if type is 'dict')
- Filtration criteria need unique setup for each catalog

#### Usage
- setup path to local database under `config/dbs_path.yml` and change the value for `dbs_path` to the database.

- window #1
    1. Set path to database
        - Using local: set the path to `/rg-db-group/db`. 
        - for permanent: setup path to local database under `config/dbs_path.yml`
          and change the value for `dbs_path` to the database
    1. Select a desired catalog. 
    1. Export --> enter window #2 
    
- window #2
    1. (opt.) Filter (currently for Projectum only)
    1. Select entry _id
    1. view or edit
    1. Update
    1. Save  --> Update + dump to local file

-  Explore (`RightArrow`) window
    - shows nested dictionary or a list of dictionaries.
    - If list of dict:
       1. select an index in the list
       1. view/ edit
       1. `add` or `delete` items
       1. `Update` or `Finish` (=Update and close)
               
 - Features for window #2 and Explore window
    - To edit a list, press the `pencil icon`
    - To find a date, press the `calendar icon`
    - To enter a nested dict or a list of dict, press the `RightArrow icon` next to 'explore'
   
    