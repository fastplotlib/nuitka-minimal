import fastplotlib as fpl
import numpy as np

vid = np.random.rand(100, 512, 512)

iw = fpl.ImageWidget(vid, figure_kwargs={"size": (800, 600)})

iw.show()

fpl.loop.run()
