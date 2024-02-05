module register#(
    parameter WIDTH = 8
)(
    input wire clk, 
    input wire [WIDTH-1:0] d, 
    output reg [WIDTH-1:0] q
);

initial q = 0;

always@(posedge clk) begin
    q <= d;
end

endmodule

