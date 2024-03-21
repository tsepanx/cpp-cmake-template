# /****************************************************************************
# **
# ** This file is part of the {{ cookiecutter.project_name }}
# **
# ****************************************************************************/

cmake_minimum_required(VERSION 3.16)
project({{ cookiecutter.project_name }} VERSION {{ cookiecutter.version }} LANGUAGES CXX)

message(PROJECT_NAME: ${PROJECT_NAME})

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_INCLUDE_DIRECTORIES_PROJECT_BEFORE ON)

add_compile_options(-W -Wall -fvisibility=hidden)

add_definitions(${GCC_COVERAGE_COMPILE_FLAGS})
include_directories(.)

include(GoogleTest)
enable_testing()

{% if cookiecutter.type == "regular" %}
add_executable(${PROJECT_NAME}
        src/main.cpp
)

{% elif cookiecutter.type == "boost" %}
find_package(Boost COMPONENTS thread program_options REQUIRED)

add_executable(${PROJECT_NAME}
        src/main.cpp
)

target_link_libraries(${PROJECT_NAME} PRIVATE ${Boost_LIBRARIES})
{% elif cookiecutter.type == "qt-gui" %}
find_package(Qt6 REQUIRED COMPONENTS Core Widgets)
qt_standard_project_setup()

qt_add_executable(${PROJECT_NAME}
    mainwindow.ui
    mainwindow.cpp
    main.cpp
)

target_link_libraries(${PROJECT_NAME} PRIVATE Qt6::Widgets)
set_target_properties(${PROJECT_NAME} PROPERTIES
    WIN32_EXECUTABLE ON
    MACOSX_BUNDLE ON
)
{% elif cookiecutter.type == "qt-cli" %}
find_package(Qt6 REQUIRED COMPONENTS Core)
qt_standard_project_setup()

qt_add_executable(${PROJECT_NAME}
    main.cpp
)

target_link_libraries(${PROJECT_NAME} PRIVATE Qt6::Core)
{% endif %}

# Google Tests
add_executable(tests
        tests/mocks.cpp
        tests/tests.cpp
)

target_link_libraries(tests                  gtest gtest_main gmock pthread)
add_dependencies(tests ${PROJECT_NAME})

gtest_discover_tests(tests)

set_target_properties(tests
    PROPERTIES OUTPUT_NAME "${PROJECT_NAME}-tests"
)

install(
        TARGETS ${PROJECT_NAME}
        DESTINATION bin
)

install(
        TARGETS tests
        DESTINATION /opt/tests
)

