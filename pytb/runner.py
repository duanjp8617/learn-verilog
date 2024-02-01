from cocotb_test.simulator import run
import pytest

def test_line():
    run(
        verilog_sources=["../rtl/line.v"], 
        toplevel="line",          
        module="line_test",
        timescale="1ns/1ps",
        force_compile=True,
    )

def test_adder():
    run(
        verilog_sources=["../rtl/adder.v"], 
        toplevel="adder",          
        module="adder_test",
        timescale="1ns/1ps",
        force_compile=True,
    )

def test_input_regroup():
    run(
        verilog_sources=["../rtl/input_regroup.v"], 
        toplevel="input_regroup",          
        module="input_regroup_test",
        timescale="1ns/1ps",
        force_compile=True,
    )

@pytest.mark.parametrize(
    "parameters", [{"INPUT_DATA_WIDTH": "16", "OUTPUT_DATA_WIDTH": "16"}, {"INPUT_DATA_WIDTH": "16", "OUTPUT_DATA_WIDTH": "8"}]
)
def test_param_adder(parameters):
    run(
        verilog_sources=["../rtl/param_adder.v"], 
        toplevel="param_adder",          
        module="param_adder_test",
        timescale="1ns/1ps",
        force_compile=True,
        parameters=parameters,
    )