# -*- coding: utf-8 -*-
'''
/***************************************************************************
 Open eQuarter Dialogs

                             -------------------
        begin                : 2014-10-07
        copyright            : (C) 2014 by Kim Gülle / UdK-Berlin
        email                : firstdayofjune@users.noreply.github.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
'''
from PyQt4 import QtGui
from PyQt4 import QtCore
from functools import partial
from qgis.core import QgsMapLayerRegistry, QgsMapLayer

from ui_color_picker_dialog import Ui_color_picker_dialog
from oeq_ui_classes import QRemoveEntryButton, QColorizedLineEdit, QColorTableDelegate, QColorTableModel
from ui_main_process_dock import Ui_MainProcess_dock, _fromUtf8
from ui_project_does_not_exist_dialog import Ui_ProjectDoesNotExist_dialog
from ui_project_settings_form import Ui_project_settings_form
from ui_modular_info_dialog import Ui_ModularInfo_dialog
from ui_modular_dialog import Ui_Modular_dialog
from ui_request_wms_url_dialog import Ui_RequestWmsUrl_dialog
from ui_estimated_energy_demand_dialog import Ui_EstimatedEnergyDemand_dialog
from mole.model.file_manager import ColorEntryManager, MunicipalInformationTree
from mole.qgisinteraction import layer_interaction

