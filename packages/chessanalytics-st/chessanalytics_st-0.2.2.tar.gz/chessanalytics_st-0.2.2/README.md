# chessanalytics_st

Graphical representation of functions from chessanalytics designed for Streamlit apps.

# NOTE.

Not all functions from chessanalytics could be presented in graphical way. Functions returning single integer or two-element list do not have huge potential 
of graphical representation. That is why the two libraries may vary a little - chessanalytics_st does not have all functions from chessanalytics, but has some that chessanalytics does not have. This library strictly focuses on streamlit and uses 'st.' functions for plotting, representing data and so on. 

# Installation.

     $ pip install chessanalytics_st


# Initializing class.

      from chessanalytics_st import CAST
      cast = CAST('path/to/file/with/games', 'username')


# W/D/L Functions.

### WDL_date

Generates a plot showing the win, draw, and loss statistics by date.

        Params:
        - colors (list): A list of colors for the bars representing win, draw, and loss. Default is ['green', 'gray', 'red'].
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by date'.
        - xaxis_name (str): The label for the x-axis. Default is 'Date'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.


### WDL_day

Generates a plot showing the win, draw, and loss statistics by day.

        Params: 
        - colors (list): A list of colors for the bars representing win, draw, and loss. Default is ['green', 'gray', 'red'].
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by day'.
        - xaxis_name (str): The label for the x-axis. Default is 'Day'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.

### WDL_opening

Generates a plot showing the win, draw, and loss statistics by opening.

        Params:
        - colors (list): A list of colors for the bars representing win, draw, and loss. Default is ['green', 'gray', 'red'].
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by opening'.
        - xaxis_name (str): The label for the x-axis. Default is 'Opening'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.


### WDL_part

Generates a plot showing the win, draw, and loss statistics by part of the day.

        Params:
        - type (str): The type of chart to display. Default is 'pie'. Options are 'pie' or 'bar'.
        - colors (list): A list of colors for the bars representing win, draw, and loss. Default is ['green', 'gray', 'red'].
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by opening'.
        - xaxis_name (str): The label for the x-axis. Default is 'Opening'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.

### WDL_time

Generates a bar chart showing the win, draw, and loss statistics by time.

        Parameters:
        - colors (list): A list of colors for the bars representing win, draw, and loss. Default is ['green', 'gray', 'red'].
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by time'.
        - xaxis_name (str): The label for the x-axis. Default is 'Hour'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.

### WDL_accurate_elo

Displays the win/draw/loss statistics in st.metric format against players with a specified Elo rating range.

        Parameters:
        - elo (int): The Elo rating of the players to compare against.
        - colors (list): A list of colors to use for the metrics. Default is ['green', 'gray', 'red'].
        - title (bool): Whether to display the title. Default is True.

### WDL_elo

Generates a bar plot or dataframe showing the win/draw/loss statistics by opponent's elo.

        Parameters:
        - plot (str): Specifies the type of plot to generate. Default is 'bar'. Options are 'bar' or 'df'.
        - colors (list): Specifies the colors for the bars in the plot. Default is ['green', 'gray', 'red'].
        - title (str): Specifies the title of the plot. Default is "Win/Draw/Loss stats by opponent's elo".
        - xaxis_name (str): Specifies the label for the x-axis. Default is 'elo'.
        - yaxis_name (str): Specifies the label for the y-axis. Default is 'Number of games'.

### WDL_time_control

Generates a pie chart visualization of the win/draw/loss statistics by time control.

        Parameters:
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by time control'.
        - plot_height (int): The height of the chart in pixels. Default is 700.
        - plot_hole (float): The size of the hole in the center of the pie chart. Default is 0.3.

### WDL_gametype

Generates a pie chart or dataframe showing the win/draw/loss statistics by game type.

        Params:
        - plot (str): The type of chart to display. Default is 'pie'. Options are 'pie', 'bar' or 'df'.
        - colors (list): The colors for the pie chart. Default is ['green', 'gray', 'red'].
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by game type'.
        - xaxis_name (str): The label for the x-axis. Default is 'Game type'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.
        - plot_height (int): The height of the chart in pixels. Default is 700.
        - plot_hole (float): The size of the hole in the center of the pie chart. Default is 0.3.
        



# Time related Functions.

### ranked_unranked

Generates a pie chart showing the distribution of ranked and unranked games.

        Params:
        - title (str): The title of the chart. Default is 'Ranked vs Unranked games'.

### count_games_date

Generates a plotly chart showing the count of games played by date.

        Parameters:
        - type (str): The type of chart to display. Options are 'bar' (default) or 'scatter'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.
        - xaxis_name (str): The label for the x-axis. Default is 'Day'.
        - title (str): The title of the chart. Default is 'Number of games played by date'.


