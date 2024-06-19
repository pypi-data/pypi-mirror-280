from typing import List, Optional, Dict, Iterable
import aspose.pycore
import aspose.pydrawing
import aspose.cellsgridjs
import aspose.cellsgridjs.chart

class AreaObject:
    '''internal use'''
    
    @property
    def color(self) -> str:
        '''color'''
        ...
    
    @color.setter
    def color(self, value : str):
        '''color'''
        ...
    
    @property
    def _color(self) -> str:
        '''color'''
        ...
    
    @_color.setter
    def _color(self, value : str):
        '''color'''
        ...
    
    ...

class AxisLineObject:
    '''internal use'''
    
    @property
    def color(self) -> str:
        '''color'''
        ...
    
    @color.setter
    def color(self, value : str):
        '''color'''
        ...
    
    @property
    def weight_px(self) -> float:
        ...
    
    @weight_px.setter
    def weight_px(self, value : float):
        ...
    
    @property
    def style(self) -> str:
        '''style'''
        ...
    
    @style.setter
    def style(self, value : str):
        '''style'''
        ...
    
    @property
    def _color(self) -> str:
        ...
    
    @_color.setter
    def _color(self, value : str):
        ...
    
    @property
    def _weight_px(self) -> float:
        ...
    
    @_weight_px.setter
    def _weight_px(self, value : float):
        ...
    
    @property
    def _style(self) -> str:
        ...
    
    @_style.setter
    def _style(self, value : str):
        ...
    
    ...

class AxisObject:
    '''internal use'''
    
    @property
    def is_visible(self) -> bool:
        ...
    
    @is_visible.setter
    def is_visible(self, value : bool):
        ...
    
    @property
    def title(self) -> aspose.cellsgridjs.TitleObject:
        '''title'''
        ...
    
    @title.setter
    def title(self, value : aspose.cellsgridjs.TitleObject):
        '''title'''
        ...
    
    @property
    def category_data(self) -> List[aspose.cellsgridjs.CellData]:
        ...
    
    @category_data.setter
    def category_data(self, value : List[aspose.cellsgridjs.CellData]):
        ...
    
    @property
    def axis_line(self) -> aspose.cellsgridjs.AxisLineObject:
        ...
    
    @axis_line.setter
    def axis_line(self, value : aspose.cellsgridjs.AxisLineObject):
        ...
    
    @property
    def _is_visible(self) -> bool:
        ...
    
    @_is_visible.setter
    def _is_visible(self, value : bool):
        ...
    
    @property
    def _title(self) -> aspose.cellsgridjs.TitleObject:
        ...
    
    @_title.setter
    def _title(self, value : aspose.cellsgridjs.TitleObject):
        ...
    
    @property
    def _category_data(self) -> List[aspose.cellsgridjs.CellData]:
        ...
    
    @_category_data.setter
    def _category_data(self, value : List[aspose.cellsgridjs.CellData]):
        ...
    
    @property
    def _axis_line(self) -> aspose.cellsgridjs.AxisLineObject:
        ...
    
    @_axis_line.setter
    def _axis_line(self, value : aspose.cellsgridjs.AxisLineObject):
        ...
    
    ...

class BackgroundColorObject:
    '''internal use'''
    
    ...

class BorderObject:
    '''internal use'''
    
    @property
    def weight_px(self) -> float:
        ...
    
    @weight_px.setter
    def weight_px(self, value : float):
        ...
    
    @property
    def color(self) -> str:
        '''color'''
        ...
    
    @color.setter
    def color(self, value : str):
        '''color'''
        ...
    
    @property
    def style(self) -> str:
        '''style'''
        ...
    
    @style.setter
    def style(self, value : str):
        '''style'''
        ...
    
    @property
    def _weight_px(self) -> float:
        ...
    
    @_weight_px.setter
    def _weight_px(self, value : float):
        ...
    
    @property
    def _color(self) -> str:
        ...
    
    @_color.setter
    def _color(self, value : str):
        ...
    
    @property
    def _style(self) -> str:
        ...
    
    @_style.setter
    def _style(self, value : str):
        ...
    
    ...

class CellData:
    '''internal use'''
    
    @property
    def name(self) -> str:
        '''name'''
        ...
    
    @name.setter
    def name(self, value : str):
        '''name'''
        ...
    
    @property
    def sheet_name(self) -> str:
        ...
    
    @sheet_name.setter
    def sheet_name(self, value : str):
        ...
    
    @property
    def sheet_index(self) -> int:
        ...
    
    @sheet_index.setter
    def sheet_index(self, value : int):
        ...
    
    @property
    def _name(self) -> str:
        ...
    
    @_name.setter
    def _name(self, value : str):
        ...
    
    @property
    def _sheet_name(self) -> str:
        ...
    
    @_sheet_name.setter
    def _sheet_name(self, value : str):
        ...
    
    @property
    def _sheet_index(self) -> int:
        ...
    
    @_sheet_index.setter
    def _sheet_index(self, value : int):
        ...
    
    ...

