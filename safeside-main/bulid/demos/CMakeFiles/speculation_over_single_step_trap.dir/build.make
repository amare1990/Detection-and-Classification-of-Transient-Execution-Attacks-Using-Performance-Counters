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
include demos/CMakeFiles/speculation_over_single_step_trap.dir/depend.make

# Include the progress variables for this target.
include demos/CMakeFiles/speculation_over_single_step_trap.dir/progress.make

# Include the compile flags for this target's objects.
include demos/CMakeFiles/speculation_over_single_step_trap.dir/flags.make

demos/CMakeFiles/speculation_over_single_step_trap.dir/speculation_over_single_step_trap.cc.o: demos/CMakeFiles/speculation_over_single_step_trap.dir/flags.make
demos/CMakeFiles/speculation_over_single_step_trap.dir/speculation_over_single_step_trap.cc.o: ../demos/speculation_over_single_step_trap.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/am/Documents/safeside-main/bulid/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object demos/CMakeFiles/speculation_over_single_step_trap.dir/speculation_over_single_step_trap.cc.o"
	cd /home/am/Documents/safeside-main/bulid/demos && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/speculation_over_single_step_trap.dir/speculation_over_single_step_trap.cc.o -c /home/am/Documents/safeside-main/demos/speculation_over_single_step_trap.cc

demos/CMakeFiles/speculation_over_single_step_trap.dir/speculation_over_single_step_trap.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/speculation_over_single_step_trap.dir/speculation_over_single_step_trap.cc.i"
	cd /home/am/Documents/safeside-main/bulid/demos && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/am/Documents/safeside-main/demos/speculation_over_single_step_trap.cc > CMakeFiles/speculation_over_single_step_trap.dir/speculation_over_single_step_trap.cc.i

demos/CMakeFiles/speculation_over_single_step_trap.dir/speculation_over_single_step_trap.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/speculation_over_single_step_trap.dir/speculation_over_single_step_trap.cc.s"
	cd /home/am/Documents/safeside-main/bulid/demos && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/am/Documents/safeside-main/demos/speculation_over_single_step_trap.cc -o CMakeFiles/speculation_over_single_step_trap.dir/speculation_over_single_step_trap.cc.s

# Object files for target speculation_over_single_step_trap
speculation_over_single_step_trap_OBJECTS = \
"CMakeFiles/speculation_over_single_step_trap.dir/speculation_over_single_step_trap.cc.o"

# External object files for target speculation_over_single_step_trap
speculation_over_single_step_trap_EXTERNAL_OBJECTS =

demos/speculation_over_single_step_trap: demos/CMakeFiles/speculation_over_single_step_trap.dir/speculation_over_single_step_trap.cc.o
demos/speculation_over_single_step_trap: demos/CMakeFiles/speculation_over_single_step_trap.dir/build.make
demos/speculation_over_single_step_trap: demos/libsafeside.a
demos/speculation_over_single_step_trap: demos/CMakeFiles/speculation_over_single_step_trap.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/am/Documents/safeside-main/bulid/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable speculation_over_single_step_trap"
	cd /home/am/Documents/safeside-main/bulid/demos && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/speculation_over_single_step_trap.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
demos/CMakeFiles/speculation_over_single_step_trap.dir/build: demos/speculation_over_single_step_trap

.PHONY : demos/CMakeFiles/speculation_over_single_step_trap.dir/build

demos/CMakeFiles/speculation_over_single_step_trap.dir/clean:
	cd /home/am/Documents/safeside-main/bulid/demos && $(CMAKE_COMMAND) -P CMakeFiles/speculation_over_single_step_trap.dir/cmake_clean.cmake
.PHONY : demos/CMakeFiles/speculation_over_single_step_trap.dir/clean

demos/CMakeFiles/speculation_over_single_step_trap.dir/depend:
	cd /home/am/Documents/safeside-main/bulid && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/am/Documents/safeside-main /home/am/Documents/safeside-main/demos /home/am/Documents/safeside-main/bulid /home/am/Documents/safeside-main/bulid/demos /home/am/Documents/safeside-main/bulid/demos/CMakeFiles/speculation_over_single_step_trap.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : demos/CMakeFiles/speculation_over_single_step_trap.dir/depend

