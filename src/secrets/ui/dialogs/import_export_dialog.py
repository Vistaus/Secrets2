import gi
import json
import csv
import os
from typing import Dict, List, Tuple, Optional

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw, Gio, GLib

from secrets.app_info import APP_ID


@Gtk.Template(resource_path=f'/{APP_ID.replace(".", "/")}/ui/dialogs/import_export_dialog.ui')
class ImportExportDialog(Adw.Window):
    """Dialog for importing and exporting password data."""

    __gtype_name__ = "ImportExportDialog"

    # Template widgets
    export_json_button = Gtk.Template.Child()
    export_csv_button = Gtk.Template.Child()
    import_json_button = Gtk.Template.Child()
    import_csv_button = Gtk.Template.Child()

    def __init__(self, parent_window, password_store, toast_manager, refresh_callback=None, **kwargs):
        super().__init__(**kwargs)

        self.set_transient_for(parent_window)

        self.password_store = password_store
        self.toast_manager = toast_manager
        self.refresh_callback = refresh_callback

        self._setup_signals()
    
    def _setup_signals(self):
        """Setup signal connections for UI elements."""
        # Connect signals
        self.export_json_button.connect("clicked", self._on_export_json)
        self.export_csv_button.connect("clicked", self._on_export_csv)
        self.import_json_button.connect("clicked", self._on_import_json)
        self.import_csv_button.connect("clicked", self._on_import_csv)
    
    def _on_export_json(self, button):
        """Export passwords to JSON format."""
        file_dialog = Gtk.FileDialog()
        file_dialog.set_title("Export to JSON")
        file_dialog.set_initial_name("passwords_export.json")
        
        # Set up file filter
        json_filter = Gtk.FileFilter()
        json_filter.set_name("JSON files")
        json_filter.add_pattern("*.json")
        
        filter_list = Gio.ListStore.new(Gtk.FileFilter)
        filter_list.append(json_filter)
        file_dialog.set_filters(filter_list)
        
        file_dialog.save(self, None, self._on_export_json_response, None)
    
    def _on_export_json_response(self, dialog, result, user_data):
        """Handle JSON export file selection."""
        try:
            file = dialog.save_finish(result)
            if file:
                self._export_to_json(file.get_path())
        except Exception as e:
            self.toast_manager.show_error(f"Export cancelled or failed: {e}")
    
    def _export_to_json(self, file_path: str):
        """Export passwords to JSON file."""
        try:
            passwords = self.password_store.list_passwords()
            export_data = []
            
            for password_path in passwords:
                details = self.password_store.get_parsed_password_details(password_path)
                if 'error' not in details:
                    export_data.append({
                        'path': password_path,
                        'password': details.get('password', ''),
                        'username': details.get('username', ''),
                        'url': details.get('url', ''),
                        'notes': details.get('notes', '')
                    })
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            self.toast_manager.show_success(f"Exported {len(export_data)} passwords to {file_path}")
            
        except Exception as e:
            self.toast_manager.show_error(f"Export failed: {e}")
    
    def _on_export_csv(self, button):
        """Export passwords to CSV format."""
        file_dialog = Gtk.FileDialog()
        file_dialog.set_title("Export to CSV")
        file_dialog.set_initial_name("passwords_export.csv")
        
        # Set up file filter
        csv_filter = Gtk.FileFilter()
        csv_filter.set_name("CSV files")
        csv_filter.add_pattern("*.csv")
        
        filter_list = Gio.ListStore.new(Gtk.FileFilter)
        filter_list.append(csv_filter)
        file_dialog.set_filters(filter_list)
        
        file_dialog.save(self, None, self._on_export_csv_response, None)
    
    def _on_export_csv_response(self, dialog, result, user_data):
        """Handle CSV export file selection."""
        try:
            file = dialog.save_finish(result)
            if file:
                self._export_to_csv(file.get_path())
        except Exception as e:
            self.toast_manager.show_error(f"Export cancelled or failed: {e}")
    
    def _export_to_csv(self, file_path: str):
        """Export passwords to CSV file."""
        try:
            passwords = self.password_store.list_passwords()
            
            with open(file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Path', 'Password', 'Username', 'URL', 'Notes'])
                
                exported_count = 0
                for password_path in passwords:
                    details = self.password_store.get_parsed_password_details(password_path)
                    if 'error' not in details:
                        writer.writerow([
                            password_path,
                            details.get('password', ''),
                            details.get('username', ''),
                            details.get('url', ''),
                            details.get('notes', '')
                        ])
                        exported_count += 1
            
            self.toast_manager.show_success(f"Exported {exported_count} passwords to {file_path}")
            
        except Exception as e:
            self.toast_manager.show_error(f"Export failed: {e}")
    
    def _on_import_json(self, button):
        """Import passwords from JSON format."""
        file_dialog = Gtk.FileDialog()
        file_dialog.set_title("Import from JSON")
        
        # Set up file filter
        json_filter = Gtk.FileFilter()
        json_filter.set_name("JSON files")
        json_filter.add_pattern("*.json")
        
        filter_list = Gio.ListStore.new(Gtk.FileFilter)
        filter_list.append(json_filter)
        file_dialog.set_filters(filter_list)
        
        file_dialog.open(self, None, self._on_import_json_response, None)
    
    def _on_import_json_response(self, dialog, result, user_data):
        """Handle JSON import file selection."""
        try:
            file = dialog.open_finish(result)
            if file:
                self._import_from_json(file.get_path())
        except Exception as e:
            self.toast_manager.show_error(f"Import cancelled or failed: {e}")
    
    def _import_from_json(self, file_path: str):
        """Import passwords from JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                import_data = json.load(f)
            
            imported_count = 0
            skipped_count = 0
            
            for entry in import_data:
                if isinstance(entry, dict) and 'path' in entry:
                    path = entry['path']
                    password = entry.get('password', '')
                    username = entry.get('username', '')
                    url = entry.get('url', '')
                    notes = entry.get('notes', '')
                    
                    # Build content in pass format
                    content_lines = [password]
                    if username:
                        content_lines.append(f"username: {username}")
                    if url:
                        content_lines.append(f"url: {url}")
                    if notes:
                        content_lines.append(f"notes: {notes}")
                    
                    content = '\n'.join(content_lines)
                    
                    # Try to import
                    success, message = self.password_store.insert_password(path, content, multiline=True, force=False)
                    if success:
                        imported_count += 1
                    else:
                        skipped_count += 1
            
            self.toast_manager.show_success(f"Imported {imported_count} passwords, skipped {skipped_count}")

            # Refresh the UI to show imported passwords
            if imported_count > 0:
                self._refresh_password_list()

        except Exception as e:
            self.toast_manager.show_error(f"Import failed: {e}")
    
    def _on_import_csv(self, button):
        """Import passwords from CSV format."""
        file_dialog = Gtk.FileDialog()
        file_dialog.set_title("Import from CSV")
        
        # Set up file filter
        csv_filter = Gtk.FileFilter()
        csv_filter.set_name("CSV files")
        csv_filter.add_pattern("*.csv")
        
        filter_list = Gio.ListStore.new(Gtk.FileFilter)
        filter_list.append(csv_filter)
        file_dialog.set_filters(filter_list)
        
        file_dialog.open(self, None, self._on_import_csv_response, None)
    
    def _on_import_csv_response(self, dialog, result, user_data):
        """Handle CSV import file selection."""
        try:
            file = dialog.open_finish(result)
            if file:
                self._import_from_csv(file.get_path())
        except Exception as e:
            self.toast_manager.show_error(f"Import cancelled or failed: {e}")
    
    def _import_from_csv(self, file_path: str):
        """Import passwords from CSV file."""
        try:
            imported_count = 0
            skipped_count = 0
            
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    path = row.get('Path', '').strip()
                    password = row.get('Password', '').strip()
                    username = row.get('Username', '').strip()
                    url = row.get('URL', '').strip()
                    notes = row.get('Notes', '').strip()
                    
                    if not path or not password:
                        skipped_count += 1
                        continue
                    
                    # Build content in pass format
                    content_lines = [password]
                    if username:
                        content_lines.append(f"username: {username}")
                    if url:
                        content_lines.append(f"url: {url}")
                    if notes:
                        content_lines.append(f"notes: {notes}")
                    
                    content = '\n'.join(content_lines)
                    
                    # Try to import
                    success, message = self.password_store.insert_password(path, content, multiline=True, force=False)
                    if success:
                        imported_count += 1
                    else:
                        skipped_count += 1
            
            self.toast_manager.show_success(f"Imported {imported_count} passwords, skipped {skipped_count}")

            # Refresh the UI to show imported passwords
            if imported_count > 0:
                self._refresh_password_list()

        except Exception as e:
            self.toast_manager.show_error(f"Import failed: {e}")

    def _refresh_password_list(self):
        """Refresh the password list in the main window."""
        if self.refresh_callback:
            self.refresh_callback()
