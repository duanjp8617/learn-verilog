module adder#(
    parameter WIDTH = 8
)(
    input wire [WIDTH-1:0] a,
    input wire [WIDTH-1:0] b,
    output wire [WIDTH-1:0] y
);

assign y = a + b;

endmodule