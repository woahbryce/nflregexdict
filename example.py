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

    dictkeys_pattern = re.compile('|'.join(nfl_teams_dict), re.IGNORECASE)

    #If string is found in the pattern, match to key in the dictionary and return corresponding value.
    team_found = re.findall(dictkeys_pattern, input_str)
    if team_found:
        team = []
        for i in team_found: 
            for k, v in nfl_teams_dict.items():
                if re.match(k, i, re.IGNORECASE):
                    team.append(v)
        return team
    else:
        team = None
        return team

def main():
    # Example dataframe with its possible entries, randomized
    example_list = ['New Englang Patriots', 'NE Patriots', 'Pats', 'NE pats', 'New York Buffalo Bills', 'Buffalo bills', 'NY biLls', 'Bills Mafia',
    'Green Bay Packers', 'gb packers', 'packers', 'New York Jets', 'jets', 'NY Jets', 'Minnesota Vikings', 'vikings', 'MN Viking',
    'Philadelphia Eagles', 'Eagles', 'Philly eagles', 'The New England Patriots lost to Bills Mafia!!']
    df = pd.DataFrame(np.arange(10000), columns=['team_entry']).applymap(lambda x: np.random.choice(example_list))

    df['teams'] = df.team_entry.apply(parse)
    '''
    print(df.head())
                                           team_entry                                  teams
    0                                         NE pats                 [New England Patriots]
    1  The New England Patriots lost to Bills Mafia!!  [New England Patriots, Buffalo Bills]
    2                             Philadelphia Eagles                  [Philadelphia Eagles]
    3                                          Eagles                  [Philadelphia Eagles]
    4                                       MN Viking                    [Minnesota Vikings]
    '''

if __name__ == '__main__':
    main()
