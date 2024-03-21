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

# find_package(Qt6 REQUIRED COMPONENTS Core)

include(GoogleTest)
enable_testing()

add_executable(${PROJECT_NAME}
        src/main.cpp
)

# target_link_libraries(${PROJECT_NAME} PRIVATE Qt6::Core)

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

