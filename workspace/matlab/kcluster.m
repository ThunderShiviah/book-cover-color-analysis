%%%Calculates clustering of colors using k means%%%

X = importdata('rgb_avg_values.txt');

size(X);

idx3 = kmeans(X,4,'distance','city');
[silh3,h] = silhouette(X,idx3,'city');
set(get(gca,'Children'),'FaceColor',[.8 .8 1])
xlabel('Silhouette Value')
ylabel('Cluster')

idx4 = kmeans(X,4, 'dist','city', 'display','iter'); %Checks for the correct number of clusters

[idx4,cent4,sumdist] = kmeans(X,4,'dist','city',...
                       'display',X,'final','replicates',5); %for avoiding local minima