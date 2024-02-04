import cocotb
from cocotb_test.simulator import run
import pytest

from cocotb.triggers import Timer

@cocotb.test()
async def method(dut):
    dut.a.value = 5
    dut.b.value = 5

    print(f"width of a {len(dut.a)}")
    print(f"width of c {len(dut.c)}")

    await Timer(1, 'ns')

    assert dut.c.value == 10, f"Error when adding 100 + 50"
    
    pass

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