# Copyright (C) 2023  Intel Corporation. All rights reserved.
# Your use of Intel Corporation's design tools, logic functions 
# and other software and tools, and any partner logic 
# functions, and any output files from any of the foregoing 
# (including device programming or simulation files), and any 
# associated documentation or information are expressly subject 
# to the terms and conditions of the Intel Program License 
# Subscription Agreement, the Intel Quartus Prime License Agreement,
# the Intel FPGA IP License Agreement, or other applicable license
# agreement, including, without limitation, that your use is for
# the sole purpose of programming logic devices manufactured by
# Intel and sold by Intel or its authorized distributors.  Please
# refer to the applicable agreement for further details, at
# https://fpgasoftware.intel.com/eula.

# Quartus Prime: Generate Tcl File for Project
# File: top_level.tcl
# Generated on: Fri Apr 26 16:56:35 2024

# Load Quartus Prime Tcl Project package
package require ::quartus::project
package require ::quartus::sta

set need_to_close_project 0
set make_assignments 1

# Check that the right project is open
if {[is_project_open]} {
	if {[string compare $quartus(project) "top_level"]} {
		puts "Project top_level is not open"
		set make_assignments 0
	}
} else {
	# Only open if not already open
	if {[project_exists top_level]} {
		project_open -revision top_level top_level
	} else {
		project_new -revision top_level top_level
	}
	set need_to_close_project 1
}

