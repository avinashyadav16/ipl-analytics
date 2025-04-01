import streamlit as st


def app():
    st.markdown(
        '''
            <h1 style='text-align:center; color: #c089f8;'><strong>🏏 IPL ANALYSIS AND PREDICTIONS 🏏 </strong></h1>
            <hr style="border-top: 3px solid #c089f8;">
            <br>

            <center>
                <img style="width: 66%; border-radius: 25px;" 
                src='https://i.pinimg.com/736x/99/7d/36/997d369f389c02e363c9b0689af575d4.jpg' 
                alt='IPL Image'>
            </center>

            <br>

            <div style='text-align:justify; width:66%; margin:auto;'>
            
            The Indian Premier League (IPL), launched in 2008, is a professional Twenty20 (T20) cricket league held annually from April to June. The tournament begins with a round-robin phase, where each team plays against every other team twice—once at home and once away. Teams earn two points for a win, while a no-result match gives each side one point.

            At the end of the round-robin stage, the top four teams advance to the playoffs, and the remaining teams are eliminated. The playoffs start with the first qualifier, where the top two teams compete, with the winner earning a direct spot in the final. The third and fourth-ranked teams then face off in the eliminator, with the winner progressing to the second qualifier and the loser being eliminated. In the second qualifier, the winner of the eliminator plays against the loser of the first qualifier for the final spot in the championship match.

            This project offers a comprehensive analysis of the IPL from its inception through the 2024 season. It covers various aspects such as match statistics, player performance, team comparisons, and more, using the most up-to-date and complete IPL dataset available.
            
            <br>

            
            ## **Teams Played IPL Till Date:**
            
            <div style='display: flex; justify-content: space-between;'>
                <div style='width: 40%; padding-left:10px;'>
                    <ul style='list-style-type:none; padding-left:0; color: green;'>
                        <li> ▪ Royal Challengers Bengaluru</li>
                        <li> ▪ Kings XI Punjab</li>
                        <li> ▪ Sunrisers Hyderabad</li>
                        <li> ▪ Delhi Capitals</li>
                        <li> ▪ Gujarat Titans</li>
                        <li> ▪ Mumbai Indians</li>
                        <li> ▪ Kolkata Knight Riders</li>
                        <li> ▪ Lucknow Super Giants</li>
                        <li> ▪ Rajasthan Royals</li>
                        <li> ▪ Chennai Super Kings</li>
                    </ul>
                </div>
                <div style='width: 40%;'>
                    <ul style='list-style-type:none; padding-left:0; color: orange;'>
                        <li> ▪ Royal Challengers Bangalore</li>
                        <li> ▪ Punjab Kings</li>
                        <li> ▪ Deccan Chargers</li>
                        <li> ▪ Delhi Daredevils</li>
                        <li> ▪ Gujarat Lions</li>
                        <li> ▪ Pune Warriors</li>
                        <li> ▪ Rising Pune Supergiant</li>
                        <li> ▪ Rising Pune Supergiants</li>
                        <li> ▪ Kochi Tuskers Kerala</li>
                    </ul>
                </div>
            </div>
            

            <br>
            
            
            ## **Functionalities Integrated:** 🌟
            
            <div padding:15px; border-radius:10px;'>
                <ul style='list-style-type:none; padding-left:10px;'>
                    <li style='margin-bottom:10px;'>
                        <span style='font-size:1.2em; font-weight:bold; color:#007bff;'>1. Predict First Innings Score:</span><br>
                        <span style='color:#555; padding-left:20px;'>Get a prediction of the first innings score based on the current match situation.</span>
                    </li>
                    <li style='margin-bottom:10px;'>
                        <span style='font-size:1.2em; font-weight:bold; color:#007bff;'>2. Winner Probability Analysis:</span><br>
                        <span style='color:#555; padding-left:20px;'>Determine the winning probability for any given scenario in the second innings.</span>
                    </li>
                    <li style='margin-bottom:10px;'>
                        <span style='font-size:1.2em; font-weight:bold; color:#007bff;'>3. Detailed Exploratory Data Analysis (EDA):</span><br>
                        <span style='color:#555; padding-left:20px;'>Perform a deep dive into the IPL dataset with comprehensive EDA.</span>
                    </li>
                    <li style='margin-bottom:10px;'>
                        <span style='font-size:1.2em; font-weight:bold; color:#007bff;'>4. Team vs Team Analysis:</span><br>
                        <span style='color:#555; padding-left:20px;'>Compare and analyze the performance of two teams head-to-head.</span>
                    </li>
                    <li style='margin-bottom:10px;'>
                        <span style='font-size:1.2em; font-weight:bold; color:#007bff;'>5. Player vs Player Analysis:</span><br>
                        <span style='color:#555; padding-left:20px;'>Analyze individual player performances against each other.</span>
                    </li>
                    <li style='margin-bottom:10px;'>
                        <span style='font-size:1.2em; font-weight:bold; color:#007bff;'>6. Team Past Records:</span><br>
                        <span style='color:#555; padding-left:20px;'>Review and analyze the historical performance of teams.</span>
                    </li>
                    <li style='margin-bottom:10px;'>
                        <span style='font-size:1.2em; font-weight:bold; color:#007bff;'>7. Player Career Analysis:</span><br>
                        <span style='color:#555; padding-left:20px;'>Explore the career statistics of players as batsmen and bowlers.</span>
                    </li>
                </ul>
            </div>
            
            <br><hr><br>
            
            ### ©️ Avinash Yadav &nbsp;&nbsp;|&nbsp;&nbsp; 2025
            <a href="https://www.linkedin.com/in/avinash-yadav-16hgnisgar" target="_blank"><strong>LinkedIn</strong></a> &nbsp;&nbsp;|&nbsp;&nbsp;
            <a href="https://github.com/avinashyadav16" target="_blank"><strong>GitHub</strong></a> &nbsp;&nbsp;|&nbsp;&nbsp;
            <a href="https://medium.com/@avinashyadav16" target="_blank"><strong>Medium</strong></a> 
    
            </div>
        ''',
        unsafe_allow_html=True
    )
    st.image("Images/divider.png")
