{% if cookiecutter.type == "regular" or cookiecutter.type == "boost" %}
#include<iostream>

int main() {
    std::cout << "Hello world!\n";
    return 0;
}

{% elif cookiecutter.type == "qt-gui" %}

#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
    return a.exec();
}

{% elif cookiecutter.type == "qt-cli" %}
{% endif %}

