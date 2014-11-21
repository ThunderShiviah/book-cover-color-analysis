%%%Exploratory data analysis of book cover colors%%%%
%% We are using RGB averaged colors from Japanese book covers from 
%%% Amazon.co.jp top 20 list from 2000 to 2014. 

clc

data = csvread('rgb_avg_values.txt');


%scatter3(data(:,1),data(:,2),data(:,3));

X = data(:,1);
Y = data(:,2);
Z = data(:,3);

%% Creates a linear fit of the color data.
createFit(X, Y, Z)