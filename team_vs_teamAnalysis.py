import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from scrollToTop import create_scroll_to_top_button
from datasetPreprocessing import new_matchesDF, new_deliveriesDF


###########################################################
# ------------->   MAPPING TEAM TO COLORS    <------------
###########################################################
def gen_colors(t1, t2):
    team_colors = {
        'Mumbai Indians': 'blue',
        'Chennai Super Kings': 'yellow',
        'Royal Challengers Bangalore': 'green',
        'Royal Challengers Bengaluru': 'green',
        'Sunrisers Hyderabad': 'orange',
        'Delhi Capitals': 'lightblue',
        'Delhi Daredevils': 'lightblue',
        'Kolkata Knight Riders': 'purple',
        'Kings XI Punjab': 'red',
        'Punjab Kings': 'red',
        'Rajasthan Royals': 'magenta',
        'Deccan Chargers': 'darkblue',
        'Kochi Tuskers Kerala': 'teal',
        'Pune Warriors': 'skyblue',
        'Gujarat Lions': 'darkorange',
        'Rising Pune Supergiants': 'darkred',
        'Rising Pune Supergiant': 'darkred',
        'Lucknow Super Giants': 'navyblue',
        'Gujarat Titans': 'gold'
    }

    # default ==  'grey' if not found
    color_t1 = team_colors.get(t1, 'grey')
    color_t2 = team_colors.get(t2, 'grey')

    return [color_t1, color_t2]


