import streamlit as st
import plotly.graph_objects as go
from scrollToTop import create_scroll_to_top_button
from datasetPreprocessing import new_deliveriesDF


def app():
    st.markdown(
        '''
            <h1 style='text-align:center; color: #4fb9fc;'><strong>🏏 PLAYER ANALYSIS 🏏</strong></h1>
            <hr style="border-top: 3px solid #4fb9fc;">
        ''',
        unsafe_allow_html=True
    )

    Batsman = new_deliveriesDF['batter'].unique().tolist()
    Bowler = new_deliveriesDF['bowler'].unique().tolist()

    Batsman.extend(Bowler)
    Players = list(set(Batsman))

    player = st.selectbox("Select A Player", Players)
    Analyze = st.button('Analyze')

    ###########################################################
    # --------------->   PLAYER AS BATSMAN      <--------------
    ###########################################################

    if Analyze:
        selected_player_bat_df = new_deliveriesDF[
            new_deliveriesDF['batter'] == player
        ]

        if len(selected_player_bat_df) != 0:
            ###########################################################
            # ----------->   RUNS AGAINST OTHER TEAMS      <-----------
            ###########################################################

            player_runs_against_teams = selected_player_bat_df.groupby('bowling_team')['total_runs'].sum().reset_index().sort_values(
                by='total_runs',
                ascending=False
            )

            fig = go.Figure()

            fig.add_trace(
                go.Bar(
                    x=player_runs_against_teams['bowling_team'],
                    y=player_runs_against_teams['total_runs'],
                    marker=dict(
                        color=player_runs_against_teams['total_runs'],
                        colorscale='Viridis'
                    ),
                    text=player_runs_against_teams['total_runs'],
                    textposition='auto',
                    hoverinfo='y+x',
                )
            )

            fig.update_layout(
                title=(
                    f"{player.strip()}'s Batting Performance Against Other Teams"),
                xaxis_title="Teams",
                yaxis_title="Total Runs Scored",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                xaxis=dict(tickangle=-45),
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.image("Images/divider.png")

            #############################################################
            # --------->   RUNS AGAINST DIFFERENT BOWLERS      <---------
            #############################################################
            player_runs_against_bowlers = selected_player_bat_df.groupby('bowler')['total_runs'].sum().reset_index().sort_values(
                by='total_runs',
                ascending=False
            )[:15]

            fig = go.Figure()

            fig.add_trace(
                go.Bar(
                    x=player_runs_against_bowlers['bowler'],
                    y=player_runs_against_bowlers['total_runs'],
                    marker=dict(
                        color=player_runs_against_bowlers['total_runs'],
                        colorscale='Viridis'
                    ),
                    text=player_runs_against_bowlers['total_runs'],
                    textposition='auto',
                    hoverinfo='y+x',
                ))

            fig.update_layout(
                title=(
                    f"{player.strip()}'s Batting Performance Against Different Bowlers [Top 15]"),
                xaxis_title="Bowlers",
                yaxis_title="Total Runs Scored",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                xaxis=dict(tickangle=-45),
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.image("Images/divider.png")

            #############################################################
            # ---------------->   PARTNERSHIP RUNS      <----------------
            #############################################################
            player_partnership_runs = selected_player_bat_df.groupby('non_striker')['total_runs'].sum().reset_index().sort_values(
                by='total_runs',
                ascending=False
            )[:15]

            fig = go.Figure()

            fig.add_trace(
                go.Bar(
                    x=player_partnership_runs['non_striker'],
                    y=player_partnership_runs['total_runs'],
                    marker=dict(
                        color=player_partnership_runs['total_runs'],
                        colorscale='Viridis'
                    ),
                    text=player_partnership_runs['total_runs'],
                    textposition='auto',
                    hoverinfo='y+x',
                )
            )

            fig.update_layout(
                title=(
                    f"{player.strip()}'s Batting Runs With Partner At non-striker [Top 15]"),
                xaxis_title="Players",
                yaxis_title="Total Runs Scored",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                xaxis=dict(
                    tickangle=-45,
                    tickfont=dict(size=12)
                ),
                height=500,
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.image("Images/divider.png")

            #############################################################
            # ------->   PLAYER'S RUNS IN DIFFERENT INNINGS      <-------
            #############################################################
            innings_runs = selected_player_bat_df[
                selected_player_bat_df['inning'] < 3
            ]

            innings = innings_runs.groupby(
                'inning')['total_runs'].sum().reset_index()

            fig = go.Figure()

            fig.add_trace(
                go.Bar(
                    x=innings['inning'],
                    y=innings['total_runs'],
                    text=innings['total_runs'],
                    textposition='auto',
                    marker=dict(
                        color=innings['total_runs'],
                        colorscale='Viridis'
                    ),
                    hoverinfo='y+x',
                )
            )

            fig.update_layout(
                title=f"{player.strip()}'s Batting Runs In Different Innings",
                xaxis_title="Innings",
                yaxis_title="Runs Scored",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                xaxis=dict(
                    tickfont=dict(size=12)
                ),
                height=600,
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.image("Images/divider.png")

        else:
            st.markdown(
                f"<h5 style='text-align: center; color: red;'> ⚠ Oops! Looks Like We Couldn't Find Any Batting Stats For {player} In IPL History ⚠</h5>",
                unsafe_allow_html=True
            )

        ###########################################################
        # --------------->   PLAYER AS BOWLER      <--------------
        ###########################################################

        selected_player_boll_df = new_deliveriesDF[
            new_deliveriesDF['bowler'] == player
        ]

        if len(selected_player_boll_df) != 0:
            #############################################################
            # -------->   RUNS GIVEN TO DIFFERENT PLAYERS      <--------
            #############################################################
            player_df_bowl_players = selected_player_boll_df.groupby('batter')['total_runs'].sum().reset_index().sort_values(
                by='total_runs',
                ascending=False
            )[:15]

            fig = go.Figure()

            fig.add_trace(
                go.Bar(
                    x=player_df_bowl_players['batter'],
                    y=player_df_bowl_players['total_runs'],
                    text=player_df_bowl_players['total_runs'],
                    textposition='auto',
                    marker=dict(
                        color=player_df_bowl_players['total_runs'],
                        colorscale='Viridis'
                    ),
                    hoverinfo='y+x',
                )
            )

            fig.update_layout(
                title=(
                    f"Runs Scored By Different Players Against {player.strip()}'s (Top 15)"),
                xaxis_title="Players",
                yaxis_title="Runs",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(
                    color='white'
                ),
                xaxis=dict(
                    tickangle=-45,
                    tickfont=dict(size=12)
                ),
                height=600,
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.image("Images/divider.png")

            #############################################################
            # --------->   RUNS GIVEN IN DIFFERENT OVERS      <---------
            #############################################################

            player_df_bowl_overs = selected_player_boll_df.groupby('over')['total_runs'].sum().reset_index().sort_values(
                by='over',
                ascending=True
            )

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=player_df_bowl_overs['over'],
                    y=player_df_bowl_overs['total_runs'],
                    mode='lines+markers+text',
                    text=player_df_bowl_overs['total_runs'],
                    textposition='top center',
                    marker=dict(
                        color='purple',
                        size=8
                    ),
                    line=dict(
                        color='purple',
                        width=2
                    ),
                )
            )

            for i in range(len(player_df_bowl_overs)):
                fig.add_trace(
                    go.Scatter(
                        x=[
                            player_df_bowl_overs['over'][i],
                            player_df_bowl_overs['over'][i]
                        ],
                        y=[
                            0,
                            player_df_bowl_overs['total_runs'][i]
                        ],
                        mode='lines',
                        line=dict(
                            color='purple',
                            width=1,
                            dash='dot'
                        ),
                        showlegend=False
                    )
                )

            fig.update_layout(
                title=(
                    f'Total Runs Given By {player.strip()} in Different Overs'),
                xaxis_title="Overs",
                yaxis_title="Total Runs",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                xaxis=dict(
                    tickmode='linear',
                    tick0=1,
                    dtick=1,
                    range=[-1, 20],
                    fixedrange=True
                ),
                height=600,
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.image("Images/divider.png")

            #############################################################
            # --------->   OVERS THROWN BY THE PLAYER      <---------
            #############################################################
            selected_player_boll_over = selected_player_boll_df['over'].value_counts(
            ).reset_index()

            selected_player_boll_over.columns = [
                'over', 'count'
            ]

            selected_player_boll_over['over'] = selected_player_boll_over['over'].astype(
                int
            )

            selected_player_boll_over = selected_player_boll_over.sort_values(
                by='over'
            )

            selected_player_boll_over['count'] = (
                selected_player_boll_over['count'] / 6
            ).round(2)

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=selected_player_boll_over['over'],
                    y=selected_player_boll_over['count'],
                    mode='lines+markers+text',
                    text=selected_player_boll_over['count'],
                    textposition='top center',
                    marker=dict(
                        color='purple',
                        size=8
                    ),
                    line=dict(
                        color='purple',
                        width=2
                    ),
                )
            )

            for i in range(len(selected_player_boll_over)):
                fig.add_trace(
                    go.Scatter(
                        x=[
                            selected_player_boll_over['over'][i],
                            selected_player_boll_over['over'][i]
                        ],
                        y=[
                            0,
                            selected_player_boll_over['count'][i]
                        ],
                        mode='lines',
                        line=dict(
                            color='purple',
                            width=1,
                            dash='dot'
                        ),
                        showlegend=False
                    )
                )

            fig.update_layout(
                title=f'Number of Times an Over is Bowled By {player.strip()}',
                xaxis_title="Overs",
                yaxis_title="Count (Overs)",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                xaxis=dict(
                    tickmode='linear',
                    dtick=1
                ),
                height=600,
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.image("Images/divider.png")

            #############################################################
            # --------->   RUNS GIVEN TO DIFFERENT TEAMS      <---------
            #############################################################
            player_df_bowl_n = new_deliveriesDF[
                new_deliveriesDF['bowler'] == player
            ]

            player_df_bowl_teams = player_df_bowl_n.groupby('batting_team')['total_runs'].sum().reset_index().sort_values(
                by='total_runs',
                ascending=False
            )[:15]

            fig = go.Figure()

            fig.add_trace(
                go.Bar(
                    x=player_df_bowl_teams['batting_team'],
                    y=player_df_bowl_teams['total_runs'],
                    text=player_df_bowl_teams['total_runs'],
                    textposition='outside',
                    marker=dict(
                        color=player_df_bowl_teams['total_runs'],
                        colorscale='Viridis'
                    ),
                )
            )

            fig.update_layout(
                title=(
                    f'Runs Scored By Different Teams Against {player.strip()}'),
                xaxis_title='Teams',
                yaxis_title='Runs',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                xaxis=dict(
                    tickangle=-45,
                    tickmode='array',
                    tickvals=player_df_bowl_teams['batting_team']
                ),
                height=500,
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.image("Images/divider.png")

        else:
            st.markdown(
                f"<h5 style='text-align: center; color: red;'> ⚠ Oops! Looks Like We Couldn't Find Any Bowling Stats For {player} In IPL History ⚠</h5>",
                unsafe_allow_html=True
            )

    create_scroll_to_top_button(key_suffix="playerAnalysis")
    st.image("Images/divider.png")
