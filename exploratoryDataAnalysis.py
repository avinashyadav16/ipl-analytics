import plotly
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.offline as pyo
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def latest_teams(df, cols):

    temp = df.copy()
    teams = [
        'Royal Challengers Bengaluru',
        'Kings XI Punjab',
        'Sunrisers Hyderabad',
        'Delhi Capitals',
        'Gujarat Titans',
        'Mumbai Indians',
        'Kolkata Knight Riders',
        'Lucknow Super Giants',
        'Rajasthan Royals',
        'Chennai Super Kings',
        'Gujarat Lions',
        'Pune Warriors',
        'Rising Pune Supergiant',
        'Rising Pune Supergiants',
        'Kochi Tuskers Kerala'
    ]

    for col in cols:
        temp[col] = temp[col].str.replace(
            'Deccan Chargers',
            'Sunrisers Hyderabad')

        temp[col] = temp[col].str.replace(
            'Delhi Daredevils',
            'Delhi Capitals')

        temp[col] = temp[col].str.replace(
            'Royal Challengers Bangalore',
            'Royal Challengers Bengaluru')

        temp[col] = temp[col].str.replace(
            'Punjab Kings',
            'Kings XI Punjab')

    for col in cols:
        temp = temp[(temp[col].isin(teams))]

    return temp


def app():
    st.markdown(''' 
    <h1 style='text-align:center;'> 🌟EXPLORATORY DATA ANALYSIS🌟</h1>
    ''', unsafe_allow_html=True)

    #################################################################
    ################## MATCHES DATASET LOADING ######################
    #################################################################
    with st.expander('👉 Matches Dataset: 2008 - 2024'):
        matches_df = pd.read_csv('matches_2008-2024.csv')
        matches_df.columns = matches_df.columns.str.strip()

        st.write(matches_df.head(5))

        if st.checkbox(label="View Code", key=0):
            st.code('''
                        matches_df = pd.read_csv('matches_2008-2024.csv')
                        matches_df.columns = matches_df.columns.str.strip()
                        
                        st.write(matches_df.head(5))
                    ''', language='python')

    #################################################################
    ################## DELEVERY DATASET LOADING #####################
    #################################################################
    with st.expander('👉 Deliveries Dataset: 2008 - 2024'):
        deliveries_df = pd.read_csv('deliveries_2008-2024.csv')
        deliveries_df.columns = deliveries_df.columns.str.strip()

        st.write(deliveries_df.head(5))

        if st.checkbox(label="View Code", key=1):
            st.code('''
                        matches_df = pd.read_csv('matches_2008-2024.csv')
                        deliveries_df.columns = deliveries_df.columns.str.strip()
                        
                        st.write(matches_df.head(5))
                    ''', language='python')

    matches_team = latest_teams(
        matches_df, ['team1', 'team2', 'toss_winner', 'winner'])

    #################################################################
    ################## MATCHES PER SEASON ###########################
    #################################################################
    with st.expander("👉 Matches Per Season"):
        season_counts = matches_df['season'].value_counts().sort_index()

        trace = go.Bar(x=season_counts.index,
                       y=season_counts.values,
                       marker={'color': '#636efa'})

        layout = go.Layout(title="Matches Per Season",
                           xaxis={'title': 'Season'},
                           yaxis={'title': 'Number of Matches Played'})

        fig = go.Figure(data=[trace],
                        layout=layout)

        st.plotly_chart(fig,
                        transparent=True,
                        use_container_width=True)

        if st.checkbox(label="View Code", key=2):
            st.code('''
                        season_counts = matches_df['season'].value_counts().sort_index()
                        
                        trace = go.Bar(x=season_counts.index,
                                       y=season_counts.values,
                                       marker={'color': '#636efa'})
                        
                        layout = go.Layout(title="Matches Per Season",
                                        xaxis={'title': 'Season'},
                                        yaxis={'title': 'Number of Matches Played'})
                        
                        fig = go.Figure(data=[trace], 
                                        layout=layout)
                        
                        st.plotly_chart(fig, 
                                        transparent=True, 
                                        use_container_width=True)
                    ''', language='python')

    ####################################################################
    ########## Most Man of The Match Award Received By Players #########
    ###################################################################
    with st.expander("👉 Most POTM Awards"):
        top_20 = matches_df['player_of_match'].value_counts(
        ).iloc[:20].sort_values()

        fig = px.bar(y=top_20.index,
                     x=top_20.values,
                     labels={
                         'y': 'Player',
                         'x': 'POTM Awards'
                     })

        st.plotly_chart(fig,
                        transparent=True,
                        use_container_width=True)

        if st.checkbox(label="View Code", key=3):
            st.code('''
                        top_20 = matches_df['player_of_match'].value_counts().iloc[:20].sort_values()
                        fig = px.bar(y=top_20.index,x=top_20.values,
                        labels={
                            'y':'Player',
                            'x':'POTM Awards'
                        })
                        st.plotly_chart(fig,
                                        transparent=True,
                                        use_container_width=True)
                    ''', language='python')


