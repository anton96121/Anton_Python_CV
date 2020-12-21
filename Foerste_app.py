import pandas as pd
from dash.dependencies import Input,Output,State
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import dash
import plotly.offline as pyoff
import plotly.plotly as py
import plotly.graph_objs as go
import base64
import html5lib
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

exp=dict(PFA=pd.date_range('2020-09-01','2021-01-01'),
        DTU_Teacher=pd.date_range('2018-09-01','2019-06-30'),
        Swim_Coach=pd.date_range('2014-06-01','2016-10-30'),
        Teacher=pd.date_range('2016-10-29','2016-12-23'),
        )

pri_edu=dict(BSc_DTU=pd.date_range('2017-09-01','2020-07-01'),
        BSc_KU=pd.date_range('2020-09-01','2020-12-17'),
        Exchange_NTU=pd.date_range('2019-08-04','2020-01-01'),
        Gymnasium = pd.date_range('2013-08-04','2016-01-07'),
        Danmark = pd.date_range('2017-01-01','2017-06-01'),
            )


expDict = [
           dict(date='Sep 2020 - Present',name='Student Assistant at Finance & Actuarial Department @PFA',skills='Programming, Applied Statistics',description='This is my present job where I work in the department of risk and profitability. I work in the team associated with risk and injury reporting.'),
          dict(date='Sep 2018 - Jun 2019',name='Teaching assistant in Advanced Engineering Mathematics 1 @DTU',skills='Mathematics, Communication, Teaching',description='I was teaching a large 20 ECTS-points large course. I taught linear algebra, complex numbers, differential equation, basic vector analysis and basic extrema analysis.'),
           dict(date='Nov 2016 - Dec 2016',name = 'Math Teacher', skills='Teaching, Cultural Differences', description = 'I teached mathematics for two months at an orphanage in Uganda'),
    dict(date='Jun 2014 - Oct 2016',name='Swin Choach @SKS',skills='Teaching, Communication',description='I teached all ages and skill levels including 6 years and no experience, competetive teams and adult fitness swimming.'),
         
        ]

priEduDict = [
          dict(date='Feb 2021 - Jun 2023',name='MSc Mathematical Modeling and Computing @DTU',skills='Advanced Statistics, Advanced Mathematics, Finance, Advanced Computing, Advanced Machine Learning',description='I will have my main focuse on stochastic modeling. Besides that I will be taking courses in machine learning, finance and computing.'),
          dict(date='Sep 2020 - Dec 2020',name='BSc Actuarial Mathematics @KU',skills='Theoretical foundation', description='I wanted to see if theoretical mathematics was something for me but it was to theoretical and I feelt a lack of focus on implementation.'),
    dict(date='Aug 2019 - Jan 2020',name='Study Abroad, Nanyang Technological University, Singapore @NTU',skills='Algorithms, Mathematics, Machine Learning',description='Studied half a year at Nanyang Technological University in Singapore. Here I had courses in mathematics and computer science.'),      
    dict(date='Sep 2017 - Jun 2020',name='BSc General Engineering, Cyber Systems @DTU',skills='Programming, Mathematics, Statistics, Machine Learning',description='It is a bachelor in in between mathematics and computer science.'),
          dict(date='Jan 2017 - Jun 2017',name='Ordinary Seaman, Skoleskibet Danmark, MARTEC', skills = 'Team Work Under Stress', description = 'I took the introductory courses but I have not taken the internship in the industry afterwards.'),
        dict(date='Aug 2013 - Jun 2016',name='High School, Sønderborg Statsskole @SSS', skills = 'General Education', description = 'I went to a STX in Sønderborg where I has mathematics and chemistry on high level'),
          
          ]

listOfExp = [pd.Series(index=exp.get(j), name=j, data=np.ones(len(exp.get(j)))*1.15) for j in exp.keys()]
listOfPriEdu = [pd.Series(index=pri_edu.get(j), name=j, data=np.ones(len(pri_edu.get(j)))*1.1) for j in pri_edu.keys()]

dataExp = pd.concat(listOfExp, axis=1).stack().reset_index()
dataPriEdu = pd.concat(listOfPriEdu, axis=1).stack().reset_index()

dataExp.columns = ['dates','names','value']
dataPriEdu.columns = ['dates','names','value']

trace_exp = go.Scatter(
    x=dataExp['dates'],
    y=dataExp['value'],
    text = dataExp['names'],
    mode='markers',
    marker = dict(color='salmon'),
    opacity = 0.8,
    name = 'Experience',
    hoverinfo='text+name',
    connectgaps=False,
    fill='none')

