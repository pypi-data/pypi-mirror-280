
```
pip install SimpleRichTradingJournal --upgrade
```

After the package update, the following should be executed:

```
srtj upgrade all
```

**See [srtj upgrade all](https://github.com/Simple-Rich-Trading-Journal#srtj-upgrade-all).**

---

#### Patches

#### 0.5.1 & 0.5.2

v0.5 now also runs under Windows.
Windows uses a different method to start processes, this patch fixes that.
Further process management will follow in v0.5.3. 

#### Minor (0.5)

##### New Features

![](https://raw.githubusercontent.com/Simple-Rich-Trading-Journal/docs/main/srtj-u5/about.png)

- srtj now checks the available version at startup and informs about available 
  updates in the bottom bar.
- It is now possible to exit the srtj server from the graphical interface.

[Your Display Environ (GUI)](https://github.com/Simple-Rich-Trading-Journal#your-display-environ-gui)

- A configuration file is now available that allows a shell command to which the 
  url of the srtj-server is passed to be executed at the start.

![](https://raw.githubusercontent.com/Simple-Rich-Trading-Journal/docs/main/srtj-u5/per_y.png)

- New columns and suitable configuration 
  [statisticsHypothesisPerDay](https://github.com/Simple-Rich-Trading-Journal/Simple-Rich-Trading-Journal/blob/master/src/SimpleRichTradingJournal/__env__/rconfig.py#L211)
  added.

![](https://raw.githubusercontent.com/Simple-Rich-Trading-Journal/docs/main/srtj-u5/c_upd.png)

- The functionality of the course update interval has been optimized. 
- In addition, an update can now also be initiated manually even if 
  [coursePluginUpdateInterval](https://github.com/Simple-Rich-Trading-Journal/Simple-Rich-Trading-Journal/blob/master/src/SimpleRichTradingJournal/__env__/rconfig.py#L291) 
  is not activated.

##### Bug Fixes

- The copy/paste function is a bit more stable.
- The bug where the cell values are deleted after tab 
  navigation during editing is now fixed.
- `demo` now works as described without the `init` directive.
- The bug where an error is thrown after canceling an edit 
  of an amount cell with an existing value is fixed.
- The column state caching is now more stable.
- The configuration 
  [statisticsGroupDefault](https://github.com/Simple-Rich-Trading-Journal/Simple-Rich-Trading-Journal/blob/master/src/SimpleRichTradingJournal/__env__/rconfig.py#L178)\[2]
  is now `0` by default.
- The file path within the file drop function of the note 
  interface has been corrected.
