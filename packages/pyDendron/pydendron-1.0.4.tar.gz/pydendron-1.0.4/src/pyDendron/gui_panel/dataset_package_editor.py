"""
File Name: dataset_tabulator_filter.py
Author: Sylvain Meignier
Organization: Le Mans Université, LIUM (https://lium.univ-lemans.fr/)
Creation Date: 2023-12-03
Description: fontend application based on sidecar
This file is governed by the terms of the GNU General Public License v3.0.
Please see the LICENSE file for more details.
"""

import pandas as pd
import param
import panel as pn
from panel.viewable import Viewer

from pyDendron.app_logger import logger
from pyDendron.gui_panel.dataset_package import DatasetPackage
from pyDendron.dataname import *
#from pyDendron.gui_panel.tabulator import (_cell_text_align, _cell_editors, _header_filters, _cell_formatters, 
#                                           _hidden_columns)

class DatasetPackageEditor(Viewer):
    selection = param.List(default=[], doc='path')

    def __init__(self, dataset, param_column, param_package, **params):
        bt_size = 150
        super(DatasetPackageEditor, self).__init__(**params) 
        
        self.dataset = dataset
        
        self.package = DatasetPackage(dataset, param_column, param_package)
        self.panel_tabulator = self.package.panel_tabulator
        self.wselection_name = self.package.wselection_name
        self.wtabulator = self.package.wtabulator
        
        self.bt_delete = pn.widgets.Button(name='Delete package', icon='file-off', button_type='primary', width=bt_size, align=('start', 'end'))
        self.bt_delete.on_click(self.on_delete)
        self.bt_erase = pn.widgets.Button(name='Remove row', icon='eraser', button_type='primary', width=bt_size, align=('start', 'end'))
        self.bt_erase.on_click(self.on_erase)
        
        self.bt_save = pn.widgets.Button(name='Save package', icon='file', button_type='primary', width=bt_size, align=('start', 'end'))
        self.bt_save.on_click(self.on_save)

        self._layout = pn.Column(self.package, 
                                 pn.Row(self.bt_erase, self.bt_save, self.bt_delete))
        #self.dt_info.visible = True
        self.panel_tabulator.collapsed = False
        
    def __panel__(self):
        return self._layout

    def on_delete(self, event):
        if self.wselection_name.value != '':
            self.dataset.delete_package(self.wselection_name.value)
            #self.sync_dataset(event)
            #self.wtabulator.value = pd.DataFrame(columns=list(dtype_view.keys()))
    
    def on_save(self, event):
        try:
            self._layout.loading = True
            self.package.save()
        except Exception as inst:
            logger.error(f'on_erase: {inst}', exc_info=True)
            self.wtabulator.value = pd.DataFrame(columns=list(dtype_view.keys()))
        finally:
            self._layout.loading = False

    def on_erase(self, event):
        try:
            self._layout.loading = True
            self.wtabulator.value = self.wtabulator.value.drop(self.wtabulator.selection)
        except Exception as inst:
            logger.error(f'on_erase: {inst}', exc_info=True)
            self.wtabulator.value = pd.DataFrame(columns=list(dtype_view.keys()))
        finally:
            self.wtabulator.selection = []
            self._layout.loading = False
