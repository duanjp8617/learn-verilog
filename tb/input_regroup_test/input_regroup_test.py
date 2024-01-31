import cocotb

from cocotb.triggers import Timer

@cocotb.test()
async def test_method(dut):
    dut.a.value = 0xfe
    dut.b.value = 0xba

    await Timer(1, 'ns')

    assert dut.c.value == 0xfa

    pass
