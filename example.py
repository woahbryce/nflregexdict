# Import modules 
import pandas as pd 
import numpy as np 
import regex as re

# Function to parse dataframe column
def parse(input_str):
    # Dictionary with regex keys will be used as the pattern by turning it into a list then to a string.
    nfl_teams_dict = {
        'N?[ew]*\s?E?[nglad]*\s?Pat[riots]*': 'New England Patriots',
        'N?[ew]*\s?Y?[ork]*\s?[Bufalo]*\s?Bills?\s?[Mafia]*': 'Buffalo Bills',
        '[Gren]*\s?[Bay]*\s?Packers?': 'Green Bay Packers',
        'N?[ew]*\s?Y?[ork]*\s?Jets?': 'New York Jets',
        'M?[inesota\.]*\s?Vik[ings]*': 'Minnesota Vikings',
        '[Philadey]*\s?Eagles?': 'Philadelphia Eagles'
    }

    _ = list(nfl_teams_dict.keys())
    dictkeys_pattern = re.compile('|'.join(list(_)), re.IGNORECASE)

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

def main():
    # Example dataframe with its possible entries, randomized
    example_list = ['New Englang Patriots', 'NE Patriots', 'Pats', 'NE pats', 'New York Buffalo Bills', 'Buffalo bills', 'NY biLls', 'Bills Mafia',
    'Green Bay Packers', 'gb packers', 'packers', 'New York Jets', 'jets', 'NY Jets', 'Minnesota Vikings', 'vikings', 'MN Viking',
    'Philadelphia Eagles', 'Eagles', 'Philly eagles']
    df = pd.DataFrame(np.arange(10000), columns=['team_entry']).applymap(lambda x: np.random.choice(example_list))

    df['team_corrected'] = df.team_entry.apply(parse)
    '''
    print(df.head())
                 team_entry        team_corrected
    0                  Pats  New England Patriots
    1               packers     Green Bay Packers
    2  New Englang Patriots  New England Patriots
    3               MN Viking   Minnesota Vikings
    4           Bills Mafia         Buffalo Bills
    '''

if __name__ == '__main__':
    main()