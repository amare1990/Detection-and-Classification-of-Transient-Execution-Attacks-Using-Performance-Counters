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
include demos/CMakeFiles/ret2spec_sa.dir/depend.make

# Include the progress variables for this target.
include demos/CMakeFiles/ret2spec_sa.dir/progress.make

# Include the compile flags for this target's objects.
include demos/CMakeFiles/ret2spec_sa.dir/flags.make

demos/CMakeFiles/ret2spec_sa.dir/ret2spec_sa.cc.o: demos/CMakeFiles/ret2spec_sa.dir/flags.make
demos/CMakeFiles/ret2spec_sa.dir/ret2spec_sa.cc.o: ../demos/ret2spec_sa.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/am/Documents/safeside-main/bulid/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object demos/CMakeFiles/ret2spec_sa.dir/ret2spec_sa.cc.o"
	cd /home/am/Documents/safeside-main/bulid/demos && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/ret2spec_sa.dir/ret2spec_sa.cc.o -c /home/am/Documents/safeside-main/demos/ret2spec_sa.cc

demos/CMakeFiles/ret2spec_sa.dir/ret2spec_sa.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ret2spec_sa.dir/ret2spec_sa.cc.i"
	cd /home/am/Documents/safeside-main/bulid/demos && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/am/Documents/safeside-main/demos/ret2spec_sa.cc > CMakeFiles/ret2spec_sa.dir/ret2spec_sa.cc.i

demos/CMakeFiles/ret2spec_sa.dir/ret2spec_sa.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ret2spec_sa.dir/ret2spec_sa.cc.s"
	cd /home/am/Documents/safeside-main/bulid/demos && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/am/Documents/safeside-main/demos/ret2spec_sa.cc -o CMakeFiles/ret2spec_sa.dir/ret2spec_sa.cc.s

demos/CMakeFiles/ret2spec_sa.dir/ret2spec_common.cc.o: demos/CMakeFiles/ret2spec_sa.dir/flags.make
demos/CMakeFiles/ret2spec_sa.dir/ret2spec_common.cc.o: ../demos/ret2spec_common.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/am/Documents/safeside-main/bulid/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object demos/CMakeFiles/ret2spec_sa.dir/ret2spec_common.cc.o"
	cd /home/am/Documents/safeside-main/bulid/demos && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/ret2spec_sa.dir/ret2spec_common.cc.o -c /home/am/Documents/safeside-main/demos/ret2spec_common.cc

demos/CMakeFiles/ret2spec_sa.dir/ret2spec_common.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ret2spec_sa.dir/ret2spec_common.cc.i"
	cd /home/am/Documents/safeside-main/bulid/demos && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/am/Documents/safeside-main/demos/ret2spec_common.cc > CMakeFiles/ret2spec_sa.dir/ret2spec_common.cc.i

demos/CMakeFiles/ret2spec_sa.dir/ret2spec_common.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ret2spec_sa.dir/ret2spec_common.cc.s"
	cd /home/am/Documents/safeside-main/bulid/demos && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/am/Documents/safeside-main/demos/ret2spec_common.cc -o CMakeFiles/ret2spec_sa.dir/ret2spec_common.cc.s

# Object files for target ret2spec_sa
ret2spec_sa_OBJECTS = \
"CMakeFiles/ret2spec_sa.dir/ret2spec_sa.cc.o" \
"CMakeFiles/ret2spec_sa.dir/ret2spec_common.cc.o"

# External object files for target ret2spec_sa
ret2spec_sa_EXTERNAL_OBJECTS =

demos/ret2spec_sa: demos/CMakeFiles/ret2spec_sa.dir/ret2spec_sa.cc.o
demos/ret2spec_sa: demos/CMakeFiles/ret2spec_sa.dir/ret2spec_common.cc.o
demos/ret2spec_sa: demos/CMakeFiles/ret2spec_sa.dir/build.make
demos/ret2spec_sa: demos/libsafeside.a
demos/ret2spec_sa: demos/CMakeFiles/ret2spec_sa.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/am/Documents/safeside-main/bulid/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable ret2spec_sa"
	cd /home/am/Documents/safeside-main/bulid/demos && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ret2spec_sa.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
demos/CMakeFiles/ret2spec_sa.dir/build: demos/ret2spec_sa

.PHONY : demos/CMakeFiles/ret2spec_sa.dir/build

demos/CMakeFiles/ret2spec_sa.dir/clean:
	cd /home/am/Documents/safeside-main/bulid/demos && $(CMAKE_COMMAND) -P CMakeFiles/ret2spec_sa.dir/cmake_clean.cmake
.PHONY : demos/CMakeFiles/ret2spec_sa.dir/clean

demos/CMakeFiles/ret2spec_sa.dir/depend:
	cd /home/am/Documents/safeside-main/bulid && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/am/Documents/safeside-main /home/am/Documents/safeside-main/demos /home/am/Documents/safeside-main/bulid /home/am/Documents/safeside-main/bulid/demos /home/am/Documents/safeside-main/bulid/demos/CMakeFiles/ret2spec_sa.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : demos/CMakeFiles/ret2spec_sa.dir/depend
