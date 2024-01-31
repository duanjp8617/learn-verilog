import cocotb
import random

from cocotb.triggers import Timer

@cocotb.test()
async def adder_test(dut):
    dut.a.value = 100
    dut.b.value = 50

    await Timer(1, 'ns')

    assert dut.c.value == 150, f"Error when adding 100 + 50"
    
    pass

@cocotb.test()
async def overflow_test(dut):
    dut.a.value = 0b11111111
    dut.b.value = 0x01

    await Timer(1, 'ns')

    assert dut.c.value == 0x00, f"Error when performing overflow add"

    pass