class ChartDimensionObject:
    '''internal use'''
    
    @property
    def width(self) -> float:
        '''width'''
        ...
    
    @width.setter
    def width(self, value : float):
        '''width'''
        ...
    
    @property
    def height(self) -> float:
        '''height'''
        ...
    
    @height.setter
    def height(self, value : float):
        '''height'''
        ...
    
    @property
    def x(self) -> float:
        '''x'''
        ...
    
    @x.setter
    def x(self, value : float):
        '''x'''
        ...
    
    @property
    def y(self) -> float:
        '''y'''
        ...
    
    @y.setter
    def y(self, value : float):
        '''y'''
        ...
    
    @property
    def upper_left_column(self) -> int:
        ...
    
    @upper_left_column.setter
    def upper_left_column(self, value : int):
        ...
    
    @property
    def upper_left_row(self) -> int:
        ...
    
    @upper_left_row.setter
    def upper_left_row(self, value : int):
        ...
    
    @property
    def _width(self) -> float:
        ...
    
    @_width.setter
    def _width(self, value : float):
        ...
    
    @property
    def _height(self) -> float:
        ...
    
    @_height.setter
    def _height(self, value : float):
        ...
    
    @property
    def _x(self) -> float:
        ...
    
    @_x.setter
    def _x(self, value : float):
        ...
    
    @property
    def _y(self) -> float:
        ...
    
    @_y.setter
    def _y(self, value : float):
        ...
    
    @property
    def _upper_left_column(self) -> int:
        ...
    
    @_upper_left_column.setter
    def _upper_left_column(self, value : int):
        ...
    
    @property
    def _upper_left_row(self) -> int:
        ...
    
    @_upper_left_row.setter
    def _upper_left_row(self, value : int):
        ...
    
    ...

class ColorStop:
    '''internal use'''
    
    @property
    def offset(self) -> float:
        '''offset'''
        ...
    
    @offset.setter
    def offset(self, value : float):
        '''offset'''
        ...
    
    @property
    def color(self) -> str:
        '''color'''
        ...
    
    @color.setter
    def color(self, value : str):
        '''color'''
        ...
    
    @property
    def _offset(self) -> float:
        ...
    
    @_offset.setter
    def _offset(self, value : float):
        ...
    
    @property
    def _color(self) -> str:
        ...
    
    @_color.setter
    def _color(self, value : str):
        ...
    
    ...

class DataLabelsObject:
    '''internal use'''
    
    @property
    def show_value(self) -> bool:
        ...
    
    @show_value.setter
    def show_value(self, value : bool):
        ...
    
    @property
    def position(self) -> str:
        '''position'''
        ...
    
    @position.setter
    def position(self, value : str):
        '''position'''
        ...
    
    @property
    def _show_value(self) -> bool:
        ...
    
    @_show_value.setter
    def _show_value(self, value : bool):
        ...
    
    @property
    def _position(self) -> str:
        ...
    
    @_position.setter
    def _position(self, value : str):
        ...
    
    ...

class FontObject:
    '''internal use'''
    
    @property
    def color(self) -> str:
        '''color'''
        ...
    
    @color.setter
    def color(self, value : str):
        '''color'''
        ...
    
    @property
    def is_italic(self) -> bool:
        ...
    
    @is_italic.setter
    def is_italic(self, value : bool):
        ...
    
    @property
    def is_bold(self) -> bool:
        ...
    
    @is_bold.setter
    def is_bold(self, value : bool):
        ...
    
    @property
    def name(self) -> str:
        '''name'''
        ...
    
    @name.setter
    def name(self, value : str):
        '''name'''
        ...
    
    @property
    def size(self) -> float:
        '''size'''
        ...
    
    @size.setter
    def size(self, value : float):
        '''size'''
        ...
    
    @property
    def _color(self) -> str:
        ...
    
    @_color.setter
    def _color(self, value : str):
        ...
    
    @property
    def _is_italic(self) -> bool:
        ...
    
    @_is_italic.setter
    def _is_italic(self, value : bool):
        ...
    
    @property
    def _is_bold(self) -> bool:
        ...
    
    @_is_bold.setter
    def _is_bold(self, value : bool):
        ...
    
    @property
    def _name(self) -> str:
        ...
    
    @_name.setter
    def _name(self, value : str):
        ...
    
    @property
    def _size(self) -> float:
        ...
    
    @_size.setter
    def _size(self, value : float):
        ...
    
    ...

