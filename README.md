# nflregexdict
Demonstration of using a dictionary as a regex map with nfl teams.

# Medium Pairing and Discussion
https://medium.com/@_bryceli/using-dictionaries-as-regex-in-python-de9033bb3e0f?sk=adf7298ec3759ccbc900298ed1072cf6

# Notes
This function is best paired with a separate file containing the dictionary for more modular and neat code. 

The code in example.py matches multiple groups and returns a list. If you are only looking for one value (e.g., entry form for current
residing state), the following is more succint and uses one less for-loop, re.findall vs re.search, and returns a string rather than a
list of values. 

    dictkeys_pattern = re.compile('|'.join(nfl_teams_dict), re.IGNORECASE)

    #If string is found in the pattern, match to key in the dictionary and return corresponding value.
    team_found = re.search(dictkeys_pattern, input_str)
    if team_found:
        for k, v in nfl_teams_dict.items():
            if re.match(k, team_found.group(), re.IGNORECASE):
                team = v
                return team
    else:
        team = None
        return team
   
# Dependencies
  - Python 3.7.4
  - regex
  - Pandas 0.25.1
  - Numpy 1.17.4
