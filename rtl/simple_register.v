`timescale 1ns/1ps

module simple_register(
    input wire d, clk,
    output wire q
);

reg r;
assign q = r;

always@(posedge clk) begin
    r <= d;
end

endmodule