class GradientBackground(BackgroundColorObject):
    '''internal use'''
    
    @property
    def type(self) -> str:
        '''type'''
        ...
    
    @type.setter
    def type(self, value : str):
        '''type'''
        ...
    
    @property
    def color_stops(self) -> List[aspose.cellsgridjs.ColorStop]:
        ...
    
    @color_stops.setter
    def color_stops(self, value : List[aspose.cellsgridjs.ColorStop]):
        ...
    
    @property
    def x(self) -> Optional[float]:
        '''x'''
        ...
    
    @x.setter
    def x(self, value : Optional[float]):
        '''x'''
        ...
    
    @property
    def y(self) -> Optional[float]:
        '''y'''
        ...
    
    @y.setter
    def y(self, value : Optional[float]):
        '''y'''
        ...
    
    @property
    def x2(self) -> Optional[float]:
        '''x2'''
        ...
    
    @x2.setter
    def x2(self, value : Optional[float]):
        '''x2'''
        ...
    
    @property
    def y2(self) -> Optional[float]:
        '''y2'''
        ...
    
    @y2.setter
    def y2(self, value : Optional[float]):
        '''y2'''
        ...
    
    @property
    def r(self) -> Optional[float]:
        '''r'''
        ...
    
    @r.setter
    def r(self, value : Optional[float]):
        '''r'''
        ...
    
    @property
    def _type(self) -> str:
        ...
    
    @_type.setter
    def _type(self, value : str):
        ...
    
    @property
    def _color_stops(self) -> List[aspose.cellsgridjs.ColorStop]:
        ...
    
    @_color_stops.setter
    def _color_stops(self, value : List[aspose.cellsgridjs.ColorStop]):
        ...
    
    @property
    def _x(self) -> Optional[float]:
        ...
    
    @_x.setter
    def _x(self, value : Optional[float]):
        ...
    
    @property
    def _y(self) -> Optional[float]:
        ...
    
    @_y.setter
    def _y(self, value : Optional[float]):
        ...
    
    @property
    def _x2(self) -> Optional[float]:
        ...
    
    @_x2.setter
    def _x2(self, value : Optional[float]):
        ...
    
    @property
    def _y2(self) -> Optional[float]:
        ...
    
    @_y2.setter
    def _y2(self, value : Optional[float]):
        ...
    
    @property
    def _r(self) -> Optional[float]:
        ...
    
    @_r.setter
    def _r(self, value : Optional[float]):
        ...
    
    ...

