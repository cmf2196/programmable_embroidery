# programmable_embroidery


Authors: Connor Finn, Drew Deperro
Date: March 24th, 2019

Project Overview: 

The goal of this project was to predict the tournament outcomes of the Power Five and Big East conferences for men’s NCAA Division I college basketball. Statistical data for teams in all six conferences for regular season play and tournament play was collected from sports-reference.com. Data was collected for the previous 5 seasons for every team in every conference. Once the data was scraped and cleaned, it was put into databases where further analyses were performed. Jupyter notebook was used in conjunction with Pandas and Beautiful Soup, for data collection, analysis and extraction. The current deliverable yields every team’s probability of beating every team in their conference with a testing accuracy of ~0.70.  Further analyses were done to predict the outcome of each conference tournament. The models were found to select the correct winner of the Big East Tournament with 36% accuracy, the Big 10 Tournament with 65% accuracy, the Big 12 Tournament with 58% accuracy, the Pac 12 Tournament with 40%, the ACC Tournament with 24% accuracy, and the SEC Tournament with 27% accuracy.  These results were compared with those of models based on random selection of a winner, and tounament simulations where each game's odds were indicated to be even.  The machine learning model outperformed both other methods.
Keywords: machine learning, basketball, python, college sports

Files Included: 

                2019_Tournament_Case_Study.ipynb
                PowerSixTournament_data_collection.ipynb
                GenerateOdds.ipynb
                Data_Science_Final_Paper.pdf
                
Model Generation Instructions:

                First run the PowerSixTournament_data_collection.ipynb
                Secondly Run the GenerateOdds.ipynb
                Third run the 2019_Tournament_Case_Study.ipynb
                
Credits:  

This is a semester project for Columbia University Class MECEE_4520, Data Science for Mechanical Systems.
Thank you to Dr. Joshua Browne for guidance with this project, as well as his facilitation of our Data science knowlegde through out the course. We further would like to achknowledge the numerous guest speakers who assisted us with our project throughout the semsets, especially Alejandro Mesa and Erik Allen.

Additional Comments:

This model is based off of season long data. Therefore, predictions are based off of the teams' general body of work and do consider game specific performances. When training the model, only conference tournament games are considered; thus, this model should not be applied to regular season games

