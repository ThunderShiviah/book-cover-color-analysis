x = load('colors.txt'); % makes a 12x3 matrix
x = reshape(x, 2, 6, 3); % reshape pulls columnwise, assume 6x2 image
x = x/255; %scale the data to be between 0 and 1
x
image(x)
