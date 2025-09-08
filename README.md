# FolderForge 📁

A powerful and intuitive tool for creating complex folder structures with ease. Whether you need to organize project files, create game level directories, or set up any nested folder hierarchy, FolderForge has you covered with both GUI and CLI interfaces.

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macOS%20%7C%20linux-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## ✨ Features

- 🖥️ **Dual Interface**: User-friendly GUI and powerful CLI
- 📊 **JSON Support**: Define complex nested structures using JSON
- 📝 **Simple Text Mode**: Create folders from plain text lists
- 🌳 **Visual Builder**: Interactive tree view for building structures
- 📚 **Template Library**: Pre-built templates for common use cases
- 💾 **Import/Export**: Save and load folder configurations
- 📋 **Real-time Logging**: Track folder creation progress
- 🎮 **Game-Ready**: Perfect for organizing game assets and levels
- 🏗️ **Project Structure**: Ideal for software project organization

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- tkinter (usually included with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tharinduxd0/folderforge.git
   cd folderforge
   ```

2. **Run the application**
   ```bash
   python folderforge.py
   ```

That's it! No additional dependencies required.

## 📖 Usage

### GUI Mode (Default)

Simply run the script without arguments to launch the GUI:

```bash
python folderforge.py
```

#### GUI Features:
- **Base Directory**: Select where to create your folder structure
- **Template Library**: Choose from pre-built templates
- **Text Input**: Enter folder names or JSON structure
- **Visual Builder**: Use the tree view to build structures interactively
- **Import/Export**: Save configurations for reuse

### CLI Mode

For automation and scripting:

```bash
python folderforge.py <base_directory> <structure_file.json>
```

**Example:**
```bash
python folderforge.py ./my_project structure.json
```

## 📊 Input Formats

### Simple Text List
```
Documents
Images
Videos
Projects
```

### JSON Structure (Nested)
```json
{
  "Ashina Outskirts": [
    "General Naomori Kawarada",
    "Chained Ogre", 
    "Gyoubu Masataka Oniwa"
  ],
  "Ashina Depths": [
    "Mist Noble",
    "O'Rin of the Water",
    "Corrupted Monk (illusion)"
  ]
}
```

### Complex Nested Structure
```json
{
  "src": {
    "components": ["Header", "Footer", "Sidebar"],
    "utils": ["helpers", "constants"],
    "assets": {
      "images": ["icons", "backgrounds"],
      "styles": ["css", "scss"]
    }
  },
  "docs": ["design", "specs", "api"],
  "tests": ["unit", "integration", "e2e"]
}
```

## 🏗️ Built-in Templates

### Game Levels Template
```json
{
  "Level 1": ["Enemies", "Loot", "Boss"],
  "Level 2": ["Enemies", "Loot", "Boss"]
}
```

### Project Structure Template
```json
{
  "src": ["components", "utils", "assets"],
  "docs": ["design", "specs"]
}
```

## 🖼️ Screenshots

### Main GUI Interface

![FolderForge GUI](https://i.postimg.cc/1zx8WLpR/image.png)

The intuitive interface makes folder creation simple and visual:
- Base directory selection
- Template library dropdown
- JSON/text input area
- Visual tree builder
- Real-time logging

### Visual Builder
Interactive tree view allows you to:
- Add folders visually
- Nest structures by dragging
- Convert to JSON format
- Preview before creation

## 🛠️ Advanced Usage

### Creating Game Asset Structures
Perfect for game developers organizing assets:

```json
{
  "Assets": {
    "Characters": {
      "Player": ["Animations", "Textures", "Models"],
      "NPCs": ["Merchants", "Guards", "Enemies"]
    },
    "Environments": {
      "Forest": ["Trees", "Rocks", "Water"],
      "Dungeon": ["Walls", "Props", "Lighting"]
    },
    "Audio": ["Music", "SFX", "Voice"]
  }
}
```

### Project Organization
Ideal for software projects:

```json
{
  "backend": {
    "src": ["controllers", "models", "routes", "middleware"],
    "tests": ["unit", "integration"],
    "docs": ["api", "database"]
  },
  "frontend": {
    "src": ["components", "pages", "hooks", "utils"],
    "public": ["images", "icons"],
    "tests": ["components", "pages"]
  },
  "shared": ["types", "constants", "utils"]
}
```

### Batch Operations
Use CLI mode for automation:

```bash
#!/bin/bash
# Create multiple project structures
for project in web-app mobile-app desktop-app; do
    python folderforge.py "./projects/$project" project_template.json
done
```

## 🔧 Configuration

### Custom Templates
You can extend the template library by modifying the `templates` dictionary in the code:

```python
templates = {
    "Custom Template": {
        "folder1": ["subfolder1", "subfolder2"],
        "folder2": ["subfolder3", "subfolder4"]
    }
}
```

### Default Directory
The application defaults to the script's directory. You can modify this by changing:

```python
default_dir = os.path.dirname(os.path.abspath(__file__))
```

## 📝 Examples

<details>
<summary>Click to see more examples</summary>

### Photography Project
```json
{
  "2024_Wedding_Photos": {
    "RAW": ["Ceremony", "Reception", "Portraits"],
    "Edited": {
      "High_Res": ["Ceremony", "Reception", "Portraits"],
      "Web_Ready": ["Gallery", "Social_Media"]
    },
    "Backups": ["Local", "Cloud"]
  }
}
```

### Research Project
```json
{
  "Research_Project": {
    "Data": {
      "Raw": ["surveys", "interviews", "observations"],
      "Processed": ["cleaned", "analyzed", "visualized"]
    },
    "Analysis": ["statistical", "qualitative", "mixed_methods"],
    "Reports": ["drafts", "final", "presentations"],
    "References": ["papers", "books", "websites"]
  }
}
```

### YouTube Channel
```json
{
  "YouTube_Channel": {
    "Videos": {
      "2024": ["Q1", "Q2", "Q3", "Q4"],
      "Archive": ["2023", "2022", "2021"]
    },
    "Assets": {
      "Thumbnails": ["templates", "final"],
      "Audio": ["music", "sfx", "voiceovers"],
      "Graphics": ["logos", "overlays", "transitions"]
    },
    "Scripts": ["drafts", "final", "notes"]
  }
}
```

</details>

## 🐛 Troubleshooting

### Common Issues

**Issue**: "No module named 'tkinter'"
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS
brew install python-tk

# Windows
# tkinter is usually included with Python
```

**Issue**: Permission denied when creating folders
- Ensure you have write permissions to the target directory
- Try running as administrator/sudo if necessary
- Check if the directory path exists and is accessible

**Issue**: JSON parsing errors
- Validate your JSON using a JSON validator
- Ensure proper comma placement and bracket matching
- Use the GUI's visual builder if JSON is complex

## 🤝 Contributing

Contributions are what make the open source community amazing! Any contributions are **greatly appreciated**.

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Development Setup

1. Fork and clone the repository
2. Make your changes
3. Test thoroughly with both GUI and CLI modes
4. Ensure code follows Python best practices
5. Add appropriate comments and documentation

### Ideas for Contributions

- 🎨 Additional templates for common use cases
- 🔧 Configuration file support
- 📱 Cross-platform improvements
- 🌐 Internationalization support
- 📊 Progress bars and better UX
- 🔍 Search functionality in templates
- 📋 Drag-and-drop support
- 🎯 Folder validation before creation

## 📋 Changelog

### v1.0.0 (Current)
- ✅ GUI interface with tkinter
- ✅ CLI support with argparse
- ✅ JSON and text input formats
- ✅ Visual tree builder
- ✅ Template library
- ✅ Import/export functionality
- ✅ Real-time logging
- ✅ Cross-platform compatibility

## 🗺️ Roadmap

- [ ] **v1.1.0**: Configuration file support
- [ ] **v1.2.0**: Progress bars and animations  
- [ ] **v1.3.0**: Drag-and-drop interface
- [ ] **v1.4.0**: Template marketplace
- [ ] **v1.5.0**: Batch operations GUI
- [ ] **v2.0.0**: Plugin system

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

```
MIT License

Copyright (c) 2024 tharinduxd0

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 👨‍💻 Author

**tharinduxd0**
- GitHub: [@tharinduxd0](https://github.com/tharinduxd0)
- Project Link: [https://github.com/tharinduxd0/folderforge](https://github.com/tharinduxd0/folderforge)

## 🙏 Acknowledgments

- Thanks to the Python community for the excellent standard library
- Inspired by the need for better project organization tools
- Special thanks to all contributors and users providing feedback

---

⭐ **Star this repository if it helped you organize your projects!**

*Made with ❤️ for developers, creators, and organizers everywhere*
