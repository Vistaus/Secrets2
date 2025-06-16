# Secrets - A GTK4/Libadwaita GUI for pass

Secrets is a modern desktop application that provides a clean and user-friendly graphical interface for managing your passwords with `pass`, the standard unix password manager. It leverages the power and security of `pass`, GPG, and Git, wrapped in a beautiful GTK4/Libadwaita UI.

## ✨ Features

### 🔐 **Password Management**
- **Hierarchical folder organization** with expandable tree view
- **Add, edit, delete, and move** password entries
- **Structured password fields**: username, password, URL, notes, TOTP
- **TOTP support** with live 6-digit codes and countdown timers
- **Recovery codes management** for 2FA backup
- **Password generator** with customizable options and strength indicator
- **Copy to clipboard** with automatic clearing for security

### 🔍 **Search & Navigation**
- **Full-text search** across all password content
- **Real-time filtering** as you type
- **Keyboard shortcuts** for efficient navigation
- **Quick access** to frequently used passwords

### 🎨 **Modern Interface**
- **GTK4/Libadwaita design** following GNOME HIG
- **Adaptive layout** with split-view navigation
- **Dark/light theme support** with system integration
- **Toast notifications** for user feedback
- **Responsive design** that works on different screen sizes

### 🔧 **Advanced Features**
- **Advanced Git integration** with platform support and repository management
- **GPG integration** with automatic setup wizard
- **Flatpak compatibility** with enhanced GPG environment setup
- **Import/export** functionality (JSON, CSV formats)
- **Comprehensive preferences** with security settings
- **Automatic clipboard clearing** for enhanced security
- **Internationalization** support for multiple languages

### 🌐 **Git Integration & Platform Support**
- **Multi-platform support**: GitHub, GitLab, Codeberg, and custom Git servers
- **Repository setup wizard** with guided configuration
- **Automatic repository detection** and status monitoring
- **Real-time Git status** with ahead/behind indicators
- **Auto-commit and auto-push** options for seamless synchronization
- **Repository management** through preferences with setup and status dialogs
- **Git history viewer** with commit details and author information
- **Conflict detection** and branch management
- **Platform API integration** for repository validation and information
- **Conditional UI elements** - Git buttons only appear when Git is properly configured

### 🔒 **Security Features**
- **Automatic idle locking** - Lock application after configurable inactivity period
- **Master password timeout** - Require re-entering GPG passphrase periodically
- **Failed attempt protection** - Lockout after too many failed unlock attempts
- **Memory clearing** - Clear sensitive data from memory when locked
- **Screen lock integration** - Lock application when system screen locks
- **Configurable timeouts** - Auto-hide passwords and clear clipboard
- **Export security** - Require master password for data export operations
- **Session management** - Comprehensive security controls in preferences

### ⌨️ **Keyboard Shortcuts**
- `Ctrl+N` - Add new password
- `Ctrl+E` - Edit password
- `Ctrl+C` - Copy password
- `Ctrl+Shift+C` - Copy username
- `Ctrl+F` - Focus search
- `Ctrl+G` - Generate password
- `Ctrl+Shift+P` - Git pull
- `Ctrl+Shift+U` - Git push
- `Ctrl+Shift+S` - Git status dialog
- `Ctrl+Shift+G` - Git setup dialog
- `Ctrl+,` - Preferences
- `F5` - Refresh

## 📸 Screenshots

### Main Interface
![Main Window](data/screenshots/main-window.png)
*Main application window with hierarchical password organization*

![Password Details](data/screenshots/password-page-view.png)
*Password details view with TOTP support and structured fields*

### Dialogs and Features
![Add Password](data/screenshots/add-new-password.png)
*Add new password dialog with comprehensive field options*

![Edit Password](data/screenshots/edit-password.png)
*Edit password dialog with comprehensive field options*

### Settings and Configuration
![Git Settings](data/screenshots/git-settings.png)
*Git integration settings with multi-platform support*

