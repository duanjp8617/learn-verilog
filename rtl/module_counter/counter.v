module counter#(
    parameter WIDTH = 'd8,
    parameter COUNTS = 'd10
)(
    input wire rst,
    input wire clk,
    output wire [WIDTH-1:0] dout
);

initial begin
    if ($clog2(COUNTS) > WIDTH) begin
        $error("error: counter overflow (instance %m)");
        $finish;
    end
end

wire [WIDTH-1:0] a;
wire [WIDTH-1:0] b;
wire [WIDTH-1:0] y;
adder#(
    .WIDTH(WIDTH)
) 
adder(
    .a (a),
    .b (b),
    .y (y)
);

// this is super problematic but I don't know how to fix it yet
reg [WIDTH-1:0] d;
register#(
    .WIDTH(WIDTH)
)
register(
    .clk (clk),
    .d (d),
    .q (dout)
);

// wire can only be assigned outside always block
assign a = 'd1;
assign b = dout;

// reg can only be assigned within always block
// this is true because we are simulating a mux here
always @* begin
    if ( (rst == 1) || (dout == COUNTS-1) )
        d = 0;
    else
        d = y;
end

endmodule