class GridChartResponseType:
    '''internal use'''
    
    @property
    def title(self) -> aspose.cellsgridjs.TitleObject:
        '''title'''
        ...
    
    @title.setter
    def title(self, value : aspose.cellsgridjs.TitleObject):
        '''title'''
        ...
    
    @property
    def category_axis(self) -> aspose.cellsgridjs.AxisObject:
        ...
    
    @category_axis.setter
    def category_axis(self, value : aspose.cellsgridjs.AxisObject):
        ...
    
    @property
    def value_axis(self) -> aspose.cellsgridjs.AxisObject:
        ...
    
    @value_axis.setter
    def value_axis(self, value : aspose.cellsgridjs.AxisObject):
        ...
    
    @property
    def legend(self) -> aspose.cellsgridjs.LegendObject:
        '''legend'''
        ...
    
    @legend.setter
    def legend(self, value : aspose.cellsgridjs.LegendObject):
        '''legend'''
        ...
    
    @property
    def n_series(self) -> List[aspose.cellsgridjs.NSeriesDetails]:
        ...
    
    @n_series.setter
    def n_series(self, value : List[aspose.cellsgridjs.NSeriesDetails]):
        ...
    
    @property
    def id(self) -> int:
        '''id'''
        ...
    
    @id.setter
    def id(self, value : int):
        '''id'''
        ...
    
    @property
    def background_color(self) -> aspose.cellsgridjs.BackgroundColorObject:
        ...
    
    @background_color.setter
    def background_color(self, value : aspose.cellsgridjs.BackgroundColorObject):
        ...
    
    @property
    def name(self) -> str:
        '''name'''
        ...
    
    @name.setter
    def name(self, value : str):
        '''name'''
        ...
    
    @property
    def type(self) -> str:
        '''type'''
        ...
    
    @type.setter
    def type(self, value : str):
        '''type'''
        ...
    
    @property
    def chart_object(self) -> aspose.cellsgridjs.ChartDimensionObject:
        ...
    
    @chart_object.setter
    def chart_object(self, value : aspose.cellsgridjs.ChartDimensionObject):
        ...
    
    @property
    def worksheet(self) -> aspose.cellsgridjs.WorksheetObject:
        '''worksheet'''
        ...
    
    @worksheet.setter
    def worksheet(self, value : aspose.cellsgridjs.WorksheetObject):
        '''worksheet'''
        ...
    
    @property
    def _title(self) -> aspose.cellsgridjs.TitleObject:
        ...
    
    @_title.setter
    def _title(self, value : aspose.cellsgridjs.TitleObject):
        ...
    
    @property
    def _category_axis(self) -> aspose.cellsgridjs.AxisObject:
        ...
    
    @_category_axis.setter
    def _category_axis(self, value : aspose.cellsgridjs.AxisObject):
        ...
    
    @property
    def _value_axis(self) -> aspose.cellsgridjs.AxisObject:
        ...
    
    @_value_axis.setter
    def _value_axis(self, value : aspose.cellsgridjs.AxisObject):
        ...
    
    @property
    def _legend(self) -> aspose.cellsgridjs.LegendObject:
        ...
    
    @_legend.setter
    def _legend(self, value : aspose.cellsgridjs.LegendObject):
        ...
    
    @property
    def _n_series(self) -> List[aspose.cellsgridjs.NSeriesDetails]:
        ...
    
    @_n_series.setter
    def _n_series(self, value : List[aspose.cellsgridjs.NSeriesDetails]):
        ...
    
    @property
    def _i_d(self) -> int:
        ...
    
    @_i_d.setter
    def _i_d(self, value : int):
        ...
    
    @property
    def _background_color(self) -> aspose.cellsgridjs.BackgroundColorObject:
        ...
    
    @_background_color.setter
    def _background_color(self, value : aspose.cellsgridjs.BackgroundColorObject):
        ...
    
    @property
    def _name(self) -> str:
        ...
    
    @_name.setter
    def _name(self, value : str):
        ...
    
    @property
    def _type(self) -> str:
        ...
    
    @_type.setter
    def _type(self, value : str):
        ...
    
    @property
    def _chart_object(self) -> aspose.cellsgridjs.ChartDimensionObject:
        ...
    
    @_chart_object.setter
    def _chart_object(self, value : aspose.cellsgridjs.ChartDimensionObject):
        ...
    
    @property
    def _worksheet(self) -> aspose.cellsgridjs.WorksheetObject:
        ...
    
    @_worksheet.setter
    def _worksheet(self, value : aspose.cellsgridjs.WorksheetObject):
        ...
    
    ...

class LegendObject:
    '''internal use'''
    
    @property
    def show_legend(self) -> bool:
        ...
    
    @show_legend.setter
    def show_legend(self, value : bool):
        ...
    
    @property
    def position(self) -> str:
        '''position'''
        ...
    
    @position.setter
    def position(self, value : str):
        '''position'''
        ...
    
    @property
    def _show_legend(self) -> bool:
        ...
    
    @_show_legend.setter
    def _show_legend(self, value : bool):
        ...
    
    @property
    def _position(self) -> str:
        ...
    
    @_position.setter
    def _position(self, value : str):
        ...
    
    ...

class NSeriesDetails:
    '''internal use'''
    
    @property
    def data(self) -> List[aspose.cellsgridjs.CellData]:
        '''data'''
        ...
    
    @data.setter
    def data(self, value : List[aspose.cellsgridjs.CellData]):
        '''data'''
        ...
    
    @property
    def values(self) -> str:
        '''values'''
        ...
    
    @values.setter
    def values(self, value : str):
        '''values'''
        ...
    
    @property
    def name(self) -> aspose.cellsgridjs.CellData:
        '''name'''
        ...
    
    @name.setter
    def name(self, value : aspose.cellsgridjs.CellData):
        '''name'''
        ...
    
    @property
    def area(self) -> aspose.cellsgridjs.AreaObject:
        '''area'''
        ...
    
    @area.setter
    def area(self, value : aspose.cellsgridjs.AreaObject):
        '''area'''
        ...
    
    @property
    def data_labels(self) -> aspose.cellsgridjs.DataLabelsObject:
        ...
    
    @data_labels.setter
    def data_labels(self, value : aspose.cellsgridjs.DataLabelsObject):
        ...
    
    @property
    def is_filtered(self) -> bool:
        ...
    
    @is_filtered.setter
    def is_filtered(self, value : bool):
        ...
    
    @property
    def _data(self) -> List[aspose.cellsgridjs.CellData]:
        ...
    
    @_data.setter
    def _data(self, value : List[aspose.cellsgridjs.CellData]):
        ...
    
    @property
    def _values(self) -> str:
        ...
    
    @_values.setter
    def _values(self, value : str):
        ...
    
    @property
    def _name(self) -> aspose.cellsgridjs.CellData:
        ...
    
    @_name.setter
    def _name(self, value : aspose.cellsgridjs.CellData):
        ...
    
    @property
    def _area(self) -> aspose.cellsgridjs.AreaObject:
        ...
    
    @_area.setter
    def _area(self, value : aspose.cellsgridjs.AreaObject):
        ...
    
    @property
    def _data_labels(self) -> aspose.cellsgridjs.DataLabelsObject:
        ...
    
    @_data_labels.setter
    def _data_labels(self, value : aspose.cellsgridjs.DataLabelsObject):
        ...
    
    @property
    def _is_filtered(self) -> bool:
        ...
    
    @_is_filtered.setter
    def _is_filtered(self, value : bool):
        ...
    
    ...

