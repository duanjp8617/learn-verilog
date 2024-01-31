module param_adder#(
    INPUT_DATA_WIDTH = 4,
    OUTPUT_DATA_WIDTH = 4
)
(
    input wire [INPUT_DATA_WIDTH-1:0] a,
    input wire [INPUT_DATA_WIDTH-1:0] b,
    output wire [OUTPUT_DATA_WIDTH-1:0] c
);

assign c = a + b;

endmodule