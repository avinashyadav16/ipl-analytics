import plotly
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.offline as pyo
import exploratoryDataAnalysis
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datasetPreprocessing import new_matchesDF, new_deliveriesDF


def app():
    st.markdown('''
    <h1 style='text-align:center;'> 🏏 PLAYER ANALYSIS 🏏</h1>
    ''', unsafe_allow_html=True)

    # Batsman = [batsman.strip()
    #            for batsman in new_deliveriesDF['batter'].unique().tolist()]
    # Bowler = [bowler.strip()
    #           for bowler in new_deliveriesDF['bowler'].unique().tolist()]

    Batsman = new_deliveriesDF['batter'].unique().tolist()
    Bowler = new_deliveriesDF['bowler'].unique().tolist()

    Batsman.extend(Bowler)
    Players = list(set(Batsman))

    player = st.selectbox("Select A Player", Players)
    Analyze = st.button('Analyze')

    if Analyze:
        ###########################################################
        # --------------->   PLAYER AS BATSMAN      <--------------
        ###########################################################
        selected_player_df = new_deliveriesDF[new_deliveriesDF['batter'] == player]

        if len(selected_player_df) != 0:
            ###########################################################
            # ----------->   RUNS AGAINST OTHER TEAMS      <-----------
            ###########################################################
            st.markdown(f"<h3 style='text-align: center; color: white;'><em>{
                        player}'s Performance Against Other Teams</em></h3>", unsafe_allow_html=True)

            player_runs_against_teams = selected_player_df.groupby('bowling_team')['total_runs'].sum().reset_index().sort_values(
                by='total_runs', ascending=False)

            fig = plt.figure(figsize=(12, 6))

            custom_palette = sns.color_palette("coolwarm",
                                               len(player_runs_against_teams))

            ax = sns.barplot(data=player_runs_against_teams,
                             x='bowling_team',
                             y='total_runs',
                             palette=custom_palette)

            for container in ax.containers:
                ax.bar_label(container,
                             fontsize=10,
                             padding=3,
                             weight='bold')

            plt.xticks(fontsize=10,
                       rotation=45,
                       ha='right')

            plt.xlabel('Teams',
                       fontsize=14,
                       color='blue',
                       weight='bold')

            plt.ylabel('Total Runs Scored',
                       fontsize=14,
                       color='blue',
                       weight='bold')

            plt.grid(axis='y',
                     linestyle='--',
                     color='gray',
                     alpha=0.7)

            st.pyplot(fig,
                      transparent=True)

            st.image("Images/divider.png")

        #############################################################
        # Runs Against Different Bowlers
        #############################################################

            st. markdown(f"<h5 style='text-align: center; color: white;'> {
                         player} Performance Against Different Bowlers (Top 15)  </h5>", unsafe_allow_html=True)

            player_runs_against_bowlers = selected_player_df.groupby('bowler')['total_runs'].sum(
            ).reset_index().sort_values(by='total_runs', ascending=False)
            player_runs_against_bowlers = player_runs_against_bowlers[:15]
            fig = plt.figure(figsize=(20, 5))
            ax = sns.barplot(data=player_runs_against_bowlers,
                             x='bowler', y='total_runs')
            ax.bar_label(ax.containers[0])
            plt.title(
                f'{player} Performance Against Different Bowlers (Top 15)')
            plt.xlabel('Bewlers')
            plt.ylabel('Runs')
            plt.xticks(fontsize=10)
            st.pyplot(fig, transparent=True)
            st.image("Images/divider.png")
        #############################################################
        # Partnership runs
        #############################################################

            st. markdown(f"<h5 style='text-align: center; color: white;'> {
                         player} Runs With Partner At non-striker (Top 15)  </h5>", unsafe_allow_html=True)

            player_partnership_runs = selected_player_df.groupby('non_striker')['total_runs'].sum(
            ).reset_index().sort_values(by='total_runs', ascending=False)
            player_partnership_runs = player_partnership_runs[:15]
            fig = plt.figure(figsize=(20, 5))
            ax = sns.barplot(data=player_partnership_runs,
                             x='non_striker', y='total_runs')
            ax.bar_label(ax.containers[0])
            plt.title(f'{player} Runs With Partner At non-striker (Top 15)')
            plt.xlabel('Players')
            plt.ylabel('Runs')
            plt.xticks(fontsize=12)

            st.pyplot(fig, transparent=True)
            st.image("Images/divider.png")
        #############################################################
        # Player Runs In Different Innings
        #############################################################
            st. markdown(f"<h5 style='text-align: center; color: white;'> {
                         player} Runs On Different Innings  </h5>", unsafe_allow_html=True)

            fig = plt.figure(figsize=(8, 4))
            innings_runs = selected_player_df[selected_player_df['inning'] < 3]
            innings = innings_runs.groupby('inning')['total_runs'].sum()
            ax = sns.barplot(x=innings.index, y=innings.values)
            ax.bar_label(ax.containers[0])
            plt.title(f'{player} Runs On Different Innings')
            plt.xlabel('Innings')
            plt.ylabel('Runs')
            plt.xticks(fontsize=12)
            st.pyplot(fig, transparent=True)
            st.image("Images/divider.png")

        else:
            st. markdown(f"<h5 style='text-align: center; color: red;'> OOPS! No Data Found For Batting Carrer of {
                         player} in IPL </h5>", unsafe_allow_html=True)
    #############################################################
    ###### Player as bowler ####################################
    #############################################################

        player_df_bowl = new_deliveriesDF[new_deliveriesDF['bowler'] == player]

        if len(player_df_bowl) != 0:
            tr = player_df_bowl['total_runs'].sum()
            st. markdown(f"<h5 style='text-align: center; color: white;'> Runs Given Against Different Players For {
                         player} (Top 15)  </h5>", unsafe_allow_html=True)

            # Runs Given Against Different Players
            player_df_bowl_players = player_df_bowl.groupby('batter')['total_runs'].sum(
            ).reset_index().sort_values(by='total_runs', ascending=False)[:15]
            fig = plt.figure(figsize=(20, 5))
            ax = sns.barplot(data=player_df_bowl_players,
                             x='batter', y='total_runs')
            ax.bar_label(ax.containers[0])
            # plt.title(f'Runs Given Against Different Players For {player} (Top 15) ')
            plt.xlabel('Players')
            plt.ylabel('Runs')
            plt.xticks(fontsize=12)
            st.pyplot(fig, transparent=True)
            st.image("Images/divider.png")
            # Runs Given In Different Overs

            st. markdown(f"<h5 style='text-align: center; color: white;'> Total Runs Given By {
                         player} in different overs </h5>", unsafe_allow_html=True)

            player_df_bowl_overs = player_df_bowl.groupby('over')['total_runs'].sum(
            ).reset_index().sort_values(by='over', ascending=True)
            fig = plt.figure(figsize=(10, 6))
            ax = sns.lineplot(data=player_df_bowl_overs,
                              x='over', y='total_runs', markers=True)
            for x, y in zip(player_df_bowl_overs['over'], player_df_bowl_overs['total_runs']):
                plt.text(x=x, y=y, s='{:.0f}'.format(
                    y), color='white').set_backgroundcolor('purple')
            ax.set_xticks(range(0, 21, 1))
            # ax.set_title(f'Total Runs Given By {player} in different overs')
            st.pyplot(fig, transparent=True)
            st.image("Images/divider.png")

            st. markdown(f"<h5 style='text-align: center; color: white;'> Overs Thrown By {
                         player} </h5>", unsafe_allow_html=True)

            # Number of Times a Over is Balled By The Player
            player_df_bowl_overs_n = player_df_bowl['over'].value_counts(
            ).reset_index()

            player_df_bowl_overs_n['over'] = player_df_bowl_overs_n['over'].astype(
                int)

            player_df_bowl_overs_n = player_df_bowl_overs_n.rename(
                columns={'index': 'over', "over": 'count'})
            player_df_bowl_overs_n = player_df_bowl_overs_n.sort_values(
                by='over')
            player_df_bowl_overs_n['count'] = (
                player_df_bowl_overs_n['count']/6).round(2)

            fig = plt.figure(figsize=(10, 6))
            ax = sns.lineplot(data=player_df_bowl_overs_n,
                              x='over', y='count', markers=True)
            for x, y in zip(player_df_bowl_overs_n['over'], player_df_bowl_overs_n['count']):
                plt.text(x=x, y=y, s='{:.2f}'.format(
                    y), color='white').set_backgroundcolor('purple')
            ax.set_xticks(range(0, 21, 1))
            # ax.set_title(f'Overs Thrown By {player}')
            st.pyplot(fig, transparent=True)
            st.image("Images/divider.png")
            st. markdown(f"<h5 style='text-align: center; color: white;'> Runs Given Against Different Teams For {
                         player} </h5>", unsafe_allow_html=True)

            # Runs Given Against Different Teams
            player_df_bowl_n = new_deliveriesDF[new_deliveriesDF['bowler'] == player]
            player_df_bowl_teams = player_df_bowl_n.groupby('batting_team')['total_runs'].sum(
            ).reset_index().sort_values(by='total_runs', ascending=False)[:15]

            fig = plt.figure(figsize=(20, 5))
            ax = sns.barplot(data=player_df_bowl_teams,
                             x='batting_team', y='total_runs')
            ax.bar_label(ax.containers[0])
            # plt.title(f'Runs Given Against Different Teams For {player}')
            plt.xlabel('Teams')
            plt.ylabel('Runs')
            plt.xticks(fontsize=9)

            st.pyplot(fig, transparent=True)
            st.image("Images/divider.png")

        else:
            st. markdown(f"<h5 style='text-align: center; color: red;'> OOPS! No Data Found For Bowling Carrer of {
                         player} in IPL </h5>", unsafe_allow_html=True)

        st.image("Images/divider.png")
        st. markdown(f"<h6 style='text-align: center; color: white;'> “A wise man learns by the mistakes of others, a fool by own.”– Adam Gilchrist </h6>", unsafe_allow_html=True)
