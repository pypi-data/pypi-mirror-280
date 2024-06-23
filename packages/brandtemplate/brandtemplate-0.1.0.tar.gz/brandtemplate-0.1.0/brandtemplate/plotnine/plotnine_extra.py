from itertools import cycle

def plotnine_titles(
    plotnine_fig,
    title=None,
    subtitle=None,
    caption=None,
    fontfamily=None,
    title_size=32,
    title_color='black',
    subtitle_size=20,
    subtitle_color='darkgrey',
    caption_size=15,
    caption_color='grey',
    draw_fig=True,
    **kwargs
    ):
  """
  Adds titles, subtitles and captions to a plotnine figure.
    For text (title, subtitle and caption) and the color and size for each element you can pass either a string or a array of strings. 
    If an array of strings is used for the text variable then arrays on the other variables are used to reformat each of the strings in the text array (e.g. color part of the text a different color).

  Args:
      plotnine_fig: The Plotnine figure object.
      title (str or array, optional): The title of the plot. Defaults to None.
      subtitle (str or array, optional): The subtitle of the plot. Defaults to None.
      caption (str or array, optional): The caption of the plot. Defaults to None. 
      fontfamily (str, optional): The font family to use for text elements. Defaults to None. 
      title_size (int or array, optional): The font size for the title. Defaults to 32. 
      title_color (str or array, optional): The color of the title text. Defaults to 'black'. 
      subtitle_size (int or array, optional): The font size for the subtitle. Defaults to 20. 
      subtitle_color (str or array, optional): The color of the subtitle text. Defaults to 'darkgrey'. 
      caption_size (int or array, optional): The font size for the caption. Defaults to 15. 
      caption_color (str or array, optional): The color of the caption text. Defaults to 'grey'. 
      draw_fig (bool, optional): You can only draw() the figure once. If passing in a plotnine figure directly then use True otherwise False. Defaults to True.
      **kwargs: Additional arguments for matplotlib.text().

  Returns:
      The customized Plotnine figure object.  
  """
  if draw_fig:
    plotnine_fig = plotnine_fig.draw()

  y_title = 1.02 if subtitle is None or subtitle == '' else 1.13
  if title is not None:
    plotnine_fig = plotnine_text(
      plotnine_fig=plotnine_fig, 
      text=title, 
      x=0, 
      y=y_title, 
      size=title_size, 
      color=title_color,
      ha='left', 
      va='bottom', 
      fontfamily=fontfamily,
      draw_fig=False,
      **kwargs
      )
    
  if subtitle is not None:
    plotnine_fig = plotnine_text(
      plotnine_fig=plotnine_fig,
      text=subtitle, 
      x=0, 
      y=1.02, 
      size=subtitle_size, 
      color=subtitle_color,
      ha='left', 
      va='bottom', 
      fontfamily=fontfamily, 
      draw_fig=False,
      **kwargs
      )

  if caption is not None:
    plotnine_fig = plotnine_text(
      plotnine_fig=plotnine_fig,
      text=caption, 
      x=0, 
      y=-0.05, 
      size=caption_size, 
      color=caption_color,
      ha='left', 
      va='top', 
      fontfamily=fontfamily, 
      draw_fig=False,
      **kwargs
      )

  return plotnine_fig

def plotnine_coloured_axis_labels(
    plotnine_fig,
    label_color_dict,
    default_label_color='#36454f',
    axis='X',  
    draw_fig=True      
    ):
  """
  Applies custom colors to axis labels of a Plotnine figure.

  Args:
      plotnine_fig (plotnine.ggplot): The Plotnine figure to which the colored axis labels will be applied.
      label_color_dict (dict): A dictionary mapping axis labels to their corresponding colors.
      default_label_color (str, optional): The default color for labels not specified in `label_color_dict`. Default is '#36454f'.
      axis (str, optional): The axis to which the label colors will be applied. Options are 'X' or 'Y'. Default is 'X'.
      draw_fig (bool, optional): You can only draw() the figure once. If passing in a plotnine figure directly then use True otherwise False. Defaults to True.
      
  Returns:
      plotnine.ggplot: The Plotnine figure with the colored axis labels.
  """

  if draw_fig:
    plotnine_fig = plotnine_fig.draw()
  
  for ax in plotnine_fig.axes:
    if 'X' in axis.upper():
      for l in ax.get_xticklabels():
        c = label_color_dict.get(l.get_text())
        if c is None:
          c = default_label_color
        l.set_color(c)

    if 'Y' in axis.upper():
      for l in ax.get_yticklabels():
        c = label_color_dict.get(l.get_text())
        if c is None:
          c = default_label_color
        l.set_color(c)
       
  return plotnine_fig

def plotnine_text(
    plotnine_fig,
    x,
    y,
    text,
    color='black',
    weight='regular',
    size=20,
    style='normal',
    va='bottom',
    ax_id=0,
    draw_fig=True,
    **kwargs
  ):
  """
  Adds text annotations to a Plotnine figure.

  For text, color, weight, size, style you can pass either a string or a array of strings. 
  If an array of strings is used for the text variable then arrays on the other variables are used to reformat each of the strings in the text array (e.g. color part of the text a different color).

  Args:
      plotnine_fig (plotnine.ggplot): The Plotnine figure to which the text will be added.
      x (float): The x-coordinate for the text position relative to the overall figure.
      y (float): The y-coordinate for the text position relative to the overall figure.
      text (str or array): The text string to be added to the plot. 
      color (str or array, optional): The color of the text. Default is 'black'.
      weight (str or array, optional): The font weight of the text. Options are 'light', 'normal', 'bold', etc. Default is 'regular'.
      size (int or array, optional): The size of the text in points. Default is 20.
      style (str or array, optional): The font style of the text. Options are 'normal', 'italic', etc. Default is 'normal'.
      va (str, optional): The vertical alignment of the text. Options are 'top', 'bottom', 'center', etc. Default is 'bottom'.
      ax_id (int, optional): The index of the axis on which to draw the text (if multiple axes are present). Default is 0.
      draw_fig (bool, optional): You can only draw() the figure once. If passing in a plotnine figure directly then use True otherwise False. Default is True.
      **kwargs: Additional arguments for matplotlib.text().

  Returns:
      plotnine.ggplot: The Plotnine figure with the added text annotation.
  """
  if draw_fig:
    plotnine_fig = plotnine_fig.draw()

  ax = plotnine_fig.axes[ax_id]

  #convert to lists if not already so can iterate through
  text = text if isinstance(text, list) else [text]
  color = color if isinstance(color, list) else [color]
  weight = weight if isinstance(weight, list) else [weight]
  size = size if isinstance(size, list) else [size]
  style = style if isinstance(style, list) else [style]

  for idx, (t, c, w, sz, st) in enumerate(zip(text, cycle(color), cycle(weight), cycle(size), cycle(style))):
    if idx == 0:
      text = plotnine_fig.text(s=t, x=x, y=y, fontweight=w, size=sz, color=c, style=st, va=va, **kwargs)
    else:
      text = ax.annotate(text=t, xycoords=text, xy=(1,0), fontweight=w, size=sz, color=c, style=st, va=va, **kwargs)
  
  return plotnine_fig