##########################################################################
################ Venues With Most Matches ################################
##########################################################################
    with st.expander("👉 Top 20 Venues With Most Matches"):

        top_20 = matches_df['venue'].value_counts().iloc[:20]

        fig = px.bar(x=top_20.index,
                     y=top_20.values,
                     labels={
                         'x': 'Venue',
                         'y': 'Matches Count'
                     })

        st.plotly_chart(fig, transparent=True, use_container_width=True)

        if st.checkbox(label="View Code", key=4):
            st.code(''' 
                        top_20 = matches_df['venue'].value_counts().iloc[:20]
                        
                        fig = px.bar(x=top_20.index,
                                     y=top_20.values,
                                     labels={
                                         'x':'Venue',
                                         'y':'Matches Count'
                                     })
                        
                        st.plotly_chart(fig, 
                                        transparent=True,
                                        use_container_width=True)
                    ''', language='python')


##########################################################################
########### Team With Most Toss Wins ################
###########################################################################

    with st.expander('👉 Team With Most Match Wins'):
        top_20 = matches_df['winner'].value_counts().iloc[:20].sort_values()

        fig = px.bar(y=top_20.index, x=top_20.values,
                     labels={
                         'y': 'Count',
                         'x': 'Team'
                     })

        st.plotly_chart(fig,
                        transparent=True,
                        use_container_width=True)

        if st.checkbox(label="View Code", key=5):
            st.code(''' 
                        top_20 = matches_df['winner'].value_counts().iloc[:20].sort_values()
                        fig = px.bar(y=top_20.index,x=top_20.values,
                        labels={
                            'y':'Team',
                            'x':'Count'
                        })
                        st.plotly_chart(fig,
                                        transparent=True,
                                        use_container_width=True)
            ''', language='python')

##################################################################
#################### Team With Most Toss Wins ####################
#################################################################
    with st.expander('👉 Team With Most Toss Wins'):
        temp = matches_team['toss_winner'].value_counts()

        fig = px.bar(x=temp.index,
                     y=temp.values,
                     title='Toss Winners')

        st.plotly_chart(fig,
                        transparent=True,
                        use_container_width=True)

        if st.checkbox(label="View Code", key=6):
            st.code(''' 
                temp = matches_team['toss_winner'].value_counts()
                fig = px.bar(x=temp.index,
                            y=temp.values,
                            title='Toss Winners')
                
                st.plotly_chart(fig,
                                transparent=True,
                                use_container_width=True)
        ''', language='python')

