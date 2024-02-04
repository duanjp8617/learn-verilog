module counter#(
    // bit width of the counter
    parameter WIDTH = 8, 

    // total number of the counts
    parameter COUNTS = 16
)(
    input wire clk, 
    input wire rst,
    output wire [WIDTH-1:0] dout
);

initial begin
    if($clog2(COUNTS) > WIDTH) begin
        $error("Error: count to value overflow (instance %m)");
        $finish;
    end
end

reg [WIDTH-1:0] counter;
assign dout = counter;

always@(posedge clk) begin
    if(rst == 1) begin
        counter <= 'd0;
    end
    else begin
        if (counter == (COUNTS - 1)) 
            counter <= 'd0;
        else
            counter <= counter + 1;
    end
end

endmodule