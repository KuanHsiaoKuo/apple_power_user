# karabiner配置说明

<!--ts-->


<!--te-->

## 路径

```
~/.config/karabiner
```

## 分层

Hyper 键只有一颗，用久了总有键位冲突不够用的那天，比如我既想用 S 键触发 Search，又想用它激活 Sorted 3。利用层（layer）的概念，可以让键盘上的每个键都能成为独一无二的修饰键。

```admonish tip title\='所谓层'
所谓层，可以理解为按下某个键后，键盘上其他键的功能随之发生变化，例如下图就是按下 option 键后键盘的变化，我们可以称之为「option 层」。
```

![img](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/38a1657e2d8f0fa9ab00c7e9106caa90.gif)

```admonish info title='其他可以作为分层键的'
其他可作为 modifier key 的按键有：
\
,
.
space
Tab
```

## karabiner.json

1. Disable command + Q in web browser
2. Change right_option to shift+control+command
3. Change right_command to command+control+option+shift, press alone be escape
4. Change left_cotnril+hjkl to arrow keys
5. Change left_control+0/$/d/u to home/end/page_down/page_up
6. Mapping `[left_option={1-0,-,=}]` to {F1-F10, F11, F12}

```json
{
  "global": {
    "check_for_updates_on_startup": true,
    "show_in_menu_bar": true,
    "show_profile_name_in_menu_bar": false
  },
  "profiles": [
    {
      "complex_modifications": {
        "parameters": {
          "basic.simultaneous_threshold_milliseconds": 50,
          "basic.to_delayed_action_delay_milliseconds": 500,
          "basic.to_if_alone_timeout_milliseconds": 1000,
          "basic.to_if_held_down_threshold_milliseconds": 500,
          "mouse_motion_to_scroll.speed": 100
        },
        "rules": [
          {
            "description": "Disable command + Q in web browser",
            "manipulators": [
              {
                "conditions": [
                  {
                    "bundle_identifiers": [
                      "^org\\.mozilla\\.firefox$",
                      "^com\\.google\\.Chrome$",
                      "^com\\.apple\\.Safari$"
                    ],
                    "type": "frontmost_application_if"
                  }
                ],
                "from": {
                  "key_code": "q",
                  "modifiers": {
                    "mandatory": [
                      "command"
                    ],
                    "optional": [
                      "caps_lock"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "vk_none"
                  }
                ],
                "type": "basic"
              }
            ]
          },
          {
            "description": "Change right_option to shift+control+command",
            "manipulators": [
              {
                "from": {
                  "key_code": "right_option"
                },
                "to": [
                  {
                    "key_code": "left_shift",
                    "modifiers": [
                      "left_control",
                      "left_command"
                    ]
                  }
                ],
                "type": "basic"
              }
            ]
          },
          {
            "description": "Change right_command to command+control+option+shift,press alone be escape",
            "manipulators": [
              {
                "from": {
                  "key_code": "right_command",
                  "modifiers": {
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "left_option",
                    "modifiers": [
                      "left_command",
                      "left_control",
                      "left_shift"
                    ]
                  }
                ],
                "to_if_alone": [
                  {
                    "key_code": "escape"
                  }
                ],
                "type": "basic"
              }
            ]
          },
          {
            "description": "Change left_control+hjkl to arrow keys",
            "manipulators": [
              {
                "from": {
                  "key_code": "h",
                  "modifiers": {
                    "mandatory": [
                      "left_control"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "left_arrow"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "j",
                  "modifiers": {
                    "mandatory": [
                      "left_control"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "down_arrow"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "k",
                  "modifiers": {
                    "mandatory": [
                      "left_control"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "up_arrow"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "l",
                  "modifiers": {
                    "mandatory": [
                      "left_control"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "right_arrow"
                  }
                ],
                "type": "basic"
              }
            ]
          },
          {
            "description": "Change left_control+0/$/d/u to home/end/page_down/page_up (rev 2)",
            "manipulators": [
              {
                "from": {
                  "key_code": "0",
                  "modifiers": {
                    "mandatory": [
                      "left_control"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "home"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "$",
                  "modifiers": {
                    "mandatory": [
                      "left_control"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "end"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "d",
                  "modifiers": {
                    "mandatory": [
                      "left_control"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "page_down"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "u",
                  "modifiers": {
                    "mandatory": [
                      "left_control"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "page_up"
                  }
                ],
                "type": "basic"
              }
            ]
          },
          {
            "description": "Mapping [left_option-{1-0,-,=} to {F1-F10,F11,F12}",
            "manipulators": [
              {
                "from": {
                  "key_code": "1",
                  "modifiers": {
                    "mandatory": [
                      "left_option"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "f1"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "2",
                  "modifiers": {
                    "mandatory": [
                      "left_option"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "f2"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "3",
                  "modifiers": {
                    "mandatory": [
                      "left_option"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "f3"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "4",
                  "modifiers": {
                    "mandatory": [
                      "left_option"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "f4"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "5",
                  "modifiers": {
                    "mandatory": [
                      "left_option"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "f5"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "6",
                  "modifiers": {
                    "mandatory": [
                      "left_option"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "f6"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "7",
                  "modifiers": {
                    "mandatory": [
                      "left_option"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "f7"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "8",
                  "modifiers": {
                    "mandatory": [
                      "left_option"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "f8"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "9",
                  "modifiers": {
                    "mandatory": [
                      "left_option"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "f9"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "0",
                  "modifiers": {
                    "mandatory": [
                      "left_option"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "f10"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "hyphen",
                  "modifiers": {
                    "mandatory": [
                      "left_option"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "f11"
                  }
                ],
                "type": "basic"
              },
              {
                "from": {
                  "key_code": "equal_sign",
                  "modifiers": {
                    "mandatory": [
                      "left_option"
                    ],
                    "optional": [
                      "any"
                    ]
                  }
                },
                "to": [
                  {
                    "key_code": "f12"
                  }
                ],
                "type": "basic"
              }
            ]
          }
        ]
      },
      "devices": [],
      "fn_function_keys": [
        {
          "from": {
            "key_code": "f1"
          },
          "to": [
            {
              "key_code": "display_brightness_decrement"
            }
          ]
        },
        {
          "from": {
            "key_code": "f2"
          },
          "to": [
            {
              "key_code": "display_brightness_increment"
            }
          ]
        },
        {
          "from": {
            "key_code": "f3"
          },
          "to": [
            {
              "key_code": "mission_control"
            }
          ]
        },
        {
          "from": {
            "key_code": "f4"
          },
          "to": [
            {
              "key_code": "launchpad"
            }
          ]
        },
        {
          "from": {
            "key_code": "f5"
          },
          "to": [
            {
              "key_code": "illumination_decrement"
            }
          ]
        },
        {
          "from": {
            "key_code": "f6"
          },
          "to": [
            {
              "key_code": "illumination_increment"
            }
          ]
        },
        {
          "from": {
            "key_code": "f7"
          },
          "to": [
            {
              "key_code": "rewind"
            }
          ]
        },
        {
          "from": {
            "key_code": "f8"
          },
          "to": [
            {
              "key_code": "play_or_pause"
            }
          ]
        },
        {
          "from": {
            "key_code": "f9"
          },
          "to": [
            {
              "key_code": "fastforward"
            }
          ]
        },
        {
          "from": {
            "key_code": "f10"
          },
          "to": [
            {
              "key_code": "mute"
            }
          ]
        },
        {
          "from": {
            "key_code": "f11"
          },
          "to": [
            {
              "key_code": "volume_decrement"
            }
          ]
        },
        {
          "from": {
            "key_code": "f12"
          },
          "to": [
            {
              "key_code": "volume_increment"
            }
          ]
        }
      ],
      "name": "Default profile",
      "parameters": {
        "delay_milliseconds_before_open_device": 1000
      },
      "selected": true,
      "simple_modifications": [
        {
          "from": {
            "key_code": "caps_lock"
          },
          "to": [
            {
              "key_code": "left_control"
            }
          ]
        }
      ],
      "virtual_hid_keyboard": {
        "caps_lock_delay_milliseconds": 0,
        "country_code": 0,
        "indicate_sticky_modifier_keys_state": true,
        "keyboard_type": "ansi",
        "mouse_key_xy_scale": 100
      }
    }
  ]
}

```

## 参考资源

- [The location of the configuration file | Karabiner-Elements](https://karabiner-elements.pqrs.org/docs/manual/misc/configuration-file-path/)
- [Karabiner God Mode. Use Karabiner to take your use of mac… | by Nikita | Medium](https://medium.com/@nikitavoloboev/karabiner-god-mode-7407a5ddc8f6)