![Security Settings](data/screenshots/security-settings.png)
*Advanced security settings with session management*

![General Settings](data/screenshots/general-settings.png)
*General application preferences*

### Additional Features
![Git Status](data/screenshots/git-status-dialog.png)
*Git status and repository information*

![Keyboard Shortcuts](data/screenshots/keyboard-shortcuts.png)
*Keyboard shortcuts help dialog*

![About Dialog](data/screenshots/about-dialog.png)
*About dialog with application information*

## 🔒 Security

Secrets provides comprehensive security features to protect your sensitive data:

### Session Security
- **Idle Lock**: Automatically lock the application after a configurable period of inactivity (1-120 minutes)
- **Screen Lock Integration**: Lock application when the system screen locks
- **Master Password Timeout**: Require re-entering GPG passphrase after a configurable period (15-480 minutes, or never)
- **Memory Clearing**: Clear sensitive data from memory when the application is locked

### Access Protection
- **Failed Attempt Lockout**: Lock out users after too many failed unlock attempts (1-10 attempts)
- **Lockout Duration**: Configurable lockout period after failed attempts (1-60 minutes)
- **Secure Unlock Dialog**: Password entry with attempt tracking and countdown display

### Data Protection
- **Auto-hide Passwords**: Automatically hide visible passwords after timeout (5-300 seconds)
- **Clipboard Security**: Automatically clear clipboard after copying sensitive data (10-300 seconds)
- **Export Security**: Require master password confirmation for data export operations
- **Delete Confirmation**: Require confirmation before deleting password entries

### Configuration
All security features are configurable through **Preferences → Security**:
- **Password Display**: Auto-hide settings and timeouts
- **Clipboard**: Auto-clear timeout configuration
- **Session Security**: Idle lock, screen lock, and master password timeouts
- **Advanced Security**: Memory clearing, export protection, and failed attempt settings

### Security Benefits
- **Defense in Depth**: Multiple layers of protection (UI lock + memory clearing + timeouts)
- **User Control**: Balance security vs convenience with configurable settings
- **Automatic Protection**: Passive security that doesn't require user intervention
- **Visual Feedback**: Clear indication of security status and remaining time

## 🌐 Git Integration

Secrets provides comprehensive Git integration for synchronizing your password store across devices and platforms.

### Supported Platforms
- **GitHub** - Full API integration with repository validation
- **GitLab** - Complete GitLab.com and self-hosted support
- **Codeberg** - Gitea-based platform integration
- **Custom Git Servers** - Support for any Git repository

### Git Features
- **Repository Setup Wizard** - Guided setup for new or existing repositories
- **Real-time Status Monitoring** - Live Git status in the header bar
- **Automatic Operations** - Auto-pull on startup, auto-push on changes, auto-commit
- **Visual Indicators** - Git status with ahead/behind commit counts
- **Repository Management** - Complete repository configuration through preferences
- **History Viewer** - Browse commit history with author and date information
- **Conflict Detection** - Visual indication of repository conflicts
- **Platform Integration** - Repository validation using platform APIs

### Git Configuration Options
Available in **Preferences → Git**:

#### Basic Settings
- **Auto-pull on startup** - Automatically pull changes when application starts
- **Auto-push on changes** - Automatically push changes after modifications
- **Show Git status** - Display Git status information in the UI
- **Git timeout** - Timeout for Git operations (5-120 seconds)

#### Advanced Settings
- **Auto-commit on changes** - Automatically commit changes before push/pull
- **Show Git notifications** - Display toast notifications for Git operations
- **Check remote on startup** - Verify remote repository status on application start
- **Custom commit messages** - Configure default commit message template

#### Repository Management
- **Repository Setup** - Configure Git repository and remote connections
- **Repository Status** - View detailed Git status and commit history
- **Platform Integration** - Connect to GitHub, GitLab, or custom Git servers
- **Remote Configuration** - Manage remote URLs and authentication

