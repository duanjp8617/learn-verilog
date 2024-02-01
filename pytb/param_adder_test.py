import cocotb

from cocotb.triggers import Timer

@cocotb.test()
async def adder_test(dut):
    dut.a.value = 5
    dut.b.value = 5

    print(f"width of a {len(dut.a)}")
    print(f"width of c {len(dut.c)}")

    await Timer(1, 'ns')

    assert dut.c.value == 10, f"Error when adding 100 + 50"
    
    pass