trace_pri_edu = go.Scatter(
    x=dataPriEdu['dates'],
    y=dataPriEdu['value'],
    text = dataPriEdu['names'],
    mode='markers',
    marker = dict(color='paleturquoise'),
    opacity = 0.8,
    name = 'Formal Education',
    hoverinfo='text+name',
    connectgaps=False,
    fill='none')



data = [trace_exp, trace_pri_edu]



layout = go.Layout(
    title='<b>Timeline Overview</b>',
    hovermode='x',
    legend=dict(x=0.7,
                y=1.2,
                orientation='h'),
    xaxis=dict(
        rangeselector=dict(bgcolor='black',
                           activecolor='red',
                           font=dict(color='white'),
                           y=1.1,
            buttons=list([
                dict(count=6,
                     label='6months',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                     label='1year',
                     step='year',
                     stepmode='backward'),
                dict(count=2,
                     label='2years',
                     step='year',
                     stepmode='backward'),
                dict(count=9,
                     label='9years',
                     step='year',
                     stepmode='backward')
            ])
        ),
#         rangeslider=dict(
#             visible = True
#         ),
        type='date',
        side='top'
    ),
    yaxis=dict(visible=False,
              range=[0.98,1.18]
              )
)

initial_range = [
    '2017-06-01', '2021-01-01'
]

fig = dict(data=data, layout=layout)
fig['layout']['xaxis'].update(range=initial_range)

figure=dict(data=[go.Table(
                              columnorder = [1,2,3,4],
                              columnwidth = [43,60,50,207],
                              header = dict(
                                            values = [['<b>DATE</b>'],['<b>NAME</b>'],['<b>SKILLS</b>'],['<b>DESCRIPTION</b>']],
                                            line = dict(color = 'black'),
                                            fill = dict(color = 'white'),
                                            align = ['left','center'],
                                            font = dict(color = 'black', size = 12),
                                            height = 13
                                            ),
                              cells = dict(
                                        values = [[i['date'] for i in expDict],['<em>'+i['name']+'</em>' for i in expDict],[i['skills'] for i in expDict],[i['description'] for i in expDict]],
                                        line = dict(color = ['#506784']), #, width=3
#                                         fill = dict(color = [['red','blue','green'], 'white']),
                                        align = ['left'],
                                        font = dict(color = ['black'], size = 13),
                                        height = 20
                                          )
                                        )
                              ]
                            ,layout=go.Layout(margin=dict(l=15, b=0, t=0, r=15))
                            )

app = dash.Dash()
server = app.server
app.config['suppress_callback_exceptions'] = True
# app.config.include_asset_files = True
# app.config.assets_folder = '/Users/joaosoares/PycharmProjects/untitled/assets'

# default values
# app.config.assets_folder = 'assets'     # The path to the assets folder.
# app.config.include_asset_files = True   # Include the files in the asset folder
# app.config.assets_external_path = ''    # The external prefix if serve_locally == False
# app.config.assets_url_path = '/assets'  # the local url prefix ie `/assets/*.js`

app.css.append_css({
   'external_url': (
       'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
       'https://use.fontawesome.com/releases/v5.5.0/css/all.css'
   )
})

