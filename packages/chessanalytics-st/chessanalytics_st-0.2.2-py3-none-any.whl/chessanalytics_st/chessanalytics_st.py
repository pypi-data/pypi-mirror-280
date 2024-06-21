from chessanalytics import CA
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd


class CAST:

    def __init__(self, file, name):
        self.file = file
        self.name = name
        self.ca = CA(self.file, self.name)


                                                        ##########          Win/Draw/Loss Related functions          ##########



    def WDL_date(self, colors : list = ['green', 'gray', 'red'], title : str ='Win/Draw/Loss stats by date', xaxis_name:str='Date', yaxis_name : str ='Number of games'):

        '''
        Generates a plot showing the win, draw, and loss statistics by date.

        Params:
        - colors (list): A list of colors for the bars representing win, draw, and loss. Default is ['green', 'gray', 'red'].
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by date'.
        - xaxis_name (str): The label for the x-axis. Default is 'Date'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.
        '''


        assert len(colors) == 3, 'Bars contain colours for win,draw and loss. There is no place for less or more colours.'

        data = self.ca.WDL_Date()

        colorz = colors


        fig = go.Figure()

        for key, value in data.items():
            for i in range(len(value)):
                fig.add_trace(go.Bar(
                    x=[key],
                    y=[value[i]],
                    marker_color=colorz[i],
                    name=f'Index {i}'
                ))

        fig.update_layout(
            title=f'{title}',
            xaxis_title=f'{xaxis_name}',
            yaxis_title=f'{yaxis_name}',
            barmode='stack',
            showlegend=False
        )

        st.plotly_chart(fig)


    def WDL_day(self, colors : list = ['green', 'gray', 'red'], title : str ='Win/Draw/Loss stats by day', xaxis_name:str='Day', yaxis_name : str ='Number of games'):
        '''
        Generates a plot showing the win, draw, and loss statistics by day.

        Params: 
        - colors (list): A list of colors for the bars representing win, draw, and loss. Default is ['green', 'gray', 'red'].
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by day'.
        - xaxis_name (str): The label for the x-axis. Default is 'Day'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.
        '''

        assert len(colors) == 3, 'Bars contain colours for win,draw and loss. There is no place for less or more colours.'

        data = self.ca.WDL_Day()

        colorz = colors


        fig = go.Figure()

        for key, value in data.items():
            for i in range(len(value)):
                fig.add_trace(go.Bar(
                    x=[key],
                    y=[value[i]],
                    marker_color=colorz[i],
                    name=f'Index {i}'
                ))

        fig.update_layout(
            title=f'{title}',
            xaxis_title=f'{xaxis_name}',
            yaxis_title=f'{yaxis_name}',
            barmode='stack',
            showlegend=False
        )

        st.plotly_chart(fig)


    def WDL_opening(self, colors : list = ['green', 'gray', 'red'], title : str ='Win/Draw/Loss stats by opening', xaxis_name:str='Opening', yaxis_name : str ='Number of games'):
        '''
        Generates a plot showing the win, draw, and loss statistics by opening.

        Params:
        - colors (list): A list of colors for the bars representing win, draw, and loss. Default is ['green', 'gray', 'red'].
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by opening'.
        - xaxis_name (str): The label for the x-axis. Default is 'Opening'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.
        '''

        assert len(colors) == 3, 'Bars contain colours for win,draw and loss. There is no place for less or more colours.'

        data = self.ca.WDL_Opening()

        colorz = colors

        wdl = ['win', 'draw', 'loss']


        fig = go.Figure()

        for key, value in data.items():
            for i in range(len(value)):
                fig.add_trace(go.Bar(
                    x=[key],
                    y=[value[i]],
                    marker_color=colorz[i],
                    name=f'{wdl[i]}'
                ))

        fig.update_layout(
            title=f'{title}',
            xaxis_title=f'{xaxis_name}',
            yaxis_title=f'{yaxis_name}',
            barmode='stack',
            showlegend=False
        )

        st.plotly_chart(fig)


    def WDL_part(self, type : str = 'pie', colors : list = ['green', 'gray', 'red'], title : str ='Win/Draw/Loss stats by opening', xaxis_name:str='Opening', 
                 yaxis_name : str ='Number of games'):
        '''
        Generates a plot showing the win, draw, and loss statistics by part of the day.

        Params:
        - type (str): The type of chart to display. Default is 'pie'. Options are 'pie' or 'bar'.
        - colors (list): A list of colors for the bars representing win, draw, and loss. Default is ['green', 'gray', 'red'].
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by opening'.
        - xaxis_name (str): The label for the x-axis. Default is 'Opening'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.
        '''

        assert len(colors) == 3, 'Bars contain colours for win,draw and loss. There is no place for less or more colours.'

        data = self.ca.WDL_Part()

        colorz = colors


        fig = go.Figure()

        if type=='bar':

            for key, value in data.items():
                for i in range(len(value)):
                    fig.add_trace(go.Bar(
                        x=[key],
                        y=[value[i]],
                        marker_color=colorz[i],
                        name=f'Index {i}'
                    ))

            fig.update_layout(
                title=f'{title}',
                xaxis_title=f'{xaxis_name}',
                yaxis_title=f'{yaxis_name}',
                barmode='stack',
                showlegend=False
            )


        ### todo : dodac emoji zamiast nazw coby wygladalo slicznie
        
        elif type=='pie':
            colors = ['green', 'gray', 'red']

           
            fig = make_subplots(rows=2, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}],
                                                    [{'type':'domain'}, {'type':'domain'}]],
                                subplot_titles=list(data.keys()))

            
            row, col = 1, 1
            for key, values in data.items():
                fig.add_trace(go.Pie(
                    labels=['Wins', 'Draws', 'Losses'],
                    values=values,
                    marker=dict(colors=colors),
                    name=key
                ), row=row, col=col)
                col += 1
                if col > 2:
                    col = 1
                    row += 1

            
            fig.update_layout(
                title_text=f"{title}",
                height=600,
                width=600,
            )


        st.plotly_chart(fig)



    def WDL_time(self, colors: list = ['green', 'gray', 'red'], title: str = 'Win/Draw/Loss stats by time', xaxis_name: str = 'Hour', yaxis_name: str = 'Number of games'):
        """
        Generates a bar chart showing the win, draw, and loss statistics by time.

        Parameters:
        - colors (list): A list of colors for the bars representing win, draw, and loss. Default is ['green', 'gray', 'red'].
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by time'.
        - xaxis_name (str): The label for the x-axis. Default is 'Hour'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.

        """

        assert len(colors) == 3, 'Bars contain colours for win, draw and loss. There is no place for less or more colours.'

        data = self.ca.WDL_Time()

        colorz = colors

        names = ['Win', 'Draw', 'Loss']

        fig = go.Figure()

        for key, value in data.items():
            for i in range(len(value)):
                fig.add_trace(go.Bar(
                    x=[key],
                    y=[value[i]],
                    marker_color=colorz[i],
                    name=f'{names[i]}'
                ))

        fig.update_layout(
            title=f'{title}',
            xaxis_title=f'{xaxis_name}',
            yaxis_title=f'{yaxis_name}',
            barmode='stack',
            showlegend=False
        )

        st.plotly_chart(fig)


    def WDL_accurate_elo(self, elo, colors: list = ['green', 'gray', 'red'], title: bool = True):
        """
        Calculates and displays the win/draw/loss statistics against players with a specific Elo rating range.

        Parameters:
        - elo (int): The Elo rating of the players to compare against.
        - colors (list): A list of colors to use for the metrics. Default is ['green', 'gray', 'red'].
        - title (bool): Whether to display the title. Default is True.

        """

        if title:
            st.header(f'Win/Draw/Loss stats against {elo} - {elo+99} rated players.') 
            
        wdl_acelo = self.ca.WDL_accurate_elo(elo)

        col1, col2, col3 = st.columns(3)

       
        with col1:
            st.metric(label="Wins", value=wdl_acelo[0], delta=wdl_acelo[0])

        with col2:
            st.metric(label="Draws", value=wdl_acelo[1], delta=wdl_acelo[1], delta_color='off')

        with col3:
            st.metric(label="Losses", value=wdl_acelo[2], delta=wdl_acelo[2], delta_color='inverse')

    
    def WDL_elo(self, plot='bar', colors: list = ['green', 'gray', 'red'], title: str = "Win/Draw/Loss stats by opponent's elo", xaxis_name: str = 'elo', yaxis_name: str = 'Number of games'):
        """
        Generates a bar plot or dataframe showing the win/draw/loss statistics by opponent's elo.

        Parameters:
        - plot (str): Specifies the type of plot to generate. Default is 'bar'. Options are 'bar' or 'df'.
        - colors (list): Specifies the colors for the bars in the plot. Default is ['green', 'gray', 'red'].
        - title (str): Specifies the title of the plot. Default is "Win/Draw/Loss stats by opponent's elo".
        - xaxis_name (str): Specifies the label for the x-axis. Default is 'elo'.
        - yaxis_name (str): Specifies the label for the y-axis. Default is 'Number of games'.

        Returns:
        - If plot='df', returns a pandas DataFrame containing the win/draw/loss statistics by opponent's elo.
        - If plot='bar', displays a bar plot using Plotly.

        Example usage:
        ca.WDL_elo(plot='bar', colors=['green', 'gray', 'red'], title="Win/Draw/Loss stats by opponent's elo", xaxis_name='elo', yaxis_name='Number of games')
        """

        data = self.ca.WDL_elo()

        idx = ['Win', 'Draw', 'Loss']


        if plot=='df':

            st.dataframe(data)

        elif plot=='bar':

            fig = go.Figure()

            colorz = colors

            for key, value in data.items():
                for i in range(len(value)):
                    fig.add_trace(go.Bar(
                        x=[key],
                        y=[value[i]],
                        marker_color=colorz[i],
                        name=f' {idx[i]}'
                    ))

            fig.update_layout(
                title=f'{title}',
                xaxis_title=f'{xaxis_name}',
                yaxis_title=f'{yaxis_name}',
                barmode='stack',
                showlegend=False
            )

            st.plotly_chart(fig)


  

    def WDL_time_control(self, title: str = 'Win/Draw/Loss stats by time control', plot_height: int = 700, plot_hole : float = 0.3):

        """
        Generates a pie chart visualization of the win/draw/loss statistics by time control.

        Parameters:
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by time control'.
        - plot_height (int): The height of the chart in pixels. Default is 700.
        - plot_hole (float): The size of the hole in the center of the pie chart. Default is 0.3.


        This function retrieves the win/draw/loss statistics by time control from the 'ca' object and generates a pie chart
        visualization using the Plotly library. Each time control category is represented by a separate pie chart.

        Example usage:
        ca = ChessAnalytics()
        ca.WDL_time_control(title='Win/Draw/Loss by Time Control', plot_height=800, plot_hole=0.4)
        """


        xyz = self.ca.WDL_time_control()

        fig = go.Figure()

        for i, (key, values) in enumerate(xyz.items()):
            fig.add_trace(go.Pie(
                labels=['Win', 'Draw', 'Loss'],
                values=values,
                name=key,
                hole=plot_hole,
            ).update(domain=dict(row=i // 2, column=i % 2), title=key))

        fig.update_layout(
            grid=dict(rows=2, columns=2),
            title=f'{title}',
            height=plot_height
        )

        st.plotly_chart(fig)



    def WDL_gametype(self, plot='pie', colors: list = ['green', 'gray', 'red'], title: str = "Win/Draw/Loss stats by game type", 
                     xaxis_name: str = 'Game type', yaxis_name: str = 'Number of games', plot_height: int = 700, plot_hole : float = 0.3):
        '''
        Generates a pie chart or dataframe showing the win/draw/loss statistics by game type.

        Params:
        - plot (str): The type of chart to display. Default is 'pie'. Options are 'pie', 'bar' or 'df'.
        - colors (list): The colors for the pie chart. Default is ['green', 'gray', 'red'].
        - title (str): The title of the chart. Default is 'Win/Draw/Loss stats by game type'.
        - xaxis_name (str): The label for the x-axis. Default is 'Game type'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.
        - plot_height (int): The height of the chart in pixels. Default is 700.
        - plot_hole (float): The size of the hole in the center of the pie chart. Default is 0.3.
        
        '''

        gmtp = self.ca.WDL_gametype()

        idx = ['Win', 'Draw', 'Loss']

        fig = go.Figure()

        if plot=='df':
            st.dataframe(gmtp)

        elif plot=='bar':

            fig = go.Figure()

            colorz = colors

            for key, value in gmtp.items():
                for i in range(len(value)):
                    fig.add_trace(go.Bar(
                        x=[key],
                        y=[value[i]],
                        marker_color=colorz[i],
                        name=f' {idx[i]}'
                    ))

            fig.update_layout(
                title=f'{title}',
                xaxis_title=f'{xaxis_name}',
                yaxis_title=f'{yaxis_name}',
                barmode='stack',
                showlegend=False
            )

            st.plotly_chart(fig)

        elif plot=='pie':

            for i, (key, values) in enumerate(gmtp.items()):
                fig.add_trace(go.Pie(
                    labels=['Win', 'Draw', 'Loss'],
                    values=values,
                    name=key,
                    hole=plot_hole,
                ).update(domain=dict(row=i // 2, column=i % 2), title=key))

            fig.update_layout(
                grid=dict(rows=2, columns=2),
                title=f'{title}',
                height=plot_height
            )

            st.plotly_chart(fig)
            




                                                        ##########          Time Related functions          ##########





    def count_games_date(self, type: str = 'bar', yaxis_name: str = 'Number of games', xaxis_name: str = 'Day', title: str = 'Number of games played by date') -> st.plotly_chart:
        """
        Generates a plotly chart showing the count of games played by date.

        Parameters:
        - type (str): The type of chart to display. Options are 'bar' (default) or 'scatter'.
        - yaxis_name (str): The label for the y-axis. Default is 'Number of games'.
        - xaxis_name (str): The label for the x-axis. Default is 'Day'.
        - title (str): The title of the chart. Default is 'Number of games played by date'.

        Returns:
        - None

        Example usage:
        Count_ofgames_Date(type='scatter', yaxis_name='Games Count', xaxis_name='Date', title='Games Count by Date')
        """
        fcj = self.ca.count_ofGames_Date()

        x, y = list(fcj.keys()), list(fcj.values())

        if type == 'scatter':
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))
        elif type == 'bar':
            fig = go.Figure(data=go.Bar(x=x, y=y))

        fig.update_layout(
            title=f'{title}',
            xaxis_title=f'{xaxis_name}',
            yaxis_title=f'{yaxis_name}'
        )

        st.plotly_chart(fig)


    
    def ranked_unranked(self, title: str = 'Ranked vs Unranked games'):
        '''
        Generates a pie chart showing the distribution of ranked and unranked games.

        Params:
        - title (str): The title of the chart. Default is 'Ranked vs Unranked games'.
        '''

        data = self.ca.ranked_unranked()

        if title:
            st.header(title)

        fig = go.Figure(data=[go.Pie(labels=list(data.keys()), values=list(data.values()))])

        st.plotly_chart(fig)




                                                        ################   PLAYER STATS RELATED FUNCTIONS     ################

    

    def bullet_progress(self, x_title : str='Number of games', y_title : str='Elo', plot_title: str ='Elo progress over time'):
        '''
        Generates a plot showing the progress of the player's elo progress in bullet games over time.

        Params:
        - x_title (str): The title of the x-axis. Default is 'Number of games'.
        - y_title (str): The title of the y-axis. Default is 'Elo'.
        - plot_title (str): The title of the plot. Default is 'Elo progress over time'.
        '''
        bulprog = self.ca.bullet_progress()

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=list(range(len(bulprog))),
            y=bulprog,
            mode='lines+markers'
        ))

        fig.update_layout(
            title=plot_title,
            xaxis_title=f'{x_title}',
            yaxis_title=f'{y_title}'
        )

        st.plotly_chart(fig)

    
    def blitz_progress(self, x_title : str ='Number of games', y_title : str ='Elo', plot_title : str ='Elo progress over time'):
        '''
        Generates a plot showing the progress of the player's elo progress in blitz games over time.

        Params:
        - x_title (str): The title of the x-axis. Default is 'Number of games'.
        - y_title (str): The title of the y-axis. Default is 'Elo'.
        - plot_title (str): The title of the plot. Default is 'Elo progress over time'.
        '''

        bulprog = self.ca.blitz_progress()

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=list(range(len(bulprog))),
            y=bulprog,
            mode='lines+markers'
        ))


        fig.update_layout(
            title=plot_title,
            xaxis_title=f'{x_title}',
            yaxis_title=f'{y_title}'
        )

        st.plotly_chart(fig)


    def rapid_progress(self, x_title : str ='Number of games', y_title : str ='Elo', plot_title : str ='Elo progress over time'):

        '''
        Generates a plot showing the progress of the player's elo progress in rapid games over time.

        Params:
        - x_title (str): The title of the x-axis. Default is 'Number of games'.
        - y_title (str): The title of the y-axis. Default is 'Elo'.
        - plot_title (str): The title of the plot. Default is 'Elo progress over time'.

        '''

        raprog = self.ca.blitz_progress()

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=list(range(len(raprog))),
            y=raprog,
            mode='lines+markers'
        ))


        fig.update_layout(
            title=plot_title,
            xaxis_title=f'{x_title}',
            yaxis_title=f'{y_title}'
        )

        st.plotly_chart(fig)

    
    def bullet_progress_date(self, title : str = 'Bullet elo progress by date', x_title : str = 'Date', y_title : str = 'Elo'):
        '''
        Generates a plot showing the progress of the player's elo progress in bullet games by date.

        Params:
        - title (str): The title of the plot. Default is 'Bullet elo progress by date'.
        - x_title (str): The title of the x-axis. Default is 'Date'.
        - y_title (str): The title of the y-axis. Default is 'Elo'.
        '''

        bulprog = self.ca.bullet_progress_date()

        klucze = list(sorted(bulprog.keys()))
        wartosci = list(bulprog.values())

        # Tworzenie wykresu
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=klucze, y=wartosci, mode='lines+markers', name='Wartości'))

        # Dodanie tytułów osi
        fig.update_layout(
            title=f'{title}',
            xaxis_title=f'{x_title}',
            yaxis_title=f'{y_title}'
        )

        st.plotly_chart(fig)


    def blitz_progress_date(self, title : str = 'Blitz elo progress by date', x_title : str = 'Date', y_title : str = 'Elo'):

        '''
        Generates a plot showing the progress of the player's elo progress in blitz games by date.

        Params:
        - title (str): The title of the plot. Default is 'Blitz elo progress by date'.
        - x_title (str): The title of the x-axis. Default is 'Date'.
        - y_title (str): The title of the y-axis. Default is 'Elo'.
        '''

        blzprog = self.ca.bullet_progress_date()

        klucze = list(sorted(blzprog.keys()))
        wartosci = list(blzprog.values())

        # Tworzenie wykresu
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=klucze, y=wartosci, mode='lines+markers', name='Wartości'))

        # Dodanie tytułów osi
        fig.update_layout(
            title=f'{title}',
            xaxis_title=f'{x_title}',
            yaxis_title=f'{y_title}'
        )

        st.plotly_chart(fig)


    def rapid_progress_date(self, title : str = 'Rapid elo progress by date', x_title : str = 'Date', y_title : str = 'Elo'):
        '''
        Generates a plot showing the progress of the player's elo progress in rapid games by date.

        Params:
        - title (str): The title of the plot. Default is 'Rapid elo progress by date'.
        - x_title (str): The title of the x-axis. Default is 'Date'.
        - y_title (str): The title of the y-axis. Default is 'Elo'.

        '''

        raprog = self.ca.bullet_progress_date()

        klucze = list(sorted(raprog.keys()))
        wartosci = list(raprog.values())

        # Tworzenie wykresu
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=klucze, y=wartosci, mode='lines+markers', name='Wartości'))

        # Dodanie tytułów osi
        fig.update_layout(
            title=f'{title}',
            xaxis_title=f'{x_title}',
            yaxis_title=f'{y_title}'
        )

        st.plotly_chart(fig)


    def bullet_progress_hour(self, title : str = 'Bullet elo progress by hour', x_title : str = 'Hour', y_title : str = 'Elo',
                             type : str = 'bar'):
        
        '''
        Generates a plot showing the progress of the player's elo progress in bullet games by hour of game.

        Params:
        - title (str): The title of the plot. Default is 'Bullet elo progress by hour'.
        - x_title (str): The title of the x-axis. Default is 'Hour'.
        - y_title (str): The title of the y-axis. Default is 'Elo'.
        - type (str): The type of plot to generate. Default is 'bar'. Options are 'bar' or 'line'.
        '''

        bph = self.ca.bullet_progress_hour()

        klucze = list(sorted(bph.keys()))
        wartosci = list(bph.values())

        if type=='line':

            # Tworzenie wykresu
            fig = go.Figure()

            fig.add_trace(go.Scatter(x=klucze, y=wartosci, mode='lines+markers', name='Wartości'))

            # Dodanie tytułów osi
            fig.update_layout(
                title=f'{title}',
                xaxis_title=f'{x_title}',
                yaxis_title=f'{y_title}'
            )

            st.plotly_chart(fig)

        elif type=='bar':

            fig = go.Figure()

            fig.add_trace(go.Bar(x=klucze, y=wartosci))

            # Dodanie tytułów osi
            fig.update_layout(
                title=f'{title}',
                xaxis_title=f'{x_title}',
                yaxis_title=f'{y_title}'
            )

            st.plotly_chart(fig)
    


    def blitz_progress_hour(self, title : str = 'Blitz elo progress by hour', x_title : str = 'Hour', y_title : str = 'Elo',
                             type : str = 'bar'):

        '''
        Generates a plot showing the progress of the player's elo progress in blitz games by hour of game.

        Params:
        - title (str): The title of the plot. Default is 'Blitz elo progress by hour'.
        - x_title (str): The title of the x-axis. Default is 'Hour'.
        - y_title (str): The title of the y-axis. Default is 'Elo'.
        - type (str): The type of plot to generate. Default is 'bar'. Options are 'bar' or 'line'.
        '''

        bph = self.ca.bullet_progress_hour()

        klucze = list(sorted(bph.keys()))
        wartosci = list(bph.values())

        if type=='line':

            fig = go.Figure()

            fig.add_trace(go.Scatter(x=klucze, y=wartosci, mode='lines+markers'))


            fig.update_layout(
                title=f'{title}',
                xaxis_title=f'{x_title}',
                yaxis_title=f'{y_title}'
            )

            st.plotly_chart(fig)

        elif type=='bar':

            fig = go.Figure()

            fig.add_trace(go.Bar(x=klucze, y=wartosci))

            fig.update_layout(
                title=f'{title}',
                xaxis_title=f'{x_title}',
                yaxis_title=f'{y_title}'
            )

            st.plotly_chart(fig)


    def rapid_progress_hour(self, title : str = 'Rapid elo progress by hour', x_title : str = 'Hour', y_title : str = 'Elo',
                             type : str = 'bar'):
        
        '''
        Generates a plot showing the progress of the player's elo progress in rapid games by hour of game.

        Params:
        - title (str): The title of the plot. Default is 'Rapid elo progress by hour'.
        - x_title (str): The title of the x-axis. Default is 'Hour'.
        - y_title (str): The title of the y-axis. Default is 'Elo'.
        - type (str): The type of plot to generate. Default is 'bar'. Options are 'bar' or 'line'.
        '''

        rph = self.ca.bullet_progress_hour()

        klucze, wartosci = list(sorted(rph.keys())),list(rph.values())

        if type=='line':


            fig = go.Figure()

            fig.add_trace(go.Scatter(x=klucze, y=wartosci, mode='lines+markers', name='Wartości'))


            fig.update_layout(
                title=f'{title}',
                xaxis_title=f'{x_title}',
                yaxis_title=f'{y_title}'
            )

            st.plotly_chart(fig)

        elif type=='bar':

            fig = go.Figure()

            fig.add_trace(go.Bar(x=klucze, y=wartosci))

       
            fig.update_layout(
                title=f'{title}',
                xaxis_title=f'{x_title}',
                yaxis_title=f'{y_title}'
            )

            st.plotly_chart(fig)




    def last_games_stats(self, title : str = 'Last games stats', amount : int = 20, plot_type : str = 'metric_flashy'):

        '''

        Generates a plot showing the statistics of the last games played.

        Params:
        - title (str): The title of the plot. Default is 'Last games stats'.
        - amount (int): The number of games to display. Default is 20.
        - plot_type (str): The type of plot to generate. Default is 'metric_flashy'. Options are 'df', 'metric_classy', 'metric_flashy', 'json'.
        
        '''

        i = 0
        d = {}

        with open (self.file, 'r') as plik:

            for line in plik:

                if '[Event ' in line:

                    i += 1

                    d[f'Game {i}'] = []

                    if 'bullet' in line:
                        d[f'Game {i}'].append('bullet')

                    elif 'blitz' in line:
                        d[f'Game {i}'].append('blitz')
                        
                    elif 'rapid' in line:
                        d[f'Game {i}'].append('rapid')

                    else:
                        d[f'Game {i}'].append('other')

                    while '[Site' not in line:
                        line = next(plik)

                    d[f'Game {i}'].append(line.split('"')[1].split('/')[3])

                    while '[Date ' not in line:
                        line = next(plik)

                    d[f'Game {i}'].append(line.split('"')[1])

                    while '[White ' not in line:
                        line = next(plik)

                    d[f'Game {i}'].append(line.split('"')[1])

                    if self.name in line:
                        zaw = 1

                    else:
                        zaw = 2

                    while '[Black ' not in line:
                        line = next(plik)

                    d[f'Game {i}'].append(line.split('"')[1])

                    while '[Result ' not in line:
                        line = next(plik)

                    if '1-0' in line:
                        if zaw==1:
                            d[f'Game {i}'].append('Win')
                        else:
                            d[f'Game {i}'].append('Loss')

                    elif '0-1' in line:
                        if zaw==1:
                            d[f'Game {i}'].append('Loss')
                        else:
                            d[f'Game {i}'].append('Win')

                    elif '1/2-1/2' in line:
                        d[f'Game {i}'].append('Draw')

                    while '[UTCTime ' not in line:
                        line = next(plik)

                    d[f'Game {i}'].append(line.split('"')[1])

                    while '[WhiteElo ' not in line:
                        line = next(plik)

                    d[f'Game {i}'].append(line.split('"')[1])

                    while '[BlackElo ' not in line:
                        line = next(plik)

                    d[f'Game {i}'].append(line.split('"')[1])

                    while '[Variant ' not in line:
                        line = next(plik)

                    d[f'Game {i}'].append(line.split('"')[1])

                    while '[TimeControl ' not in line:
                        line = next(plik)

                    d[f'Game {i}'].append(line.split('"')[1])


                    while '[Termination ' not in line:
                        line = next(plik)

                    d[f'Game {i}'].append(line.split('"')[1])

        d = dict(list(d.items())[:5])


        if plot_type=='df':

            df = pd.DataFrame(d).T

            st.write(df)
                    
        elif plot_type=='metric_classy':   # hood but classy kaz balagane

            vals = ['Game type', 'Game ID', 'Date', 'White player', 'Black player', 'Result', 'Time', 'White elo', 'Black elo', 'Variant', 'Time control', 'Termination']

            for game, values in d.items():

                st.header(game)
                num_columns = 3  # Liczba kolumn w rzędzie
                for i in range(0, len(values), num_columns):
                    cols = st.columns(num_columns)
                    for j in range(num_columns):
                        if i + j < len(values):
                            with cols[j]:
                                st.metric(label=f"{vals[i+j]}", value=values[i + j])
                                st.write('---------------------------------------------------------------------------------------')

        elif plot_type=='metric_flashy':

            ### emotes, lotta colours, bolds, italics, underlines, errytang you can imagine, best one of em all

            for val in d.values():

                if val[0] == 'bullet':
                    val[0] = '🔥'

                elif val[0] == 'blitz':
                    val[0] = '⚡'

                elif val[0] == 'rapid':
                    val[0] = '🐇'

                if val[5] == 'Win':
                    val[5] = '🟢'

                elif val[5] == 'Draw':
                    val[5] = '🟡'

                elif val[5] == 'Loss':
                    val[5] = '🔴'

            for game, value in d.items():

                st.header(game)
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.code(f"Game type: {value[0]}")
                    st.code(f"Game ID: {value[1]}")
                    st.code(f"Date: {value[2]}")
                    st.code(f"Time: {value[6]}")
                    st.write('---------------------------------------------------------------------------------------')

                with col2:
                    st.code(f"Black: {value[4]}")
                    st.code(f"White: {value[3]}")
                    st.code(f"Result: {value[5]}")
                    st.code(f"White elo: {value[7]}")
                    st.write('---------------------------------------------------------------------------------------')

                with col3:
                    st.code(f"Black elo: {value[8]}")
                    st.code(f"Variant: {value[9]}")
                    st.code(f"Time control: {value[10]}")
                    st.code(f"Termination: {value[11]}")
                    st.write('---------------------------------------------------------------------------------------')




        elif plot_type=='json':
            st.write(d)




                                                ##########          PIECE MOVES RELATED FUNCTIONS          ##########


