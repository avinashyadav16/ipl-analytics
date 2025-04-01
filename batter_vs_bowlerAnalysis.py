import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from datasetPreprocessing import new_deliveriesDF


def app():
    st.markdown(
        '''
            <h1 style='text-align:center; color: #c50d66;'><strong> 🏏 BATTER V/S BOWLER ANALYSIS ⚽ </strong></h1>
            <hr style="border-top: 3px solid #c50d66;">
        ''',
        unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='text-align:center;'>Select Batsman and Bowler for Analysis</h4>",
        unsafe_allow_html=True
    )

    Batsman = new_deliveriesDF['batter'].unique().tolist()
    Bowler = new_deliveriesDF['bowler'].unique().tolist()

    c1, c2 = st.columns([1, 1])

    with c1:
        batsman = st.selectbox("Choose Batsman", Batsman)
    with c2:
        bowler = st.selectbox("Choose Bowler", Bowler)

    if batsman == bowler:
        st.error("Batsman and Bowler can't be the same")
    else:
        Analyze = st.button('Analyze')
        if Analyze:
            st.markdown(
                (f"<h3 style='text-align: center;'> {batsman} vs {bowler} </h3>"),
                unsafe_allow_html=True
            )

            head_to_head = new_deliveriesDF[
                (new_deliveriesDF['batter'].str.strip().str.lower() == batsman.strip().lower()) &
                (new_deliveriesDF['bowler'].str.strip(
                ).str.lower() == bowler.strip().lower())
            ]

            if len(head_to_head) != 0:
                st.markdown(
                    (f"<h4 style='text-align: center;'> Head to Head Details </h4>"),
                    unsafe_allow_html=True
                )

                ###########################################################
                # --------------->   HEAD TO HEAD DATA      <--------------
                ###########################################################

                st.markdown(
                    "<h6 style='text-align: center;'>Match-wise Head-to-Head Data</h6>",
                    unsafe_allow_html=True
                )

                col1, col2 = st.columns([1, 1])

                with col1:
                    st.dataframe(
                        head_to_head[
                            [
                                'match_id',
                                'batting_team',
                                'bowling_team',
                                'over',
                                'ball',
                                'batter',
                                'bowler',
                                'total_runs'
                            ]
                        ]
                    )

                ###########################################################
                # ----------------->   BASIC DETAILS      <----------------
                ###########################################################

                total_bowls = len(head_to_head)
                total_runs = head_to_head['total_runs'].sum()

                # Calculating boundaries and extras
                sixes = head_to_head[
                    head_to_head['batsman_runs'] == 6
                ].shape[0]

                fours = head_to_head[
                    head_to_head['batsman_runs'] == 4
                ].shape[0]

                dot_balls = head_to_head[
                    head_to_head['batsman_runs'] == 0
                ].shape[0]

                wide_balls = head_to_head[
                    head_to_head['extras_type'].fillna('') == 'wides'
                ].shape[0]

                legbyes = head_to_head[
                    head_to_head['extras_type'].fillna('') == 'legbyes'
                ].shape[0]

                byes = head_to_head[
                    head_to_head['extras_type'].fillna('') == 'byes'
                ].shape[0]

                noballs = head_to_head[
                    head_to_head['extras_type'].fillna('') == 'noballs'
                ].shape[0]

                penalty = head_to_head[
                    head_to_head['extras_type'].fillna('') == 'penalty'
                ].shape[0]

                summary_df = pd.DataFrame(
                    {'Statistic': [
                        'Total Balls Bowled',
                        'Total Runs',
                        'Sixes',
                        'Fours',
                        'Dot Balls',
                        'Wide Balls',
                        'Leg Byes',
                        'Byes',
                        'No Balls',
                        'Penalties'
                    ],
                        f'{batsman} vs {bowler}': [
                            total_bowls,
                            total_runs,
                            sixes,
                            fours,
                            dot_balls,
                            wide_balls,
                            legbyes,
                            byes,
                            noballs,
                            penalty
                    ]
                    }
                )

                with col2:
                    sns.set(style="whitegrid")

                    values = summary_df[f'{batsman} vs {bowler}'].values
                    labels = summary_df['Statistic'].values

                    fig, ax = plt.subplots(
                        figsize=(8, 6),
                        dpi=100
                    )

                    bars = ax.barh(
                        labels,
                        values,
                        color=sns.color_palette("tab10")
                    )

                    for bar in bars:
                        ax.text(
                            bar.get_width() + 0.1,
                            bar.get_y() + bar.get_height() / 2,
                            f'{bar.get_width()}',
                            va='center',
                            fontsize=10
                        )

                    ax.set_title(
                        f'Distribution of {batsman} vs {bowler}',
                        fontsize=16,
                        color='black',
                        pad=20
                    )

                    ax.set_xlabel(
                        'Values',
                        fontsize=12
                    )
                    ax.set_ylabel(
                        'Metrics',
                        fontsize=12
                    )

                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    st.pyplot(fig)

                ###########################################################
                # ----------------->   SUMMARY TABLE      <----------------
                ###########################################################

                st.markdown(
                    "<h6 style='text-align: center;'> Summary of Analysis </h6>",
                    unsafe_allow_html=True
                )

                st.table(summary_df.style)

                st.write('---')

            else:
                # If no data is found for the selected pair
                st.write(
                    f'OOPS! No Data Found for {batsman} vs {bowler} in IPL'
                )
                st.markdown(
                    "<h4 style='text-align: center; color: red;'>No Records Found</h4>",
                    unsafe_allow_html=True
                )

        st.image("Images/divider.png")
