# Platformio-FLTK-Demo

### 介绍
 * FLTK 是一个跨平台的 GUI 开发工具包，可以用于创建各种图形界面应用程序。
 * PlatformIO则是一个用于开发嵌入式系统的开源项目。它提供了一个统一的命令行接口，用于管理项目、构建代码和上传固件。PlatformIO还支持多种开发环境，包括Visual Studio Code、Atom和Sublime Text。

本代码库是一个使用PlatformIO开发的FLTK GUI应用程序的项目示例。该示例展示了如何在VSCode中使用PlatformIO构建和运行FLTK应用程序。

### platformio.ini
```
[env:fltk]
platform = windows_x86
build_flags = 
            -I./lib/ 
            -L./static/win32
            -lfltk
            -lgdi32
            -lole32
            -lcomctl32
            -lstrmiids
            -lpthread 
            -lm
            -mwindows
extra_scripts = post:scripts/build.py
```

### 示例代码
```
#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include <FL/fl_ask.H>

int main() 
{
  Fl_Window window(200, 100);  // 创建一个窗口
  Fl_Button button(10, 10, 80, 20, "Click me!"); // 在窗口中添加一个按钮
  // 为按钮添加事件处理程序
  button.callback([](Fl_Widget* widget) 
  { 
    fl_alert("Button clicked!"); // 按钮被点击时，执行此代码
  });
  window.show(); // 显示窗口
  return Fl::run(); // 运行应用程序
}
```


有关更多信息，请参阅以下资源：

 * PlatformIO文档: https://docs.platformio.org/
 * FLTK文档: https://www.fltk.org/doc-1.3