#TABS
app.layout = html.Div([
    dcc.Tabs(id="tabs", value='basicInfo', children=[
        dcc.Tab(label='Introduction', value='basicInfo', style=dict(fontWeight=800)),
        dcc.Tab(label='Experience and Learning', value='XP', style=dict(fontWeight=800)),
        dcc.Tab(label='Skills', value='Skills', style=dict(fontWeight=800))
    ]),
    html.Div(id='tabs-content')
                      ], style=dict(marginBottom=0, paddingBottom=0)
                     )

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'basicInfo':
        return html.Div([
                        html.Div([
                                  html.Div([html.Img(src='https://www.dropbox.com/s/tewrjollx6up3lr/beskar2.jpg?raw=1',
                                                     style=dict(width='200px', height='270px')
                                                  ),
                                            html.Div([
                                                      html.H4(id='name',
                                                              children=' Anton Ruby Larsen'
                                                             ),
                                                      html.Div([html.Span([html.I(className='fas fa-at'),
                                                                           html.A('anton96121@gmail.com',href='mailto:anton96121@gmail.com'                                                                               )
                                                                          ],className='d-block'
                                                                         ),
                                                                html.Span([html.I(className='fas fa-mobile-alt'),
                                                                           html.P(' +4527622273',
                                                                                   className='font-weight-normal d-inline'
                                                                                  )
                                                                          ],className='py-2 m-0 d-block'
                                                                         ),
                                                                html.Span([html.I(className='fab fa-linkedin'),
                                                                           html.A('LinkedIn',href='https://www.linkedin.com/in/anton-ruby-larsen-458497ba/'
                                                                                  )
                                                                          ],className='d-block'
                                                                         )])
                                                      ],style=dict(padding=10)),
                                                              
                                           ], className='row col-5 p-4 mt-2',style=dict(padding=10)
                                          ),
                                  html.Div([
                                            html.H4('Summary',
                                                    className='display-6 col-9 mb-3 border-bottom pb-1'),
                                            html.Div(html.P(['I am finished with my bachelor in Cyber Systems from DTU this summer where the focus have been on statistics, machine learning, applied mathematics and programming.',html.Br(),
                                                            ' At my 3rd and 4th semester I taught mathematics as an assistant teacher at the course Advanced Engineering Mathematics 1. I spend my 5th semester abroad in Singapore where I studied at Nanyang Technological University and this semester, I have written my bachelor thesis. It focused on the topic of intrusion detection in network traffic by use of machine learning.'])
                                                     )
                                           ], className='row col-7 align-content-start pt-4 ml-2 pl-5 pr-0')
                                 ], className='row mt-5 bg-light rounded pt-2'),
                        html.Div([
                                 html.Div([
                                     html.H4(['About This Application']),
                                     html.P(['I built this application as a demonstration of my skills using Python for visualization.',
                                             ' The application is build in Dash by Plotly and created in an Anaconda enviroment.', 
                                             ' I have also experience with Shiny by RStudio but in the job advertisement you demanded experince with Python and Anaconda so this is the reason behind the choice of platform.'])
                                          ], style=dict(lineHeight=1.6, padding = 10)
                                         )
                                 ], className='row mt-5 bg-light rounded'
                                )
                     ],className='container'
                    )
    elif tab == 'XP':
        return html.Div([
                        html.Div([
                                dcc.Graph(id='exp',
                                          figure=fig,
                                          config=dict(displayModeBar=False)
                                         )
                                ],
                                style=dict(height='40vh', width='100vw'),
                                className = 'col-12'
                               ),
                        html.Div([dcc.RadioItems(id='table-options',
                                                 options=[dict(value=1, label=' Experience'),
                                                          dict(value=2, label=' Formal Education')
                                                         ],
                                                 labelStyle=dict(marginRight=10,
                                                                 fontWeight='bold'
                                                                ),
                                                 value=1,
                                                 className='btn btn-primary btn-sm'
                                                )
                                 ]
                                ,className='col-4 mx-auto'
                                ),
                        html.Div([
                                dcc.Graph(id='table',
                                          figure=figure,
                                          config=dict(displayModeBar=False)
                                         )
                                ],className='col-12 pt-1 pl-5 pr-3 mt-1'
                               )
                        ]
                       )
    elif tab == 'Skills':
        return html.Div([
                        html.Div([
                                        html.Div(
                                                 [
                                            html.Button('Relevant Competences',
                                                        id='data-skills',
                                                        n_clicks_timestamp=-1,
                                                       style=dict(display='block', height='60px', width='200px')),
                                            html.Button('Programming Languages', 
                                                        id='code-skills',
                                                        n_clicks_timestamp =-1,
                                                       style=dict(display='block', height='60px', width='200px')),
                                            html.Button('Spoken Languages',
                                                        id='biz-skills',
                                                        n_clicks_timestamp=-1,
                                                       style=dict(display='block', height='60px', width='200px'))
                                                 ]
                                                )
                                            ],
                                               className='row-8 col-3 d-flex justify-content-end', style = dict(padding = 30)
                                ),
                        html.Div([
                                dcc.Graph(id='my-skills',
                                         figure=dataSkills,
                                         config=dict(displayModeBar=False)
                                        )
                                 ],
                                    className='col-9')
                        ], className='row mx-auto justify-content-center'
                       )