#####################################################################
#### Chances of A Team Wiining Match if They Win The Toss ###########
#####################################################################
    with st.expander('👉 Probability of a Team Winning the Match After Winning the Toss'):
        fig = plt.figure(figsize=(20, 5))

        db = round(
            (
                matches_team[matches_team['toss_winner'] == matches_team['winner']
                             ]['winner'].value_counts() / matches_team['toss_winner'].value_counts()
            ) * 100).sort_values(ascending=False)

        explode = [0.1] + [0] * (len(db) - 1)

        plt.rcParams.update({'text.color': "white",
                            'axes.labelcolor': "black"})

        db.plot(kind='pie',
                autopct='%1.1f%%',
                explode=explode,
                shadow=True,
                startangle=90)

        plt.ylabel('')

        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(fig,
                      transparent=True)

        with col2:
            st.write('Overall Record Based On Team: ')

            dt = round(
                (
                    matches_team[matches_team['toss_winner'] == matches_team['winner']
                                 ]['winner'].value_counts() / matches_team['toss_winner'].value_counts()
                )*100).sort_values(ascending=False)

            st.write(dt)


#####################################################################
################### Team Wins Toss and Matches #######################
#####################################################################

    with st.expander('👉 Teams Winning Toss and Matches Both Since 2008'):
        fig = plt.figure(figsize=(10, 6))

        color = ['white',
                 'yellow',
                 'purple',
                 'red',
                 'green',
                 'magenta',
                 'cyan']

        winners = matches_team[matches_team['toss_winner'] == matches_team['winner']
                               ]['winner'].value_counts()

        plt.rcParams.update({'text.color': "white",
                             'axes.labelcolor': "white",
                             'xtick.color': 'white',
                             'ytick.color': 'white'})

        winners.plot(kind='bar',
                     color=color)

        font = {"size": 20}
        plt.xticks(fontsize=18)

        plt.title("Teams Winning Both Toss and Matches Since 2008",
                  fontdict=font)

        plt.xlabel("Team",
                   fontdict=font)

        plt.ylabel("Matches Won",
                   fontdict=font)

        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(fig,
                      transparent=True)

        with col2:
            st.dataframe(winners,
                         width=500,
                         height=650)


############################################################################
############ Player With Most Runs #########################################
###########################################################################
    with st.expander('👉 Top 20 Players With Most Runs'):
        fig = plt.figure(figsize=(10, 6))

        top_20_run_scorer = deliveries_df.groupby(
            'batter')['batsman_runs'].sum().sort_values(ascending=False)[:20]

        plt.rcParams.update({'text.color': "white",
                             'axes.labelcolor': "white",
                             'xtick.color': 'white',
                             'ytick.color': 'white'})

        plt.barh(top_20_run_scorer.index[::-1],
                 top_20_run_scorer.values[::-1],
                 color=color)

        font = {"size": 20}
        plt.xticks(fontsize=25)

        plt.title("Top 20 Players With Most Runs",
                  fontdict=font)

        plt.xlabel("Runs",
                   fontdict=font)

        plt.ylabel("Player",
                   fontdict=font)

        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(fig,
                      transparent=True)

        with col2:
            st.dataframe(top_20_run_scorer,
                         width=500,
                         height=250)


