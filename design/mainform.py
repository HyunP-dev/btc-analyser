# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainform.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QDockWidget, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QSplitter, QStatusBar,
    QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 625)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.addrEdit = QLineEdit(self.centralwidget)
        self.addrEdit.setObjectName(u"addrEdit")

        self.horizontalLayout.addWidget(self.addrEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.detailView = QTreeWidget(self.tab)
        self.detailView.setObjectName(u"detailView")

        self.verticalLayout_3.addWidget(self.detailView)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.tab_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.txView = QTreeWidget(self.splitter)
        self.txView.setObjectName(u"txView")
        self.txView.setRootIsDecorated(False)
        self.txView.setUniformRowHeights(True)
        self.splitter.addWidget(self.txView)
        self.txIOView = QTreeWidget(self.splitter)
        self.txIOView.setObjectName(u"txIOView")
        self.txIOView.setRootIsDecorated(False)
        self.txIOView.setUniformRowHeights(True)
        self.txIOView.setSortingEnabled(True)
        self.splitter.addWidget(self.txIOView)

        self.horizontalLayout_2.addWidget(self.splitter)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 870, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.webEngineView = QWebEngineView(self.dockWidgetContents_2)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setEnabled(True)
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.webEngineView)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.dockWidget_2)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bitcoin Analyser", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"address:", None))
        ___qtreewidgetitem = self.detailView.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Property", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Details", None))
        ___qtreewidgetitem1 = self.txView.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Timestamp", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Transaction ID", None));
        ___qtreewidgetitem2 = self.txIOView.headerItem()
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Sanctions", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Address", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"Visualization", None))
    # retranslateUi

