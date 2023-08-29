import pandas as pd
import numpy as np
import sklearn.decomposition as sk
import matplotlib as plt


sk.PCA(n_components=2)
# PCA model -> find low dimensional representations of our data
# Unfeasable to represent large datasets as 2d or 3d plots with X features
# PCA allows us to capture as much variation as possible
# Need to do a bit more research of meaning of 'increasing dimensions as you increase features`
# additionally, need to go through excel data and begin creating methods with proper column selection based on excel column names