def app():
    st.markdown(
        ''' <h1 style='text-align:center; color: #259073;'><strong> 🎯 TEAM V/S TEAM ANALYSIS 🎯</strong></h1>
            <hr style="border-top: 3px solid #259073;">
        ''',
        unsafe_allow_html=True
    )

    combine_df = new_matchesDF.merge(
        new_deliveriesDF,
        left_on='id',
        right_on='match_id',
        how='left'
    )

    Teams = new_matchesDF.team1.unique().tolist()

    c1, c2 = st.columns(2)

    with c1:
        t1 = st.selectbox("Select Team 1", Teams)
    with c2:
        t2 = st.selectbox("Select Team 2", Teams)

    if t1 == t2:
        st.markdown(
            f"<h5 style='text-align: center; color: red;'> ⚠ Oops! Looks Like Team1 and Team2 Are Same ⚠</h5>",
            unsafe_allow_html=True
        )
    else:
        colors = gen_colors(t1, t2)

        Analyze = st.button('Analyze')

        if Analyze:
            st.markdown(
                f"<h3 style='text-align: center;'> {t1} vs {t2} </h3>",
                unsafe_allow_html=True
            )

            # Total Match Played
            t1_batting = new_matchesDF[
                (new_matchesDF['team1'] == t1) & (new_matchesDF['team2'] == t2)
            ]

            t2_batting = new_matchesDF[
                (new_matchesDF['team1'] == t2) & (new_matchesDF['team2'] == t1)
            ]

            total = pd.concat(
                [t1_batting, t2_batting],
                ignore_index=True
            )

            if total.empty:
                st.markdown(
                    f"<h5 style='text-align: center; color: red;'> ⚠ {t1} and {t2} have not played any matches together ⚠</h5>",
                    unsafe_allow_html=True
                )
            else:

                ###########################################################
                # --------------------->   WINNER    <--------------------
                ###########################################################
                fig = plt.figure(
                    figsize=(6, 4)
                )

                ax = sns.countplot(
                    total['winner'],
                    palette=colors
                )

                ax.bar_label(ax.containers[0])

                plt.title(f'{t1} vs {t2} : Match Winners', fontsize=10)
                plt.xlabel('Teams')
                plt.ylabel('Winning Count')

                st.pyplot(
                    fig,
                    transparent=True
                )

                ###########################################################
                # -------------------->   TOSS WINS    <-------------------
                ###########################################################
                st.image("Images/divider.png")
                fig = plt.figure(
                    figsize=(6, 4)
                )

                print(total['toss_winner'].value_counts())

                ax = sns.countplot(
                    total['toss_winner'],
                    palette=colors
                )

                ax.bar_label(ax.containers[0])

                plt.title(
                    f'{t1} vs {t2} : Toss Winners',
                    fontsize=10
                )

                plt.xlabel('Teams')
                plt.ylabel('Winning Count')

                st.pyplot(
                    fig,
                    transparent=True
                )

                ###########################################################
                # --------------->   PLAYER OF THE MATCH    <--------------
                ###########################################################
                st.image("Images/divider.png")
                fig = plt.figure(
                    figsize=(6, 8)
                )

                ax = sns.countplot(
                    y=total['player_of_match'],
                    hue=total['winner'],
                    order=total['player_of_match'].value_counts().index,
                    palette=colors
                )

                if len(ax.containers) > 0:
                    ax.bar_label(ax.containers[0])

                if len(ax.containers) > 1:
                    ax.bar_label(ax.containers[1])

                legend = plt.legend()
                frame = legend.get_frame()
                frame.set_facecolor('black')

                st.pyplot(
                    fig,
                    transparent=True
                )

                t1_batting = combine_df[
                    (
                        (combine_df['batting_team'] == t1) &
                        (combine_df['bowling_team'] == t2)
                    )
                ]

                t2_batting = combine_df[
                    (
                        (combine_df['batting_team'] == t2) &
                        (combine_df['bowling_team'] == t1)
                    )
                ]

                total_del = pd.concat(
                    [t1_batting, t2_batting],
                    ignore_index=True
                )

                ###########################################################
                # --------------->   BATTING TEAM T1 AVG    <--------------
                ###########################################################
                st.image("Images/divider.png")

                temp = total_del.groupby(
                    [
                        'season',
                        'match_id',
                        'inning',
                        'batting_team',
                        'bowling_team'
                    ]
                )['total_runs'].sum().reset_index()

                temp = temp[
                    temp['inning'] < 3
                ]

                runs = temp[temp.batting_team == t1]['total_runs',
                                                     'season', 'match_id', 'inning']

                runs_avg = runs.groupby(by='season').mean().reset_index()

                fig = px.line(
                    data_frame=runs_avg,
                    x='season',
                    y='total_runs',
                    title=f'{t1} vs {t2} : {t1} Average Total Score',
                    labels={
                        'total_runs': "Runs",
                        'season': f"Bowling :{t2}"
                    }
                )

                st.plotly_chart(
                    fig,
                    transparent=True,
                    use_container_width=True
                )

                ###########################################################
                # --------------->   BATTING TEAM T2 AVG    <--------------
                ###########################################################
                st.image("Images/divider.png")
                fig = plt.figure(
                    figsize=(10, 4)
                )

                temp = total_del.groupby(
                    [
                        'season',
                        'match_id',
                        'inning',
                        'batting_team',
                        'bowling_team'
                    ]
                )['total_runs'].sum().reset_index()

                temp = temp[
                    temp['inning'] < 3
                ]

                runs = temp[temp.batting_team == t2][
                    ['total_runs', 'season', 'match_id', 'inning']]

                runs_avg = runs.groupby(by='season').mean().reset_index()

                fig = px.line(
                    data_frame=runs_avg,
                    x='season',
                    y='total_runs',
                    title=f'{t1} vs {t2} : {t2} Average Total Score',
                    labels={
                        'total_runs': "Runs",
                        'season': f"Bowling :{t1}"
                    }
                )

                st.plotly_chart(
                    fig,
                    transparent=True,
                    use_container_width=True
                )

                ###########################################################
                # ----------->   MATCHES WINS BASED ON CITY    <----------
                ###########################################################
                st.image("Images/divider.png")
                st.markdown(
                    f"<h4 style='text-align: center; color: white;'> {t1} vs {t2} : Match Win Based On City  </h4>",
                    unsafe_allow_html=True
                )

                fig = plt.figure(
                    figsize=(10, 4)
                )

                ax = sns.countplot(
                    x=total['city'],
                    hue=total['winner'],
                    palette=colors
                )

                if len(ax.containers) > 0:
                    ax.bar_label(ax.containers[0])

                if len(ax.containers) > 1:
                    ax.bar_label(ax.containers[1])

                legend = plt.legend()
                frame = legend.get_frame()
                frame.set_facecolor('black')

                plt.title(
                    f'{t1} vs {t2} : Match Win Based On City',
                    fontsize=10
                )

                plt.xlabel('City Names')
                plt.ylabel('frequency')

                st.pyplot(
                    fig,
                    transparent=True,
                    use_container_width=True
                )

                ###########################################################
                # ---------------->   HEAD TO HEAD INFO    <---------------
                ###########################################################
                st.image("Images/divider.png")

                def info(team):
                    t = team
                    er = total_del[
                        total_del.bowling_team == t
                    ]['extra_runs'].sum()

                    sixes = total_del[
                        (total_del['batting_team'] == t) &
                        (total_del['total_runs'] == 6)
                    ].count()[0]

                    fours = total_del[
                        (total_del['batting_team'] == t) &
                        (total_del['total_runs'] == 4)
                    ].count()[0]

                    doubles = total_del[
                        (total_del['batting_team'] == t) &
                        (total_del['total_runs'] == 2)
                    ].count()[0]

                    singles = total_del[
                        (total_del['batting_team'] == t) &
                        (total_del['total_runs'] == 1)
                    ].count()[0]

                    total_runs = total_del[
                        total_del['batting_team'] == t
                    ]['total_runs'].sum()

                    return [er, sixes, fours, doubles, singles, total_runs]

                df = pd.DataFrame(
                    columns=[
                        'info',
                        f'{t1}',
                        f'{t2}'
                    ],
                    index=None
                )

                df['info'] = [
                    'Extra Runs',
                    'Sixes',
                    'Fours',
                    'Doubles',
                    'Singles',
                    'Total Runs'
                ]

                df[f'{t1}'] = info(t1)
                df[f'{t2}'] = info(t2)

                st.markdown(
                    f"<h4 style='text-align: center; color: white;'> HEAD TO HEAD INFO </h4>", unsafe_allow_html=True)

                st.table(df)

                ###########################################################
                # ------------------>   TEAM T1 SIXES    <-----------------
                ###########################################################
                st.image("Images/divider.png")
                st.markdown(
                    f"<h4 style='text-align: center; color: white;'>  Team {t1} Players Total Sixes Against {t2} </h4>",
                    unsafe_allow_html=True
                )

                fig = plt.figure(
                    figsize=(12, 10),
                    dpi=150
                )

                t1_player_six = total_del[
                    (total_del['batting_team'] == t1) &
                    (total_del['total_runs'] == 6)
                ]['batter']

                ax = sns.countplot(
                    y=t1_player_six,
                    order=t1_player_six.value_counts().iloc[:10].index
                )

                ax.bar_label(ax.containers[0])

                plt.title(
                    f"Number of Sixes Hitted By Players of Team {t1} vs {t2}"
                )
                plt.ylabel('Players')
                plt.xlabel('Number of Sixes')

                st.pyplot(
                    fig,
                    transparent=True
                )

                ###########################################################
                # ------------------>   TEAM T1 FOURS    <-----------------
                ###########################################################
                st.image("Images/divider.png")
                st.markdown(
                    f"<h4 style='text-align: center; color: white;'>  Team {t1} Players Total Fours Against {t2} </h4>",
                    unsafe_allow_html=True
                )

                fig = plt.figure(
                    figsize=(12, 10),
                    dpi=150
                )

                t1_player_six = total_del[
                    (total_del['batting_team'] == t1) &
                    (total_del['total_runs'] == 4)
                ]['batter']

                ax = sns.countplot(
                    y=t1_player_six,
                    order=t1_player_six.value_counts().iloc[:10].index
                )

                ax.bar_label(ax.containers[0])

                plt.title(
                    f"Number of Fours Hitted By Players of Team {t1} vs {t2}"
                )
                plt.ylabel('Players')
                plt.xlabel('Number of Fours')

                st.pyplot(
                    fig,
                    transparent=True
                )

                ###########################################################
                # ------------------>   TEAM T2 SIXES    <-----------------
                ###########################################################
                st.image("Images/divider.png")
                st.markdown(
                    f"<h4 style='text-align: center; color: white;'>  Team {t2} Players Total Sixes Against {t1} </h4>",
                    unsafe_allow_html=True
                )

                fig = plt.figure(
                    figsize=(12, 10),
                    dpi=150
                )

                t1_player_six = total_del[
                    (total_del['batting_team'] == t2) &
                    (total_del['total_runs'] == 6)
                ]['batter']

                ax = sns.countplot(
                    y=t1_player_six,
                    order=t1_player_six.value_counts().iloc[:10].index
                )

                ax.bar_label(ax.containers[0])

                plt.title(
                    f"Number of Sixes Hitted By Players of Team {t2} vs {t1}"
                )
                plt.ylabel('Players')
                plt.xlabel('Number of Sixes')

                st.pyplot(
                    fig,
                    transparent=True
                )

                ###########################################################
                # ------------------>   TEAM T2 FOURS    <-----------------
                ###########################################################
                st.image("Images/divider.png")
                st.markdown(
                    f"<h4 style='text-align: center; color: white;'>  Team {t2} Players Total Fours Against {t1} </h4>",
                    unsafe_allow_html=True
                )

                fig = plt.figure(
                    figsize=(12, 10),
                    dpi=150
                )

                t1_player_six = total_del[
                    (total_del['batting_team'] == t2) &
                    (total_del['total_runs'] == 4)
                ]['batter']

                ax = sns.countplot(
                    y=t1_player_six,
                    order=t1_player_six.value_counts().iloc[:10].index
                )

                ax.bar_label(ax.containers[0])

                plt.title(
                    f"Number of fours Hitted By Players of Team {t2} vs {t1}",
                )
                plt.ylabel('Players')
                plt.xlabel('Number of fours')

                st.pyplot(
                    fig,
                    transparent=True
                )

                st.image("Images/divider.png")

    create_scroll_to_top_button(key_suffix="teamAnalysis")
    st.image("Images/divider.png")
