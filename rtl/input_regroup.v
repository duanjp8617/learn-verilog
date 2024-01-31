module input_regroup(
    input wire [7:0] a,
    input wire [7:0] b,
    output wire [7:0] c
);

// assign c = {a[7:4], b[3:0]};

assign c[7:4] = a[7:4];
assign c[3:0] = b[3:0];

endmodule