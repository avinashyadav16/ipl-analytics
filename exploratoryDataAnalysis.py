import plotly
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.offline as pyo
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datasetPreprocessing import new_matchesDF, new_deliveriesDF


def app():
    st.markdown('''
    <h1 style='text-align:center;'> 🌟EXPLORATORY DATA ANALYSIS🌟</h1>
    ''', unsafe_allow_html=True)

    #################################################################
    ################## MATCHES DATASET LOADING ######################
    #################################################################
    with st.expander('👉 Matches Dataset: 2008 - 2024'):
        st.write(new_matchesDF.head(5))

        if st.checkbox(label="View Code", key=0):
            st.code('''
                        new_matchesDF = pd.read_csv('matches_2008-2024.csv')
                        
                        new_matchesDF.columns = new_matchesDF.columns.str.strip()

                        st.write(new_matchesDF.head(5))
                    ''', language='python')

    #################################################################
    ################## DELEVERY DATASET LOADING #####################
    #################################################################
    with st.expander('👉 Deliveries Dataset: 2008 - 2024'):
        st.write(new_deliveriesDF.head(5))

        if st.checkbox(label="View Code", key=1):
            st.code('''
                        new_deliveriesDF = pd.read_csv('deliveries_2008-2024.csv')
                        
                        new_deliveriesDF.columns = new_deliveriesDF.columns.str.strip()
                        
                        st.write(new_deliveriesDF.head(5))
                    ''', language='python')

    #################################################################
    ################## MATCHES PER SEASON ###########################
    #################################################################
    with st.expander("👉 Matches Per Season"):
        matches_per_season = new_matchesDF['season'].value_counts(
        ).sort_index()

        colors = px.colors.qualitative.Safe
        color_list = [colors[i % len(colors)]
                      for i in range(len(matches_per_season))]

        trace = go.Bar(
            x=matches_per_season.index,
            y=matches_per_season.values,
            marker={'color': color_list}
        )

        layout = go.Layout(
            title="Matches Per Season",
            xaxis={'title': 'Season'},
            yaxis={'title': 'Number of Matches Played'}
        )

        fig = go.Figure(data=[trace], layout=layout)

        st.plotly_chart(fig, transparent=True, use_container_width=True)

        if st.checkbox(label="View Code", key=2):
            st.code('''
                        matches_per_season = new_matchesDF['season'].value_counts().sort_index()

                        colors = px.colors.qualitative.Safe
                        
                        color_list = [colors[i % len(colors)]
                                      for i in range(len(matches_per_season))]
                        
                        trace = go.Bar(x = matches_per_season.index,
                                       y = matches_per_season.values,
                                        marker={'color': color_list})

                        layout = go.Layout(title = "Matches Per Season",
                                           xaxis = {'title': 'Season'},
                                           yaxis = {'title': 'Number of Matches Played'})

                        fig = go.Figure(data = [trace], layout = layout)

                        st.plotly_chart(fig,
                                        transparent = True,
                                        use_container_width = True)
                    ''', language='python')

    ####################################################################
    ########## Most Man of The Match Award Received By Players #########
    ###################################################################
    with st.expander("👉 Most POTM Awards"):
        top_20_POTM = new_matchesDF['player_of_match'].value_counts(
        ).iloc[:20].sort_values()

        fig = px.bar(y=top_20_POTM.index,
                     x=top_20_POTM.values,
                     labels={
                         'y': 'Player',
                         'x': 'POTM Awards'
                     },
                     color=top_20_POTM.index,
                     color_discrete_sequence=px.colors.qualitative.Safe)

        st.plotly_chart(fig,
                        transparent=True,
                        use_container_width=True)

        if st.checkbox(label="View Code", key=3):
            st.code('''
                        top_20_POTM = new_matchesDF['player_of_match'].value_counts().iloc[:20].sort_values()
                        
                        fig = px.bar(y = top_20_POTM.index,x=top_20_POTM.values,
                                     labels = {
                                         'y':'Player',
                                         'x':'POTM Awards'
                                     },
                                     color=top_20_POTM.index,
                                     color_discrete_sequence=px.colors.qualitative.Safe)
                        
                        st.plotly_chart(fig,
                                        transparent = True,
                                        use_container_width = True)
                    ''', language='python')

    ##########################################################################
    ################ Venues With Most Matches ################################
    ##########################################################################
    with st.expander("👉 Top 20 Venues With Most Matches"):
        top_20_venue = new_matchesDF['venue'].value_counts().iloc[:20]

        fig = px.bar(x=top_20_venue.index,
                     y=top_20_venue.values,
                     labels={
                         'x': 'Venue',
                         'y': 'Total Matches Played'
                     },
                     color=top_20_venue.index,
                     color_discrete_sequence=px.colors.qualitative.Safe)

        st.plotly_chart(fig,
                        transparent=True,
                        use_container_width=True)

        if st.checkbox(label="View Code", key=4):
            st.code('''
                        top_20_venue = new_matchesDF['venue'].value_counts().iloc[:20]

                        fig = px.bar(x=top_20_venue.index,
                                     y=top_20_venue.values,
                                     labels={
                                         'x':'Venue',
                                         'y':'Total Matches Played'
                                     },
                                     color=top_20_venue.index,
                                     color_discrete_sequence=px.colors.qualitative.Safe)

                        st.plotly_chart(fig,
                                        transparent=True,
                                        use_container_width=True)
                    ''', language='python')

    ###########################################################################
    ###################### Team With Most Match Wins ##########################
    ###########################################################################
    with st.expander('👉 Team With Most Match Wins'):
        teams_total_toss_win = new_matchesDF['winner'].value_counts(
        ).iloc[:].sort_values()

        fig = px.bar(
            y=teams_total_toss_win.index,
            x=teams_total_toss_win.values,
            labels={
                'y': 'Total Matches Won',
                'x': 'Team'
            },
            color=teams_total_toss_win.index,
            color_discrete_sequence=px.colors.qualitative.Safe
        )

        st.plotly_chart(fig,
                        transparent=True,
                        use_container_width=True)

        if st.checkbox(label="View Code", key=5):
            st.code('''
                        teams_total_toss_win = new_matchesDF['winner'].value_counts().iloc[:20].sort_values()
                        
                        fig = px.bar(y=teams_total_toss_win.index,
                                     x=teams_total_toss_win.values,
                                     labels={
                                         'y':'Team',
                                         'x':'Total Wins'
                                     },
                                     color=teams_total_toss_win.index,
                                     color_discrete_sequence=px.colors.qualitative.Safe
                        
                        st.plotly_chart(fig,
                                        transparent=True,
                                        use_container_width=True)
            ''', language='python')

    ##################################################################
    #################### Team With Most Toss Wins ####################
    ##################################################################
    with st.expander('👉 Team With Most Toss Wins'):
        teams_toss_win_count = new_matchesDF['toss_winner'].value_counts()

        fig = px.bar(x=teams_toss_win_count.index,
                     y=teams_toss_win_count.values,
                     title='Toss Winners',
                     labels={
                         'y': 'Total Tosses Won',
                         'x': 'Team'
                     },
                     color=teams_toss_win_count.index,
                     color_discrete_sequence=px.colors.qualitative.Safe)

        st.plotly_chart(fig,
                        transparent=True,
                        use_container_width=True)

        if st.checkbox(label="View Code", key=6):
            st.code('''
                teams_toss_win_count = matches_team['toss_winner'].value_counts()
                
                fig = px.bar(x=teams_toss_win_count.index,
                             y=teams_toss_win_count.values,
                             title='Toss Winners'
                             color=teams_toss_win_count.index,
                             color_discrete_sequence=px.colors.qualitative.Safe)

                st.plotly_chart(fig,
                                transparent=True,
                                use_container_width=True)
        ''', language='python')

    #####################################################################
    ########### Win Percentage of Team after Winning The Toss  ##########
    #####################################################################
    with st.expander('👉 Win Percentage of Team after Winning The Toss'):
        fig = plt.figure(figsize=(15, 8))

        win_percentage_after_toss = round(
            (
                new_matchesDF[new_matchesDF['toss_winner']
                              == new_matchesDF['winner']]
                ['winner'].value_counts() / new_matchesDF['toss_winner'].value_counts()
            ) * 100
        ).sort_values(ascending=False)

        explode = [0.1] + [0] * (len(win_percentage_after_toss) - 1)

        plt.rcParams.update({'text.color': "white",
                             'axes.labelcolor': "black"})

        win_percentage_after_toss.plot(kind='pie',
                                       autopct='%1.1f%%',
                                       explode=explode,
                                       shadow=True,
                                       startangle=90)

        plt.ylabel('')
        plt.title('Win Percentage of Team after Winning The Toss')

        col1, col2 = st.columns([3, 2])

        with col1:
            st.pyplot(fig,
                      transparent=True)

        with col2:
            st.write('### Overall Record:')
            st.dataframe(win_percentage_after_toss, width=500, height=575)

        if st.checkbox(label="View Code", key=7):
            st.code('''
                win_percentage_after_toss = round(
                    (
                        new_matchesDF[new_matchesDF['toss_winner']
                                    == new_matchesDF['winner']]
                        ['winner'].value_counts() / new_matchesDF['toss_winner'].value_counts()
                    ) * 100
                ).sort_values(ascending=False)

                explode = [0.1] + [0] * (len(win_percentage_after_toss) - 1)

                win_percentage_after_toss.plot(kind='pie',
                                            autopct='%1.1f%%',
                                            explode=explode,
                                            shadow=True,
                                            startangle=90)
                                            
                plt.rcParams.update({'text.color': "white",
                                    'axes.labelcolor': "black"})

                fig = plt.figure(figsize=(15, 8))
                
                plt.ylabel('')
                
                plt.title('Win Percentage of Team after Winning The Toss')

                st.pyplot(fig, transparent=True)
        ''', language='python')

    #####################################################################
    ############### Teams Winning Both Toss and Matches #################
    #####################################################################
    with st.expander('👉 Teams Winning Both Toss and Matches Since 2008'):
        toss_Match_winner = new_matchesDF[new_matchesDF['toss_winner'] == new_matchesDF['winner']
                                          ]['winner'].value_counts()

        plt.rcParams.update({'text.color': "white",
                             'axes.labelcolor': "white",
                             'xtick.color': 'white',
                             'ytick.color': 'white'})

        fig = plt.figure(figsize=(15, 8))

        color = ['white',
                 'yellow',
                 'purple',
                 'red',
                 'green',
                 'magenta',
                 'cyan']

        toss_Match_winner.plot(kind='bar',
                               color=color)

        font = {"size": 20}
        plt.xticks(fontsize=18)

        plt.xlabel("Teams",
                   fontdict=font)

        plt.ylabel("Total Matches Won",
                   fontdict=font)

        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(fig,
                      transparent=True)

        with col2:
            st.write('### Records:')
            st.dataframe(toss_Match_winner,
                         width=400,
                         height=570)

        if st.checkbox(label="View Code", key=8):
            st.code('''
                        toss_Match_winner = new_matchesDF[new_matchesDF['toss_winner'] == new_matchesDF['winner']
                                            ]['winner'].value_counts()

                        plt.rcParams.update({'text.color': "white",
                                            'axes.labelcolor': "white",
                                            'xtick.color': 'white',
                                            'ytick.color': 'white'})

                        fig = plt.figure(figsize=(10, 6))

                        color = ['white',
                                'yellow',
                                'purple',
                                'red',
                                'green',
                                'magenta',
                                'cyan']

                        toss_Match_winner.plot(kind='bar',
                                            color=color)

                        font = {"size": 20}
                        plt.xticks(fontsize=18)

                        plt.title("Teams Winning Both Toss and Matches Since 2008",
                                fontdict=font)

                        plt.xlabel("Team",
                                fontdict=font)

                        plt.ylabel("Matches Won",
                                fontdict=font)

                        st.pyplot(fig, transparent=True)
        ''', language='python')

    ############################################################################
    ################## Top 20 Players With Most Runs ###########################
    ############################################################################
    with st.expander('👉 Top 20 Players With Most Runs'):
        top_20_run_scorer = new_deliveriesDF.groupby(
            'batter')['batsman_runs'].sum().sort_values(ascending=False)[:20]

        top_20_run_scorer_df = top_20_run_scorer.reset_index()
        top_20_run_scorer_df.columns = ['Player', 'Runs']

        fig = px.bar(
            top_20_run_scorer_df,
            x='Runs',
            y='Player',
            labels={
                'Player': 'Player',
                'Runs': 'Total Runs'
            },
            color='Player',
            color_discrete_sequence=px.colors.qualitative.Safe
        )

        fig.update_layout(
            yaxis_title='Player',
            xaxis_title='Total Runs',
            yaxis=dict(categoryorder='total ascending')
        )

        st.plotly_chart(fig, transparent=True, use_container_width=True)

        if st.checkbox(label="View Code", key=9):
            st.code('''
                        top_20_run_scorer = new_deliveriesDF.groupby(
                                            'batter')['batsman_runs'].sum().sort_values(ascending=False)[:20]

                        top_20_run_scorer_df = top_20_run_scorer.reset_index()
                        top_20_run_scorer_df.columns = ['Player', 'Runs']

                        fig = px.bar(
                            top_20_run_scorer_df,
                            x='Runs',
                            y='Player',
                            labels={
                                'Player': 'Player',
                                'Runs': 'Total Runs'
                            },
                            color='Player',
                            color_discrete_sequence=px.colors.qualitative.Safe
                        )

                        fig.update_layout(
                            yaxis_title='Player',
                            xaxis_title='Total Runs',
                            yaxis=dict(categoryorder='total ascending')
                        )

                        st.plotly_chart(fig, transparent=True, use_container_width=True)

        ''', language='python')

    #############################################################################
    ###############           MOST EXPENSIVE BOWLERS              ###############
    #############################################################################

    def plot_bar(data, title, xlabel, ylabel, col_width=2, rows=1):
        fig = plt.figure(figsize=(10, 6))

        ax = sns.barplot(x='bowler',
                         y='total_runs',
                         data=data[:10],
                         palette='viridis',
                         hue=None,
                         legend=False)

        plt.xticks(rotation=90, fontsize=10)

        ax.bar_label(ax.containers[0])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        st.pyplot(fig, transparent=True)

    with st.expander("👉 Most Expensive Bowler"):
        st.write("> Overall Most Expensive Bowler:")
        col1, col2 = st.columns([3, 2])

        with col1:
            overall = new_deliveriesDF.groupby('bowler')['total_runs'].agg('sum').reset_index().sort_values('total_runs',
                                                                                                            ascending=False).head(30)
            plot_bar(overall,
                     'Overall Most Expensive Bowler',
                     'Bowler',
                     'Total Runs')

        with col2:
            st.dataframe(overall,
                         width=400,
                         height=400)

        st.write('> Most Expensive Bowler in 1st Over:')
        col3, col4 = st.columns([3, 2])

        with col3:
            first_over = new_deliveriesDF[new_deliveriesDF['over'] == 0]

            group = first_over.groupby('bowler')['total_runs'].agg('sum').reset_index().sort_values('total_runs',
                                                                                                    ascending=False).head(30)
            plot_bar(group,
                     'Most Expensive Bowler in 1st Over',
                     'Bowler',
                     'Total Runs')

        with col4:
            st.dataframe(group,
                         width=400,
                         height=400)

        st.write('> Most Expensive Bowler in 20th Over:')
        col5, col6 = st.columns([3, 2])

        with col5:
            twenty_over = new_deliveriesDF[new_deliveriesDF['over'] == 19]

            group = twenty_over.groupby('bowler')['total_runs'].agg('sum').reset_index().sort_values('total_runs',
                                                                                                     ascending=False).head(30)
            plot_bar(group,
                     'Most Expensive Bowler in 20th Over',
                     'Bowler',
                     'Total Runs')

        with col6:
            st.dataframe(group,
                         width=400,
                         height=400)

        if st.checkbox(label="View Code", key=10):
            st.code('''
                        overall = new_deliveriesDF.groupby('bowler')['total_runs'].agg('sum').reset_index().sort_values('total_runs', 
                                                                                                                                    ascending=False).head(30)

                        fig = plt.figure(figsize=(10, 6))

                        top_bowlers = overall.head(10)

                        ax = sns.barplot(x='bowler',
                                        y='total_runs',
                                        data=top_bowlers,
                                        palette='viridis')

                        plt.xticks(rotation=90, 
                                    fontsize=10)

                        ax.bar_label(ax.containers[0])

                        plt.title('Overall Most Expensive Bowler')
                        plt.xlabel('Bowler')
                        plt.ylabel('Total Runs')

                        st.pyplot(fig, transparent=True)
        ''', language='python')

    #######################################################################
    #####       Overwise Average Runs For Each Team Since 2008      #######
    #######################################################################
    with st.expander('👉 Overwise Average Runs For Each Team Since 2008'):
        corr = new_deliveriesDF.pivot_table(values='total_runs',
                                            index='batting_team',
                                            columns='over',
                                            aggfunc='mean').fillna(0) * 6

        for over in range(0, 20):
            if over not in corr.columns:
                corr[over] = 0

        corr = corr[sorted(corr.columns)]

        corr_transposed = corr.T

        fig = px.imshow(corr_transposed,
                        color_continuous_scale="viridis",
                        labels=dict(x="Team",
                                    y="Over",
                                    color="Runs"),
                        x=corr_transposed.columns,
                        y=corr_transposed.index)

        fig.update_yaxes(tickvals=list(range(1, 21)),
                         title_text='Overs',
                         title_font_size=16)

        fig.update_xaxes(title_text='Teams',
                         title_font_size=16,
                         tickangle=45)

        st.plotly_chart(fig,
                        transparent=True,
                        use_container_width=True)

    ########################################################################
    #######          Toss Decision Based On Top Venues         #############
    ########################################################################
    with st.expander('👉 Toss Decision Based on Top Venues'):
        top_venues = new_matchesDF['venue'].value_counts().head(
            15).index.to_list()

        top_venues_matches = new_matchesDF[new_matchesDF['venue'].isin(
            top_venues)]

        top_venues_matches['venue_location'] = top_venues_matches['venue'].astype(
            str) + ", " + top_venues_matches['city'].astype(str)

        venue_toss_stats = top_venues_matches.groupby(
            ['venue_location', 'toss_decision']).size().reset_index(name='count')

        venue_toss_stats = venue_toss_stats.sort_values(by='count',
                                                        ascending=False)

        fig, ax = plt.subplots(figsize=(15, 8))

        plt.rcParams.update({'text.color': "white",
                            'axes.labelcolor': "white",
                             'xtick.color': 'white',
                             'ytick.color': 'white'})

        sns.barplot(x='venue_location',
                    y='count',
                    hue='toss_decision',
                    data=venue_toss_stats,
                    legend=False,
                    ax=ax)

        ax.bar_label(ax.containers[0],
                     label_type='edge',
                     color='white')

        ax.bar_label(ax.containers[1],
                     label_type='edge',
                     color='white')

        legend = plt.legend()
        for text in legend.get_texts():
            text.set_color("black")

        plt.xticks(rotation=45,
                   ha='right',
                   fontsize=10)

        plt.title('Toss Decision Based on Top Venues', fontsize=16)
        plt.xlabel('Venue and City', fontsize=14)
        plt.ylabel('Count', fontsize=14)

        st.pyplot(fig, transparent=True)

        venue_toss_stats = venue_toss_stats.rename(
            columns={'count': 'Count',
                     'toss_decision': 'Decision Taken'})

        st.dataframe(venue_toss_stats.sort_values(by='Count', ascending=False),
                     width=800,
                     height=400)

    #############################################################################
    ###########         Average Runs By Teams In Last Over         ##############
    #############################################################################
    with st.expander('👉 Average Runs Scored By Teams In Last Over'):
        fig, ax = plt.subplots(figsize=(10, 6))

        last_over = new_deliveriesDF[new_deliveriesDF['over'] == 19]

        twenty_over_scores = round(
            last_over.groupby('batting_team')['total_runs'].mean() * 6
        ).sort_values(ascending=False)

        sns.barplot(x=twenty_over_scores.values,
                    y=twenty_over_scores.index,
                    palette=sns.color_palette(
                        "viridis", n_colors=len(twenty_over_scores)),
                    hue=None,
                    legend=False,
                    ax=ax)

        ax.bar_label(ax.containers[0])

        plt.xlabel('Average Runs')
        plt.ylabel('Teams')

        st.pyplot(fig, transparent=True)

    ##############################################################################
    #####           Total Runs Scored By Teams In Last Over Since 2008       #####
    ##############################################################################
    with st.expander('👉 Total Runs Scored By Teams In Last Over Since 2008'):
        last_over = new_deliveriesDF[new_deliveriesDF['over'] == 19]

        twenty_over_scores = last_over.groupby('batting_team')[
            'total_runs'].sum().sort_values(ascending=False)

        fig = px.bar(x=twenty_over_scores.values,
                     y=twenty_over_scores.index,
                     orientation='h',
                     labels={'x': 'Total Runs', 'y': 'Teams'},
                     color=twenty_over_scores.index,
                     color_discrete_sequence=px.colors.sequential.Viridis,
                     text=twenty_over_scores.values)

        fig.update_layout(yaxis=dict(
            autorange="reversed",
            showgrid=False
        ),
            xaxis=dict(showgrid=False),
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False)

        st.plotly_chart(fig,
                        use_container_width=True)

        combine_df = new_matchesDF.merge(
            new_deliveriesDF,
            left_on='id',
            right_on='match_id',
            how='left')

    ##############################################################################
    ###                    Total Runs Scored in Each Season                 ######
    ##############################################################################
    with st.expander('👉 Total Runs Scored in Each Season'):
        plt.rcParams.update({'text.color': "white",
                            'axes.labelcolor': "white",
                             'xtick.color': 'white',
                             'ytick.color': 'white'})

        new_matchesDF['season'] = new_matchesDF['season'].astype(str)

        season_runs = new_matchesDF.groupby(
            'season')['target_runs'].sum().reset_index()

        temp4 = season_runs.set_index('season')

        fig = px.line(data_frame=temp4,
                      x=temp4.index,
                      y='target_runs',
                      labels={'target_runs': 'Total Runs', 'Season': 'Season'},
                      markers=True)

        fig.update_layout(
            xaxis_title='Season',
            yaxis_title='Total Runs',
            title_x=0.5,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True),
        )

        st.plotly_chart(fig,
                        use_container_width=True)

    #####################################################################
    ###           Count of Matches By Different Umpires               ###
    #####################################################################
    with st.expander('👉 Count of Matches Umpired By Different Umpires'):
        fig = plt.figure(figsize=(15, 8))

        umpires = pd.concat(
            [new_matchesDF['umpire1'],
             new_matchesDF['umpire2']]).value_counts()

        top_10_umpires = umpires.nlargest(10)

        ax = sns.barplot(x=top_10_umpires.index,
                         y=top_10_umpires.values,
                         palette=sns.color_palette(
                             "viridis", len(top_10_umpires)),
                         hue=None,
                         legend=False)

        ax.bar_label(ax.containers[0])

        plt.xlabel('Umpire Name')
        plt.ylabel('Matches Umpired')

        st.pyplot(fig,
                  transparent=True)

    ###########################################################################
    ############ Lucky Venue For Teams ########################################
    ###########################################################################
    with st.expander('👉  Lucky Venue For Teams'):
        teams = new_matchesDF.team1.unique().tolist()

        # new_matchesDF['venue'] = new_matchesDF['venue'] + \
        #     ", " + new_matchesDF['city']
        new_matchesDF['venue'] = new_matchesDF['venue']

        for team in teams:
            fig = plt.figure(figsize=(15, 8))

            team_name = team

            lucky_venues = new_matchesDF[new_matchesDF['winner']
                                         == team_name]['venue'].value_counts().nlargest(10)

            num_venues = len(lucky_venues)

            explode = [0.1] * num_venues
            colors = ['turquoise', 'lightblue',
                      'lightgreen', 'crimson', 'magenta', 'orange']
            colors = colors * (num_venues // len(colors) + 1)
            colors = colors[:num_venues]

            plt.rcParams.update({'text.color': "white",
                                'axes.labelcolor': "white",
                                 'xtick.color': 'white',
                                 'ytick.color': 'white'})

            lucky_venues.plot(kind='pie',
                              autopct='%1.1f%%',
                              explode=explode,
                              shadow=True,
                              startangle=20,
                              textprops={'fontsize': 10},
                              colors=colors)

            plt.title(f'Win Percentage at Different Venues for {team}')

            plt.ylabel('')

            st.pyplot(fig, transparent=True)

    #####################################################################
    ####              Teams with more than 200+ scores               ####
    #####################################################################
    with st.expander('👉 Teams With More Than 200+ Scores'):
        runs = new_deliveriesDF.groupby(['match_id', 'inning', 'batting_team', 'bowling_team'])[
            'total_runs'].sum().reset_index()

        runs_over_200_df = runs[runs['total_runs'] > 200]

        runs_over_200 = runs_over_200_df['batting_team'].value_counts()

        fig = plt.figure(figsize=(10, 7))

        plt.rcParams.update({'text.color': "white",
                             'axes.labelcolor': "white",
                            'xtick.color': 'white',
                             'ytick.color': 'white'})

        ax = sns.barplot(x=runs_over_200.index,
                         y=runs_over_200.values, palette='viridis',
                         hue=None,
                         legend=False)

        ax.bar_label(ax.containers[0])

        plt.xticks(rotation='vertical')
        plt.title('Most 200+ Runs Scored By Teams')
        plt.xlabel('Teams')
        plt.ylabel('Number of Instances')

        st.pyplot(fig, transparent=True)
