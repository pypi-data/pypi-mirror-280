# easyqt
Wrappers and custom classes for pyqt to make widget development faster, simpler and fun!

## Installation
```bash
pip install easyqt
```

## Usage
```python
from easyqt import ButtonGroupWidget

buttonList = [('test1', 'TestONE'), ('test2', 'Test TWO')]
fw = ButtonGroupWidget(button_list=buttonList, label='My Test', exclusive=True, vertical=True)
fw.show()
```

```python
from easyqt import SearchFieldWidget

search_list = ['some', 'words', 'to', 'search', 'for', 'in', 'the', 'search', 'field', 'widget']
sf = SearchFieldWidget(string_list=search_list)
```