# Make assignments
if {$make_assignments} {
	set_global_assignment -name TOP_LEVEL_ENTITY TOP_LEVEL
	set_global_assignment -name DEVICE 5CEBA4F23C7
	set_global_assignment -name EDA_OUTPUT_DATA_FORMAT "VERILOG HDL" -section_id eda_simulation
	set_global_assignment -name EDA_SIMULATION_TOOL "Questa Intel FPGA (Verilog)"
	set_global_assignment -name FAMILY "Cyclone V"
	set_global_assignment -name NUM_PARALLEL_PROCESSORS ALL
	set_global_assignment -name PROJECT_IP_REGENERATION_POLICY SKIP_REGENERATING_IP_IF_HDL_MODIFIED
	set_global_assignment -name TIMING_ANALYZER_MULTICORNER_ANALYSIS ON
	set_global_assignment -name VHDL_INPUT_VERSION VHDL_2008
	set_global_assignment -name PARTITION_NETLIST_TYPE SOURCE -section_id Top
	set_global_assignment -name PARTITION_FITTER_PRESERVATION_LEVEL PLACEMENT_AND_ROUTING -section_id Top
	set_global_assignment -name PARTITION_COLOR 16764057 -section_id Top
	set_global_assignment -name VHDL_FILE ../src/TOP_LEVEL_CONSTANTS.vhd
	set_global_assignment -name VHDL_FILE ../src/TOP_LEVEL.vhd
	set_global_assignment -name VHDL_FILE ../src/STAGE_WB.vhd
	set_global_assignment -name VHDL_FILE ../src/STAGE_MEM.vhd
	set_global_assignment -name VHDL_FILE ../src/STAGE_IF.vhd
	set_global_assignment -name VHDL_FILE ../src/STAGE_ID.vhd
	set_global_assignment -name VHDL_FILE ../src/STAGE_EX.vhd
	set_global_assignment -name VHDL_FILE ../src/RV32I_REGISTER_FILE.vhd
	set_global_assignment -name VHDL_FILE ../src/RV32I_INSTRUCTION_DECODER.vhd
	set_global_assignment -name VHDL_FILE ../src/RV32I_FORWARDING_UNIT_ALU.vhd
	set_global_assignment -name VHDL_FILE ../src/RV32I_ALU_CONTROLLER.vhd
	set_global_assignment -name VHDL_FILE ../src/RV32I_ALU_BIT.vhd
	set_global_assignment -name VHDL_FILE ../src/RV32I_ALU.vhd
	set_global_assignment -name VHDL_FILE ../src/MODULE_WRITE_BACK.vhd
	set_global_assignment -name VHDL_FILE ../src/MODULE_REGISTER_FILE.vhd
	set_global_assignment -name VHDL_FILE ../src/MODULE_PC.vhd
	set_global_assignment -name VHDL_FILE ../src/MODULE_CONTROL_UNIT.vhd
	set_global_assignment -name VHDL_FILE ../src/MODULE_ALU_REGISTER_SOURCE.vhd
	set_global_assignment -name VHDL_FILE ../src/MODULE_ALU_CONTROLLER.vhd
	set_global_assignment -name VHDL_FILE ../src/MODULE_ALU.vhd
	set_global_assignment -name VHDL_FILE ../src/GENERIC_SIGNAL_EXTENDER.vhd
	set_global_assignment -name VHDL_FILE ../src/GENERIC_ROM.vhd
	set_global_assignment -name VHDL_FILE ../src/GENERIC_REGISTER.vhd
	set_global_assignment -name VHDL_FILE ../src/GENERIC_RAM.vhd
	set_global_assignment -name VHDL_FILE ../src/GENERIC_MUX_4X1.vhd
	set_global_assignment -name VHDL_FILE ../src/GENERIC_MUX_2X1.vhd
	set_global_assignment -name VHDL_FILE ../src/GENERIC_FLIP_FLOP.vhd
	set_global_assignment -name VHDL_FILE ../src/GENERIC_EDGE_DETECTOR.vhd
	set_global_assignment -name VHDL_FILE ../src/GENERIC_DEBOUNCE.vhd
	set_global_assignment -name VHDL_FILE ../src/GENERIC_COUNTER.vhd
	set_global_assignment -name VHDL_FILE ../src/GENERIC_ADDER.vhd
	set_global_assignment -name LAST_QUARTUS_VERSION "23.1std.0 Lite Edition"
	set_global_assignment -name EDA_TIME_SCALE "1 ps" -section_id eda_simulation
	set_global_assignment -name OPTIMIZE_TIMING NORMAL_COMPILATION
	set_global_assignment -name ADV_NETLIST_OPT_SYNTH_WYSIWYG_REMAP ON
	set_global_assignment -name ADV_NETLIST_OPT_SYNTH_GATE_RETIME ON
	set_location_assignment PIN_M9 -to CLOCK_50
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to CLOCK_50
	set_location_assignment PIN_U21 -to HEX0[0]
	set_location_assignment PIN_V21 -to HEX0[1]
	set_location_assignment PIN_W22 -to HEX0[2]
	set_location_assignment PIN_W21 -to HEX0[3]
	set_location_assignment PIN_Y22 -to HEX0[4]
	set_location_assignment PIN_Y21 -to HEX0[5]
	set_location_assignment PIN_AA22 -to HEX0[6]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX0[0]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX0[1]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX0[2]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX0[3]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX0[4]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX0[5]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX0[6]
	set_instance_assignment -name CURRENT_STRENGTH_NEW DEFAULT -to HEX0
	set_instance_assignment -name SLEW_RATE 1 -to HEX0
	set_location_assignment PIN_AA20 -to HEX1[0]
	set_location_assignment PIN_AB20 -to HEX1[1]
	set_location_assignment PIN_AA19 -to HEX1[2]
	set_location_assignment PIN_AA18 -to HEX1[3]
	set_location_assignment PIN_AB18 -to HEX1[4]
	set_location_assignment PIN_AA17 -to HEX1[5]
	set_location_assignment PIN_U22 -to HEX1[6]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX1[0]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX1[1]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX1[2]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX1[3]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX1[4]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX1[5]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX1[6]
	set_instance_assignment -name CURRENT_STRENGTH_NEW DEFAULT -to HEX1
	set_instance_assignment -name SLEW_RATE 1 -to HEX1
	set_location_assignment PIN_Y19 -to HEX2[0]
	set_location_assignment PIN_AB17 -to HEX2[1]
	set_location_assignment PIN_AA10 -to HEX2[2]
	set_location_assignment PIN_Y14 -to HEX2[3]
	set_location_assignment PIN_V14 -to HEX2[4]
	set_location_assignment PIN_AB22 -to HEX2[5]
	set_location_assignment PIN_AB21 -to HEX2[6]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX2[0]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX2[1]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX2[2]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX2[3]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX2[4]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX2[5]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX2[6]
	set_instance_assignment -name CURRENT_STRENGTH_NEW DEFAULT -to HEX2
	set_instance_assignment -name SLEW_RATE 1 -to HEX2
	set_location_assignment PIN_Y16 -to HEX3[0]
	set_location_assignment PIN_W16 -to HEX3[1]
	set_location_assignment PIN_Y17 -to HEX3[2]
	set_location_assignment PIN_V16 -to HEX3[3]
	set_location_assignment PIN_U17 -to HEX3[4]
	set_location_assignment PIN_V18 -to HEX3[5]
	set_location_assignment PIN_V19 -to HEX3[6]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX3[0]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX3[1]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX3[2]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX3[3]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX3[4]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX3[5]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX3[6]
	set_instance_assignment -name CURRENT_STRENGTH_NEW DEFAULT -to HEX3
	set_instance_assignment -name SLEW_RATE 1 -to HEX3
	set_location_assignment PIN_U20 -to HEX4[0]
	set_location_assignment PIN_Y20 -to HEX4[1]
	set_location_assignment PIN_V20 -to HEX4[2]
	set_location_assignment PIN_U16 -to HEX4[3]
	set_location_assignment PIN_U15 -to HEX4[4]
	set_location_assignment PIN_Y15 -to HEX4[5]
	set_location_assignment PIN_P9 -to HEX4[6]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX4[0]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX4[1]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX4[2]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX4[3]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX4[4]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX4[5]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX4[6]
	set_instance_assignment -name CURRENT_STRENGTH_NEW DEFAULT -to HEX4
	set_instance_assignment -name SLEW_RATE 1 -to HEX4
	set_location_assignment PIN_N9 -to HEX5[0]
	set_location_assignment PIN_M8 -to HEX5[1]
	set_location_assignment PIN_T14 -to HEX5[2]
	set_location_assignment PIN_P14 -to HEX5[3]
	set_location_assignment PIN_C1 -to HEX5[4]
	set_location_assignment PIN_C2 -to HEX5[5]
	set_location_assignment PIN_W19 -to HEX5[6]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX5[0]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX5[1]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX5[2]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX5[3]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX5[4]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX5[5]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to HEX5[6]
	set_instance_assignment -name CURRENT_STRENGTH_NEW DEFAULT -to HEX5
	set_instance_assignment -name SLEW_RATE 1 -to HEX5
	set_location_assignment PIN_U7 -to KEY[0]
	set_location_assignment PIN_W9 -to KEY[1]
	set_location_assignment PIN_M7 -to KEY[2]
	set_location_assignment PIN_M6 -to KEY[3]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to KEY[0]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to KEY[1]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to KEY[2]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to KEY[3]
	set_location_assignment PIN_P22 -to FPGA_RESET_N
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to FPGA_RESET_N
	set_location_assignment PIN_AA2 -to LEDR[0]
	set_location_assignment PIN_AA1 -to LEDR[1]
	set_location_assignment PIN_W2 -to LEDR[2]
	set_location_assignment PIN_Y3 -to LEDR[3]
	set_location_assignment PIN_N2 -to LEDR[4]
	set_location_assignment PIN_N1 -to LEDR[5]
	set_location_assignment PIN_U2 -to LEDR[6]
	set_location_assignment PIN_U1 -to LEDR[7]
	set_location_assignment PIN_L2 -to LEDR[8]
	set_location_assignment PIN_L1 -to LEDR[9]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to LEDR[0]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to LEDR[1]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to LEDR[2]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to LEDR[3]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to LEDR[4]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to LEDR[5]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to LEDR[6]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to LEDR[7]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to LEDR[8]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to LEDR[9]
	set_instance_assignment -name CURRENT_STRENGTH_NEW DEFAULT -to LEDR
	set_instance_assignment -name SLEW_RATE 1 -to LEDR
	set_location_assignment PIN_U13 -to SW[0]
	set_location_assignment PIN_V13 -to SW[1]
	set_location_assignment PIN_T13 -to SW[2]
	set_location_assignment PIN_T12 -to SW[3]
	set_location_assignment PIN_AA15 -to SW[4]
	set_location_assignment PIN_AB15 -to SW[5]
	set_location_assignment PIN_AA14 -to SW[6]
	set_location_assignment PIN_AA13 -to SW[7]
	set_location_assignment PIN_AB13 -to SW[8]
	set_location_assignment PIN_AB12 -to SW[9]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to SW[0]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to SW[1]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to SW[2]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to SW[3]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to SW[4]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to SW[5]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to SW[6]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to SW[7]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to SW[8]
	set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to SW[9]
	set_instance_assignment -name PARTITION_HIERARCHY root_partition -to | -section_id Top

	# Commit assignments
	export_assignments

	# Always create the netlist first
	create_timing_netlist
	read_sdc top_level.sdc
	update_timing_netlist

	# Output results in the form of messages
	report_clock_fmax_summary

	# Report both with report panel and messages
	report_clock_fmax_summary -panel_name Fmax -stdout -file Fmax.html

	# The following command is optional
	delete_timing_netlist

	
	# Close project
	if {$need_to_close_project} {
		project_close
	}
}
