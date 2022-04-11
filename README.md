# EHMTX Notify component for Home Assistant


### Installation

You can either use HACS or install the component manually:

- Put the files from `/custom_components/ehmtx/` in your folder `<config directory>/custom_components/ehmtx/`

If you wish to add to the provided application images (such as Netflix) place '.png' images with names the same as the application in the following folder:

- `<config directory>/custom_components/ehmtx/static/`

For channels where there is no EPG, this can also be utilised to provide a channel image. Place an image file in the same directory with the same name as your channel source name (e.g. raiuno.png).

#### YAML

Add a ehmtx platform entry in your configuration.yaml as below.

**Example of basic configuration.yaml**

```
notify:
  - platform: ehmtx
    name: myehmtx32
    device: ehmtx32
    icon: error

```

#### Configuration variables

| **YAML**                                        | **UI**                            | **Default** | **Details** |
| ------------------------------------------------|-----------------------------------|:-----------:|-------------|
| platform<br>_(string)(Required)_                | n/a                               |             | Must be set to ehmtx |
| device<br>_(string)(Required)_                  | n/a                               |             | The name of your esphome device, e.g. ehmtx8266 |
| name<br>_(string)(Required)_                    | n/a                               |             | The name you would like to give to the ehmtx the notifier |
| icon<br>_(string)(Required)_                    | n/a                               |error        | a standard icon for situations where no icon is specified in service call|

#### usage in service calls

```
service: notify.myehmtx32
data:
  message: Show this text
  data:
    icon: alien
```

| **YAML**                                        | **Default** | **Details** |
| ------------------------------------------------|:-----------:|-------------|
| platform<br>_(string)(Required)_                |             | Must be set to ehmtx |
| device<br>_(string)(Required)_                  |             | The name of your esphome device, e.g. ehmtx32 |
| name<br>_(string)(Required)_                    |             | The name you would like to give to the ehmtx the notifier e.g. myehmtx32|
| icon<br>_(string)(Required)_                    |error        | the icon for this screen|

