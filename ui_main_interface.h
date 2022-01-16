#ifndef MAIN_INTERFACEQVISPD_H
#define MAIN_INTERFACEQVISPD_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include "PySide2extn.RoundProgressBar.h"
#include "PySide2extn.SpiralProgressBar.h"

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout;
    QFrame *header_frame;
    QHBoxLayout *horizontalLayout;
    QFrame *header_left_frame;
    QHBoxLayout *horizontalLayout_4;
    QPushButton *open_close_slider_bar_button;
    QFrame *header_center_frame;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_2;
    QFrame *header_right_frame;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *minmize_window_button;
    QPushButton *restore_window_button;
    QPushButton *close_window_button;
    QFrame *main_body_frame;
    QHBoxLayout *horizontalLayout_7;
    QFrame *left_menu_const_frame;
    QHBoxLayout *horizontalLayout_8;
    QFrame *menu_frame;
    QGridLayout *gridLayout;
    QPushButton *activity_button;
    QPushButton *system_information_button;
    QPushButton *battery_button;
    QPushButton *cpu_button;
    QLabel *label_3;
    QPushButton *storage_button;
    QPushButton *sensors_button;
    QPushButton *network_button;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_6;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_9;
    QFrame *main_body_contents_frame;
    QVBoxLayout *verticalLayout_3;
    QStackedWidget *stackedWidget;
    QWidget *cpu_and_memory;
    QVBoxLayout *verticalLayout_4;
    QFrame *cpu_info_frame;
    QGridLayout *gridLayout_2;
    QLabel *cpu_main_core;
    QLabel *cpu_per;
    QLabel *label_13;
    QLabel *label_10;
    QLabel *cpu_count;
    QLabel *label_11;
    roundProgressBar *cpu_percentage;
    QFrame *ram_info_frame;
    QGridLayout *gridLayout_3;
    QLabel *total_ram;
    QLabel *used_ram;
    QLabel *label_19;
    QLabel *label_18;
    QLabel *label_20;
    QLabel *free_ram;
    QLabel *available_ram;
    QLabel *ram_Usage;
    QLabel *label_16;
    QLabel *label_17;
    spiralProgressBar *ram_percantage;
    QWidget *battery;
    QVBoxLayout *verticalLayout_5;
    QLabel *label_26;
    QFrame *frame;
    QGridLayout *gridLayout_6;
    QLabel *label_27;
    QLabel *battery_plugged;
    QLabel *label_28;
    QLabel *battery_charge;
    QLabel *label_29;
    QLabel *battery_time_left;
    QLabel *label_30;
    QLabel *battery_status;
    roundProgressBar *battery_usage;
    QWidget *system_information;
    QVBoxLayout *verticalLayout_6;
    QFrame *frame_2;
    QGridLayout *gridLayout_4;
    QLabel *system_system;
    QLabel *label_45;
    QLabel *label_38;
    QLabel *system_platform;
    QLabel *label_43;
    QLabel *label_39;
    QLabel *label_44;
    QLabel *label_37;
    QLabel *system_version;
    QLabel *system_date;
    QLabel *label_35;
    QLabel *system_processor;
    QLabel *system_machine;
    QLabel *system_time;
    QWidget *activities;
    QVBoxLayout *verticalLayout_7;
    QFrame *frame_3;
    QGridLayout *gridLayout_5;
    QFrame *frame_6;
    QHBoxLayout *horizontalLayout_9;
    QLineEdit *activity_search;
    QPushButton *pushButton_3;
    QLabel *label_49;
    QLabel *label_50;
    QLabel *label_51;
    QFrame *frame_4;
    QVBoxLayout *verticalLayout_8;
    QTableWidget *tableWidget;
    QFrame *frame_5;
    QHBoxLayout *horizontalLayout_10;
    QPushButton *pushButton_4;
    QPushButton *pushButton_5;
    QPushButton *pushButton_6;
    QPushButton *pushButton_7;
    QWidget *storage;
    QVBoxLayout *verticalLayout_9;
    QLabel *label_52;
    QTableWidget *storageTable;
    QWidget *sensor;
    QVBoxLayout *verticalLayout_10;
    QLabel *label_53;
    QTableWidget *sensorTable;
    QWidget *network;
    QVBoxLayout *verticalLayout_11;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QVBoxLayout *verticalLayout_14;
    QFrame *frame_7;
    QVBoxLayout *verticalLayout_13;
    QLabel *label_54;
    QTableWidget *net_stats_table;
    QFrame *frame_8;
    QVBoxLayout *verticalLayout_12;
    QLabel *label_55;
    QTableWidget *net_io_table;
    QFrame *frame_9;
    QVBoxLayout *verticalLayout_15;
    QLabel *label_56;
    QTableWidget *net_addresses_table;
    QFrame *frame_11;
    QVBoxLayout *verticalLayout_16;
    QLabel *label_57;
    QTableWidget *net_connections_table;
    QFrame *footer_frame;
    QHBoxLayout *horizontalLayout_5;
    QFrame *footer_left_frame;
    QVBoxLayout *verticalLayout_2;
    QLabel *label;
    QFrame *footer_right_frame;
    QHBoxLayout *horizontalLayout_6;
    QPushButton *pushButton_2;
    QFrame *size_grip;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(629, 506);
        MainWindow->setStyleSheet(QString::fromUtf8("*{\n"
"border:none;\n"
"background-color:\"#001f3f\";\n"
"}\n"
""));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout = new QVBoxLayout(centralwidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        header_frame = new QFrame(centralwidget);
        header_frame->setObjectName(QString::fromUtf8("header_frame"));
        header_frame->setStyleSheet(QString::fromUtf8("*{\n"
"background-color:\"#001f3f\";\n"
"}"));
        header_frame->setFrameShape(QFrame::NoFrame);
        header_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout = new QHBoxLayout(header_frame);
        horizontalLayout->setSpacing(0);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        header_left_frame = new QFrame(header_frame);
        header_left_frame->setObjectName(QString::fromUtf8("header_left_frame"));
        header_left_frame->setStyleSheet(QString::fromUtf8("padding:0;\n"
"margin:0;\n"
""));
        header_left_frame->setFrameShape(QFrame::StyledPanel);
        header_left_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_4 = new QHBoxLayout(header_left_frame);
        horizontalLayout_4->setSpacing(0);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        horizontalLayout_4->setContentsMargins(0, 0, 0, 0);
        open_close_slider_bar_button = new QPushButton(header_left_frame);
        open_close_slider_bar_button->setObjectName(QString::fromUtf8("open_close_slider_bar_button"));
        QFont font;
        font.setPointSize(10);
        font.setBold(true);
        font.setWeight(75);
        open_close_slider_bar_button->setFont(font);
        open_close_slider_bar_button->setStyleSheet(QString::fromUtf8("margin:0;\n"
"color: rgb(255, 255, 255);\n"
"\n"
""));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/icons/menumulti.svg"), QSize(), QIcon::Normal, QIcon::Off);
        open_close_slider_bar_button->setIcon(icon);
        open_close_slider_bar_button->setIconSize(QSize(32, 32));

        horizontalLayout_4->addWidget(open_close_slider_bar_button, 0, Qt::AlignLeft);


        horizontalLayout->addWidget(header_left_frame, 0, Qt::AlignLeft);

        header_center_frame = new QFrame(header_frame);
        header_center_frame->setObjectName(QString::fromUtf8("header_center_frame"));
        header_center_frame->setFrameShape(QFrame::StyledPanel);
        header_center_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_3 = new QHBoxLayout(header_center_frame);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_2 = new QLabel(header_center_frame);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        QFont font1;
        font1.setPointSize(14);
        font1.setBold(true);
        font1.setWeight(75);
        label_2->setFont(font1);
        label_2->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        horizontalLayout_3->addWidget(label_2);


        horizontalLayout->addWidget(header_center_frame);

        header_right_frame = new QFrame(header_frame);
        header_right_frame->setObjectName(QString::fromUtf8("header_right_frame"));
        header_right_frame->setFrameShape(QFrame::StyledPanel);
        header_right_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_2 = new QHBoxLayout(header_right_frame);
        horizontalLayout_2->setSpacing(10);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        minmize_window_button = new QPushButton(header_right_frame);
        minmize_window_button->setObjectName(QString::fromUtf8("minmize_window_button"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icons/icons/minimize 1.svg"), QSize(), QIcon::Normal, QIcon::Off);
        minmize_window_button->setIcon(icon1);

        horizontalLayout_2->addWidget(minmize_window_button);

        restore_window_button = new QPushButton(header_right_frame);
        restore_window_button->setObjectName(QString::fromUtf8("restore_window_button"));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icons/icons/minimize.svg"), QSize(), QIcon::Normal, QIcon::Off);
        restore_window_button->setIcon(icon2);

        horizontalLayout_2->addWidget(restore_window_button);

        close_window_button = new QPushButton(header_right_frame);
        close_window_button->setObjectName(QString::fromUtf8("close_window_button"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/icons/icons/close-error.svg"), QSize(), QIcon::Normal, QIcon::Off);
        close_window_button->setIcon(icon3);

        horizontalLayout_2->addWidget(close_window_button);


        horizontalLayout->addWidget(header_right_frame, 0, Qt::AlignRight);


        verticalLayout->addWidget(header_frame, 0, Qt::AlignTop);

        main_body_frame = new QFrame(centralwidget);
        main_body_frame->setObjectName(QString::fromUtf8("main_body_frame"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(main_body_frame->sizePolicy().hasHeightForWidth());
        main_body_frame->setSizePolicy(sizePolicy);
        main_body_frame->setFrameShape(QFrame::StyledPanel);
        main_body_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_7 = new QHBoxLayout(main_body_frame);
        horizontalLayout_7->setSpacing(0);
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        horizontalLayout_7->setContentsMargins(0, 0, 0, 0);
        left_menu_const_frame = new QFrame(main_body_frame);
        left_menu_const_frame->setObjectName(QString::fromUtf8("left_menu_const_frame"));
        left_menu_const_frame->setMinimumSize(QSize(40, 0));
        left_menu_const_frame->setMaximumSize(QSize(20, 16777215));
        left_menu_const_frame->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 31, 63);"));
        left_menu_const_frame->setFrameShape(QFrame::StyledPanel);
        left_menu_const_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_8 = new QHBoxLayout(left_menu_const_frame);
        horizontalLayout_8->setSpacing(0);
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        horizontalLayout_8->setContentsMargins(0, 0, 0, 0);
        menu_frame = new QFrame(left_menu_const_frame);
        menu_frame->setObjectName(QString::fromUtf8("menu_frame"));
        menu_frame->setMinimumSize(QSize(100, 0));
        menu_frame->setFrameShape(QFrame::StyledPanel);
        menu_frame->setFrameShadow(QFrame::Raised);
        gridLayout = new QGridLayout(menu_frame);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setHorizontalSpacing(0);
        gridLayout->setVerticalSpacing(20);
        gridLayout->setContentsMargins(0, 0, 0, 0);
        activity_button = new QPushButton(menu_frame);
        activity_button->setObjectName(QString::fromUtf8("activity_button"));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/icons/icons/electrical-sensor.svg"), QSize(), QIcon::Normal, QIcon::Off);
        activity_button->setIcon(icon4);
        activity_button->setIconSize(QSize(32, 32));

        gridLayout->addWidget(activity_button, 3, 0, 1, 1, Qt::AlignLeft);

        system_information_button = new QPushButton(menu_frame);
        system_information_button->setObjectName(QString::fromUtf8("system_information_button"));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/icons/icons/computer.svg"), QSize(), QIcon::Normal, QIcon::Off);
        system_information_button->setIcon(icon5);
        system_information_button->setIconSize(QSize(32, 32));

        gridLayout->addWidget(system_information_button, 2, 0, 1, 1, Qt::AlignLeft);

        battery_button = new QPushButton(menu_frame);
        battery_button->setObjectName(QString::fromUtf8("battery_button"));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/icons/icons/batterybv.svg"), QSize(), QIcon::Normal, QIcon::Off);
        battery_button->setIcon(icon6);
        battery_button->setIconSize(QSize(32, 32));

        gridLayout->addWidget(battery_button, 1, 0, 1, 1, Qt::AlignLeft);

        cpu_button = new QPushButton(menu_frame);
        cpu_button->setObjectName(QString::fromUtf8("cpu_button"));
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/icons/icons/externalpng.png"), QSize(), QIcon::Normal, QIcon::Off);
        cpu_button->setIcon(icon7);
        cpu_button->setIconSize(QSize(32, 32));

        gridLayout->addWidget(cpu_button, 0, 0, 1, 1, Qt::AlignLeft);

        label_3 = new QLabel(menu_frame);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));
        label_3->setMargin(5);

        gridLayout->addWidget(label_3, 0, 1, 1, 1, Qt::AlignLeft);

        storage_button = new QPushButton(menu_frame);
        storage_button->setObjectName(QString::fromUtf8("storage_button"));
        QIcon icon8;
        icon8.addFile(QString::fromUtf8(":/icons/icons/folder-data-storage.svg"), QSize(), QIcon::Normal, QIcon::Off);
        storage_button->setIcon(icon8);
        storage_button->setIconSize(QSize(32, 32));

        gridLayout->addWidget(storage_button, 4, 0, 1, 1, Qt::AlignLeft);

        sensors_button = new QPushButton(menu_frame);
        sensors_button->setObjectName(QString::fromUtf8("sensors_button"));
        QIcon icon9;
        icon9.addFile(QString::fromUtf8(":/icons/icons/network-share.svg"), QSize(), QIcon::Normal, QIcon::Off);
        sensors_button->setIcon(icon9);
        sensors_button->setIconSize(QSize(32, 32));

        gridLayout->addWidget(sensors_button, 5, 0, 1, 1, Qt::AlignLeft);

        network_button = new QPushButton(menu_frame);
        network_button->setObjectName(QString::fromUtf8("network_button"));
        QIcon icon10;
        icon10.addFile(QString::fromUtf8(":/icons/icons/network (1).svg"), QSize(), QIcon::Normal, QIcon::Off);
        network_button->setIcon(icon10);
        network_button->setIconSize(QSize(32, 32));

        gridLayout->addWidget(network_button, 6, 0, 1, 1, Qt::AlignLeft);

        label_4 = new QLabel(menu_frame);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));
        label_4->setMargin(5);

        gridLayout->addWidget(label_4, 1, 1, 1, 1, Qt::AlignLeft);

        label_5 = new QLabel(menu_frame);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));
        label_5->setMargin(5);

        gridLayout->addWidget(label_5, 2, 1, 1, 1, Qt::AlignLeft);

        label_6 = new QLabel(menu_frame);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));
        label_6->setMargin(5);

        gridLayout->addWidget(label_6, 3, 1, 1, 1, Qt::AlignLeft);

        label_7 = new QLabel(menu_frame);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));
        label_7->setMargin(5);

        gridLayout->addWidget(label_7, 4, 1, 1, 1, Qt::AlignLeft);

        label_8 = new QLabel(menu_frame);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));
        label_8->setMargin(5);

        gridLayout->addWidget(label_8, 5, 1, 1, 1, Qt::AlignLeft);

        label_9 = new QLabel(menu_frame);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));
        label_9->setMargin(5);

        gridLayout->addWidget(label_9, 6, 1, 1, 1, Qt::AlignLeft);


        horizontalLayout_8->addWidget(menu_frame, 0, Qt::AlignLeft|Qt::AlignTop);


        horizontalLayout_7->addWidget(left_menu_const_frame);

        main_body_contents_frame = new QFrame(main_body_frame);
        main_body_contents_frame->setObjectName(QString::fromUtf8("main_body_contents_frame"));
        main_body_contents_frame->setFrameShape(QFrame::StyledPanel);
        main_body_contents_frame->setFrameShadow(QFrame::Raised);
        verticalLayout_3 = new QVBoxLayout(main_body_contents_frame);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        stackedWidget = new QStackedWidget(main_body_contents_frame);
        stackedWidget->setObjectName(QString::fromUtf8("stackedWidget"));
        cpu_and_memory = new QWidget();
        cpu_and_memory->setObjectName(QString::fromUtf8("cpu_and_memory"));
        verticalLayout_4 = new QVBoxLayout(cpu_and_memory);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        cpu_info_frame = new QFrame(cpu_and_memory);
        cpu_info_frame->setObjectName(QString::fromUtf8("cpu_info_frame"));
        cpu_info_frame->setFrameShape(QFrame::StyledPanel);
        cpu_info_frame->setFrameShadow(QFrame::Raised);
        gridLayout_2 = new QGridLayout(cpu_info_frame);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        cpu_main_core = new QLabel(cpu_info_frame);
        cpu_main_core->setObjectName(QString::fromUtf8("cpu_main_core"));
        cpu_main_core->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_2->addWidget(cpu_main_core, 2, 3, 1, 1);

        cpu_per = new QLabel(cpu_info_frame);
        cpu_per->setObjectName(QString::fromUtf8("cpu_per"));
        cpu_per->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_2->addWidget(cpu_per, 3, 3, 1, 1);

        label_13 = new QLabel(cpu_info_frame);
        label_13->setObjectName(QString::fromUtf8("label_13"));
        QFont font2;
        font2.setBold(true);
        font2.setWeight(75);
        label_13->setFont(font2);
        label_13->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_2->addWidget(label_13, 3, 0, 1, 1);

        label_10 = new QLabel(cpu_info_frame);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setFont(font2);
        label_10->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_2->addWidget(label_10, 0, 0, 1, 1);

        cpu_count = new QLabel(cpu_info_frame);
        cpu_count->setObjectName(QString::fromUtf8("cpu_count"));
        cpu_count->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_2->addWidget(cpu_count, 0, 3, 1, 1);

        label_11 = new QLabel(cpu_info_frame);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setFont(font2);
        label_11->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_2->addWidget(label_11, 2, 0, 1, 1);

        cpu_percentage = new roundProgressBar(cpu_info_frame);
        cpu_percentage->setObjectName(QString::fromUtf8("cpu_percentage"));
        cpu_percentage->setMinimumSize(QSize(150, 150));
        cpu_percentage->setMaximumSize(QSize(150, 150));

        gridLayout_2->addWidget(cpu_percentage, 0, 4, 4, 1);


        verticalLayout_4->addWidget(cpu_info_frame);

        ram_info_frame = new QFrame(cpu_and_memory);
        ram_info_frame->setObjectName(QString::fromUtf8("ram_info_frame"));
        ram_info_frame->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));
        ram_info_frame->setFrameShape(QFrame::StyledPanel);
        ram_info_frame->setFrameShadow(QFrame::Raised);
        gridLayout_3 = new QGridLayout(ram_info_frame);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        total_ram = new QLabel(ram_info_frame);
        total_ram->setObjectName(QString::fromUtf8("total_ram"));

        gridLayout_3->addWidget(total_ram, 0, 1, 1, 1);

        used_ram = new QLabel(ram_info_frame);
        used_ram->setObjectName(QString::fromUtf8("used_ram"));

        gridLayout_3->addWidget(used_ram, 2, 1, 1, 1);

        label_19 = new QLabel(ram_info_frame);
        label_19->setObjectName(QString::fromUtf8("label_19"));
        label_19->setFont(font2);

        gridLayout_3->addWidget(label_19, 3, 0, 1, 1);

        label_18 = new QLabel(ram_info_frame);
        label_18->setObjectName(QString::fromUtf8("label_18"));
        label_18->setFont(font2);

        gridLayout_3->addWidget(label_18, 2, 0, 1, 1);

        label_20 = new QLabel(ram_info_frame);
        label_20->setObjectName(QString::fromUtf8("label_20"));
        label_20->setFont(font2);

        gridLayout_3->addWidget(label_20, 4, 0, 1, 1);

        free_ram = new QLabel(ram_info_frame);
        free_ram->setObjectName(QString::fromUtf8("free_ram"));

        gridLayout_3->addWidget(free_ram, 3, 1, 1, 1);

        available_ram = new QLabel(ram_info_frame);
        available_ram->setObjectName(QString::fromUtf8("available_ram"));

        gridLayout_3->addWidget(available_ram, 1, 1, 1, 1);

        ram_Usage = new QLabel(ram_info_frame);
        ram_Usage->setObjectName(QString::fromUtf8("ram_Usage"));

        gridLayout_3->addWidget(ram_Usage, 4, 1, 1, 1);

        label_16 = new QLabel(ram_info_frame);
        label_16->setObjectName(QString::fromUtf8("label_16"));
        label_16->setFont(font2);

        gridLayout_3->addWidget(label_16, 0, 0, 1, 1);

        label_17 = new QLabel(ram_info_frame);
        label_17->setObjectName(QString::fromUtf8("label_17"));
        label_17->setFont(font2);

        gridLayout_3->addWidget(label_17, 1, 0, 1, 1);

        ram_percantage = new spiralProgressBar(ram_info_frame);
        ram_percantage->setObjectName(QString::fromUtf8("ram_percantage"));
        ram_percantage->setMaximumSize(QSize(150, 150));

        gridLayout_3->addWidget(ram_percantage, 0, 2, 5, 1);


        verticalLayout_4->addWidget(ram_info_frame);

        stackedWidget->addWidget(cpu_and_memory);
        battery = new QWidget();
        battery->setObjectName(QString::fromUtf8("battery"));
        verticalLayout_5 = new QVBoxLayout(battery);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        label_26 = new QLabel(battery);
        label_26->setObjectName(QString::fromUtf8("label_26"));
        QFont font3;
        font3.setPointSize(12);
        font3.setBold(true);
        font3.setWeight(75);
        label_26->setFont(font3);
        label_26->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        verticalLayout_5->addWidget(label_26);

        frame = new QFrame(battery);
        frame->setObjectName(QString::fromUtf8("frame"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(frame->sizePolicy().hasHeightForWidth());
        frame->setSizePolicy(sizePolicy1);
        frame->setFont(font2);
        frame->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        gridLayout_6 = new QGridLayout(frame);
        gridLayout_6->setObjectName(QString::fromUtf8("gridLayout_6"));
        label_27 = new QLabel(frame);
        label_27->setObjectName(QString::fromUtf8("label_27"));
        label_27->setFont(font2);

        gridLayout_6->addWidget(label_27, 0, 0, 1, 1);

        battery_plugged = new QLabel(frame);
        battery_plugged->setObjectName(QString::fromUtf8("battery_plugged"));

        gridLayout_6->addWidget(battery_plugged, 3, 1, 1, 1);

        label_28 = new QLabel(frame);
        label_28->setObjectName(QString::fromUtf8("label_28"));
        label_28->setFont(font2);

        gridLayout_6->addWidget(label_28, 1, 0, 1, 1);

        battery_charge = new QLabel(frame);
        battery_charge->setObjectName(QString::fromUtf8("battery_charge"));

        gridLayout_6->addWidget(battery_charge, 1, 1, 1, 1);

        label_29 = new QLabel(frame);
        label_29->setObjectName(QString::fromUtf8("label_29"));
        label_29->setFont(font2);

        gridLayout_6->addWidget(label_29, 2, 0, 1, 1);

        battery_time_left = new QLabel(frame);
        battery_time_left->setObjectName(QString::fromUtf8("battery_time_left"));

        gridLayout_6->addWidget(battery_time_left, 2, 1, 1, 1);

        label_30 = new QLabel(frame);
        label_30->setObjectName(QString::fromUtf8("label_30"));
        label_30->setFont(font2);

        gridLayout_6->addWidget(label_30, 3, 0, 1, 1);

        battery_status = new QLabel(frame);
        battery_status->setObjectName(QString::fromUtf8("battery_status"));

        gridLayout_6->addWidget(battery_status, 0, 1, 1, 1);

        battery_usage = new roundProgressBar(frame);
        battery_usage->setObjectName(QString::fromUtf8("battery_usage"));
        battery_usage->setMinimumSize(QSize(150, 150));
        battery_usage->setMaximumSize(QSize(150, 150));

        gridLayout_6->addWidget(battery_usage, 0, 2, 4, 1);


        verticalLayout_5->addWidget(frame);

        stackedWidget->addWidget(battery);
        system_information = new QWidget();
        system_information->setObjectName(QString::fromUtf8("system_information"));
        verticalLayout_6 = new QVBoxLayout(system_information);
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        frame_2 = new QFrame(system_information);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        gridLayout_4 = new QGridLayout(frame_2);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        system_system = new QLabel(frame_2);
        system_system->setObjectName(QString::fromUtf8("system_system"));
        system_system->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(system_system, 1, 0, 1, 1);

        label_45 = new QLabel(frame_2);
        label_45->setObjectName(QString::fromUtf8("label_45"));
        label_45->setFont(font2);
        label_45->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(label_45, 4, 2, 1, 1);

        label_38 = new QLabel(frame_2);
        label_38->setObjectName(QString::fromUtf8("label_38"));
        label_38->setFont(font2);
        label_38->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(label_38, 4, 0, 1, 1);

        system_platform = new QLabel(frame_2);
        system_platform->setObjectName(QString::fromUtf8("system_platform"));
        system_platform->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(system_platform, 2, 1, 1, 1);

        label_43 = new QLabel(frame_2);
        label_43->setObjectName(QString::fromUtf8("label_43"));
        label_43->setFont(font2);
        label_43->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(label_43, 2, 2, 1, 1);

        label_39 = new QLabel(frame_2);
        label_39->setObjectName(QString::fromUtf8("label_39"));
        label_39->setFont(font2);
        label_39->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(label_39, 3, 0, 1, 1);

        label_44 = new QLabel(frame_2);
        label_44->setObjectName(QString::fromUtf8("label_44"));
        label_44->setFont(font2);
        label_44->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(label_44, 3, 2, 1, 1);

        label_37 = new QLabel(frame_2);
        label_37->setObjectName(QString::fromUtf8("label_37"));
        label_37->setFont(font2);
        label_37->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(label_37, 2, 0, 1, 1);

        system_version = new QLabel(frame_2);
        system_version->setObjectName(QString::fromUtf8("system_version"));
        system_version->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(system_version, 3, 1, 1, 1);

        system_date = new QLabel(frame_2);
        system_date->setObjectName(QString::fromUtf8("system_date"));
        system_date->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(system_date, 4, 1, 1, 1);

        label_35 = new QLabel(frame_2);
        label_35->setObjectName(QString::fromUtf8("label_35"));
        label_35->setFont(font3);
        label_35->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(label_35, 0, 0, 1, 1, Qt::AlignTop);

        system_processor = new QLabel(frame_2);
        system_processor->setObjectName(QString::fromUtf8("system_processor"));
        system_processor->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(system_processor, 2, 3, 1, 1);

        system_machine = new QLabel(frame_2);
        system_machine->setObjectName(QString::fromUtf8("system_machine"));
        system_machine->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(system_machine, 3, 3, 1, 1);

        system_time = new QLabel(frame_2);
        system_time->setObjectName(QString::fromUtf8("system_time"));
        system_time->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_4->addWidget(system_time, 4, 3, 1, 1);


        verticalLayout_6->addWidget(frame_2);

        stackedWidget->addWidget(system_information);
        activities = new QWidget();
        activities->setObjectName(QString::fromUtf8("activities"));
        verticalLayout_7 = new QVBoxLayout(activities);
        verticalLayout_7->setObjectName(QString::fromUtf8("verticalLayout_7"));
        frame_3 = new QFrame(activities);
        frame_3->setObjectName(QString::fromUtf8("frame_3"));
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        gridLayout_5 = new QGridLayout(frame_3);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        frame_6 = new QFrame(frame_3);
        frame_6->setObjectName(QString::fromUtf8("frame_6"));
        sizePolicy1.setHeightForWidth(frame_6->sizePolicy().hasHeightForWidth());
        frame_6->setSizePolicy(sizePolicy1);
        frame_6->setMinimumSize(QSize(250, 0));
        frame_6->setMaximumSize(QSize(400, 16777215));
        frame_6->setFrameShape(QFrame::StyledPanel);
        frame_6->setFrameShadow(QFrame::Raised);
        horizontalLayout_9 = new QHBoxLayout(frame_6);
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        activity_search = new QLineEdit(frame_6);
        activity_search->setObjectName(QString::fromUtf8("activity_search"));
        activity_search->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 58, 85);"));

        horizontalLayout_9->addWidget(activity_search);

        pushButton_3 = new QPushButton(frame_6);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));
        QIcon icon11;
        icon11.addFile(QString::fromUtf8(":/icons/icons/search.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_3->setIcon(icon11);
        pushButton_3->setIconSize(QSize(30, 20));

        horizontalLayout_9->addWidget(pushButton_3);


        gridLayout_5->addWidget(frame_6, 1, 1, 1, 1, Qt::AlignRight);

        label_49 = new QLabel(frame_3);
        label_49->setObjectName(QString::fromUtf8("label_49"));
        label_49->setFont(font3);
        label_49->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        gridLayout_5->addWidget(label_49, 0, 0, 1, 1);

        label_50 = new QLabel(frame_3);
        label_50->setObjectName(QString::fromUtf8("label_50"));

        gridLayout_5->addWidget(label_50, 1, 0, 1, 1);

        label_51 = new QLabel(frame_3);
        label_51->setObjectName(QString::fromUtf8("label_51"));

        gridLayout_5->addWidget(label_51, 2, 1, 1, 1);


        verticalLayout_7->addWidget(frame_3);

        frame_4 = new QFrame(activities);
        frame_4->setObjectName(QString::fromUtf8("frame_4"));
        frame_4->setFrameShape(QFrame::StyledPanel);
        frame_4->setFrameShadow(QFrame::Raised);
        verticalLayout_8 = new QVBoxLayout(frame_4);
        verticalLayout_8->setObjectName(QString::fromUtf8("verticalLayout_8"));
        tableWidget = new QTableWidget(frame_4);
        if (tableWidget->columnCount() < 9)
            tableWidget->setColumnCount(9);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(2, __qtablewidgetitem2);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(3, __qtablewidgetitem3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(4, __qtablewidgetitem4);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(5, __qtablewidgetitem5);
        QTableWidgetItem *__qtablewidgetitem6 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(6, __qtablewidgetitem6);
        QTableWidgetItem *__qtablewidgetitem7 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(7, __qtablewidgetitem7);
        QTableWidgetItem *__qtablewidgetitem8 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(8, __qtablewidgetitem8);
        tableWidget->setObjectName(QString::fromUtf8("tableWidget"));
        tableWidget->setMinimumSize(QSize(0, 0));
        tableWidget->setStyleSheet(QString::fromUtf8("background-color:\"#001f3f\";\n"
""));

        verticalLayout_8->addWidget(tableWidget, 0, Qt::AlignVCenter);


        verticalLayout_7->addWidget(frame_4);

        frame_5 = new QFrame(activities);
        frame_5->setObjectName(QString::fromUtf8("frame_5"));
        frame_5->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";"));
        frame_5->setFrameShape(QFrame::StyledPanel);
        frame_5->setFrameShadow(QFrame::Raised);
        horizontalLayout_10 = new QHBoxLayout(frame_5);
        horizontalLayout_10->setObjectName(QString::fromUtf8("horizontalLayout_10"));
        pushButton_4 = new QPushButton(frame_5);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));
        QFont font4;
        font4.setFamily(QString::fromUtf8("MS Shell Dlg 2"));
        font4.setPointSize(8);
        font4.setBold(false);
        font4.setItalic(false);
        font4.setWeight(9);
        pushButton_4->setFont(font4);

        horizontalLayout_10->addWidget(pushButton_4);

        pushButton_5 = new QPushButton(frame_5);
        pushButton_5->setObjectName(QString::fromUtf8("pushButton_5"));
        pushButton_5->setFont(font4);

        horizontalLayout_10->addWidget(pushButton_5);

        pushButton_6 = new QPushButton(frame_5);
        pushButton_6->setObjectName(QString::fromUtf8("pushButton_6"));

        horizontalLayout_10->addWidget(pushButton_6);

        pushButton_7 = new QPushButton(frame_5);
        pushButton_7->setObjectName(QString::fromUtf8("pushButton_7"));

        horizontalLayout_10->addWidget(pushButton_7);


        verticalLayout_7->addWidget(frame_5, 0, Qt::AlignBottom);

        stackedWidget->addWidget(activities);
        storage = new QWidget();
        storage->setObjectName(QString::fromUtf8("storage"));
        verticalLayout_9 = new QVBoxLayout(storage);
        verticalLayout_9->setObjectName(QString::fromUtf8("verticalLayout_9"));
        label_52 = new QLabel(storage);
        label_52->setObjectName(QString::fromUtf8("label_52"));
        label_52->setFont(font3);
        label_52->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        verticalLayout_9->addWidget(label_52);

        storageTable = new QTableWidget(storage);
        if (storageTable->columnCount() < 9)
            storageTable->setColumnCount(9);
        QTableWidgetItem *__qtablewidgetitem9 = new QTableWidgetItem();
        storageTable->setHorizontalHeaderItem(0, __qtablewidgetitem9);
        QTableWidgetItem *__qtablewidgetitem10 = new QTableWidgetItem();
        storageTable->setHorizontalHeaderItem(1, __qtablewidgetitem10);
        QTableWidgetItem *__qtablewidgetitem11 = new QTableWidgetItem();
        storageTable->setHorizontalHeaderItem(2, __qtablewidgetitem11);
        QTableWidgetItem *__qtablewidgetitem12 = new QTableWidgetItem();
        storageTable->setHorizontalHeaderItem(3, __qtablewidgetitem12);
        QTableWidgetItem *__qtablewidgetitem13 = new QTableWidgetItem();
        storageTable->setHorizontalHeaderItem(4, __qtablewidgetitem13);
        QTableWidgetItem *__qtablewidgetitem14 = new QTableWidgetItem();
        storageTable->setHorizontalHeaderItem(5, __qtablewidgetitem14);
        QTableWidgetItem *__qtablewidgetitem15 = new QTableWidgetItem();
        storageTable->setHorizontalHeaderItem(6, __qtablewidgetitem15);
        QTableWidgetItem *__qtablewidgetitem16 = new QTableWidgetItem();
        storageTable->setHorizontalHeaderItem(7, __qtablewidgetitem16);
        QTableWidgetItem *__qtablewidgetitem17 = new QTableWidgetItem();
        storageTable->setHorizontalHeaderItem(8, __qtablewidgetitem17);
        storageTable->setObjectName(QString::fromUtf8("storageTable"));

        verticalLayout_9->addWidget(storageTable);

        stackedWidget->addWidget(storage);
        sensor = new QWidget();
        sensor->setObjectName(QString::fromUtf8("sensor"));
        verticalLayout_10 = new QVBoxLayout(sensor);
        verticalLayout_10->setObjectName(QString::fromUtf8("verticalLayout_10"));
        label_53 = new QLabel(sensor);
        label_53->setObjectName(QString::fromUtf8("label_53"));
        label_53->setFont(font3);
        label_53->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        verticalLayout_10->addWidget(label_53);

        sensorTable = new QTableWidget(sensor);
        if (sensorTable->columnCount() < 6)
            sensorTable->setColumnCount(6);
        QTableWidgetItem *__qtablewidgetitem18 = new QTableWidgetItem();
        sensorTable->setHorizontalHeaderItem(0, __qtablewidgetitem18);
        QTableWidgetItem *__qtablewidgetitem19 = new QTableWidgetItem();
        sensorTable->setHorizontalHeaderItem(1, __qtablewidgetitem19);
        QTableWidgetItem *__qtablewidgetitem20 = new QTableWidgetItem();
        sensorTable->setHorizontalHeaderItem(2, __qtablewidgetitem20);
        QTableWidgetItem *__qtablewidgetitem21 = new QTableWidgetItem();
        sensorTable->setHorizontalHeaderItem(3, __qtablewidgetitem21);
        QTableWidgetItem *__qtablewidgetitem22 = new QTableWidgetItem();
        sensorTable->setHorizontalHeaderItem(4, __qtablewidgetitem22);
        QBrush brush(QColor(0, 0, 0, 255));
        brush.setStyle(Qt::Dense6Pattern);
        QTableWidgetItem *__qtablewidgetitem23 = new QTableWidgetItem();
        __qtablewidgetitem23->setForeground(brush);
        sensorTable->setHorizontalHeaderItem(5, __qtablewidgetitem23);
        sensorTable->setObjectName(QString::fromUtf8("sensorTable"));

        verticalLayout_10->addWidget(sensorTable);

        stackedWidget->addWidget(sensor);
        network = new QWidget();
        network->setObjectName(QString::fromUtf8("network"));
        verticalLayout_11 = new QVBoxLayout(network);
        verticalLayout_11->setObjectName(QString::fromUtf8("verticalLayout_11"));
        scrollArea = new QScrollArea(network);
        scrollArea->setObjectName(QString::fromUtf8("scrollArea"));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QString::fromUtf8("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 191, 772));
        verticalLayout_14 = new QVBoxLayout(scrollAreaWidgetContents);
        verticalLayout_14->setSpacing(0);
        verticalLayout_14->setObjectName(QString::fromUtf8("verticalLayout_14"));
        verticalLayout_14->setContentsMargins(0, 0, -1, 0);
        frame_7 = new QFrame(scrollAreaWidgetContents);
        frame_7->setObjectName(QString::fromUtf8("frame_7"));
        frame_7->setFrameShape(QFrame::StyledPanel);
        frame_7->setFrameShadow(QFrame::Raised);
        verticalLayout_13 = new QVBoxLayout(frame_7);
        verticalLayout_13->setObjectName(QString::fromUtf8("verticalLayout_13"));
        label_54 = new QLabel(frame_7);
        label_54->setObjectName(QString::fromUtf8("label_54"));
        QFont font5;
        font5.setFamily(QString::fromUtf8("MS Shell Dlg 2"));
        font5.setPointSize(12);
        font5.setBold(true);
        font5.setItalic(false);
        font5.setWeight(75);
        label_54->setFont(font5);
        label_54->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        verticalLayout_13->addWidget(label_54);

        net_stats_table = new QTableWidget(frame_7);
        if (net_stats_table->columnCount() < 5)
            net_stats_table->setColumnCount(5);
        QTableWidgetItem *__qtablewidgetitem24 = new QTableWidgetItem();
        net_stats_table->setHorizontalHeaderItem(0, __qtablewidgetitem24);
        QTableWidgetItem *__qtablewidgetitem25 = new QTableWidgetItem();
        net_stats_table->setHorizontalHeaderItem(1, __qtablewidgetitem25);
        QTableWidgetItem *__qtablewidgetitem26 = new QTableWidgetItem();
        net_stats_table->setHorizontalHeaderItem(2, __qtablewidgetitem26);
        QTableWidgetItem *__qtablewidgetitem27 = new QTableWidgetItem();
        net_stats_table->setHorizontalHeaderItem(3, __qtablewidgetitem27);
        QTableWidgetItem *__qtablewidgetitem28 = new QTableWidgetItem();
        net_stats_table->setHorizontalHeaderItem(4, __qtablewidgetitem28);
        net_stats_table->setObjectName(QString::fromUtf8("net_stats_table"));
        net_stats_table->setMinimumSize(QSize(0, 150));

        verticalLayout_13->addWidget(net_stats_table);


        verticalLayout_14->addWidget(frame_7);

        frame_8 = new QFrame(scrollAreaWidgetContents);
        frame_8->setObjectName(QString::fromUtf8("frame_8"));
        frame_8->setFrameShape(QFrame::StyledPanel);
        frame_8->setFrameShadow(QFrame::Raised);
        verticalLayout_12 = new QVBoxLayout(frame_8);
        verticalLayout_12->setObjectName(QString::fromUtf8("verticalLayout_12"));
        label_55 = new QLabel(frame_8);
        label_55->setObjectName(QString::fromUtf8("label_55"));
        label_55->setFont(font3);
        label_55->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        verticalLayout_12->addWidget(label_55);

        net_io_table = new QTableWidget(frame_8);
        if (net_io_table->columnCount() < 9)
            net_io_table->setColumnCount(9);
        QTableWidgetItem *__qtablewidgetitem29 = new QTableWidgetItem();
        net_io_table->setHorizontalHeaderItem(0, __qtablewidgetitem29);
        QTableWidgetItem *__qtablewidgetitem30 = new QTableWidgetItem();
        net_io_table->setHorizontalHeaderItem(1, __qtablewidgetitem30);
        QTableWidgetItem *__qtablewidgetitem31 = new QTableWidgetItem();
        net_io_table->setHorizontalHeaderItem(2, __qtablewidgetitem31);
        QTableWidgetItem *__qtablewidgetitem32 = new QTableWidgetItem();
        net_io_table->setHorizontalHeaderItem(3, __qtablewidgetitem32);
        QTableWidgetItem *__qtablewidgetitem33 = new QTableWidgetItem();
        net_io_table->setHorizontalHeaderItem(4, __qtablewidgetitem33);
        QTableWidgetItem *__qtablewidgetitem34 = new QTableWidgetItem();
        net_io_table->setHorizontalHeaderItem(5, __qtablewidgetitem34);
        QTableWidgetItem *__qtablewidgetitem35 = new QTableWidgetItem();
        net_io_table->setHorizontalHeaderItem(6, __qtablewidgetitem35);
        QTableWidgetItem *__qtablewidgetitem36 = new QTableWidgetItem();
        net_io_table->setHorizontalHeaderItem(7, __qtablewidgetitem36);
        QTableWidgetItem *__qtablewidgetitem37 = new QTableWidgetItem();
        net_io_table->setHorizontalHeaderItem(8, __qtablewidgetitem37);
        net_io_table->setObjectName(QString::fromUtf8("net_io_table"));
        net_io_table->setMinimumSize(QSize(0, 150));

        verticalLayout_12->addWidget(net_io_table);


        verticalLayout_14->addWidget(frame_8);

        frame_9 = new QFrame(scrollAreaWidgetContents);
        frame_9->setObjectName(QString::fromUtf8("frame_9"));
        frame_9->setFrameShape(QFrame::StyledPanel);
        frame_9->setFrameShadow(QFrame::Raised);
        verticalLayout_15 = new QVBoxLayout(frame_9);
        verticalLayout_15->setObjectName(QString::fromUtf8("verticalLayout_15"));
        label_56 = new QLabel(frame_9);
        label_56->setObjectName(QString::fromUtf8("label_56"));
        label_56->setFont(font3);
        label_56->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        verticalLayout_15->addWidget(label_56);

        net_addresses_table = new QTableWidget(frame_9);
        if (net_addresses_table->columnCount() < 6)
            net_addresses_table->setColumnCount(6);
        QTableWidgetItem *__qtablewidgetitem38 = new QTableWidgetItem();
        net_addresses_table->setHorizontalHeaderItem(0, __qtablewidgetitem38);
        QTableWidgetItem *__qtablewidgetitem39 = new QTableWidgetItem();
        net_addresses_table->setHorizontalHeaderItem(1, __qtablewidgetitem39);
        QTableWidgetItem *__qtablewidgetitem40 = new QTableWidgetItem();
        net_addresses_table->setHorizontalHeaderItem(2, __qtablewidgetitem40);
        QTableWidgetItem *__qtablewidgetitem41 = new QTableWidgetItem();
        net_addresses_table->setHorizontalHeaderItem(3, __qtablewidgetitem41);
        QTableWidgetItem *__qtablewidgetitem42 = new QTableWidgetItem();
        net_addresses_table->setHorizontalHeaderItem(4, __qtablewidgetitem42);
        QTableWidgetItem *__qtablewidgetitem43 = new QTableWidgetItem();
        net_addresses_table->setHorizontalHeaderItem(5, __qtablewidgetitem43);
        net_addresses_table->setObjectName(QString::fromUtf8("net_addresses_table"));
        net_addresses_table->setMinimumSize(QSize(0, 150));

        verticalLayout_15->addWidget(net_addresses_table);


        verticalLayout_14->addWidget(frame_9);

        frame_11 = new QFrame(scrollAreaWidgetContents);
        frame_11->setObjectName(QString::fromUtf8("frame_11"));
        frame_11->setFrameShape(QFrame::StyledPanel);
        frame_11->setFrameShadow(QFrame::Raised);
        verticalLayout_16 = new QVBoxLayout(frame_11);
        verticalLayout_16->setObjectName(QString::fromUtf8("verticalLayout_16"));
        label_57 = new QLabel(frame_11);
        label_57->setObjectName(QString::fromUtf8("label_57"));
        label_57->setFont(font3);
        label_57->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        verticalLayout_16->addWidget(label_57);

        net_connections_table = new QTableWidget(frame_11);
        if (net_connections_table->columnCount() < 8)
            net_connections_table->setColumnCount(8);
        QTableWidgetItem *__qtablewidgetitem44 = new QTableWidgetItem();
        net_connections_table->setHorizontalHeaderItem(0, __qtablewidgetitem44);
        QTableWidgetItem *__qtablewidgetitem45 = new QTableWidgetItem();
        net_connections_table->setHorizontalHeaderItem(1, __qtablewidgetitem45);
        QTableWidgetItem *__qtablewidgetitem46 = new QTableWidgetItem();
        net_connections_table->setHorizontalHeaderItem(2, __qtablewidgetitem46);
        QTableWidgetItem *__qtablewidgetitem47 = new QTableWidgetItem();
        net_connections_table->setHorizontalHeaderItem(3, __qtablewidgetitem47);
        QTableWidgetItem *__qtablewidgetitem48 = new QTableWidgetItem();
        net_connections_table->setHorizontalHeaderItem(4, __qtablewidgetitem48);
        QTableWidgetItem *__qtablewidgetitem49 = new QTableWidgetItem();
        net_connections_table->setHorizontalHeaderItem(5, __qtablewidgetitem49);
        QTableWidgetItem *__qtablewidgetitem50 = new QTableWidgetItem();
        net_connections_table->setHorizontalHeaderItem(6, __qtablewidgetitem50);
        QTableWidgetItem *__qtablewidgetitem51 = new QTableWidgetItem();
        net_connections_table->setHorizontalHeaderItem(7, __qtablewidgetitem51);
        net_connections_table->setObjectName(QString::fromUtf8("net_connections_table"));
        net_connections_table->setMinimumSize(QSize(0, 150));
        net_connections_table->setStyleSheet(QString::fromUtf8(""));

        verticalLayout_16->addWidget(net_connections_table);


        verticalLayout_14->addWidget(frame_11);

        scrollArea->setWidget(scrollAreaWidgetContents);

        verticalLayout_11->addWidget(scrollArea);

        stackedWidget->addWidget(network);

        verticalLayout_3->addWidget(stackedWidget);


        horizontalLayout_7->addWidget(main_body_contents_frame);


        verticalLayout->addWidget(main_body_frame);

        footer_frame = new QFrame(centralwidget);
        footer_frame->setObjectName(QString::fromUtf8("footer_frame"));
        footer_frame->setFrameShape(QFrame::NoFrame);
        footer_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_5 = new QHBoxLayout(footer_frame);
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        footer_left_frame = new QFrame(footer_frame);
        footer_left_frame->setObjectName(QString::fromUtf8("footer_left_frame"));
        footer_left_frame->setFrameShape(QFrame::StyledPanel);
        footer_left_frame->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(footer_left_frame);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        label = new QLabel(footer_left_frame);
        label->setObjectName(QString::fromUtf8("label"));
        label->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));

        verticalLayout_2->addWidget(label, 0, Qt::AlignLeft);


        horizontalLayout_5->addWidget(footer_left_frame);

        footer_right_frame = new QFrame(footer_frame);
        footer_right_frame->setObjectName(QString::fromUtf8("footer_right_frame"));
        footer_right_frame->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));
        footer_right_frame->setFrameShape(QFrame::StyledPanel);
        footer_right_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_6 = new QHBoxLayout(footer_right_frame);
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        pushButton_2 = new QPushButton(footer_right_frame);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        horizontalLayout_6->addWidget(pushButton_2);


        horizontalLayout_5->addWidget(footer_right_frame, 0, Qt::AlignRight);

        size_grip = new QFrame(footer_frame);
        size_grip->setObjectName(QString::fromUtf8("size_grip"));
        size_grip->setMinimumSize(QSize(10, 10));
        size_grip->setMaximumSize(QSize(10, 10));
        size_grip->setFrameShape(QFrame::StyledPanel);
        size_grip->setFrameShadow(QFrame::Raised);

        horizontalLayout_5->addWidget(size_grip, 0, Qt::AlignBottom);


        verticalLayout->addWidget(footer_frame, 0, Qt::AlignBottom);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        stackedWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        open_close_slider_bar_button->setText(QCoreApplication::translate("MainWindow", "  Menu", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "GRAPHENE  MANGER", nullptr));
        minmize_window_button->setText(QString());
        restore_window_button->setText(QString());
        close_window_button->setText(QString());
        activity_button->setText(QString());
        system_information_button->setText(QString());
        battery_button->setText(QString());
        cpu_button->setText(QString());
        label_3->setText(QCoreApplication::translate("MainWindow", "CPU", nullptr));
        storage_button->setText(QString());
        sensors_button->setText(QString());
        network_button->setText(QString());
        label_4->setText(QCoreApplication::translate("MainWindow", "Battery", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "System inforamtion", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "Activity", nullptr));
        label_7->setText(QCoreApplication::translate("MainWindow", "Storage", nullptr));
        label_8->setText(QCoreApplication::translate("MainWindow", "Sensers", nullptr));
        label_9->setText(QCoreApplication::translate("MainWindow", "Network", nullptr));
        cpu_main_core->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        cpu_per->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        label_13->setText(QCoreApplication::translate("MainWindow", "CPU Per", nullptr));
        label_10->setText(QCoreApplication::translate("MainWindow", "CPU Count", nullptr));
        cpu_count->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        label_11->setText(QCoreApplication::translate("MainWindow", "CPU Main Core", nullptr));
        total_ram->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        used_ram->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        label_19->setText(QCoreApplication::translate("MainWindow", "Free RAM", nullptr));
        label_18->setText(QCoreApplication::translate("MainWindow", "Used RAM", nullptr));
        label_20->setText(QCoreApplication::translate("MainWindow", "Ram Usage", nullptr));
        free_ram->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        available_ram->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        ram_Usage->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        label_16->setText(QCoreApplication::translate("MainWindow", "Total RAM", nullptr));
        label_17->setText(QCoreApplication::translate("MainWindow", "Avalible RAM", nullptr));
        label_26->setText(QCoreApplication::translate("MainWindow", "Battery Information", nullptr));
        label_27->setText(QCoreApplication::translate("MainWindow", "Status", nullptr));
        battery_plugged->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        label_28->setText(QCoreApplication::translate("MainWindow", "Charge", nullptr));
        battery_charge->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        label_29->setText(QCoreApplication::translate("MainWindow", "Time Left", nullptr));
        battery_time_left->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        label_30->setText(QCoreApplication::translate("MainWindow", "Plugged In", nullptr));
        battery_status->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        system_system->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        label_45->setText(QCoreApplication::translate("MainWindow", "System Time", nullptr));
        label_38->setText(QCoreApplication::translate("MainWindow", "System Date", nullptr));
        system_platform->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        label_43->setText(QCoreApplication::translate("MainWindow", "Processor", nullptr));
        label_39->setText(QCoreApplication::translate("MainWindow", "Version", nullptr));
        label_44->setText(QCoreApplication::translate("MainWindow", "Machine", nullptr));
        label_37->setText(QCoreApplication::translate("MainWindow", "Platform", nullptr));
        system_version->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        system_date->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        label_35->setText(QCoreApplication::translate("MainWindow", "System Information", nullptr));
        system_processor->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        system_machine->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        system_time->setText(QCoreApplication::translate("MainWindow", "N/A", nullptr));
        activity_search->setPlaceholderText(QCoreApplication::translate("MainWindow", "Search Processes", nullptr));
        pushButton_3->setText(QString());
        label_49->setText(QCoreApplication::translate("MainWindow", "Activities", nullptr));
        label_50->setText(QString());
        label_51->setText(QString());
        QTableWidgetItem *___qtablewidgetitem = tableWidget->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QCoreApplication::translate("MainWindow", "Process ID", nullptr));
        QTableWidgetItem *___qtablewidgetitem1 = tableWidget->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QCoreApplication::translate("MainWindow", "Process Name", nullptr));
        QTableWidgetItem *___qtablewidgetitem2 = tableWidget->horizontalHeaderItem(2);
        ___qtablewidgetitem2->setText(QCoreApplication::translate("MainWindow", "Process Status", nullptr));
        QTableWidgetItem *___qtablewidgetitem3 = tableWidget->horizontalHeaderItem(3);
        ___qtablewidgetitem3->setText(QCoreApplication::translate("MainWindow", "Suspend", nullptr));
        QTableWidgetItem *___qtablewidgetitem4 = tableWidget->horizontalHeaderItem(4);
        ___qtablewidgetitem4->setText(QCoreApplication::translate("MainWindow", "Started ", nullptr));
        QTableWidgetItem *___qtablewidgetitem5 = tableWidget->horizontalHeaderItem(5);
        ___qtablewidgetitem5->setText(QCoreApplication::translate("MainWindow", "Resume", nullptr));
        QTableWidgetItem *___qtablewidgetitem6 = tableWidget->horizontalHeaderItem(6);
        ___qtablewidgetitem6->setText(QCoreApplication::translate("MainWindow", "Terminate", nullptr));
        QTableWidgetItem *___qtablewidgetitem7 = tableWidget->horizontalHeaderItem(7);
        ___qtablewidgetitem7->setText(QCoreApplication::translate("MainWindow", "Kill", nullptr));
        pushButton_4->setText(QCoreApplication::translate("MainWindow", "Suspend", nullptr));
        pushButton_5->setText(QCoreApplication::translate("MainWindow", "Resume", nullptr));
        pushButton_6->setText(QCoreApplication::translate("MainWindow", "Terminate", nullptr));
        pushButton_7->setText(QCoreApplication::translate("MainWindow", "Kill", nullptr));
        label_52->setText(QCoreApplication::translate("MainWindow", "Disk Partions", nullptr));
        QTableWidgetItem *___qtablewidgetitem8 = storageTable->horizontalHeaderItem(0);
        ___qtablewidgetitem8->setText(QCoreApplication::translate("MainWindow", "Devices", nullptr));
        QTableWidgetItem *___qtablewidgetitem9 = storageTable->horizontalHeaderItem(1);
        ___qtablewidgetitem9->setText(QCoreApplication::translate("MainWindow", "MountPoint", nullptr));
        QTableWidgetItem *___qtablewidgetitem10 = storageTable->horizontalHeaderItem(2);
        ___qtablewidgetitem10->setText(QCoreApplication::translate("MainWindow", "Max File", nullptr));
        QTableWidgetItem *___qtablewidgetitem11 = storageTable->horizontalHeaderItem(3);
        ___qtablewidgetitem11->setText(QCoreApplication::translate("MainWindow", "FS Type", nullptr));
        QTableWidgetItem *___qtablewidgetitem12 = storageTable->horizontalHeaderItem(4);
        ___qtablewidgetitem12->setText(QCoreApplication::translate("MainWindow", "Used Storage", nullptr));
        QTableWidgetItem *___qtablewidgetitem13 = storageTable->horizontalHeaderItem(5);
        ___qtablewidgetitem13->setText(QCoreApplication::translate("MainWindow", "Opts", nullptr));
        QTableWidgetItem *___qtablewidgetitem14 = storageTable->horizontalHeaderItem(6);
        ___qtablewidgetitem14->setText(QCoreApplication::translate("MainWindow", "Total Storage", nullptr));
        QTableWidgetItem *___qtablewidgetitem15 = storageTable->horizontalHeaderItem(7);
        ___qtablewidgetitem15->setText(QCoreApplication::translate("MainWindow", "Free Storage", nullptr));
        QTableWidgetItem *___qtablewidgetitem16 = storageTable->horizontalHeaderItem(8);
        ___qtablewidgetitem16->setText(QCoreApplication::translate("MainWindow", "Used Storage", nullptr));
        label_53->setText(QCoreApplication::translate("MainWindow", "Sensors", nullptr));
        QTableWidgetItem *___qtablewidgetitem17 = sensorTable->horizontalHeaderItem(0);
        ___qtablewidgetitem17->setText(QCoreApplication::translate("MainWindow", "Sensor", nullptr));
        QTableWidgetItem *___qtablewidgetitem18 = sensorTable->horizontalHeaderItem(1);
        ___qtablewidgetitem18->setText(QCoreApplication::translate("MainWindow", "Label", nullptr));
        QTableWidgetItem *___qtablewidgetitem19 = sensorTable->horizontalHeaderItem(2);
        ___qtablewidgetitem19->setText(QCoreApplication::translate("MainWindow", "Current", nullptr));
        QTableWidgetItem *___qtablewidgetitem20 = sensorTable->horizontalHeaderItem(3);
        ___qtablewidgetitem20->setText(QCoreApplication::translate("MainWindow", "Temprature", nullptr));
        QTableWidgetItem *___qtablewidgetitem21 = sensorTable->horizontalHeaderItem(4);
        ___qtablewidgetitem21->setText(QCoreApplication::translate("MainWindow", "Critical", nullptr));
        label_54->setText(QCoreApplication::translate("MainWindow", "Stats", nullptr));
        QTableWidgetItem *___qtablewidgetitem22 = net_stats_table->horizontalHeaderItem(1);
        ___qtablewidgetitem22->setText(QCoreApplication::translate("MainWindow", "ISUP", nullptr));
        QTableWidgetItem *___qtablewidgetitem23 = net_stats_table->horizontalHeaderItem(2);
        ___qtablewidgetitem23->setText(QCoreApplication::translate("MainWindow", "Duplex", nullptr));
        QTableWidgetItem *___qtablewidgetitem24 = net_stats_table->horizontalHeaderItem(3);
        ___qtablewidgetitem24->setText(QCoreApplication::translate("MainWindow", "Speed", nullptr));
        QTableWidgetItem *___qtablewidgetitem25 = net_stats_table->horizontalHeaderItem(4);
        ___qtablewidgetitem25->setText(QCoreApplication::translate("MainWindow", "MTU", nullptr));
        label_55->setText(QCoreApplication::translate("MainWindow", "Network IO Counter", nullptr));
        QTableWidgetItem *___qtablewidgetitem26 = net_io_table->horizontalHeaderItem(1);
        ___qtablewidgetitem26->setText(QCoreApplication::translate("MainWindow", "Bytes Sent", nullptr));
        QTableWidgetItem *___qtablewidgetitem27 = net_io_table->horizontalHeaderItem(2);
        ___qtablewidgetitem27->setText(QCoreApplication::translate("MainWindow", "Bytes Recived", nullptr));
        QTableWidgetItem *___qtablewidgetitem28 = net_io_table->horizontalHeaderItem(3);
        ___qtablewidgetitem28->setText(QCoreApplication::translate("MainWindow", "Packets Sent", nullptr));
        QTableWidgetItem *___qtablewidgetitem29 = net_io_table->horizontalHeaderItem(4);
        ___qtablewidgetitem29->setText(QCoreApplication::translate("MainWindow", "Packets Recived", nullptr));
        QTableWidgetItem *___qtablewidgetitem30 = net_io_table->horizontalHeaderItem(5);
        ___qtablewidgetitem30->setText(QCoreApplication::translate("MainWindow", "ERR In", nullptr));
        QTableWidgetItem *___qtablewidgetitem31 = net_io_table->horizontalHeaderItem(6);
        ___qtablewidgetitem31->setText(QCoreApplication::translate("MainWindow", "ERR Out", nullptr));
        QTableWidgetItem *___qtablewidgetitem32 = net_io_table->horizontalHeaderItem(7);
        ___qtablewidgetitem32->setText(QCoreApplication::translate("MainWindow", "Drop In", nullptr));
        QTableWidgetItem *___qtablewidgetitem33 = net_io_table->horizontalHeaderItem(8);
        ___qtablewidgetitem33->setText(QCoreApplication::translate("MainWindow", "Drop Out", nullptr));
        label_56->setText(QCoreApplication::translate("MainWindow", "Network Addresses", nullptr));
        QTableWidgetItem *___qtablewidgetitem34 = net_addresses_table->horizontalHeaderItem(1);
        ___qtablewidgetitem34->setText(QCoreApplication::translate("MainWindow", "FAMILY", nullptr));
        QTableWidgetItem *___qtablewidgetitem35 = net_addresses_table->horizontalHeaderItem(2);
        ___qtablewidgetitem35->setText(QCoreApplication::translate("MainWindow", "ADDRESS", nullptr));
        QTableWidgetItem *___qtablewidgetitem36 = net_addresses_table->horizontalHeaderItem(3);
        ___qtablewidgetitem36->setText(QCoreApplication::translate("MainWindow", "NETMASK", nullptr));
        QTableWidgetItem *___qtablewidgetitem37 = net_addresses_table->horizontalHeaderItem(4);
        ___qtablewidgetitem37->setText(QCoreApplication::translate("MainWindow", "ROADCAS", nullptr));
        QTableWidgetItem *___qtablewidgetitem38 = net_addresses_table->horizontalHeaderItem(5);
        ___qtablewidgetitem38->setText(QCoreApplication::translate("MainWindow", "PTP", nullptr));
        label_57->setText(QCoreApplication::translate("MainWindow", "Netwok Connection", nullptr));
        QTableWidgetItem *___qtablewidgetitem39 = net_connections_table->horizontalHeaderItem(1);
        ___qtablewidgetitem39->setText(QCoreApplication::translate("MainWindow", "New Column", nullptr));
        QTableWidgetItem *___qtablewidgetitem40 = net_connections_table->horizontalHeaderItem(2);
        ___qtablewidgetitem40->setText(QCoreApplication::translate("MainWindow", "Family", nullptr));
        QTableWidgetItem *___qtablewidgetitem41 = net_connections_table->horizontalHeaderItem(3);
        ___qtablewidgetitem41->setText(QCoreApplication::translate("MainWindow", "Family", nullptr));
        QTableWidgetItem *___qtablewidgetitem42 = net_connections_table->horizontalHeaderItem(4);
        ___qtablewidgetitem42->setText(QCoreApplication::translate("MainWindow", "LADDR", nullptr));
        QTableWidgetItem *___qtablewidgetitem43 = net_connections_table->horizontalHeaderItem(5);
        ___qtablewidgetitem43->setText(QCoreApplication::translate("MainWindow", "RADDR", nullptr));
        QTableWidgetItem *___qtablewidgetitem44 = net_connections_table->horizontalHeaderItem(6);
        ___qtablewidgetitem44->setText(QCoreApplication::translate("MainWindow", "Status", nullptr));
        QTableWidgetItem *___qtablewidgetitem45 = net_connections_table->horizontalHeaderItem(7);
        ___qtablewidgetitem45->setText(QCoreApplication::translate("MainWindow", "PID", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Version 1.0|AbdiMK", nullptr));
        pushButton_2->setText(QCoreApplication::translate("MainWindow", "?", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAIN_INTERFACEQVISPD_H