#############################################################################
############### MOST EXPENSIVE BOWLER #######################################
#############################################################################
    with st.expander("👉 Most Expensive Bowler"):
        st.write("> Overall Most Expensive Bowler:")

        col1, col2 = st.columns(2)

        with col1:
            fig = plt.figure(figsize=(10, 6))
            overall = deliveries_df.groupby('bowler')['total_runs'].agg('sum').reset_index().sort_values('total_runs',
                                                                                                         ascending=False).head(30)
            ax = sns.barplot(x='bowler',
                             y='total_runs',
                             data=overall[:10])

            plt.xticks(rotation='vertical',
                       fontsize=10)

            ax.bar_label(ax.containers[0])

            plt.title('Overall Most Expensive Bowler')

            st.pyplot(fig,
                      transparent=True)

        with col2:
            st.dataframe(overall,
                         400,
                         height=400)

        st.write('> Most Expensive Bowler in 1st Over:')
        col3, col4 = st.columns(2)

        with col3:
            fig = plt.figure(figsize=(10, 6))

            first_over = deliveries_df[deliveries_df['over'] == 1]

            group = first_over.groupby('bowler')['total_runs'].agg('sum').reset_index().sort_values('total_runs',
                                                                                                    ascending=False).head(30)

            ax = sns.barplot(x='bowler',
                             y='total_runs',
                             data=group[:10])

            plt.xticks(rotation='vertical',
                       fontsize=10)

            ax.bar_label(ax.containers[0])

            plt.title('Most Expensive Bowler In 1st Over')

            st.pyplot(fig,
                      transparent=True)

        with col4:
            st.dataframe(group,
                         400,
                         height=400)

        st.write('> Over Most Expensive Bowler in 20th Over:')
        col5, col6 = st.columns(2)
        with col5:
            fig = plt.figure(figsize=(10, 6))

            twenty_over = deliveries_df[deliveries_df['over'] == 19]

            group = twenty_over.groupby('bowler')['total_runs'].agg('sum').reset_index().sort_values('total_runs',
                                                                                                     ascending=False).head(30)

            ax = sns.barplot(x='bowler',
                             y='total_runs',
                             data=group[:10])

            plt.xticks(rotation='vertical',
                       fontsize=10)

            ax.bar_label(ax.containers[0])

            plt.title('Most Expensive Bowler In 20th Over')

            st.pyplot(fig,
                      transparent=True)

        with col6:
            st.dataframe(group,
                         400,
                         height=400)

    deliveries_latest = deliveries_df.copy()

    deliveries_latest = latest_teams(deliveries_latest,
                                     ['batting_team', 'bowling_team'])

#######################################################################
############################# Overwise Runs for Each Team #############
#######################################################################
    # with st.expander('👉 Average Runs per Over for Each Team (2008 - 2024)'):
    #     corr = deliveries_latest.pivot_table(
    #         values='total_runs', index='batting_team', columns='over') * 6

    #     fig = px.imshow(corr, color_continuous_scale="ylgn", labels=dict(x="Over", y="Team", color="Runs"),
    #                     x=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
    #                         "12", "13", "14", "15", "16", "17", "18", "19", "20"],
    #                     title='Overwise Average Runs For Each Team')

    #     st.plotly_chart(fig, transparent=True, use_container_width=True)

    with st.expander('👉 Overwise Average Runs For Each Team Since 2008'):
        corr = deliveries_df.pivot_table(values='total_runs',
                                         index='batting_team',
                                         columns='over',
                                         aggfunc='mean').fillna(0) * 6

        for over in range(0, 20):
            if over not in corr.columns:
                corr[over] = 0

        corr = corr[sorted(corr.columns)]

        fig = px.imshow(corr,
                        color_continuous_scale="Viridis",
                        labels=dict(x="Over",
                                    y="Team",
                                    color="Runs"),

                        x=[str(i) for i in range(0, 20)],

                        title='Overwise Average Runs For Each Team Since 2008')

        st.plotly_chart(fig,
                        transparent=True,
                        use_container_width=True)


########################################################################
############### Toss Decision Based On Top Venues ######################
########################################################################

    with st.expander('👉  Toss Decision Based On Top Venues'):
        top_venues = matches_df['venue'].value_counts()[:15].index.to_list()

        top_20_venues_matches = matches_df[matches_df['venue'].isin(
            top_venues)]
        top_20_venues_matches['venue'] = top_20_venues_matches['venue'] + \
            ", "+top_20_venues_matches['city']
        top_20 = top_20_venues_matches.groupby(['venue', 'toss_decision']).count(
        )['toss_winner'].reset_index().sort_values('venue', ascending=False)

        fig = plt.figure(figsize=(20, 5))
        plt.rcParams.update({'text.color': "white", 'axes.labelcolor': "white",
                            'xtick.color': 'white', 'ytick.color': 'white'})

        ax = sns.barplot(y='toss_winner', x='venue',
                         hue='toss_decision', data=top_20)
        ax.bar_label(ax.containers[0])
        ax.bar_label(ax.containers[1])
        leg = plt.legend()
        for text in leg.get_texts():
            text.set_color("black")
        plt.xticks(rotation='vertical', fontsize=16)
        plt.title('Toss Winner Choice Based On Venue', fontsize=16)

        st.pyplot(fig, transparent=True)
        top_20 = top_20.rename(columns={'toss_winner': 'Count'})
        st.dataframe(top_20, width=700, height=300)


