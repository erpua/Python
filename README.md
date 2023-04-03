# Python

Installing:
- version check => python --version
- https://www.python.org/downloads/
- https://www.jetbrains.com/pycharm/ instead of VSCode

---
Terminal:
- python => runs python interpreter
- exit() => coming out from python environment

--- Tips
- CTRL + "/" => multiple line comments
- desable parameter hints in VSCode settings 
- CTRL + Shift + K => deletes current line of code
- pwd (Print Working Directory) => prints the route
- CTRL + J => open terminal
- Alt + Shift + "Bottom arrow" => current line code copy
- Alt + "Bottom / Up arrow" => moving code line bottom / up
- CTRL + "D" => mark full name of the object
- CTRL + Shift + P then type format, then choose Format Document With...,
then press Enter, then choose Python, then install autopep8 ( if not appearing => pip install autopep8 command ).
- CTRL + , => calls settings. Then format on save.
- if we want to chagne all variables => choose one, right click => change all occurrences

# Settings JSON
/* PYTHON */
/* 

{
  "workbench.colorTheme": "Bluloco Dark",
  "workbench.startupEditor": "none",
  "workbench.iconTheme": "material-icon-theme",
  "[python]": {
    "editor.formatOnType": true,
    "editor.defaultFormatter": "ms-python.python"
  },
  "workbench.layoutControl.enabled": false,
  "editor.fontSize": 14,
  "editor.letterSpacing": 0.5,
  "terminal.integrated.fontSize": 14,
  "editor.minimap.enabled": false,
  "editor.hover.delay": 1500,
  "editor.glyphMargin": false,
  "workbench.colorCustomizations": {
    "statusBar.border": "#206486",
    "panel.border": "#59ace2",
  },
  "editor.tokenColorCustomizations": {
    "variables": "#F4F4E0",
    "textMateRules": [
      {
        "scope": [
          "source",
          "variable",
          "constant",
          "variable.other.constant",
          "punctuation.definition.constant",
          "constant.other.symbol",
          "constant.language.symbol",
          "support.constant",
          "support.variable.magic.python",
          "variable.other.enummember"
        ],
        "settings": {
          "foreground": "#F4F4E0"
        }
      }
    ]
  },
  "editor.formatOnSave": true,
} 

*/