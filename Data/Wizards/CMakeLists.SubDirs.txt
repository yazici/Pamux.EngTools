###########################################################################
# Disable insource build

IF(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_BINARY_DIR})
    MESSAGE(FATAL_ERROR
        "CMake generation for {PROJECT_NAME} is not allowed within the source directory!"
        "\n Remove the CMakeCache.txt file and try again from another folder, e.g.:"
        "\n "
        "\n rm CMakeCache.txt"
        "\n cd .."
        "\n mkdir cmake-make"
        "\n cd cmake-make"
        "\n cmake ../{PROJECT_NAME}"
    )
ENDIF()

CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

CMAKE_POLICY(SET CMP0003 NEW) # So library linking is more sane
CMAKE_POLICY(SET CMP0010 NEW) # So syntax problems are errors.
CMAKE_POLICY(SET CMP0005 NEW) # So BUILDINFO is automatically quoted.
CMAKE_POLICY(SET CMP0014 NEW) # Input directories must have CMakeLists.txt
CMAKE_POLICY(SET CMP0043 OLD)

PROJECT({PROJECT_NAME})

LIST(APPEND CMAKE_MODULE_PATH
    "${PROJECT_SOURCE_DIR}/src/cmake"
    "${PROJECT_SOURCE_DIR}/src/cmake/Modules"
)
INCLUDE("${PROJECT_SOURCE_DIR}/src/cmake/macros.cmake")


SET(CMAKE_BUILD_TYPE_INIT "Release")

# Global compile definitions since add_definitions() adds for all.
SET_PROPERTY(DIRECTORY APPEND PROPERTY COMPILE_DEFINITIONS_DEBUG           DEBUG _DEBUG)
SET_PROPERTY(DIRECTORY APPEND PROPERTY COMPILE_DEFINITIONS_RELEASE         NDEBUG)
SET_PROPERTY(DIRECTORY APPEND PROPERTY COMPILE_DEFINITIONS_MINSIZEREL      NDEBUG)
SET_PROPERTY(DIRECTORY APPEND PROPERTY COMPILE_DEFINITIONS_RELWITHDEBINFO  NDEBUG)

OPTION(WITH_CPU_SSE         "Enable SIMD instruction if they're detected on the host machine" ON)
OPTION(WITH_OSL             "Build with OSL support" OFF)
OPTION(WITH_OPENSUBDIV      "Build with OpenSubdiv support" OFF)
OPTION(WITH_LOGGING         "Build with logging support" OFF)
OPTION(WITH_DEBUG           "Build with with extra debug capabilties" OFF)
OPTION(WITH_CUDA_BINARIES   "Build CUDA binaries" OFF)

SET(CUDA_BINARIES_ARCH sm_20 sm_21 sm_30 sm_35 sm_50 sm_52 CACHE STRING "CUDA architectures to build binaries for")
MARK_AS_ADVANCED(CUDA_BINARIES_ARCH)

OPTION(WITH_CUDA_DYNLOAD           "Dynamically load CUDA libraries at runtime" ON)
MARK_AS_ADVANCED(WITH_CUDA_DYNLOAD)

INCLUDE(CheckCXXCompilerFlag)
INCLUDE(configure_build)

INCLUDE_DIRECTORIES(
    third_party/cuew/include
    third_party/clew/include
)

ADD_SUBDIRECTORY(3rdParty)
ADD_SUBDIRECTORY(src)
ADD_SUBDIRECTORY(tests)
ADD_SUBDIRECTORY(examples)