class ColorPicker_dialog(QtGui.QDialog, Ui_color_picker_dialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.color_entry_manager = ColorEntryManager()
        self.recent_layer = ''
        self.layers_dropdown.currentIndexChanged.connect(self.update_color_values)

        # set the table model
        self.header = ['Color value', 'Parameter Name', 'From', 'To', '']
        self.color_entry_manager.add_layer('dummy')
        self.color_entry_manager.add_color_value_quadruple_to_layer(('RGBa(0, 0, 0, 0)', ' ', 0, 0), 'dummy')
        self.dummy_model = QColorTableModel(self.color_entry_manager.layer_values_map['dummy'], self.header, self)
        self.color_table_view.setModel(self.dummy_model)
        self.setup_table()

        # connect the signals
        self.color_table_view.clicked.connect(self.remove_entry)

    def setup_table(self):
        """
        Set the basic attributes for the color-table view
        :return:
        :rtype:
        """
        for i in range(len(self.header)):
            self.color_table_view.setItemDelegateForColumn(i, QColorTableDelegate(self))

        self.color_table_view.setColumnWidth(0, 205)
        self.color_table_view.setColumnWidth(1, 205)
        self.color_table_view.setColumnWidth(2, 75)
        self.color_table_view.setColumnWidth(3, 75)
        self.color_table_view.setColumnWidth(4, 35)
        self.color_table_view.setShowGrid(False)
        self.color_table_view.setSortingEnabled(True)
        self.color_table_view.sortByColumn(2)

        # set horizontal header properties
        hor_header = self.color_table_view.horizontalHeader()
        hor_header.setStretchLastSection(True)
        hor_header.setStyleSheet('QHeaderView::section { '
                         ' border: None;'
                         ' padding: 3px;'
                         ' font-size: 13px;'
                         ' font-weight: bold;'
                         ' margin: 5px;'
                         ' background-color: rgb(237, 237, 237);'
                         '}'
                         )
        self.color_table_view.setHorizontalHeader(hor_header)

        # set row height
        ver_header = self.color_table_view.verticalHeader()
        ver_header.setDefaultSectionSize(34)
        ver_header.setStyleSheet('QHeaderView::section { '
                         ' border: None;'
                         ' padding: 3px;'
                         ' font-size: 13px;'
                         ' margin: 5px;'
                         ' margin-right: 12px;'
                         ' background-color: rgb(237, 237, 237);'
                         '}'
                         )
        self.color_table_view.setVerticalHeader(ver_header)

    def remove_entry(self, model_index):
        """
        Remove the entry from the color-entry-manager
        :param model_index: The QModelIndex of the clicked element
        :type model_index: QModelIndex
        :return:
        :rtype:
        """
        column = model_index.column()
        if column == 4:
            row = model_index.row()
            model = model_index.model()
            color_entry = model.in_data[row][0]
            layer = self.layers_dropdown.currentText()
            self.color_entry_manager.remove_color_entry_from_layer(color_entry, layer)
            color_map = self.color_entry_manager.layer_values_map[layer]
            if not color_map:
                color_map = self.color_entry_manager.layer_values_map['dummy']
            tm = QColorTableModel(color_map, self.header, self)
            self.color_table_view.setModel(tm)

    def add_color(self, color):
        """
        Insert a new color (and the values associated to it, if any), into the color-table.
        :param color: The color in RGBa
        :type color: QColor
        :return:
        :rtype:
        """
        layer = self.layers_dropdown.currentText()
        self.recent_layer = layer
        color_map = self.color_entry_manager.layer_values_map[layer]
        model = QColorTableModel(color_map, self.header, self)
        self.color_table_view.setModel(model)

        color_key = 'RGBa({}, {}, {}, {})'.format(color.red(), color.green(), color.blue(), color.alpha())
        if color_map.has_key(color_key):
            self.warning_label.setText('Attention: Color {} is defined already.'.format(color_key))

        else:
            self.warning_label.clear()
            self.color_entry_manager.add_color_value_quadruple_to_layer((color_key, '', 0, 0), layer)
            color_map = self.color_entry_manager.layer_values_map[layer]
            model = QColorTableModel(color_map, self.header, self)
            self.color_table_view.setModel(model)

    def update_color_values(self):
        """
        Change the color-table view to display the color-map of the currently selected layer.
        :return:
        :rtype:
        """
        layer = self.layers_dropdown.currentText()
        color_map = {}
        if layer in self.color_entry_manager.layer_values_map:
            color_map = self.color_entry_manager.layer_values_map[layer]
            table_model = QColorTableModel(color_map, self.header, self)
        if not color_map:
            table_model = self.dummy_model
        self.color_table_view.setModel(table_model)
        self.recent_layer = layer

    def check_character_constraint(self, parameter_name):
        """
        Check if the parameter-name has a length of ten characters at most,
        since layer-attributes are limited to 10 characters.
        :param parameter_name:
        :type parameter_name:
        :return:
        :rtype:
        """
        if len(parameter_name) == 10 and parameter_name != 'Parameter ':
            self.warning_label.setText('Warning: A maximum of 10 characters is allowed as a parameter name!')
        else:
            self.warning_label.clear()


class MainProcess_dock(QtGui.QDockWidget, Ui_MainProcess_dock):

    def __init__(self, progress_model):
        QtGui.QDockWidget.__init__(self)
        self.setupUi(self)
        self._check_mark = QtGui.QPixmap(_fromUtf8(":/Controls/icons/checkmark.png"))
        self._open_mark = QtGui.QPixmap(_fromUtf8(":/Controls/icons/openmark.png"))
        self._semiopen_mark = QtGui.QPixmap(_fromUtf8(":/Controls/icons/semiopenmark.png"))
        self.progress_model = progress_model

        for dropdown_index, list_view in enumerate(self.progress_model.section_views):
            self.process_page.addWidget(list_view)
            self.active_page_dropdown.addItem(list_view.accessibleName())
            self.active_page_dropdown.setItemData(dropdown_index, self._open_mark, QtCore.Qt.DecorationRole)
            list_view.model().itemChanged.connect(self.check_progress_status)

        self.active_page_dropdown.currentIndexChanged.connect(lambda: self.go_to_page(self.active_page_dropdown.currentText()))

        # Remove once the ui_main_process_dock was adopted to the new model
        self.active_page_dropdown.setCurrentIndex(2)
        self.active_page_dropdown.setCurrentIndex(0)

    def check_progress_status(self, changed_item):
        # explicitly check the state, since otherwise the next section gets changed, too
        if changed_item.checkState() == 1:
            current_index = self.active_page_dropdown.currentIndex()
            self.active_page_dropdown.setItemData(current_index, self._semiopen_mark, QtCore.Qt.DecorationRole)

        elif changed_item.checkState() == 2:
            model = changed_item.model()
            section_done = True
            index = 0
            while model.item(index) and section_done:
                item_done = model.item(index).checkState()
                section_done = section_done and item_done
                index += 1

            if section_done:
                current_index = self.active_page_dropdown.currentIndex()
                self.active_page_dropdown.setItemData(current_index, self._check_mark, QtCore.Qt.DecorationRole)
                self.active_page_dropdown.setCurrentIndex(current_index+1)

    def go_to_page(self, selection_name):
        for child in self.process_page.children():
            if isinstance(child, QtGui.QListView) and child.accessibleName() == selection_name:
                self.process_page.setCurrentWidget(child)
                break

    def set_checkbox_on_page(self, checkbox_name, page_name, check_yes_no):
        if isinstance(check_yes_no, bool):
            page = self.findChild(QtGui.QWidget, page_name)
            checkbox = page.findChild(QtGui.QPushButton, checkbox_name)

            if checkbox:
                checkbox.setChecked(check_yes_no)

    def is_checkbox_on_page_checked(self, checkbox_name, page_name):
        page = self.process_page.findChild(QtGui.QWidget, page_name)
        return page.findChild(QtGui.QPushButton, checkbox_name).isChecked()

    def set_current_page_done(self, value):
        if isinstance(value, bool):
            page_name = self.active_page_dropdown.currentText()
            page = self.selection_to_page[page_name]

            if (page_name) == page.accessibleName():
                index = self.active_page_dropdown.currentIndex()
                self.active_page_dropdown.setItemData(index, self._check_mark, Qt.DecorationRole)
                self.active_page_dropdown.setCurrentIndex((index+1) % len(self.selection_to_page))


class ProjectDoesNotExist_dialog(QtGui.QDialog, Ui_ProjectDoesNotExist_dialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)


class ProjectSettings_form(QtGui.QDialog, Ui_project_settings_form):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.defaults = {}
        self.municipals = [{}]
        self.location_postal.editingFinished.connect(self.find_municipal_information)
        self.municipal_information = MunicipalInformationTree()

        if self.municipal_information.tree == {}:
            self.municipal_information.split_data_to_tree_model()

        for field in self.form.findChildren(QtGui.QLineEdit)[:]:
            self.defaults[field.objectName()] = field.text()
            field.textChanged.connect(partial(self.text_changed, field))

    def text_changed(self, input_field):
        if input_field.text() != self.defaults[input_field.objectName()]:
            input_field.setStyleSheet('color: rgb(0,0,0)')

    def find_municipal_information(self):
        postcode = self.location_postal.text()

        if postcode:
            try:
                l0_key = postcode[0]
                l1_key = postcode[1]
                l2_key = postcode[2:]
                municipals = self.municipal_information.tree[l0_key][l1_key][l2_key]
            except (KeyError, ValueError):
                self.location_postal.setStyleSheet('color: rgb(255, 0, 0)')
                return

            self.municipals = municipals
            if len(municipals) == 1:
                self.lineedit_city_layout()
                self.fill_municipal_information(0)

            elif len(municipals) > 1:
                self.combobox_city_layout()
                self.location_city.clear()

                for municipal in municipals:
                    self.location_city.addItem(_fromUtf8(municipal['NAME']))

                self.location_city.currentIndexChanged.connect(self.fill_municipal_information)
                self.fill_municipal_information(0)

    def fill_municipal_information(self, index):
        municipal = self.municipals[index]

        if issubclass(type(self.location_city), QtGui.QLineEdit):
            city_name = _fromUtf8(municipal['NAME'])
            self.location_city.setText(city_name)

        try:
            pop_dens = '{}'.format(municipal['POP_DENS'])
            self.population_density.setText(pop_dens)
        except KeyError as Error:
            print(self.__module__, Error)

        try:
            avg_yoc = '{}'.format(municipal['AVG_YOC'])
            self.average_build_year.setText(avg_yoc)
        except KeyError as Error:
            print(self.__module__, Error)

    def combobox_city_layout(self):
        location_box = self.gridLayout.findChild(QtGui.QHBoxLayout, 'location_layout')
        city_edit = location_box.itemAt(0).widget()

        if isinstance(city_edit, QtGui.QLineEdit):
            location_box.removeWidget(city_edit)
            city_edit.deleteLater()
            self.location_city = QtGui.QComboBox()
            self.location_city.setObjectName('location_city')
            self.location_city.setMinimumWidth(228)
            location_box.insertWidget(0, self.location_city)

    def lineedit_city_layout(self):
        location_box = self.gridLayout.findChild(QtGui.QHBoxLayout, 'location_layout')
        city_edit = location_box.itemAt(0).widget()

        if isinstance(city_edit, QtGui.QComboBox):
            location_box.removeWidget(city_edit)
            city_edit.deleteLater()
            self.location_city = QtGui.QLineEdit(self.form)
            self.location_city.setMinimumWidth(228)
            self.location_city.setObjectName(_fromUtf8("location_city"))
            self.location_city.setStyleSheet('color: rgb(0,0,0)')
            location_box.insertWidget(0, self.location_city)


class ModularInfo_dialog(QtGui.QDialog, Ui_ModularInfo_dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


class Modular_dialog(QtGui.QDialog, Ui_Modular_dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.setContentsMargins(500, 500, 0, 0)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.help_dialog = ModularInfo_dialog()
        self.buttonBox.button(QtGui.QDialogButtonBox.Help).clicked.connect(self.help_dialog.show)

    def set_dialog_text(self, text, title=""):

        if not title.isspace():
            self.setWindowTitle(title)

        if text is not None and not text.isspace():

            html_prefix = ('<p align="center" style=" margin-top:0px; margin-bottom:0px; '
                           'margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">')

            html_postfix = "</p>"
            browser_text = html_prefix + text + html_postfix
            self.textBrowser.setHtml(QtGui.QApplication.translate('InvestigationAreaSelected_dialog', browser_text, None))


class RequestWmsUrl_dialog(QtGui.QDialog, Ui_RequestWmsUrl_dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)


class EstimatedEnergyDemand_dialog(QtGui.QDialog, Ui_EstimatedEnergyDemand_dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        layer_dict = QgsMapLayerRegistry.instance().mapLayers()
        vector_layers = filter(lambda x: x.type() == QgsMapLayer.VectorLayer, layer_dict.values())
        for layer in vector_layers:
            self.input_layer.addItem(layer.name())
            self.output_layer.addItem(layer.name())

        self.input_layer.currentIndexChanged.connect(self.update_field_dropdowns)

    def update_field_dropdowns(self, index):
        print(index)
        layer = layer_interaction.find_layer_by_name(self.input_layer.currentText())
        provider = layer.dataProvider()
        fields = provider.fieldNameMap().keys()
        self.area.clear()
        self.perimeter.clear()
        self.height.clear()
        self.floors.clear()
        self.yoc.clear()

        for field in fields:
            self.area.addItem(field)
            self.perimeter.addItem(field)
            self.height.addItem(field)
            self.floors.addItem(field)
            self.yoc.addItem(field)