### Git Workflow
1. **Setup**: Use the Git setup wizard to initialize or connect to a repository
2. **Monitor**: Git status indicator shows current repository state
3. **Sync**: Manual or automatic push/pull operations keep data synchronized
4. **History**: View commit history and repository information
5. **Manage**: Configure Git settings through comprehensive preferences

### Security Considerations
- **GPG Integration** - All Git operations respect GPG configuration
- **Secure Authentication** - Support for SSH keys and HTTPS authentication
- **Token Management** - Secure storage of platform access tokens
- **Conflict Resolution** - Safe handling of merge conflicts and repository issues

## 🌍 Internationalization

Secrets has full internationalization support with automatic locale detection and fallback to English when translations are unavailable.

### Supported Languages

- **🇧🇷 Portuguese (Brazil)** - pt_BR ⚠️ Partial (42% coverage)
- **🇵🇹 Portuguese (Portugal)** - pt_PT ⚠️ Partial (37% coverage)
- **🇺🇸 English (United States)** - en_US ✅ Complete (source)
- **🇬🇧 English (United Kingdom)** - en_GB ✅ Complete (source)
- **🇪🇸 Spanish** - es 👍 Good (79% coverage)
- **🇮🇪 Irish (Gaeilge)** - ga 👍 Good (79% coverage)

### Translation Features

- **Automatic locale detection** - Detects system locale and loads appropriate translations
- **Fallback support** - Falls back to English if translation not available
- **Development support** - Works in both development and installed environments
- **UI integration** - All user-facing strings in dialogs, menus, and interface are translatable
- **UTF-8 encoding** - Proper Unicode support for all languages

### Testing Translations

```bash
# Test specific locale
LANGUAGE=pt_BR python3 -m secrets.main

# Test Spanish interface
LANGUAGE=es ./run-dev.sh
```

### Adding New Translations

1. Add language code to `po/LINGUAS`
2. Create new .po file: `msginit --input=po/secrets.pot --locale=LANG --output=po/LANG.po`
3. Translate strings in the .po file
4. Rebuild: `meson compile -C builddir`

### Translation File Structure

```
po/
├── LINGUAS              # List of supported languages
├── secrets.pot          # Translation template
├── pt_BR.po            # Portuguese (Brazil) translations
├── pt_PT.po            # Portuguese (Portugal) translations
├── en_GB.po            # English (UK) translations
├── en_US.po            # English (US) translations
├── es.po               # Spanish translations
├── ga.po               # Irish translations
└── meson.build         # Build configuration
```

## 🛠️ Technology Stack

- **Language**: Python 3.8+
- **UI Framework**: GTK4 & Libadwaita
- **Build System**: Meson & Ninja
- **Dependencies**: PyGObject, pyotp, requests
- **Backend**: `pass`, GnuPG, Git
- **Packaging**: Flatpak with enhanced GPG environment support

## 📦 Installation

### From Flathub (Recommended)

*Coming soon - the application will be available on Flathub once submitted and approved.*

```bash
flatpak install flathub io.github.tobagin.secrets
flatpak run io.github.tobagin.secrets
```

### Building from Source

#### Prerequisites
- Python 3.8+
- GTK4 and Libadwaita development libraries
- Meson (>= 0.64.0) and Ninja
- `pass`, `git`, and `gpg` installed and configured

#### Build Steps
```bash
# Clone the repository
git clone https://github.com/tobagin/Secrets.git
cd Secrets

# Build with meson
meson setup builddir
meson compile -C builddir

# Run for development
./run-dev.sh
```

#### Development Options
```bash
./run-dev.sh                 # Recommended: run with meson devenv
./run-dev.sh --direct        # Run directly without meson
./builddir/secrets-dev       # Run generated script
python3 -m secrets.main      # Run module directly
```

### Building Flatpak Locally

```bash
# Install flatpak-builder
sudo dnf install flatpak-builder  # Fedora
sudo apt install flatpak-builder  # Ubuntu/Debian

# Build and install
flatpak-builder --user --install --force-clean build-dir io.github.tobagin.secrets.yml

# Run the Flatpak
flatpak run io.github.tobagin.secrets
```

