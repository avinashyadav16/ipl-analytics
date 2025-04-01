import pandas as pd


# Updating the team names
def latest_teams(df, cols):
    # mapping old to latest
    team_name_map = {
        'Deccan Chargers': 'Sunrisers Hyderabad',
        'Delhi Daredevils': 'Delhi Capitals',
        'Royal Challengers Bangalore': 'Royal Challengers Bengaluru',
        'Punjab Kings': 'Kings XI Punjab',
        'Rising Pune Supergiants': 'Rising Pune Supergiant'
    }

    # Replace old team names with the latest names
    for col in cols:
        if col not in df.columns:
            raise KeyError(f"Column '{col}' not found in DataFrame")
        df[col] = df[col].replace(team_name_map)

    return df


# Updating the venue names
def unique_stadium(matches_df):
    venue_map = {
        'Arun Jaitley Stadium, Delhi': 'Arun Jaitley Stadium',
        'Brabourne Stadium, Mumbai': 'Brabourne Stadium',
        'Dr DY Patil Sports Academy, Mumbai': 'Dr DY Patil Sports Academy',
        'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam': 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
        'Eden Gardens, Kolkata': 'Eden Gardens',
        'Himachal Pradesh Cricket Association Stadium, Dharamsala': 'Himachal Pradesh Cricket Association Stadium',
        'M.Chinnaswamy Stadium': 'M Chinnaswamy Stadium',
        'M Chinnaswamy Stadium, Bengaluru': 'M Chinnaswamy Stadium',
        'M Chinnaswamy Stadium, Bengalore': 'M Chinnaswamy Stadium',
        'MA Chidambaram Stadium, Chepauk': 'MA Chidambaram Stadium',
        'MA Chidambaram Stadium, Chepauk, Chennai': 'MA Chidambaram Stadium',
        'Maharashtra Cricket Association Stadium, Pune': 'Maharashtra Cricket Association Stadium',
        'Punjab Cricket Association Stadium, Mohali': 'Punjab Cricket Association IS Bindra Stadium',
        'Punjab Cricket Association IS Bindra Stadium': 'Punjab Cricket Association IS Bindra Stadium',
        'Punjab Cricket Association IS Bindra Stadium, Mohali': 'Punjab Cricket Association IS Bindra Stadium',
        'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh': 'Punjab Cricket Association IS Bindra Stadium',
        'Rajiv Gandhi International Stadium, Uppal': 'Rajiv Gandhi International Stadium',
        'Rajiv Gandhi International Stadium, Uppal, Hyderabad': 'Rajiv Gandhi International Stadium',
        'Sawai Mansingh Stadium, Jaipur': 'Sawai Mansingh Stadium',
        'Wankhede Stadium, Mumbai': 'Wankhede Stadium'
    }
    matches_df['venue'] = matches_df['venue'].replace(venue_map)


def trimSpaceInValues(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip()
    return df


# Loading and cleaning the matches data
matches_df = pd.read_csv('matches_2008-2024.csv')
matches_df.columns = matches_df.columns.str.strip()

# Loading and cleaning the deliveries data
deliveries_df = pd.read_csv('deliveries_2008-2024.csv')
deliveries_df.columns = deliveries_df.columns.str.strip()


matches_df = trimSpaceInValues(matches_df)
deliveries_df = trimSpaceInValues(deliveries_df)

# Replacing the empty values in the 'extra_types' with the 'None' When it is normal deliveries:
deliveries_df.loc[
    deliveries_df['extras_type'].str.strip() == '', 'extras_type'
] = 'None'

# Apply the cleaning functions to the matches data
new_matchesDF = latest_teams(
    matches_df,
    ['team1', 'team2', 'toss_winner', 'winner']
)

unique_stadium(new_matchesDF)


# Apply the latest_teams function to deliveries data
new_deliveriesDF = latest_teams(
    deliveries_df,
    ['batting_team', 'bowling_team']
)
