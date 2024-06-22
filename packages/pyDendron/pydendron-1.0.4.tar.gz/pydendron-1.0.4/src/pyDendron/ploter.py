"""
File Name: ploter.py
Author: Sylvain Meignier
Organization: Le Mans Université, LIUM (https://lium.univ-lemans.fr/)
Creation Date: 2023-12-03
Description: plotter panel
This file is governed by the terms of the GNU General Public License v3.0.
Please see the LICENSE file for more details.
"""
import numpy as np
import pandas as pd

import param
import panel as pn
from panel.viewable import Viewer

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, FixedTicker
from bokeh.models import Range1d
from bokeh.palettes import Category20, Category10

from pyDendron.dataname import *
from pyDendron.app_logger import logger

class Ploter(Viewer):
    ANATOMY = 'Anatomy'
    ANATOMY_COLOR = {HEARTWOOD: 'black', 
                     PITH: 'blue', PITH_MAXIMUM: 'blue', PITH_OPTIMUM: 'blue', 
                     SAPWOOD:'red', 
                     CAMBIUM:'red',
                     BARK: 'red'}
    
    figure_title = param.String(' ')
    figure_title_font_size = param.Integer(default=14, bounds=(1, 20), step=1)
    y_offset_mode = param.Selector(default='Stack', objects=['Center', 'Stack'], doc='')
    x_offset_mode = param.Selector(objects=['None', DATE_BEGIN, OFFSET], doc='')
    width = param.Integer(default=1000, bounds=(50, 4000), step=10)
    height = param.Integer(default=500, bounds=(50, 2000), step=10)
    #pith_estimation = param.Boolean(False, doc='Draw pith estimation')
    cambium_estimation = param.Boolean(False, doc='Draw cambium estimation')
    line_width_tree = param.Number(default=0.5, bounds=(0.25, 4.0), step=0.25)
    line_width_chronology = param.Number(default=1, bounds=(0.25, 4.0), step=0.25)
    circle_radius = param.Number(default=0.5, bounds=(0.1, 5), step=0.1)
    color = param.Selector(default=ANATOMY, objects=['None', KEYCODE, ANATOMY], 
            doc=f'None: all black, {KEYCODE}: one color per {KEYCODE}, {ANATOMY}: color pith, sapwood... ')
    legend = param.Selector(default='Y axe', objects=['None', 'Y axe', 'In figure'], 
            doc=f'position of the legend')
    legend_font_size = param.Integer(default=14, bounds=(1, 20), step=1)
    x_range_step = param.Integer(default=25, bounds=(5, 200), step=5)
    axis_marge = param.Integer(default=5, bounds=(0, 10), step=1)
    axis_font_size = param.Integer(default=10, bounds=(1, 20), step=1)
    draw_type = param.Selector(default='Line', objects=['Line', 'Step', 'Spaghetti'], doc='') 
    
    def __init__(self, ploter_name='ploter', **params):
        super(Ploter, self).__init__(**params)   
        self.ploter_name = ploter_name
        self.draw_data = None
        self.data = None
        self.x_range, self.y_range = None, None
        self.figure_pane = pn.pane.Bokeh(height=self.height, width=self.width)
        self._layout = self.figure_pane
 
    def __panel__(self):
        return self._layout
                
    @param.depends("width", watch=True)
    def _update_width(self):
        self.figure_pane.width = self.width

    @param.depends("height", watch=True)
    def _update_height(self):
        self.figure_pane.height = self.height
    
    def get_pith_optimun(self, data_len):
        return int(data_len*0.1)

    def get_cambium_optimun(self, cambium, bark, sapwood, values):
        def norm(x, nb):
            return max(nb, x + sapwood)
        
        if cambium or bark:
            print('get_cambium_optimun cambium or bark is True', cambium, bark)
            return 0, 0, 0
        elif pd.notna(sapwood) and sapwood > 0 and sapwood < len(values) : 
            i = max(0, sapwood - 9)
            j = min(sapwood + 1, len(values))
            rw10 = np.nanmean(values[i:j]) / 100
            x = 2.8102081 - 0.5331451 * np.log(rw10)
            print('get_cambium_optimun:', rw10, i, j, len(values), x, np.exp(x))
            nb = len(values)
            estimation = int(np.round(np.exp(x)))
            print(estimation)
            upper_bound = int(np.round(np.exp(x + 0.6087837)))
            lower_bound = int(np.round(np.exp(x - 0.6087837)))
            print('get_cambium_optimun is True', sapwood, lower_bound, estimation, upper_bound, nb)
            return norm(lower_bound, nb), norm(estimation, nb), norm(upper_bound, nb)
        print('sapwood is valide', sapwood)
        return 0, 0, 0
     
    def prepare_data(self, data):
        print('prepare_data')

        if data is None:
            return
        self.data = data
        cum_y_offset = 0

        def init_ColumnDataSource():
            #return {'x': [], 'w': [], 'y': []}
            return ColumnDataSource()

        def get_x_offset(row):
            if self.x_offset_mode == 'None':
                return 0
            elif self.x_offset_mode == DATE_BEGIN:
                return row[DATE_BEGIN]
            return row[OFFSET]

        def get_y_offset(row, cum_y_offset):
            data = row[DATA_VALUES]
            if self.draw_type == 'Spaghetti':
                v = 50
            else:
                #v = (np.nanmax(data) - np.nanmin(data)) if self.y_offset_mode == 'Stack' else 0
                v = (np.nanmax(data) ) if self.y_offset_mode == 'Stack' else 0
            cum_y_offset += v
            #print('get_y_offset', cum_y_offset, v)
            return v, cum_y_offset
        
        def get_values(row, info):
            values = row[DATA_VALUES]

            sapwood_offset = row[SAPWOOD]
            info[SAPWOOD] = init_ColumnDataSource()
            info[HEARTWOOD] = init_ColumnDataSource()
            
            if pd.isna(sapwood_offset) or sapwood_offset < 0:
                sapwood_offset = len(values) - 1
            info[HEARTWOOD].data['x'] = np.arange(0, sapwood_offset + 1) + info['x_offset']
            info[HEARTWOOD].data['w'] = values[:sapwood_offset + 1]
            info[HEARTWOOD].data['y'] = info[HEARTWOOD].data['w'] + info['y_offset'] 
            
            info['is_sapwood'] = not(pd.isna(sapwood_offset) or sapwood_offset < 0)
            info[SAPWOOD].data['x'] = np.arange(sapwood_offset, len(values)) + info['x_offset']
            info[SAPWOOD].data['w'] = values[sapwood_offset:]
            info[SAPWOOD].data['y'] = info[SAPWOOD].data['w'] + info['y_offset']
            
        def get_pith(row, info):
            values = row[DATA_VALUES]
            x_min = info['x_offset']
            i = np.where(~np.isnan(values))[0][0]
            w = values[i]
            info[PITH] = init_ColumnDataSource()
            info[PITH_OPTIMUM] = init_ColumnDataSource()
            info[PITH_MAXIMUM] = init_ColumnDataSource()
            if pd.notna(row[PITH]) and row[PITH]:
                info[PITH].data['x'] = [info['x_offset']]
                info[PITH].data['w'] = [w]
                info[PITH].data['y'] = [w + info['y_offset']]
            # elif self.pith_estimation:#pd.notna(row[PITH_OPTIMUM]):
            #     optimum = self.get_pith_optimun(row[DATA_LENGTH])
            #     info[PITH_OPTIMUM].data['x'] = np.array([optimum, 0]) + info['x_offset']
            #     info[PITH_OPTIMUM].data['w'] = np.array([w, w]) 
            #     info[PITH_OPTIMUM].data['y'] = np.array([w, w]) + info['y_offset'] 
            #     x_min = info['x_offset'] = info['x_offset'] + optimum
            return x_min
                
        def get_cambium(row, info):
            values = row[DATA_VALUES]
            x = len(values) - 1
            x_max = x + info['x_offset']

            w = values[np.where(~np.isnan(values))[0][-1]]
            info[CAMBIUM] = init_ColumnDataSource()
            info[CAMBIUM_ESTIMATED] = init_ColumnDataSource()
            info[CAMBIUM_BOUNDARIES] = init_ColumnDataSource()
            if pd.notna(row[CAMBIUM]) and row[CAMBIUM]:
                info[CAMBIUM].data['x'] = [x + info['x_offset']]
                info[CAMBIUM].data['w'] = ['NA']
                info[CAMBIUM].data['y'] = [w + info['y_offset']]
            #elif self.cambium_estimation: #pd.notna(row[CAMBIUM_OPTIMUM]):
            else:
                lower, estimated, upper = self.get_cambium_optimun(row[CAMBIUM], row[BARK], row[SAPWOOD], values)
                print('cambium estimation:', lower, estimated, upper)
                if estimated > 0:
                    xe = estimated + info['x_offset']
                    xl = lower + info['x_offset']
                    xu = upper + info['x_offset']
                    info[CAMBIUM_BOUNDARIES].data['x'] = np.arange(xl, xu) + info['x_offset']
                    info[CAMBIUM_BOUNDARIES].data['w'] = np.array(['NA']*(xu-xl))
                    info[CAMBIUM_BOUNDARIES].data['y'] = np.array([w]*(xu-xl)) + info['y_offset']
                    info[CAMBIUM_ESTIMATED].data['x'] = [xe + info['x_offset']]
                    info[CAMBIUM_ESTIMATED].data['w'] = ['NA']
                    info[CAMBIUM_ESTIMATED].data['y'] = [w + info['y_offset']]
                    x_max = xu 
            return x_max

        def get_bark(row, info):
            values = row[DATA_VALUES]
            x = len(values)
            w = values[np.where(~np.isnan(values))[-1]]
            info[BARK] = init_ColumnDataSource()
            if pd.notna(row[BARK]) and row[BARK]:
                info[BARK].data['x'] = [x + info['x_offset']]
                info[BARK].data['w'] = [w]
                info[BARK].data['y'] = [w + info['y_offset']]
        
        draw = {}
        data = data.loc[data[CATEGORY].isin([CHRONOLOGY, TREE]),:]
        if self.x_offset_mode != 'None':
            if data[self.x_offset_mode].isna().any():
                logger.error(f"NA value(s) in {self.x_offset_mode} column, can't draw")
                return draw
        
        for _, row in data.iterrows():      
            #row[DATA_VALUES] -= np.nanmean(row[DATA_VALUES])      
            #print(row[KEYCODE], row[DATA_VALUES])
            info = {}
            info[CATEGORY] = row[CATEGORY]
            if self.draw_type == 'Spaghetti':
                row[DATA_VALUES] = np.array([100] * row[DATA_LENGTH])
            
            info[KEYCODE] = row[KEYCODE]
            info['x_offset'] = get_x_offset(row)
            _, next_cum_y_offset = get_y_offset(row, cum_y_offset)
            
            info['y_offset'] = cum_y_offset
            get_values(row, info)
            get_bark(row, info)
            info['x_min'] = get_pith(row, info)
            info['x_max'] = get_cambium(row, info)

            info['w_min'] = np.nanmin(row[DATA_VALUES])
            info['w_max'] = np.nanmax(row[DATA_VALUES])
            info['w_mean'] = np.nanmean(row[DATA_VALUES])
            info['y_min'] = info['y_offset'] #info['w_min'] + info['y_offset']
            info['y_max'] = info['w_max'] + info['y_offset']
            info['y_mean'] = info['w_mean'] + info['y_offset']
            info['y_label'] = info['y_mean']

            draw[info[KEYCODE]] = info
            cum_y_offset = next_cum_y_offset
        return draw

    @param.depends('x_offset_mode', 'y_offset_mode', 'draw_type', watch=True)
    def prepare_and_plot(self, data=None):
        print('prepare_and_plot', data, self.data)
        try:
            self._layout.loading = True
            if data is not None:
                self.data = data
            if (self.data is None) or (len(self.data) == 0):
                self._layout.loading = False
                return
            self.draw_data = self.prepare_data(self.data) 
            print('end prepare_data')
        except Exception as inst:
            logger.error(f'plot : {inst}', exc_info=True)
        finally:
            self._layout.loading = False
        
        self.plot()
        print('end plot')
    
    def on_x_range_step(self):
        if (self.figure_pane.object is not None) and pd.notna(self.figure_pane.object.x_range.start):
            x_min = self.figure_pane.object.x_range.start + self.axis_marge
            x_max = self.figure_pane.object.x_range.end - self.axis_marge
            self.figure_pane.object.xaxis[0].ticker = FixedTicker(ticks= np.arange(int(x_min), int(x_max), self.x_range_step))
            label = self.x_offset_mode if self.x_offset_mode != 'None' else f'{OFFSET}'
            self.figure_pane.object.xaxis[0].axis_label = label
        
    @param.depends('figure_title', 'figure_title_font_size', watch=True)
    def on_figure_title(self):
        if self.figure_pane.object is not None:
            self.figure_pane.object.title.text = self.figure_title
            self.figure_pane.object.title.text_font_size = str(self.figure_title_font_size) + 'px'
    
    @param.depends('axis_font_size', watch=True)
    def on_axis_font_size(self):
        if self.figure_pane.object is not None:
            self.figure_pane.object.yaxis.major_label_text_font_size = f'{self.axis_font_size}px'
            self.figure_pane.object.xaxis.major_label_text_font_size = f'{self.axis_font_size}px'
    
    @param.depends('legend_font_size', watch=True)
    def on_legend_font_size(self):
        if self.figure_pane.object is not None:
            self.figure_pane.object.legend.label_text_font_size = f'{self.legend_font_size}px'
            print(self.figure_pane.object.legend.label_text_font_size)

    def on_legend(self):
        if self.figure_pane.object is not None:            
            self.figure_pane.object.legend.visible = False
            y_labels = {}
            for i, (keycode, info) in enumerate(self.draw_data.items()):
                y_labels[info['y_label']] = keycode if self.legend == 'Y axe' else str(i)
            self.figure_pane.object.yaxis.ticker = list(y_labels.keys())
            self.figure_pane.object.yaxis.major_label_overrides = y_labels
            
            if self.legend == 'In figure':
                self.figure_pane.object.legend.location = "top_left"
                self.figure_pane.object.legend.click_policy="mute"
                self.figure_pane.object.legend.visible = True
                
    def get_color(self, kind, rank):
        if self.color == self.ANATOMY:
            return self.ANATOMY_COLOR[kind]
        elif self.color == KEYCODE:
            if len(self.draw_data)  <= 10:
                return Category10[10][rank]
            else:
                return Category20[20][rank % 20]
        return 'black'
    
    @param.depends('x_range_step', 'legend', 'line_width_tree','line_width_chronology', 'circle_radius', 'color', 'axis_marge', 'cambium_estimation', watch=True)
    def plot(self, x_range = None, y_range = None):   
        try:
            # save x_range and y_range values for next plot (usefull for ligt ploter)
            if x_range is not None:
                self.x_range = x_range
            if y_range is not None:
                self.y_range = y_range
                
            print('ploter')
            self._layout.loading = True
            if self.draw_data is None:
                return
            fig = figure(margin=(5), title=self.figure_title, toolbar_location="left", height=self.height, width=self.width,
                tools="pan,wheel_zoom,box_zoom,reset,hover,save,crosshair", tooltips=[('(date/offset,value)', '(@x, @w)')])
            
            fig.output_backend = "svg"
            radius = self.circle_radius
            
            x = []
            for i, (keycode, info) in enumerate(self.draw_data.items()):
                line_width = self.line_width_tree if info[CATEGORY] == TREE else self.line_width_chronology
                x.append(info['x_min'])
                x.append(info['x_max'])
                #fig.quad(top=[info['y_max']], bottom=[info['y_min']], left=[info['x_min']], right=[info['x_max']], line_color='black', alpha=0.3, line_width=2, color=self.get_color(HEARTWOOD, i))
                fct = fig.line
                if self.draw_type == 'Step':
                    fct = fig.step
                
                fct(x='x', y='y', source=info[HEARTWOOD], line_width=line_width,  color=self.get_color(HEARTWOOD, i), legend_label=keycode)
                fct(x='x', y='y', source=info[SAPWOOD], line_width=line_width,  color=self.get_color(SAPWOOD, i), legend_label=keycode)
                #fct(x='x', y='y', source=info[PITH_OPTIMUM], line_dash='dashed', line_width=line_width, color=self.get_color(PITH_OPTIMUM, i), legend_label=keycode)
                #fct(x='x', y='y', source=info[PITH_MAXIMUM], line_dash='dotted', line_width=line_width, color=self.get_color(PITH_MAXIMUM, i), legend_label=keycode)
                if info['is_sapwood'] and self.cambium_estimation:
                    print('plot cambium estimation', info[CAMBIUM_ESTIMATED], info[CAMBIUM_BOUNDARIES])
                    fig.scatter(x='x', y='y', source=info[CAMBIUM_ESTIMATED], marker="cross", size=radius*10, color=self.get_color(SAPWOOD, i), legend_label=keycode)
                    #fig.scatter(x='x', y='y', source=info[CAMBIUM_ESTIMATED],  marker="cross")
                    fct(x='x', y='y', source=info[CAMBIUM_BOUNDARIES], line_dash='dotted', line_width=line_width, color=self.get_color(SAPWOOD, i), legend_label=keycode)

                fig.circle(x='x', y='y', source=info[PITH], radius=radius, color=self.get_color(PITH, i), legend_label=keycode)
                fig.circle(x='x', y='y', source=info[CAMBIUM], radius=radius, color=self.get_color(SAPWOOD, i), legend_label=keycode)
                fig.circle(x='x', y='y', source=info[BARK], radius=radius, color=self.get_color(BARK, i), legend_label=keycode)
            
            #fig.xaxis.major_label_text_font_size = f'{self.axis_font_size}px'
            #fig.yaxis.major_label_text_font_size = f'{self.axis_font_size}px'

            (x_min, x_max) = (np.min(x), np.max(x)) if self.x_range is None else self.x_range
            fig.x_range = Range1d(start=x_min - self.axis_marge, end=x_max + self.axis_marge)
            if self.y_range is not None:
                fig.y_range = Range1d(self.y_range[0], self.y_range[1])

            fig.legend.visible = False
            self.figure_pane.object = fig

            self.on_x_range_step()
            self.on_legend()
        except Exception as inst:
            logger.error(f'plot : {inst}', exc_info=True)
        finally:
            self._layout.loading = False