# borrowed this func from my other project chesstools. feel free to have a look if ur looking for more heatmap/ board visualization related plots
    def heatmap1(self,counter, plot_colorscale='plasma', title='Moves heatmap', plot_showscale=False):
        '''
        Generates a heatmap visualisation of the squares where the moves were made.

        Params:
        - counter (dict): A dictionary containing the count of moves made on each square.
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Moves heatmap'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        '''
        nrows, ncols = 8, 8
        heatmap_matrix = np.zeros((nrows, ncols))

        for square, count in counter.items():
            col = ord(square[0].upper()) - ord('A')  
            row = 8 - int(square[1])  
            heatmap_matrix[row][col] = count

        fig = go.Figure(data=go.Heatmap(z=heatmap_matrix, colorscale=plot_colorscale, showscale=plot_showscale))

        fig.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=list(range(8)),
                ticktext=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
            ),
            yaxis=dict(
                tickmode='array',
                tickvals=list(range(8)),
                ticktext=list(range(1, 9)[::-1]),  
                autorange='reversed' 
            ),
            title=title,
            xaxis_title="",
            yaxis_title="",
            width=600,
            height=600
        )

        st.plotly_chart(fig)
    

# i thought about making one func for all the pieces and change it by a param, something like

    # def piece_moves(self, PIECE='ROOK/QUEEN/PAWN ETC')

