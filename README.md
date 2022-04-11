# EHMTX Notify component for Home Assistant


### Installation

You can either use HACS or install the component manually:

- Put the files from `/custom_components/skyq/` in your folder `<config directory>/custom_components/skyq/`

If you wish to add to the provided application images (such as Netflix) place '.png' images with names the same as the application in the following folder:

- `<config directory>/custom_components/skyq/static/`

For channels where there is no EPG, this can also be utilised to provide a channel image. Place an image file in the same directory with the same name as your channel source name (e.g. raiuno.png).

#### YAML

Add a ehmtx platform entry in your configuration.yaml as below.

**Example of basic configuration.yaml**

```
notify:
  - platform: ehmtx
    name: awtrix
    device: awtrix
    icon: error

```

#### Configuration variables

| **YAML**                                        | **UI**                            | **Default** | **Details** |
| ------------------------------------------------|-----------------------------------|:-----------:|-------------|
| platform<br>_(string)(Required)_                | n/a                               |             |Must be set to ehmtx |
| device<br>_(string)(Required)_                  | n/a                               |             | The IP of the SkyQ set top box, e.g., 192.168.0.10. |
| name<br>_(string)(Required)_                    | n/a                               |             | The name you would like to give to the SkyQ set top box. 
| icon<br>_(string)(Required)_                    | n/a                               |error        | The name you would like to give to the SkyQ set top box. 

