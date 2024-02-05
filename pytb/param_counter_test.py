import cocotb
from cocotb_test.simulator import run
import pytest
import os

from cocotb.triggers import Timer, FallingEdge, RisingEdge
from cocotb.utils import get_sim_time
from cocotb.clock import Clock

@cocotb.test()
async def falling_edge(dut):
    
    width = int(os.environ.get("WIDTH"))
    counts = int(os.environ.get("COUNTS"))

    assert len(dut.dout) == width

    clock = Clock(dut.clk, 1, units="us")  # Create a 10us period clock on port clk
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start())

    await FallingEdge(dut.clk)
    dut.rst.value = 1

    await FallingEdge(dut.clk)
    assert dut.dout.value == 0
    dut.rst.value = 0

    for i in range(2*counts):
        await FallingEdge(dut.clk)
        assert dut.dout.value == (i+1) % counts

    pass

async def rising_edge(dut):
    
    width = int(os.environ.get("WIDTH"))
    counts = int(os.environ.get("COUNTS"))

    assert len(dut.dout) == width

    clock = Clock(dut.clk, 1, units="ns")  # Create a 10us period clock on port clk
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    dut.rst.value = 1
    await RisingEdge(dut.clk)

    await FallingEdge(dut.clk)
    assert dut.dout.value == 0

    dut.rst.value = 0
    await RisingEdge(dut.clk)
    assert dut.dout.value == 0

    print(dut.dout.value)

    for i in range(2*counts):
        await RisingEdge(dut.clk)
        assert dut.dout.value == (i+1) % counts
        
    pass

@pytest.mark.parametrize(
    "parameters", [
        {"WIDTH": "4", "COUNTS": "8"}, 
        #{"WIDTH": "8", "COUNTS": "256"}
    ]
)
def test_counter(parameters):
    run(
        verilog_sources=[
            "../rtl/module_counter/counter.v", 
            "../rtl/module_counter/adder.v",
            "../rtl/module_counter/register.v"
        ], 
        toplevel="counter",          
        module="param_counter_test",
        timescale="1ns/1ps",
        force_compile=True,
        parameters=parameters,
        extra_env=parameters,
        waves=True,
    )