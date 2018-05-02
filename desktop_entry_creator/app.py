#! /usr/bin/env python3

from os.path import dirname, expanduser
from os import access
from subprocess import call

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from slugify import slugify

DESKTOP_ENTRY_DIR = expanduser('~/.local/share/applications')


def absolute_path(relative_path):
    return dirname(__file__) + '/' + relative_path

UI_GLADE_FILE = absolute_path('res/ui.glade')


def is_blank_string(string):
    if string == '' or string.isspace():
        return True
    return False


class Entry:
    def __init__(self, key, value='', is_required=True):
        self.key = key
        self.value = value
        self.is_required = is_required


class App:
    entries = {
        'Name': Entry('Name'),
        'Exec': Entry('Exec'),
        'Icon': Entry('Icon'),
        'Type': Entry('Type', 'Application'),
        'Comment': Entry('Comment', is_required=False),
        'GenericName': Entry('GenericName', is_required=False),
        'Categories': Entry('Categories', is_required=False),
        'Keywords': Entry('Keywords', is_required=False),
    }
    use_optional_entries = False


    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_GLADE_FILE)
        self.builder.connect_signals(self)

        self.window = self.builder.get_object('MainWindow')
        self.window.connect('delete-event', Gtk.main_quit)

        self.message_dialog = self.builder.get_object('MessageDialog')
        self.message_dialog_label = self.builder.get_object('MessageDialogLabel')
        self.message_dialog_image = self.builder.get_object('MessageDialogImage')

        self.window.show_all()


    def on_text_changed(self, text_entry):
        self.entries[text_entry.get_name()].value = text_entry.get_text()


    def on_icon_selected(self, file_dialog):
        self.entries['Icon'].value = file_dialog.get_filename()


    def filled_required_entries(self):
        for entry in self.entries.values():
            if entry.is_required and is_blank_string(entry.value):
                return False

        return True


    def message_dialog_hide(self, message_dialog_button):
        self.message_dialog.hide()


    def toggle_optional_entries(self, _):
        self.use_optional_entries ^= True


    def show_message_dialog(self, dialog_type, text):
        if dialog_type == 'Success':
            image_path = 'res/success.png'
        elif dialog_type == 'Alert':
            image_path = 'res/alert.png'
        elif dialog_type == 'Error':
            image_path = 'res/error.png'
        else:
            raise "Invalid dialog type!"

        self.message_dialog.set_title(dialog_type)
        self.message_dialog_label.set_text(text)
        self.message_dialog_image.set_from_file(absolute_path(image_path))
        self.message_dialog.show()


    def on_click_save(self, button):
        if (self.filled_required_entries()):
            name_slug = slugify(self.entries['Name'].value)
            desktop_entry_path = '{}/{}.desktop'.format(DESKTOP_ENTRY_DIR, name_slug)
            try:
                with open(desktop_entry_path, 'w+') as desktop_entry_file:
                    desktop_entry_file.write('[Desktop Entry]\n')
                    for entry in self.entries.values():
                        if entry.is_required or self.use_optional_entries \
                                and not is_blank_string(entry.value):
                            desktop_entry_file.write(entry.key + '=' + entry.value + '\n')
                self.show_message_dialog(dialog_type='Success',
                    text='Desktop entry\n{}\ncreated successfully.'.format(desktop_entry_path))
            except Exception as e:
                self.show_message_dialog(dialog_type='Error',
                    text=str(e))
        else:
            self.show_message_dialog(dialog_type='Alert',
                text='Fill all required entries before saving.')


def main():
    App()
    Gtk.main()


if __name__ == '__main__':
    main()