#### Flatpak GPG Compatibility

The Flatpak version includes enhanced GPG environment setup for proper password decryption in sandboxed environments:

- **Automatic GPG environment configuration** - Sets up proper `GPG_TTY`, `GNUPGHOME`, and agent settings
- **GUI pinentry integration** - Includes pinentry-gtk2 for password prompts in the GUI
- **Robust error handling** - Graceful fallbacks when GPG components are missing
- **Seamless operation** - No manual configuration required for GPG operations

### System Installation

```bash
# Build and install system-wide
meson setup builddir --prefix=/usr
meson compile -C builddir
sudo meson install -C builddir

# Run the installed application
io.github.tobagin.secrets
```

## 🏗️ Project Structure

```
Secrets/
├── secrets/                    # Main Python package
│   ├── controllers/           # UI controllers (MVC pattern)
│   ├── managers/              # Specialized managers package
│   │   ├── git_manager.py     # Git operations and platform integration
│   │   ├── toast_manager.py   # Toast notifications
│   │   ├── clipboard_manager.py # Clipboard operations with auto-clear
│   │   ├── password_display_manager.py # Password visibility management
│   │   └── search_manager.py  # Search functionality
│   ├── ui/                    # UI components and dialogs
│   │   ├── components/        # Reusable UI components
│   │   │   └── git_status_component.py # Git status indicators
│   │   └── dialogs/           # Application dialogs
│   │       ├── git_setup_dialog.py # Git repository setup
│   │       └── git_status_dialog.py # Git status and history
│   ├── setup_wizard/          # GPG/pass setup wizard
│   ├── services/              # Business logic services
│   │   └── git_service.py     # Core Git operations
│   ├── utils/                 # Utility modules
│   └── *.py                   # Core application files
├── data/                      # Application data
│   ├── ui/                    # GTK UI definition files
│   ├── icons/                 # Application icons
│   └── *.xml.in              # Desktop/AppData metadata
├── tests/                     # Comprehensive test suite
├── po/                        # Internationalization (i18n)
│   ├── *.po                   # Translation files
│   └── LINGUAS               # Supported languages
└── *.yml                     # Flatpak manifest
```

### Architecture Patterns
- **MVC Pattern**: Controllers manage UI logic
- **Command Pattern**: Actions encapsulated as commands
- **Service Pattern**: Business logic in service classes
- **Manager Pattern**: Specialized managers for different concerns

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
python3 run_tests.py

# Or run specific test categories
python3 -m unittest tests.test_models
python3 -m unittest tests.test_services
python3 -m unittest tests.test_commands

# Test GPG environment setup (for development)
python3 test_gpg_env.py

# Test security features
python3 test_security_features.py
```

The test suite includes:
- **Model tests** (12 tests) - Data structures and validation
- **Service tests** (18 tests) - Business logic and password operations
- **Command tests** (24 tests) - User actions and clipboard operations
- **Security tests** (4 tests) - Idle detection, session locking, and security configuration
- **Git tests** (4 tests) - Git service, platform integration, and repository management
- **Performance tests** - Memory usage and response times
- **GPG environment tests** - Flatpak compatibility and GPG setup verification

## 🤝 Contributing

1. **Fork the repository** on GitHub
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** and add tests
4. **Run the test suite**: `python3 run_tests.py`
5. **Submit a pull request** with a clear description

### Development Guidelines
- Follow existing code patterns and architecture
- Add tests for new functionality
- Update documentation as needed
- Use GTK4/Libadwaita best practices
- Ensure accessibility compliance

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **pass** - The standard unix password manager
- **GNOME** - For GTK4 and Libadwaita
- **Flatpak** - For modern Linux app distribution
- **Contributors** - Everyone who helps improve this project

---

**Secrets** - Secure, modern password management for the Linux desktop.
