from video_capturing import df
from bokeh.plotting import show,figure,output_file
from bokeh.models import HoverTool,ColumnDataSource

# convert date to string for tooltip
df["Start_string"]=df["start"].dt.strftime("%Y-%m-%d %H-%M-%S")
df["End_string"]=df["end"].dt.strftime("%Y-%m-%d %H-%M-%S")

#pass data source
cds= ColumnDataSource(df)

p=figure(x_axis_type="datetime", width= 500, height= 100, title="Motion Detection Graph",
         tools="pan, reset",sizing_mode="scale_width")
p.yaxis.minor_tick_line_color= None
p.ygrid[0].ticker.desired_num_ticks = 1

# hover
h=HoverTool(tooltips=[("start","@Start_string"),("end","@End_string")])
p.add_tools(h)

# output
output_file("Motion Graph.html")
show(p)
