# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/am/Documents/safeside-main

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/am/Documents/safeside-main/bulid

# Include any dependencies generated for this target.
include experimental/CMakeFiles/cache_line_analysis.dir/depend.make

# Include the progress variables for this target.
include experimental/CMakeFiles/cache_line_analysis.dir/progress.make

# Include the compile flags for this target's objects.
include experimental/CMakeFiles/cache_line_analysis.dir/flags.make

experimental/CMakeFiles/cache_line_analysis.dir/cache_line_analysis.cc.o: experimental/CMakeFiles/cache_line_analysis.dir/flags.make
experimental/CMakeFiles/cache_line_analysis.dir/cache_line_analysis.cc.o: ../experimental/cache_line_analysis.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/am/Documents/safeside-main/bulid/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object experimental/CMakeFiles/cache_line_analysis.dir/cache_line_analysis.cc.o"
	cd /home/am/Documents/safeside-main/bulid/experimental && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/cache_line_analysis.dir/cache_line_analysis.cc.o -c /home/am/Documents/safeside-main/experimental/cache_line_analysis.cc

experimental/CMakeFiles/cache_line_analysis.dir/cache_line_analysis.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/cache_line_analysis.dir/cache_line_analysis.cc.i"
	cd /home/am/Documents/safeside-main/bulid/experimental && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/am/Documents/safeside-main/experimental/cache_line_analysis.cc > CMakeFiles/cache_line_analysis.dir/cache_line_analysis.cc.i

experimental/CMakeFiles/cache_line_analysis.dir/cache_line_analysis.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/cache_line_analysis.dir/cache_line_analysis.cc.s"
	cd /home/am/Documents/safeside-main/bulid/experimental && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/am/Documents/safeside-main/experimental/cache_line_analysis.cc -o CMakeFiles/cache_line_analysis.dir/cache_line_analysis.cc.s

# Object files for target cache_line_analysis
cache_line_analysis_OBJECTS = \
"CMakeFiles/cache_line_analysis.dir/cache_line_analysis.cc.o"

# External object files for target cache_line_analysis
cache_line_analysis_EXTERNAL_OBJECTS =

experimental/cache_line_analysis: experimental/CMakeFiles/cache_line_analysis.dir/cache_line_analysis.cc.o
experimental/cache_line_analysis: experimental/CMakeFiles/cache_line_analysis.dir/build.make
experimental/cache_line_analysis: demos/libsafeside.a
experimental/cache_line_analysis: experimental/CMakeFiles/cache_line_analysis.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/am/Documents/safeside-main/bulid/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable cache_line_analysis"
	cd /home/am/Documents/safeside-main/bulid/experimental && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/cache_line_analysis.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
experimental/CMakeFiles/cache_line_analysis.dir/build: experimental/cache_line_analysis

.PHONY : experimental/CMakeFiles/cache_line_analysis.dir/build

experimental/CMakeFiles/cache_line_analysis.dir/clean:
	cd /home/am/Documents/safeside-main/bulid/experimental && $(CMAKE_COMMAND) -P CMakeFiles/cache_line_analysis.dir/cmake_clean.cmake
.PHONY : experimental/CMakeFiles/cache_line_analysis.dir/clean

experimental/CMakeFiles/cache_line_analysis.dir/depend:
	cd /home/am/Documents/safeside-main/bulid && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/am/Documents/safeside-main /home/am/Documents/safeside-main/experimental /home/am/Documents/safeside-main/bulid /home/am/Documents/safeside-main/bulid/experimental /home/am/Documents/safeside-main/bulid/experimental/CMakeFiles/cache_line_analysis.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : experimental/CMakeFiles/cache_line_analysis.dir/depend

