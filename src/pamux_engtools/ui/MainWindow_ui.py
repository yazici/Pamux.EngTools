# Form implementation generated from reading ui file 'c:\src\Pamux.EngTools\src\pamux_engtools\ui\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelQuery = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelQuery.setObjectName("labelQuery")
        self.horizontalLayout.addWidget(self.labelQuery)
        self.editQuery = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.editQuery.setText("")
        self.editQuery.setObjectName("editQuery")
        self.horizontalLayout.addWidget(self.editQuery)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 80))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabHome = QtWidgets.QWidget()
        self.tabHome.setObjectName("tabHome")
        self.tabWidget.addTab(self.tabHome, "")
        self.tabAssetLibrary = QtWidgets.QWidget()
        self.tabAssetLibrary.setObjectName("tabAssetLibrary")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tabAssetLibrary)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableAssetContainers = QtWidgets.QTableWidget(parent=self.tabAssetLibrary)
        self.tableAssetContainers.setObjectName("tableAssetContainers")
        self.tableAssetContainers.setColumnCount(3)
        self.tableAssetContainers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableAssetContainers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAssetContainers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAssetContainers.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_3.addWidget(self.tableAssetContainers)
        self.treeAssets = QtWidgets.QTreeWidget(parent=self.tabAssetLibrary)
        self.treeAssets.setObjectName("treeAssets")
        self.treeAssets.headerItem().setText(0, "1")
        self.horizontalLayout_3.addWidget(self.treeAssets)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tabAssetLibrary, "")
        self.tabTextToSpeech = QtWidgets.QWidget()
        self.tabTextToSpeech.setObjectName("tabTextToSpeech")
        self.tabWidget.addTab(self.tabTextToSpeech, "")
        self.tabNodeEditor = QtWidgets.QWidget()
        self.tabNodeEditor.setObjectName("tabNodeEditor")
        self.tabWidget.addTab(self.tabNodeEditor, "")
        self.tabDistribution = QtWidgets.QWidget()
        self.tabDistribution.setObjectName("tabDistribution")
        self.tabWidget.addTab(self.tabDistribution, "")
        self.tabMonetization = QtWidgets.QWidget()
        self.tabMonetization.setObjectName("tabMonetization")
        self.tabWidget.addTab(self.tabMonetization, "")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabSettings)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2a = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2a.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2a.setSpacing(10)
        self.horizontalLayout_2a.setObjectName("horizontalLayout_2a")
        self.labelUnityAssetDownloadRoot = QtWidgets.QLabel(parent=self.tabSettings)
        self.labelUnityAssetDownloadRoot.setObjectName("labelUnityAssetDownloadRoot")
        self.horizontalLayout_2a.addWidget(self.labelUnityAssetDownloadRoot)
        self.editUnityAssetDownloadRoot = QtWidgets.QLineEdit(parent=self.tabSettings)
        self.editUnityAssetDownloadRoot.setObjectName("editUnityAssetDownloadRoot")
        self.horizontalLayout_2a.addWidget(self.editUnityAssetDownloadRoot)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2a)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelUnityAssetMetadataRoot = QtWidgets.QLabel(parent=self.tabSettings)
        self.labelUnityAssetMetadataRoot.setObjectName("labelUnityAssetMetadataRoot")
        self.horizontalLayout_2.addWidget(self.labelUnityAssetMetadataRoot)
        self.editUnityAssetMetadataRoot = QtWidgets.QLineEdit(parent=self.tabSettings)
        self.editUnityAssetMetadataRoot.setObjectName("editUnityAssetMetadataRoot")
        self.horizontalLayout_2.addWidget(self.editUnityAssetMetadataRoot)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tabSettings, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 937, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(parent=self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(parent=self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(parent=self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menuBar)
        self.actionQuit = QtGui.QAction(parent=MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNew)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pamux Studios Engineering Tools"))
        self.labelQuery.setText(_translate("MainWindow", "Query"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHome), _translate("MainWindow", "Home"))
        item = self.tableAssetContainers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableAssetContainers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Company"))
        item = self.tableAssetContainers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Category"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAssetLibrary), _translate("MainWindow", "Asset Library"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTextToSpeech), _translate("MainWindow", "Text To Speech"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNodeEditor), _translate("MainWindow", "Node Editor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDistribution), _translate("MainWindow", "Distribution"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMonetization), _translate("MainWindow", "Monetization"))
        self.labelUnityAssetDownloadRoot.setText(_translate("MainWindow", "Unity Asset Download Root"))
        self.editUnityAssetDownloadRoot.setText(_translate("MainWindow", "D:\\AppData\\Roaming\\Unity\\Asset Store-5.x"))
        self.labelUnityAssetMetadataRoot.setText(_translate("MainWindow", "Unity Asset Metadata Root"))
        self.editUnityAssetMetadataRoot.setText(_translate("MainWindow", "C:\\src\\Pamux.EngTools\\Data\\UnityAssetStore"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), _translate("MainWindow", "Settings"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
