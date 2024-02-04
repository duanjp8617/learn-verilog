import cocotb
import random
from cocotb_test.simulator import run

from cocotb.triggers import Timer, FallingEdge, RisingEdge
from cocotb.utils import get_sim_time
from cocotb.clock import Clock

# 500MHz
freq = 500*1000*1000

# in ns
period = 1*1000*1000*1000 / freq

async def generate_clock(dut):
    for _ in range(100):
        dut.clk.value = 0
        await Timer(period/2, units='ns')
        dut.clk.value = 1
        await Timer(period/2, units='ns')


async def register_test_builtin_clock(dut):
    dut.d.value = 0

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    # it seems that we should always wait for the first RiseEdge in order to register the input value
    await RisingEdge(dut.clk)
    expected_val = 0  # Matches initial input value
    print(dut.q.value)

    for i in range(10):
        val = random.randint(0, 1)
        dut.d.value = val  # Assign the random value val to the input port d
        await RisingEdge(dut.clk)
        assert dut.q.value == expected_val, f"output q was incorrect on the {i}th cycle"
        expected_val = val  # Save random value for next RisingEdge

    # Check the final input on the next clock
    await RisingEdge(dut.clk)
    assert dut.q.value == expected_val, "output q was incorrect on the last cycle"

    pass

async def register_test(dut):
    await cocotb.start(generate_clock(dut))
    
    print(get_sim_time('ns'))
    dut.d.value = 1
    
    await RisingEdge(dut.clk)
    print(get_sim_time('ns'))

    expected = 1
    for i in range(0, 10):
        print(f"start of iteration {i}")
        val = i % 2
        dut.d.value = val
        print(get_sim_time('ns'))

        await RisingEdge(dut.clk)
        assert expected == dut.q.value
        expected = val
        print(get_sim_time('ns'))

    await RisingEdge(dut.clk)
    assert expected == dut.q.value

    pass


async def set_value_at_falling_edge(dut):
    await cocotb.start(generate_clock(dut))
    
    print(get_sim_time('ns'))
    await FallingEdge(dut.clk)
    print(get_sim_time('ns'))
    
    for i in range(1, 5):
        print(f"start of iteration {i}")
        dut.d.value = i % 2
        print(get_sim_time('ns'))

        await FallingEdge(dut.clk)
        print(get_sim_time('ns'))
        assert dut.q.value == i % 2
        
        

@cocotb.test()
async def dff_simple_test(dut):
    """Test that d propagates to q"""

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())  # Start the clock

    # await FallingEdge(dut.clk)  # Synchronize with the clock
    # for i in range(10):
    #     val = random.randint(0, 1)
    #     dut.d.value = val  # Assign the random value val to the input port d
    #     await FallingEdge(dut.clk)
    #     assert dut.q.value == val, f"output q was incorrect on the {i}th cycle"

    print(get_sim_time('us'))
    await FallingEdge(dut.clk)
    print(get_sim_time('us'))
    
    for i in range(1, 5):
        print(f"start of iteration {i}")
        dut.d.value = i % 2
        print(get_sim_time('us'))

        await FallingEdge(dut.clk)
        print(get_sim_time('us'))
        assert dut.q.value == i % 2

def test_simple_register():
    run(
        verilog_sources=["../rtl/simple_register.v"], 
        toplevel="simple_register",          
        module="simpile_register_test",
        timescale="1ns/1ps",
        force_compile=True,
        waves=True,
    )
