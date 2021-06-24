import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import argparse

#grab data from filesystem in .csv format. Have two spreadsheet currenly --> source 
#of improvement is only use one and manipulate data in Python
data_path1 = "/Users/georgienahass/Desktop/WeissmanLab/sars-cov-2 saliva study/figure1B/fig1bD23_donor_1_handMod.csv"
data1 = pd.read_csv(data_path1)

parser = argparse.ArgumentParser()
    
parser.add_argument('-R', '--range', help = 'range of radal axis', type = int)

args = parser.parse_args()


def makeNightingaleRose(figName, dataFrame, R):
    figName = go.Figure()
    
    def addTraces(r, theta, name, markerColor):
        figName.add_trace(go.Barpolar(
            r = list(dataFrame[r]),
            theta = list(dataFrame[theta]),
            name = name,
            marker_color =markerColor,
            marker_line_color = 'black', 
            hoverinfo=['all'],
            opacity=.7
))
      #look into difference between add trace and add traces
   

    addTraces('passive drool', 'Param', 
            'Passive Drool', 'rgb(240,228,66)')

    addTraces('puresal', 'Param', 
            'Puresal', 'rgb(204,121,167)') 

    addTraces('orasure', 'Param', 
            'Orasure', 'rgb(86, 180, 233)')

    addTraces('supersal', 'Param', 
            'Supersal', 'rgb(230, 159, 0)')


  



    figName.update_layout(
        font_size=25,
        font_color='black',
        polar_angularaxis_rotation=22.5,
        width=900,
        height=900,
        showlegend = False,

        polar = dict(
                bgcolor = 'rgb(223,223,223)',
                angularaxis = 
                    dict(
                        linewidth = 3,
                        showline = True,
                        visible = True,
                        linecolor='rgb(0,0,0)',
                    ),
                radialaxis = 
                    dict(
                        showline = True,
                        visible = True,
                        linewidth = 2,
                        gridcolor = 'white',
                        linecolor= 'black',
                        gridwidth = 2,
                        categoryorder='category descending',
                        #COMMENT OUT IF DONT WANT LOG SCALE
                        type='log',
                        #CHANGE TO 0 TO SHOW TICK MARKS BETWEEN 0, 1, 10, 1000
                       # dtick=1,
                        minexponent=1,
                        ##SET STATIC RANGE OF RADIAL AXIS CHANGE THIS NUMBER TO 
                        ##SET RANGE. COMMENT OUT TO HAVE AUTORANGE ON
                        #range=[0,R],            
                )
            ),
        )
    return (figName)

print (args.range)
R = args.range
fig1 = makeNightingaleRose('fig', data1, R)
fig1.write_image('./imagesD23/IgDlog.pdf')
fig1.show()
# fig3.show()
# fig4.show()

