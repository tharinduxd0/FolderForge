# FolderForge 📁⚡

A powerful and intuitive Python GUI application that allows you to create complex nested folder structures with ease. Whether you need to organize project files, create directory templates, or set up folder hierarchies from JSON configurations, FolderForge has you covered.

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macOS%20%7C%20linux-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🎯 **Dual Input Methods**: Create folders using simple line-by-line text or complex JSON structures
- 🏗️ **Nested Structure Support**: Build unlimited levels of nested directories
- 📍 **Flexible Base Directory**: Choose any location or use the script's directory as default
- 📊 **Real-time Logging**: Track folder creation progress with detailed logs
- 🎨 **User-Friendly GUI**: Clean, intuitive interface built with Tkinter
- ⚡ **Instant Creation**: Bulk create hundreds of folders in seconds
- 🔄 **Error Handling**: Robust error handling with user-friendly messages
- 📝 **Example Templates**: Pre-loaded JSON examples to get you started

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- No additional dependencies required (uses built-in libraries)

### Installation

1. **Download the script**
   ```bash
   git clone https://github.com/yourusername/folderforge.git
   cd folderforge
   ```

2. **Run the application**
   ```bash
   python folderforge.py
   ```

That's it! The application will open with a user-friendly GUI.

## 💻 Usage

### Method 1: Simple Text Input
Enter folder names one per line:
```
Documents
Images
Videos
Projects
```

### Method 2: JSON Structure (Advanced)
Create complex nested structures using JSON:
```json
{
    "Web Projects": {
        "React Apps": [
            "portfolio-site",
            "e-commerce-app",
            "blog-platform"
        ],
        "Vue Apps": [
            "dashboard",
            "mobile-app"
        ]
    },
    "Mobile Projects": {
        "iOS": ["swift-app", "objective-c-legacy"],
        "Android": ["kotlin-app", "java-app"]
    },
    "Documentation": [
        "API Docs",
        "User Guides",
        "Technical Specs"
    ]
}
```

### Step-by-Step Guide

1. **Select Base Directory**: Choose where you want to create your folders (defaults to script location)
2. **Enter Structure**: Type folder names or paste JSON structure in the text area
3. **Click "Create Folders"**: Watch as your directory structure is built automatically
4. **Monitor Progress**: View real-time creation logs in the bottom panel

## 📸 Screenshots

### Main Interface
```
┌─ FolderForge ──────────────────────────────────────┐
│ Base Directory: [/path/to/location] [Browse]       │
│                                                     │
│ Enter folder names or JSON structure:              │
│ ┌─────────────────────────────────────────────────┐ │
│ │ {                                               │ │
│ │   "Project A": ["src", "docs", "tests"],       │ │
│ │   "Project B": ["assets", "config"]            │ │
│ │ }                                               │ │
│ └─────────────────────────────────────────────────┘ │
│                                                     │
│ [Create Folders] [Clear Log]                       │
│                                                     │
│ Folder creation log:                                │
│ ┌─────────────────────────────────────────────────┐ │
│ │ ✅ Created folder: /path/Project A               │ │
│ │ ✅ Created folder: /path/Project A/src          │ │
│ │ ✅ Created folder: /path/Project A/docs         │ │
│ └─────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

## 🏗️ Code Structure

```
folderforge.py
├── create_nested_folders()    # Core folder creation logic
├── start_creation()           # Main execution handler
├── browse_folder()           # Directory selection
├── clear_log()              # Log management
└── GUI Components           # Tkinter interface setup
```

## 🔧 Configuration Options

### JSON Structure Rules
- **Objects (dict)**: Keys become parent folders, values become contents
- **Arrays (list)**: Items become sibling folders at the same level
- **Strings**: Become individual folders
- **Nesting**: Unlimited depth supported

### Example Configurations

**Game Development Structure:**
```json
{
    "GameProject": {
        "Assets": {
            "Textures": ["Characters", "Environment", "UI"],
            "Audio": ["Music", "SFX", "Voice"],
            "Models": ["Characters", "Props", "Terrain"]
        },
        "Scripts": ["Player", "Enemies", "Managers"],
        "Scenes": ["MainMenu", "Level01", "Level02"]
    }
}
```

**Business Project Structure:**
```json
{
    "Company Project": {
        "Research": ["Market Analysis", "Competitor Study"],
        "Development": {
            "Frontend": ["React Components", "Styling"],
            "Backend": ["API", "Database", "Auth"]
        },
        "Documentation": ["Requirements", "Architecture", "User Manual"],
        "Testing": ["Unit Tests", "Integration Tests", "User Testing"]
    }
}
```

## ⚠️ Error Handling

The application handles common errors gracefully:

- **Invalid JSON**: Falls back to line-by-line processing
- **Permission Issues**: Shows clear error messages
- **Invalid Paths**: Validates directory selection
- **Empty Input**: Prompts user for required information

## 🛠️ Technical Details

### Built With
- **Python**: Core programming language
- **Tkinter**: GUI framework (built-in)
- **JSON**: Structure parsing
- **OS**: File system operations

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.6+
- **Memory**: Minimal (< 50MB)
- **Storage**: < 1MB for the script

### Performance
- **Speed**: Creates 1000+ folders in under 5 seconds
- **Memory Usage**: Efficient recursive processing
- **Scalability**: Handles complex nested structures without issues

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute
- 🐛 **Bug Reports**: Found an issue? Let us know!
- 💡 **Feature Requests**: Have an idea? We'd love to hear it!
- 🔧 **Code Contributions**: Submit pull requests for improvements
- 📖 **Documentation**: Help improve our docs

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📋 Roadmap

- [x] Basic folder creation
- [x] JSON nested structure support
- [x] GUI interface
- [x] Real-time logging
- [ ] **Template Library**: Pre-made folder structure templates
- [ ] **Drag & Drop**: Visual folder structure builder
- [ ] **Export/Import**: Save and load folder configurations
- [ ] **Command Line Interface**: CLI version for automation
- [ ] **Batch Processing**: Multiple directory operations
- [ ] **Custom Icons**: Folder icon customization

## 🐛 Troubleshooting

### Common Issues

**Issue**: "Permission denied" error
**Solution**: 
- Run as administrator (Windows) or with sudo (Linux/macOS)
- Check folder permissions in the target directory

**Issue**: JSON format error
**Solution**: 
- Validate your JSON using an online JSON validator
- The app will automatically fall back to line-by-line mode if JSON is invalid

**Issue**: Folders not appearing
**Solution**: 
- Check the base directory path is correct
- Ensure you have write permissions to the target location
- Refresh your file explorer

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

## 👨‍💻 Author

Created with ❤️ by [tharinduxd](https://github.com/tharinduxd0)

## 🙏 Acknowledgments

- **Python Community**: For the excellent standard libraries
- **Tkinter Documentation**: For comprehensive GUI guidance  
- **JSON.org**: For the JSON specification
- **Open Source Community**: For inspiration and best practices
<div align="center">

**⭐ Star this repository if you find it helpful! ⭐**

</div>
