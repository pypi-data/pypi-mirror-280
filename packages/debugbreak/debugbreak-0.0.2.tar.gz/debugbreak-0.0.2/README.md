## debugbreak


```shell
pip install debugbreak
```

Package is used to trigger Visual Studio debugging mode from the current Python session - the same way as if you would insert `__debugbreak` command in your C/C++ code.

Then Visual Studio popup will show up and you'll be able to attach Visual Studio to the current Python session.

<div style="text-align: center;">
    <img src="https://i.imgur.com/XvfCeJd.png" alt="Visual Studio Debugging">
</div>

It can be useful to either just as a fast way to open Visual Studio already attached to the current python file or as a way to get closer to the part of code in C-extension you want to debug.

Example:
```python
from debugbreak import debugbreak

debugbreak()
```
