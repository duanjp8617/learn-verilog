import cocotb
from cocotb_test.simulator import run

from cocotb.triggers import Timer

@cocotb.test()
async def method(dut):
    dut.a.value = 0xfe
    dut.b.value = 0xba

    await Timer(1, 'ns')

    assert dut.c.value == 0xfa

    pass


def test_input_regroup():
    run(
        verilog_sources=["../rtl/input_regroup.v"], 
        toplevel="input_regroup",          
        module="input_regroup_test",
        timescale="1ns/1ps",
        force_compile=True,
    )