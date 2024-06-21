#!/usr/bin/env python3
"""PB/Hybrid panel Visual inspection GUI.."""
import json
import sys
from pathlib import Path

try:
    import itkdb_gtk

except ImportError:
    cwd = Path(__file__).parent.parent
    sys.path.append(cwd.as_posix())

from itkdb_gtk import dbGtkUtils, ITkDBlogin, ITkDButils

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, Gio

HELP_LINK="https://itkdb-gtk.docs.cern.ch"

class PanelVisualInspection(dbGtkUtils.ITkDBWindow):
    """PB/Hybryd panel visual inspection GUI."""
    SN, PASSED, F_NAME, F_PATH, ALL = range(5)

    def __init__(self, session, help=HELP_LINK):
        super().__init__(title="ITkDB Dashboard",
                         session=session,
                         show_search="Find object with given SN.",
                         help=help)

        # action button in header
        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="document-send-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        button.set_tooltip_text("Click to upload ALL tests.")
        button.connect("clicked", self.upload_tests)
        self.hb.pack_end(button)

        grid = Gtk.Grid(column_spacing=5, row_spacing=1)
        self.mainBox.pack_start(grid, False, False, 5)

        lbl = Gtk.Label(label="Serial Number")
        lbl.set_xalign(0)
        grid.attach(lbl, 0, 0, 1, 1)

        self.SN = dbGtkUtils.TextEntry()
        self.SN.connect("text_changed", self.SN_ready)
        self.SN.widget.set_tooltip_text("Enter SN of PWD or Hybrid panel.")
        grid.attach(self.SN.widget, 1, 0, 1, 1)

        self.panel_type = Gtk.Label(label="")
        grid.attach(self.panel_type, 2, 0, 1, 1)

        # Paned object
        paned = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL)
        paned.set_size_request(-1, 200)
        self.mainBox.pack_start(paned, True, True, 5)

        # the list of attachments
        tree_view = self.create_tree_view()
        paned.add1(tree_view)

        # The text view
        paned.add2(self.message_panel.frame)


        self.show_all()

        dbGtkUtils.setup_scanner(self.get_qrcode)

    def create_tree_view(self, size=150):
        """Create the TreeView with the children."""
        model = Gtk.ListStore(str, bool, str, str)
        self.tree = Gtk.TreeView(model=model)
        self.tree.connect("button-press-event", self.button_pressed)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.tree)
        scrolled.set_size_request(-1, size)
        
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("SN", renderer, text=PanelVisualInspection.SN)
        self.tree.append_column(column)

        renderer = Gtk.CellRendererToggle()
        renderer.set_property("activatable", True)
        renderer.set_property("radio", True)
        renderer.set_padding(5, 0)
        
        x, y = renderer.get_alignment()
        renderer.set_alignment(0, y)
        # renderer.set_property("inconsistent", True)
        renderer.connect("toggled", self.btn_toggled)
        
        column = Gtk.TreeViewColumn("Passed", renderer, active=PanelVisualInspection.PASSED)
        self.tree.append_column(column)


        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Image", renderer, text=PanelVisualInspection.F_NAME)
        self.tree.append_column(column)


        return scrolled

    def btn_toggled(self, renderer, path, *args):
        """Toggled."""
        model = self.tree.get_model()
        val = not model[path][PanelVisualInspection.PASSED]
        model[path][PanelVisualInspection.PASSED] = val
        

    def button_pressed(self, tree, event):
        """Button pressed on tree view."""
        # double click shows attachments
        if event.button == 1 and event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
            self.write_message("This is a double click.\n")
            return

        if event.button != 3:
            return

        # Create popup menu
        select = self.tree.get_selection()
        model, iter = select.get_selected()
        values = None
        if iter:
            values = model[iter]

        if not iter:
            P = tree.get_path_at_pos(event.x, event.y)
            if P:
                print(P[0].to_string())
                iter = model.get_iter(P[0])
                values = model[iter]

        if not values:
            return
        
        menu = Gtk.Menu()
        item_show = Gtk.MenuItem(label="Upload Image")
        item_show.connect("activate", self.on_upload_image, (model, iter, values))
        menu.append(item_show)
        
        menu.show_all()
        menu.popup_at_pointer(event)

    def on_upload_image(self, item, data):
        """Choose file."""
        fdlg = Gtk.FileChooserNative(action=Gtk.FileChooserAction.OPEN, accept_label="Select")
        response = fdlg.run()
        if response == Gtk.ResponseType.ACCEPT:
            ifiles = [ipath for ipath in fdlg.get_filenames()]
            if len(ifiles)<1:
                return
             
            if len(ifiles) > 1:
                dbGtkUtils.complain("More than one file selected","Choosing first.")
            
            fnam = ifiles[0]
            model, iter, val = data
            model.set_value(iter, PanelVisualInspection.F_PATH, fnam)
            model.set_value(iter, PanelVisualInspection.F_NAME, Path(fnam).name)
            
                
        self.write_message("Upload image\n")


    def SN_ready(self, *args):
        """SN is ready in the TextEnttry."""
        SN = self.SN.get_text()
        # GEt children.
        panel = ITkDButils.get_DB_component(self.session, SN)
        if panel is None:
            self.write_message(ITkDButils.get_db_response())
            return

        SN = panel["serialNumber"]
        args[0].set_text(SN)

        if "USED" in SN:
            # Powerboard Carrier
            if not SN[6].isdigit():
                dbGtkUtils.complain("Not a Powerboard Carrier",
                                    "{}: wrong SN for a powerboard carrier".format(SN))
                self.SN.widget.set_text("")
                return

            self.panel_type.set_text("PWB carrier")

        elif "USET" in SN:
            # Hybrid test panel
            if not SN[6].isdigit or int(SN[6])>5:
                dbGtkUtils.complain("Not a Hybrid Test Panel",
                                    "{}: wrong SN for a hybrid test panel".format(SN))
                self.SN.widget.set_text("")
                return

        else:
            dbGtkUtils.complain("Invalid SN.",
                "{}\nNot a PWB carrier not HYB test panel.".format(SN))
            self.SN.widget.set_text("")
            return

        # GEt children.
        children = []
        for child in panel["children"]:
            if child["component"] is not None:
                if child["componentType"]["name"] == "Powerboard":
                    children.append(child["component"]["serialNumber"])

        model = Gtk.ListStore(str, bool, str, str)
        for child in children:
            model.append([child, True, "", ""])
            
        self.tree.set_model(model)


    def upload_tests(self, *args):
        """Upload the current test."""
        SN = self.SN.get_text()

    def get_qrcode(self, fd, state, reader):
        """Read SN from scanner."""
        txt = dbGtkUtils.scanner_get_line(reader)
        self.write_message("SN: {}\n".format(txt))
        self.SN_ready(txt, self.SN.widget)


def main():
    """Main entry."""
    # DB login
    dlg = ITkDBlogin.ITkDBlogin()
    client = dlg.get_client()
    if client is None:
        print("Could not connect to DB with provided credentials.")
        dlg.die()
        sys.exit()

    client.user_gui = dlg

    gTest = PanelVisualInspection(client)

    gTest.present()
    gTest.connect("destroy", Gtk.main_quit)
    try:
        Gtk.main()

    except KeyboardInterrupt:
        print("Arrrgggg!!!")

    dlg.die()