# but for now i think it's better to have them separated as i may make some changes in chessanalytics soon.
# 
# 
# 
# anyway may change in the future tho   

    def rook_moves(self, plot_colorscale='Viridis', title='Rook moves heatmap', plot_showscale=True, opg=False):
        '''
        Generates a heatmap of the squares where the Rook moves were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Moves heatmap'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''

        rm = self.ca.rook_moves(only_player_games=opg)

        CAST.heatmap1(self,rm,plot_colorscale, title, plot_showscale) # funfact - i forgot to add self as 1 param and it took me 30 mins to figure out 
                                                                    # what's wrong. by this time i had rewritten both this func and heatmap1 ;)


    def queen_moves(self,plot_colorscale='Viridis', title='Queen moves heatmap', plot_showscale=True, opg=False):
        '''
        Generates a heatmap of the squares where the Queen moves were made.
        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Moves heatmap'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''
        qm = self.ca.queen_moves(only_player_games=opg)

        CAST.heatmap1(self,qm,plot_colorscale, title, plot_showscale)





    def bishop_moves(self, plot_colorscale='Viridis', title='Bishop moves heatmap', plot_showscale=True,opg=False):
        '''
        Generates a heatmap of the squares where the Bishop moves were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Moves heatmap'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''
        bm = self.ca.bishop_moves(only_player_games=opg)
        CAST.heatmap1(self,bm,plot_colorscale, title, plot_showscale)

    def knight_moves(self, plot_colorscale='Viridis', title='Knight moves heatmap', plot_showscale=True, opg=False):
        '''
        Generates a heatmap of the squares where the Knight moves were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Moves heatmap'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''
        km = self.ca.knight_moves(only_player_games=opg)

        CAST.heatmap1(self,km,plot_colorscale, title, plot_showscale)

    def king_moves(self, plot_colorscale='Viridis', title='King moves heatmap', plot_showscale=True, opg=False):
        '''
        Generates a heatmap of the squares where the King moves were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Moves heatmap'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''

        km = self.ca.king_moves(only_player_games=opg)

        CAST.heatmap1(self,km,plot_colorscale, title, plot_showscale)



    def squares_pawn_captures(self, plot_colorscale='Viridis', title='Squares with pawn captures heatmap', plot_showscale=True, opg=False):
        '''
        Generates a heatmap of the squares where the Pawn captures were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Moves heatmap'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''

        spc = self.ca.squares_with_Pawncaptures(only_player_games=opg)

        CAST.heatmap1(self,spc,plot_colorscale, title, plot_showscale)

    def squares_knight_captures(self, plot_colorscale='Viridis', title='Squares with knight captures heatmap', plot_showscale=True, opg=False):
        '''
        Generates a heatmap of the squares where the King captures were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Moves heatmap'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''
        skc = self.ca.squares_with_Knightcaptures(only_player_games=opg)

        CAST.heatmap1(self,skc,plot_colorscale, title, plot_showscale)

    def squares_bishop_captures(self, plot_colorscale='Viridis', title='Squares with bishop captures heatmap', plot_showscale=True, opg=False):
        '''
        Generates a heatmap of the squares where the Bishop captures were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Moves heatmap'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''

        sbc = self.ca.squares_with_Bishopcaptures(only_player_games=opg)

        CAST.heatmap1(self,sbc,plot_colorscale, title, plot_showscale)

    def squares_rook_captures(self, plot_colorscale='Viridis', title='Squares with rook captures heatmap', plot_showscale=True, opg=False):
        '''
        Generates a heatmap of the squares where the Rook captures were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Moves heatmap'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''

        src = self.ca.squares_with_Rookcaptures(only_player_moves=opg)

        CAST.heatmap1(self,src,plot_colorscale, title, plot_showscale)

    def squares_queen_captures(self, plot_colorscale='Viridis', title='Squares with queen captures heatmap', plot_showscale=True, opg=False):
        '''
        Generates a heatmap of the squares where the Queen captures were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Squares with queen captures heatmap'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''

        sqc = self.ca.squares_with_Queencaptures(only_player_games=opg)

        CAST.heatmap1(self,sqc,plot_colorscale, title, plot_showscale)

    def squares_king_captures(self, plot_colorscale='plasma', title='Squares with king captures heatmap', plot_showscale=True, opg=False):
        '''
        Generates a heatmap of the squares where the King captures were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'Viridis'.
        - title (str): The title of the heatmap. Default is 'Squares with king captures heatmap'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''

        skc = self.ca.squares_with_Kingcaptures(only_player_games=opg)

        CAST.heatmap1(self,skc, plot_colorscale, title, plot_showscale)    

    def squares_with_mates(self, plot_colorscale='plasma',title='Squares with checkmates',plot_showscale=True,opg=False):
        '''
        Generates a heatmap of the squares where the checkmates were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'plasma'.
        - title (str): The title of the heatmap. Default is 'Squares with checkmates'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''

        swm = self.ca.squares_with_mates(only_player_games=opg)

        CAST.heatmap1(self,swm, plot_colorscale, title, plot_showscale)

    def squares_with_checks(self, plot_colorscale='plasma',title='Squares with checks',plot_showscale=True,opg=False):
        '''
        Generates a heatmap of the squares where the checks were made.

        Params:
        - plot_colorscale (str): The colorscale to use for the heatmap. Default is 'plasma'.
        - title (str): The title of the heatmap. Default is 'Squares with checks'.
        - plot_showscale (bool): Whether to show the color scale. Default is True.
        - opg (bool): Whether to show only the player's games. Default is False.
        '''

        swc = self.ca.squares_with_checks(only_player_games=opg)
        CAST.heatmap1(self,swc, plot_colorscale, title, plot_showscale)