class SolidBackground(BackgroundColorObject):
    '''internal use'''
    
    @property
    def color(self) -> str:
        '''color'''
        ...
    
    @color.setter
    def color(self, value : str):
        '''color'''
        ...
    
    @property
    def _color(self) -> str:
        ...
    
    @_color.setter
    def _color(self, value : str):
        ...
    
    ...

class TitleObject:
    '''internal use'''
    
    @property
    def text(self) -> str:
        '''text'''
        ...
    
    @text.setter
    def text(self, value : str):
        '''text'''
        ...
    
    @property
    def is_visible(self) -> bool:
        ...
    
    @is_visible.setter
    def is_visible(self, value : bool):
        ...
    
    @property
    def text_horizontal_alignment(self) -> str:
        ...
    
    @text_horizontal_alignment.setter
    def text_horizontal_alignment(self, value : str):
        ...
    
    @property
    def text_vertical_alignment(self) -> str:
        ...
    
    @text_vertical_alignment.setter
    def text_vertical_alignment(self, value : str):
        ...
    
    @property
    def font(self) -> aspose.cellsgridjs.FontObject:
        '''font'''
        ...
    
    @font.setter
    def font(self, value : aspose.cellsgridjs.FontObject):
        '''font'''
        ...
    
    @property
    def border(self) -> aspose.cellsgridjs.BorderObject:
        '''border'''
        ...
    
    @border.setter
    def border(self, value : aspose.cellsgridjs.BorderObject):
        '''border'''
        ...
    
    @property
    def x(self) -> float:
        '''x'''
        ...
    
    @x.setter
    def x(self, value : float):
        '''x'''
        ...
    
    @property
    def y(self) -> float:
        '''y'''
        ...
    
    @y.setter
    def y(self, value : float):
        '''y'''
        ...
    
    @property
    def _text(self) -> str:
        ...
    
    @_text.setter
    def _text(self, value : str):
        ...
    
    @property
    def _is_visible(self) -> bool:
        ...
    
    @_is_visible.setter
    def _is_visible(self, value : bool):
        ...
    
    @property
    def _text_horizontal_alignment(self) -> str:
        ...
    
    @_text_horizontal_alignment.setter
    def _text_horizontal_alignment(self, value : str):
        ...
    
    @property
    def _text_vertical_alignment(self) -> str:
        ...
    
    @_text_vertical_alignment.setter
    def _text_vertical_alignment(self, value : str):
        ...
    
    @property
    def _font(self) -> aspose.cellsgridjs.FontObject:
        ...
    
    @_font.setter
    def _font(self, value : aspose.cellsgridjs.FontObject):
        ...
    
    @property
    def _border(self) -> aspose.cellsgridjs.BorderObject:
        ...
    
    @_border.setter
    def _border(self, value : aspose.cellsgridjs.BorderObject):
        ...
    
    @property
    def _x(self) -> float:
        ...
    
    @_x.setter
    def _x(self, value : float):
        ...
    
    @property
    def _y(self) -> float:
        ...
    
    @_y.setter
    def _y(self, value : float):
        ...
    
    ...

class WorksheetObject:
    '''internal use'''
    
    @property
    def name(self) -> str:
        '''name'''
        ...
    
    @name.setter
    def name(self, value : str):
        '''name'''
        ...
    
    @property
    def _name(self) -> str:
        ...
    
    @_name.setter
    def _name(self, value : str):
        ...
    
    ...

