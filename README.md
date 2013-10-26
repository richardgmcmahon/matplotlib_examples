
Example plots that show some subtle issues with marker sizes
and markers in matplotlib. A marker is the equivalent of
a sysmbol in IDL.

When plotting points you can use the plot or scatter function.

They have some subtle differences. Plot adds a marker edge
that means that for small markers the marker will appear black
unless you turn the markeredge off or make the edgecolor the
same as the markerface. It sounds complicated doesn't it.
This the price of flexibility. There is a thread on the internet
suggesting that the default edgecolor should be the same as the facecolor.

I could not work out how to turn of
the marker edge.