#############################################################################
################# Average Runs By Different Teams In Last Over ##############
#############################################################################

    with st.expander('👉  Average Runs Scored By Different Teams In Last Over'):

        fig = plt.figure(figsize=(10, 6))
        twenty = deliveries_latest[deliveries_latest['over'] == 20]
        twenty_over_scores = round(twenty.groupby('batting_team')[
                                   'total_runs'].mean()*6).round(2).sort_values(ascending=False)
        ax = sns.barplot(twenty_over_scores.values, twenty_over_scores.index)
        ax.bar_label(ax.containers[0])
        plt.title('Average Runs By Different Teams In Last Over')
        plt.xlabel('Score')
        plt.ylabel('Playing Team')
        st.pyplot(fig, transparent=True)


##############################################################################
##### Total Runs Score By Different Teams In Last Over Till Start of IPL #####
##############################################################################
    with st.expander('👉  Total RUns By Different Teams In Last Over Since Start of IPL'):
        fig = plt.figure(figsize=(12, 8))
        twenty = deliveries_latest[deliveries_latest['over'] == 20]
        twenty_over_scores = (twenty.groupby('batting_team')[
                              'total_runs'].sum()).sort_values(ascending=False)
        # plt.barh(twenty_over_scores.index,twenty_over_scores.values);
        ax = sns.barplot(twenty_over_scores.values, twenty_over_scores.index)
        ax.bar_label(ax.containers[0])
        plt.title('Total Runs By Different Teams In Last Over')
        plt.xlabel('Score')
        plt.ylabel('Playing Team')
        st.pyplot(fig, transparent=True)

    # COMBINING BOTH DATASETS (Latest)
    combine_df = matches_team.merge(
        deliveries_latest, left_on='id', right_on='match_id', how='left')

###############################################################################
##### Total Runs By Different Teams In Last Over In First Edition (2008) ######
###############################################################################

    with st.expander('👉  Runs By Different Teams In Last Over In First Edition (2008)'):

        st.write('> Total Runs')

        fig = plt.figure(figsize=(12, 8))
        twenty = combine_df[(combine_df['over'] == 20) &
                            (combine_df['Season'] == 'IPL-2008')]
        twenty_over_scores = (twenty.groupby('batting_team')[
                              'total_runs'].sum()).sort_values(ascending=False)
        # plt.barh(twenty_over_scores.index,twenty_over_scores.values);
        ax = sns.barplot(twenty_over_scores.values, twenty_over_scores.index)
        ax.bar_label(ax.containers[0])
        plt.title('Total Runs By Different Teams In Last Over')
        plt.xlabel('Score')
        plt.ylabel('Playing Team')
        st.pyplot(fig, transparent=True)


###############################################################################
##### Average Runs By Different Teams In Last Over In First Edition (2008) ####
###############################################################################

        st.write('> Average Runs')

        fig = plt.figure(figsize=(12, 8))
        twenty = combine_df[(combine_df['over'] == 20) &
                            (combine_df['Season'] == 'IPL-2008')]
        twenty_over_scores = (twenty.groupby('batting_team')[
                              'total_runs'].sum()).sort_values(ascending=False)
        # plt.barh(twenty_over_scores.index,twenty_over_scores.values);
        ax = sns.barplot(twenty_over_scores.values, twenty_over_scores.index)
        ax.bar_label(ax.containers[0])
        plt.title('Average Runs By Different Teams In Last Over')
        plt.xlabel('Score')
        plt.ylabel('Playing Team')
        st.pyplot(fig, transparent=True)