### bullet_progress

Generates a plot showing the progress of the player's elo progress in bullet games over time.

        Params:
        - x_title (str): The title of the x-axis. Default is 'Number of games'.
        - y_title (str): The title of the y-axis. Default is 'Elo'.
        - plot_title (str): The title of the plot. Default is 'Elo progress over time'.

Same functions for different time controls are:

- blitz_progress
- rapid_progress

### bullet_progress_date

Generates a plot showing the progress of the player's elo progress in bullet games by date.

        Params:
        - title (str): The title of the plot. Default is 'Bullet elo progress by date'.
        - x_title (str): The title of the x-axis. Default is 'Date'.
        - y_title (str): The title of the y-axis. Default is 'Elo'.

Same functions for different time controls are:

- blitz_progress_date
- rapid_progress_date

### bullet_progress_hour

Generates a plot showing the progress of the player's elo progress in bullet games by hour of game.

        Params:
        - title (str): The title of the plot. Default is 'Bullet elo progress by hour'.
        - x_title (str): The title of the x-axis. Default is 'Hour'.
        - y_title (str): The title of the y-axis. Default is 'Elo'.
        - type (str): The type of plot to generate. Default is 'bar'. Options are 'bar' or 'line'.

Same functions for different time controls are:

- blitz_progress_hour
- rapid_progress_hour

### last_games_stats

Generates a plot showing the statistics of the last games played.

        Params:
        - title (str): The title of the plot. Default is 'Last games stats'.
        - amount (int): The number of games to display. Default is 20.
        - plot_type (str): The type of plot to generate. Default is 'metric_flashy'. Options are 'df', 'metric_classy', 'metric_flashy', 'json'.


To display info st.code() is used (for visual effects) but even if your opponent name is "print(chess)" it will not affect the plot at all, except
looking slightly different. The chart itself looks like this:

![image](https://github.com/lot022/chessanalytics_st/assets/171599696/8e60717f-e0df-4088-9cdc-7a8077868723)



# Heatmaps and graphical representation of the board.


### heatmap1

Generates a heatmap visualisation of the squares where the moves were made.

        Params:
        - counter (dict): A dictionary containing the count of moves made on each square.
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Moves heatmap'.'
        - plot_showscale (bool): Whether to show the color scale. Default is True.


### rook_moves

Generates a heatmap of the squares where the Rook moves were made.

Same function for different piece types are:

- king_moves
- queen_moves
- bishop_moves
- knight_moves

         Params:
         - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
         - title (str): The title of the heatmap. Default is '(PIECE) moves heatmap'.


### squares_rook_captures

Generates a heatmap of the squares where the Rook captures were made.

Same function for different piece types are:

- squares_king_captures
- squares_queen_captures
- squares_bishop_captures
- squares_knight_captures
- squares_pawn_captures


        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Squares with (PIECE) captures'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.



### squares_with_mates

Generates a heatmap of the squares where the checkmates were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'plasma'.
        - title (str): The title of the heatmap. Default is 'Squares with checkmates'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.


### squares_with_checks

Generates a heatmap of the squares where the checks were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'plasma'.
        - title (str): The title of the heatmap. Default is 'Squares with checks'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only moves from the player's games. Default is False.

### squares_with_captures

Generates a heatmap of the squares where the captures were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'plasma'.
        - title (str): The title of the heatmap. Default is 'Squares with captures'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only moves from the player's games. Default is False.


# How does heatmap plots look?

This is a sample heatmap of king_square_captures() with default params (colorscale set to 'plasma', showscale set to True).

(chessnalytics/plots_png/plot1.png)


Here is the same funcion but without showscale and with colorscale set to 'plotly3'. Note that setting off showscale makes heatmap look more like a rect than square and less readable. 

![image](https://github.com/lot022/chessanalytics_st/assets/171599696/a3971af4-3a9f-4dc6-8f35-3d54d23f96eb)


Here you can see how does the heatmap look without the title.

![image](https://github.com/lot022/chessanalytics_st/assets/171599696/f5d922f9-0d77-4b1a-a771-3e5c4487f052)


# TIPS AND TRICKS.

1. If you do not like how does the title look but setting it to 'None' makes the plot/heatmap look worse, set the title to " " (one space sign). 

2. If you do not like how particular funcion look but want to plot it using Streamlit, just call the function from chessanalytics library and plot it 
yourself. 

3. I have made a cheatsheet with (almost) all the functions and their possibilites. To see which type of plot in the same func is better, check it out here: will add soon :)

4. I have made a sample Streamlit app to show how can it possibly look. If you are looking for inspiration you can see it here: will add soon :)