dataSkills=dict(data=[go.Scatterpolar(
                          r = [35, 40, 38, 10, 25, 35, 35],
                          theta = ['Statistics', 'Machine<br>Learning', "Mathematics", "Economics", "Agile<br>Development", "Programming", 'Statistics'],
                          fill = 'toself',
                          line = dict(color='salmon'),
                          hoverinfo='none'
                                            )
                           ],

              layout= go.Layout(xaxis=dict(visible=False),
                                yaxis=dict(visible=False),
                                title = 'Relevant Competences',
                                font=dict(size=14),
                                polar = dict(
                                            radialaxis = dict(
                                                              visible = True,
                                                              range = [0, 50],
                                                              tickvals=[15,25,35],
                                                              ticktext=['Basic','Intermediate','Advanced'],
                                                              tickmode='array',
                                                              tickangle=25,
                                                              tickfont=dict(
                                                                    family='Arial',
                                                                    size=13,
                                                                    color='#acb3bf'
                                                                            )
                                                                )
                                              ),
                                showlegend = False,
                                height=700,
                                width=700
                                )
             )

codeSkills=dict(data=[go.Scatterpolar(
                          r = [12, 25, 30, 35, 6, 6, 30,6, 12],
                          theta = ['SAS','F Sharp', 'Python', 'R', 'MatLab', 'SQL', 'Java','C++', 'SAS'],
                          fill = 'toself',
                          line = dict(color='paleturquoise'),
                          hoverinfo='none'
                                            )
                           ],

              layout= go.Layout(xaxis=dict(visible=False),
                                yaxis=dict(visible=False),
                                title = 'Programming Languages',
                                font=dict(size=14),
                                polar = dict(
                                            radialaxis = dict(
                                                              visible = True,
                                                              range = [0, 40],
                                                              tickvals=[10,20,30],
                                                              ticktext=['Basic','Intermediate','Advanced'],
                                                              tickmode='array',
                                                              tickangle=25,
                                                              tickfont=dict(
                                                                    family='Arial',
                                                                    size=13,
                                                                    color='#acb3bf'
                                                                            )
                                                                )
                                              ),
                                showlegend = False,
                                height=700,
                                width=700
                                )
             )

bizSkills=dict(data=[go.Scatterpolar(
                          r = [10, 45, 50, 10],
                          theta = ['German', 'English', 'Danish', 'German'],
                          fill = 'toself',
                          line = dict(color='goldenrod'),
                          hoverinfo='none'
                                            )
                           ],

              layout= go.Layout(xaxis=dict(visible=False),
                                yaxis=dict(visible=False),
                                font=dict(size=14),
                                title = 'Spoken Languages',
                                polar = dict(
                                            radialaxis = dict(
                                                              visible = True,
                                                              range = [0, 50],
                                                              tickvals=[15,25,35],
                                                              ticktext=['Basic','Intermediate','Advanced'],
                                                              tickmode='array',
                                                              tickangle=25,
                                                              tickfont=dict(
                                                                    family='Arial',
                                                                    size=13,
                                                                    color='#acb3bf'
                                                                            )
                                                                )
                                              ),
                                showlegend = False,
                                height=700,
                                width=700
                                )
             )



@app.callback(
    Output('table','figure'),
    [Input('table-options','value')])
def display_table(value):
    if value == 1:
        tableData = expDict
    elif value == 2:
        tableData = priEduDict
    figure=dict(data=[go.Table(
                              columnorder = [1,2,3,4],
                              columnwidth = [43,60,50,207],
                              header = dict(
                                            values = [['<b>DATE</b>'],['<b>NAME</b>'],['<b>SKILLS</b>'],['<b>DESCRIPTION</b>']],
                                            line = dict(color = 'black'),
                                            fill = dict(color = 'white'),
                                            align = ['left','center'],
                                            font = dict(color = 'black', size = 12),
                                            height = 13
                                            ),
                              cells = dict(
                                        values = [[i['date'] for i in tableData],['<em>'+i['name']+'</em>' for i in tableData],[i['skills'] for i in tableData],[i['description'] for i in tableData]],
                                        line = dict(color = ['#506784']), #, width=3
                                        align = ['left'],
                                        font = dict(color = ['black'], size = 13),
                                        height = 20
                                          )
                                        )
                              ]
                            ,layout=go.Layout(margin=dict(l=15, b=0, t=0, r=15))
                            )
    return figure
    
    
@app.callback(Output('my-skills','figure'),
              [Input('data-skills', 'n_clicks_timestamp'),
              Input('code-skills', 'n_clicks_timestamp'),
              Input('biz-skills', 'n_clicks_timestamp')])
def displayClick(btn1, btn2, btn3):
    print(btn1)
    print(btn2)
    print(btn3)

    if btn1==-1 and btn2==-1 and btn3==-1:
        return dataSkills
    elif btn1>btn2 and btn1>btn3:
        return dataSkills
    elif btn2>btn1 and btn2>btn3:
        return codeSkills
    else:
        return bizSkills
    return dataSkills





if __name__ == '__main__':
    app.run_server()