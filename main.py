import datetime
import pickle
import os
from multiprocessing import Pool

from PySide6.QtWidgets import *

from generated.sdn import SdnList
from design.mainform import Ui_MainWindow
from toolkit import bitcoin


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.addrEdit.returnPressed.connect(self.search)
        self.txView.itemSelectionChanged.connect(self.txView_itemSelectionChanged)

        self.blacks = set()
        with open('dataset/sdn.pickle', 'rb') as f:
            self.sdn: SdnList = pickle.loads(f.read())
        for entry in self.sdn.sdn_entry:
            if entry.id_list:
                for id_ in entry.id_list.id:
                    if id_.id_type == "Digital Currency Address - XBT":
                        self.blacks.add(id_.id_number)
    def txView_itemSelectionChanged(self):
        item = self.txView.currentItem()
        tx_id = item.toolTip(0)
        tx = bitcoin.get_tx_info(tx_id)

        self.txIOView.clear()
        for input_ in sorted(tx["inputs"], key=lambda e: e["value"]):
            item = QTreeWidgetItem([input_["address"], str(input_["address"] in self.blacks), str(input_["value"] / 100)])
            self.txIOView.addTopLevelItem(item)
        for output in sorted(tx["outputs"], key=lambda e: e["value"]):
            item = QTreeWidgetItem([output["address"], str(output["address"] in self.blacks), "-" + str(output["value"] / 100)])
            self.txIOView.addTopLevelItem(item)

    def search(self):
        addr = self.addrEdit.text()
        balance_info = bitcoin.get_balance_info(addr)
        balance_root = QTreeWidgetItem(["Balance Information"])
        balance_root.addChildren([
            QTreeWidgetItem(["Address", balance_info.address]),
            QTreeWidgetItem(["TXs", str(balance_info.txs)]),
            QTreeWidgetItem(["Received", str(balance_info.received)])
        ])



        target_entry = None
        for entry in self.sdn.sdn_entry:
            if entry.id_list is None:
                continue
            for id_ in entry.id_list.id:
                if id_.id_number == addr:
                    target_entry = entry
                    break

        self.detailView.clear()
        self.detailView.addTopLevelItem(balance_root)
        balance_root.setFirstColumnSpanned(True)

        if target_entry:
            ofac_root = QTreeWidgetItem(["OFAC Information"])

            program_root = QTreeWidgetItem(["Programs"])
            id_root = QTreeWidgetItem(["Identifications"])
            aka_root = QTreeWidgetItem(["A.K.A. List"])
            addr_root = QTreeWidgetItem(["Addresses"])

            for program in target_entry.program_list.program:
                program_root.addChild(QTreeWidgetItem(["Program", program]))

            for id_ in target_entry.id_list.id:
                id_root.addChild(QTreeWidgetItem([id_.id_type, id_.id_number]))

            for aka in target_entry.aka_list.aka:
                aka_root.addChild(QTreeWidgetItem([aka.type_value, aka.last_name]))

            for i, address in enumerate(target_entry.address_list.address):
                addr_item = QTreeWidgetItem([f"Address #{i + 1}"])
                addr_item.addChild(QTreeWidgetItem(["Country", address.country or ""]))
                addr_item.addChild(QTreeWidgetItem(["City", address.city or ""]))
                addr_item.addChild(QTreeWidgetItem(["State or Province", address.state_or_province or ""]))
                addr_root.addChild(addr_item)

            ofac_root.addChildren([
                QTreeWidgetItem(["First Name", target_entry.first_name]),
                QTreeWidgetItem(["Last Name", target_entry.last_name]),
                QTreeWidgetItem(["SDN Type", target_entry.sdn_type]),
                QTreeWidgetItem(["Remarks", target_entry.remarks])
            ])
            ofac_root.addChild(program_root)
            ofac_root.addChild(id_root)
            ofac_root.addChild(aka_root)
            ofac_root.addChild(addr_root)
            self.detailView.addTopLevelItem(ofac_root)
            ofac_root.setFirstColumnSpanned(True)

        self.detailView.expandAll()

        self.txView.clear()
        self.txIOView.clear()
        tx_ids = bitcoin.get_tx_ids(addr)

        with Pool(12) as pool:
            txs = pool.map(bitcoin.get_tx_info, tx_ids)

        for tx_id in tx_ids:
            short_tx_id = tx_id[:5] + "..." + tx_id[-5:]
            tx_item = QTreeWidgetItem([short_tx_id,
                                       str(datetime.datetime.fromtimestamp(dict(zip(tx_ids, txs))[tx_id]["time"]))])
            tx_item.setToolTip(0, tx_id)
            self.txView.addTopLevelItem(tx_item)


if __name__ == "__main__":
    if not os.path.exists("dataset/sdn.pickle"):
        from xsdata.formats.dataclass.parsers import XmlParser

        parser = XmlParser()
        sdn = parser.parse("dataset/sdn.xml", SdnList)

        with open('dataset/sdn.pickle', 'wb') as f:
            f.write(pickle.dumps(sdn))

    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
