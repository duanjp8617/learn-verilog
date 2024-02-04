import cocotb
import cocotb_test.simulator
import os

from cocotb.triggers import Timer

@cocotb.test()
async def straight_line(dut):
    input = (0,0,1,1)
    print("wtf")

    for i in range(4):
        dut.i_port.value = input[i]
        await Timer(1, 'ns')
        assert dut.o_port.value == input[i], f"Error at iteration {i}"

    pass

def test_line():
    cocotb_test.simulator.run(
        verilog_sources=["../rtl/line.v"], 
        toplevel="line",          
        module="line_test",
        timescale="1ns/1ps",
        force_compile=True,
    )

# print(os.path.splitext(os.path.basename(__file__))[0])