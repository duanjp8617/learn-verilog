import cocotb
from cocotb_test.simulator import run
import random

from cocotb.triggers import Timer

async def method(dut):
    dut.a.value = 100
    dut.b.value = 50

    await Timer(1, 'ns')

    assert dut.c.value == 150, f"Error when adding 100 + 50"
    
    pass

@cocotb.test()
async def overflow(dut):
    dut.a.value = 0b11111111
    dut.b.value = 0x01

    await Timer(1, 'ns')

    assert dut.c.value == 0x00, f"Error when performing overflow add"

    pass

def test_adder():
    run(
        verilog_sources=["../rtl/adder.v"], 
        toplevel="adder",          
        module="adder_test",
        timescale="1ns/1ps",
        force_compile=True,
    )