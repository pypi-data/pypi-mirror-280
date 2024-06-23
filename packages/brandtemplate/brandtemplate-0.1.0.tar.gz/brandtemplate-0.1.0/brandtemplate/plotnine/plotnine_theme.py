from plotnine import theme_bw, theme

from plotnine.themes.elements import (
  element_blank,
  element_line,
  element_rect,
  element_text
)

BASE_FONT_SIZE=15
BASE_FAMILY='Inter'
TITLE_SIZE=32
SUBTITLE_SIZE=20
CAPTION_SIZE=15
BASE_GRAPH_COLOR='#36454f'
GRIDLINES_COLOR='#ededed'
TITLE_COLOR='#36454f'
SUBTITLE_COLOR='#5E6A72'
CAPTION_COLOR='#5E6A72'
LEGEND_POSITION='bottom'
LEGEND_DIRECTION='horizontal'


class brandtemplate_plotnine_theme(theme_bw):
  """
  A custom theme for plotnine.

  Args:
      base_size (int, optional): The base font size for the plot. Defaults to 15.
      base_family (str, optional): The base font family for the plot. Defaults to 'Inter'.
      gridlines (str, optional): Determines which gridlines to display. Values are 'X', 'Y' or 'XY'. Defaults to 'X'.
      axis_title (str, optional): Determins the title for the axes to display. Values are 'X', 'Y' or 'XY'. Defaults to ''.
      axis_line (str, optional): Determines if axis lines are displayed. Values are 'X', 'Y' or 'XY'. Defaults to 'X'.
      axis_start_zero (str, optional): Recolors the axis if it doesn't start at zero. Values are 'X', 'Y' or 'XY'. Defaults to 'X'.
      title_size (int, optional): Font size for the plot title. Defaults to 32.
      subtitle_size (int, optional): Font size for the plot subtitle. Defaults to 20.
      caption_size (int, optional): Font size for the plot caption. Defaults to 15.

  Returns:
      None
  """

  def __init__(
      self, 
      base_size=BASE_FONT_SIZE, 
      base_family=BASE_FAMILY,
      gridlines='X',
      axis_title='',
      axis_line='X',
      axis_start_zero='X',
      title_size=TITLE_SIZE,
      subtitle_size=SUBTITLE_SIZE,
      caption_size=CAPTION_SIZE
      ):
    super().__init__(base_size, base_family)
    self += theme(
      line=element_rect(color=BASE_GRAPH_COLOR),
      rect=element_rect(fill='white', color='black'),
      text=element_text(color=BASE_GRAPH_COLOR, fontweight='regular'), 
      title=element_text(color=BASE_GRAPH_COLOR),
      
      plot_background=element_rect(color='white', fill='white'),
      strip_background=element_rect(fill='white'),

      plot_title=element_text(color=TITLE_COLOR, fontweight='bold', size=title_size),
      plot_subtitle=element_text(color=SUBTITLE_COLOR, fontweight='regular', size=subtitle_size),
      plot_caption=element_text(color=CAPTION_COLOR, fontweight='regular', size=caption_size),

      plot_margin=0, #check this

      panel_border=element_blank(),
      panel_grid_major=element_line(color = GRIDLINES_COLOR),
      panel_grid_major_x=element_line(color=GRIDLINES_COLOR) if 'X' in gridlines.upper() else element_blank(),
      panel_grid_major_y=element_line(color=GRIDLINES_COLOR) if 'Y' in gridlines.upper() else element_blank(),
      panel_grid_minor=element_blank(),

      axis_title_x=element_text() if 'X' in axis_title.upper() else element_blank(),
      axis_title_y=element_text() if 'Y' in axis_title.upper() else element_blank(),
      axis_ticks=element_blank(),
      axis_line_x=element_blank if 'X' not in axis_line.upper() else element_line() if 'X' in axis_start_zero.upper() else element_line(color=GRIDLINES_COLOR),
      axis_line_y=element_blank if 'Y' not in axis_line.upper() else element_line() if 'Y' in axis_start_zero.upper() else element_line(color=GRIDLINES_COLOR),

      legend_background=element_blank(),
      legend_position=LEGEND_POSITION,
      legend_box='vertical',
      legend_direction=LEGEND_DIRECTION
      )