##############################################################################
### Total Runs Scored in Each Season #########################
##############################################################################

    with st.expander('👉  Total Runs Scored in Each Season'):
        # fig = plt.figure(figsize=(10,8))
        plt.rcParams.update({'text.color': "white", 'axes.labelcolor': "white",
                            'xtick.color': 'white', 'ytick.color': 'white'})

        combine_df['Season'] = combine_df['Season'].apply(
            lambda x: x.split('-')[-1])
        season = combine_df.groupby('Season')['total_runs'].sum().reset_index()
        temp4 = season.set_index('Season')

        # ax = sns.relplot(x=temp4.index,y=temp4['total_runs'],kind='line',height=5, aspect=2)
        # plt.title("Total Runs Scored In Each Season",fontsize=16)
        # plt.xticks(fontsize=16)
        # plt.xlabel("IPL Season",fontdict={'size':18})
        # plt.ylabel("Total Runs",fontdict={'size':18})
        # col00, col01 = st.columns(2)
        # with col00:
        #     st.pyplot(ax,transparent=True)
        # with col01:
        #     st.dataframe(temp4,width=500,height=300)

        fig = px.line(data_frame=temp4, x=temp4.index, y='total_runs',
                      title='Total Runs Scored In Each Season')
        st.plotly_chart(fig, transparent=True, use_container_width=True)


#####################################################################
############ Count of Matches By Different Umpires ##################
#####################################################################

    with st.expander('👉  Count of Matches By Different Umpires'):
        fig = plt.figure(figsize=(15, 8))
        umpires = pd.concat(
            [matches_df['umpire1'], matches_df['umpire2']]).value_counts()
        top_10_umpires = umpires.nlargest(10)
        ax = sns.barplot(top_10_umpires.index, top_10_umpires.values)
        ax.bar_label(ax.containers[0])
        plt.title('Maches Played By Umpires')
        plt.xlabel('Umpire Name')
        plt.ylabel('Matches Played')
        st.pyplot(fig, transparent=True)


###########################################################################
############ Lucky Venue For Teams ########################################
###########################################################################

    with st.expander('👉  Lucky Venue For Teams'):
        teams = matches_team.team1.unique().tolist()
        matches_team['venue'] = matches_team['venue']+", "+matches_team['city']
        for team in teams:
            fig = plt.figure(figsize=(15, 8))
            team_name = team
            lucky_venues = matches_team[matches_team['winner'] ==
                                        team_name]['venue'].value_counts().nlargest(10)
            explode = (0.1, 0.1, 0, 0, 0, 0, 0, 0, 0, 0)
            colors = ['turquoise', 'lightblue',
                      'lightgreen', 'crimson', 'magenta', 'orange']
            plt.rcParams.update({'text.color': "white", 'axes.labelcolor': "white",
                                'xtick.color': 'white', 'ytick.color': 'white'})
            lucky_venues.plot(kind='pie', autopct='%1.1f%%', explode=explode,
                              shadow=True, startangle=20, textprops={'fontsize': 10}, colors=colors)
            plt.title(f'Win at different Venues for {team}')
            plt.ylabel('')
            st.pyplot(fig, transparent=True)


#####################################################################
#################### Teams with more than 200+ scores ###############
#####################################################################

    with st.expander('👉  Teams With More Than 200+ Scores'):
        fig = plt.figure(figsize=(10, 7))
        plt.rcParams.update({'text.color': "white", 'axes.labelcolor': "white",
                            'xtick.color': 'white', 'ytick.color': 'white'})
        runs = deliveries_latest.groupby(['match_id', 'inning', 'batting_team', 'bowling_team'])[
            'total_runs'].sum().reset_index()
        runs_over_200_df = runs[runs['total_runs'] > 200]
        runs_over_200 = runs_over_200_df['batting_team'].value_counts()

        ax = sns.barplot(runs_over_200.index, runs_over_200.values)
        ax.bar_label(ax.containers[0])
        plt.xticks(rotation='vertical')
        plt.title('Most 200+ Runs Scored By Teams')
        plt.xlabel('Teams')
        plt.ylabel('Runs')
        st.pyplot(fig, transparent=True)
